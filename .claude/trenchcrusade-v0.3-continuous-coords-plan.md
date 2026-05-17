# Trench Crusade v0.3 工程化计划 — 连续坐标 + Mesh Raycast

> **前置**：v0.2 已完成 Phase A-C（脚手架 + MCP server 20 工具 / 146 tests + AI prompt 425 行）+ Phase D 用 HTML 3D viewer 取代 CLI + Phase E 试玩中（third-blood T2）。详见 [[trenchcrusade-v0.2-engineering-plan]]。
> **v0.3 目标**：把 cell 抽象 + `blocks_los` flag 升级为**连续坐标 + 真 mesh raycast**，让 LOS / cover / 高度差 / 移动范围全部几何精确，前端纯预览高亮可达区域和射击 ray。
> **本文版本**：v0.3 plan v0.1
> **总估时**：~1.5 工作周（7-8 工作日 solo）
> **前置条件**：third-blood 比赛结束 → main 干净 → 开 worktree

---

## 0. v0.2 → v0.3 缺口表

v0.2 让"开打"可行，v0.3 让"算几何"精确。

| 缺口 | 现状 | v0.3 补位 |
|---|---|---|
| 坐标系 | int cell `[x, y, z]`，z 是 layer index | float `[x, y, z]`（英寸），z 是世界高度 |
| Terrain 表示 | `cell × blocks_los/cover/movement_cost` flags | 几何 primitives（box / cylinder / ramp / sphere）有 transform |
| LOS | Bresenham + flag 查询（trench `blocks_los: false` 永远透视） | trimesh raycast，墙、cover、烟雾全是真 geometry |
| Cover | terrain flag `partial/full` | 几何遮挡比例 / 半身遮挡自动判定 |
| 高度差移动成本 | 手动估，validate_move v0.5 stub 不验证 | A* on nav-graph，边权含 climb / fall / difficult |
| 模型基座体积 | `base_size: [w, h]` 纯逻辑 | 真 cylinder mesh，参与 raycast 自遮挡 |
| 烟雾 / 黑暗 | 没建模 | 加 `volume` 类 terrain，raycast 穿过时降 DICE |
| 玩家预览 LOS / 可达区 | 只能心算或问 Claude | 浏览器 hover/click 即时高亮（纯前端，不动 state） |
| `valid_charge_paths` | v0.5 stub | 真 A* + interposing enemy 检测 |

**架构原则不变**（v0.2 plan §0 reiterated）：

- **MCP/LLM 控制循环不动**：所有 state 变更仍只能 Claude → MCP → Python → YAML
- **UI 只读**：浏览器可计算预览（raycast / pathfind），但不能直接提交 state（v0.4 才考虑）
- **Python + Three.js 双端同 mesh**：terrain_compiler 输出两种格式，保证 AI 看到的 LOS == 玩家看到的 LOS

---

## 1. Phase 概览

| Phase | 内容 | 依赖 | 估时 | 产出 |
|---:|---|---|---:|---|
| **A** | Schema 迁移：连续坐标 + terrain primitives | v0.2 ✅ + third-blood 收 | 1d | 新 `match-template.yaml` + 迁移脚本 + 旧 yaml 转换器 |
| **B** | `terrain_compiler.py`：YAML → trimesh + Three.js JSON | A | 1d | 单一 SSoT 输出两端可读 mesh，配套 tests |
| **C** | MCP raycast 化：`get_los` / `get_cover` / `valid_move_area` / `valid_charge_paths` 真实现 | B | 3d | 4 个工具升级 + 旧工具兼容删除 + tests |
| **D** | Three.js 纯预览层：可达区高亮 + 射击 ray 预览 + HUD 坐标 | B | 2-3d | render_three.py 新模块 + 鼠标交互 |
| **E** | 迁移测试 + 文档回填 | A-D | 1d | third-blood 复刻 + CLAUDE.md / coordinate-system.md 更新 + 旧 cell 文档归档 |

**v0.4+ 暂缓**：UI 直接驱动 state / WebSocket bridge / 多人模式 / 4 待导 faction（v0.2 backlog 顺延）

---

## Phase A — Schema 迁移：连续坐标 + terrain primitives（1 工作日）

**目标**：把坐标系从 cell × layer 改成 float-inch，把 terrain 从 cell stack 改成几何 primitive。

### A.1 新 `match-template.yaml` schema

**坐标改动**：

```yaml
# v0.2
pos: [12, 17, 0]              # int cell × layer index
battlefield:
  size: [36, 36]              # cells
  layer_height: 3             # 每 z 层 = 3"

# v0.3
pos: [12.0, 17.0, 0.0]        # float inches, 世界坐标
battlefield:
  size_inches: [36, 36]       # 直接英寸
  # layer_height 字段删除（不再需要）
```

**Terrain 改动**：

```yaml
# v0.2
terrain:
  - id: trench_central
    type: trench
    bounds: [4, 17, 32, 19]   # cell range
    base_z: -1
    height: 1
    blocks_los: false
    cover: partial
    movement_cost: 1

# v0.3
terrain:
  - id: trench_central
    type: trench
    shape: box
    pos: [18.0, 18.0, -1.5]   # 中心，世界坐标
    size: [28.0, 2.0, 3.0]    # 长 × 宽 × 深（inches）
    rotation: 0               # 度数，绕 z 轴
    movement_cost: 1
    # 不再写 blocks_los / cover — 全部由几何决定
    # 可选：climb_aids: [ladder_at_x10_y18, rope_at_x25_y19]
```

**支持 shape 类型**（v0.3 最小集）：
- `box`：长方体（trench / wall / 墙）
- `cylinder`：圆柱（柱子 / 树）
- `ramp`：斜坡（梯子 / 楼梯，触发 climb-aid 行为）
- `volume`：体积体（烟雾 / 黑暗 / 气体；raycast 穿过累计 -DICE）
- 复杂建筑用多个 box 组合（v0.3 不引入 GLB 导入，v0.4 再说）

**Model 基座**：

```yaml
- id: red.yeoman_1
  pos: [7.0, 16.0, 0.0]      # 脚位置，世界坐标
  base_shape: circle
  base_dimensions_mm: [28, 28]  # 不变
  model_height_mm: 32          # 新字段：raycast 用模型本体高度
```

### A.2 迁移脚本 `tools/mcp-server/scripts/migrate_v02_to_v03.py`

输入旧 yaml，输出新 yaml：
- `pos: [x, y, z]` → `pos: [float(x), float(y), float(z) * layer_height]`
- terrain `bounds + base_z + height` → `shape: box + pos: center + size: dims`
- 删 `blocks_los / cover` 字段（compiler 会从几何重算）
- 模型加 `model_height_mm: 32`（默认值）+ 大型保留 `45`

迁移 third-blood 作为验证集。

### A.3 完成判定

- [ ] 新 schema 在 `output/TrenchCrusade/matches/match-template.yaml` 落地
- [ ] 迁移脚本能跑通 third-blood + test-match，输出可读 v0.3 yaml
- [ ] `coordinate-system.md` §1-3 改写（旧版本归档为 `coordinate-system-v0.2.md`）

### A.4 风险

- **schema 不兼容**：v0.2 yaml 不能直接读，需走迁移脚本；MCP server 启动时检测版本字段，拒绝读 v0.2 文件并提示
- **战场图迁移**：terrain primitives 写起来比 cell bounds 麻烦——预先准备 5-6 个常用 terrain template snippet（trench / ruin / hill / crater field / barbed wire / objective）

---

## Phase B — `terrain_compiler.py`：YAML → trimesh + Three.js JSON（1 工作日）

**目标**：单一 SSoT，输出 Python 和 JS 两端都能读的 mesh。

### B.1 模块结构

```
tools/mcp-server/src/
├── terrain_compiler.py        ← 新
├── geometry/
│   ├── __init__.py
│   ├── primitives.py          ← box/cylinder/ramp/volume 构造器
│   ├── raycast.py             ← trimesh 包装（LOS / cover）
│   └── nav.py                 ← A* / dijkstra on terrain
└── ...
```

### B.2 编译流程

```python
def compile_terrain(match_state: dict) -> CompiledScene:
    """
    输入：match-state.yaml dict
    输出：CompiledScene {
      trimesh_scene: trimesh.Scene,    # Python raycast 用
      three_json: dict,                 # Three.js BufferGeometry JSON
      nav_graph: dict,                  # A* 用（0.5" 间隔节点图）
      bbox: tuple,                      # 战场 bounding box
    }
    """
```

**输出文件**（compile 后写入 match 目录）：
- `matches/<name>/terrain.glb`（trimesh 直读，二进制）
- `matches/<name>/terrain.three.json`（Three.js 直读，文本）
- `matches/<name>/nav.pickle`（A* graph 缓存，避免每次重算）

`save_match` 在 terrain 节有变化时**自动重 compile**（hash 比对）；模型 pos 变化不触发 recompile。

### B.3 Three.js JSON 格式

用 Three.js 原生 `BufferGeometry.toJSON()` 输出，避免自定义 parser：

```json
{
  "scene_version": "0.3",
  "objects": [
    {
      "id": "trench_central",
      "type": "trench",
      "geometry": { /* BufferGeometry.toJSON() output */ },
      "transform": [1,0,0,0, 0,1,0,0, 0,0,1,0, 18,18,-1.5,1],
      "material_hint": { "color": "#3a2820", "opacity": 1.0 }
    },
    ...
  ]
}
```

Three.js 端：

```js
const loader = new THREE.BufferGeometryLoader();
fetch('terrain.three.json').then(r => r.json()).then(scene => {
  scene.objects.forEach(obj => {
    const geom = loader.parse(obj.geometry);
    const mat = new THREE.MeshStandardMaterial(obj.material_hint);
    const mesh = new THREE.Mesh(geom, mat);
    mesh.applyMatrix4(new THREE.Matrix4().fromArray(obj.transform));
    scene.add(mesh);
    // 同时作为 raycast 目标
    raycastTargets.push(mesh);
  });
});
```

### B.4 测试

`tests/test_terrain_compiler.py`：

- box 5×2×3 在 origin → trimesh box dims 一致
- ramp 高 3" 宽 1" 长 2" → 法向斜率正确
- 同一 yaml compile 两次 → 输出 hash 一致（决定性）
- compile 后 trimesh raycast 与 Three.js raycast 在 10 个采样点结果一致（运行 puppeteer / node 跑 Three.js 端）

### B.5 完成判定

- [ ] `compile_terrain(state)` 返回 3 个产物
- [ ] save_match 在 terrain hash 变化时自动 recompile（其他时候不重做）
- [ ] tests pass（含两端 raycast 一致性）
- [ ] third-blood 迁移版能 compile，输出 `terrain.glb` + `terrain.three.json`

### B.6 风险

- **trimesh ↔ Three.js 几何不一致**：trimesh 默认 Y-up 转 Z-up 时偶尔翻法向；写 compile 时显式指定坐标系，并加单测在两端采 10 点 raycast 对比
- **复杂 ruin 多 box 组合 perf**：v0.3 战场全 mesh 量级 ~50-100 primitives，单次 raycast O(log N) BVH 不是问题；nav graph 0.5" × 36×36 战场 = ~5000 nodes × 8 edges，pickle 几 MB

---

## Phase C — MCP raycast 化（3 工作日）

**目标**：4 个核心几何工具用真 mesh 重写；旧 stub 删除。

### C.1 升级清单

| 工具 | v0.2 实现 | v0.3 实现 |
|---|---|---|
| `get_distance` | 3D 欧氏 on cell × layer_height | 3D 欧氏 on float inches（公式不变，输入变） |
| `get_los(from, to)` | Bresenham + cell `blocks_los` flag | trimesh raycast(from_eye, to_eye) → `{state, blocker_id, hit_pos}` |
| `get_cover(from, to)` | 检查直线沿途 cell `cover` flag | 取 model 5 个采样点（head / shoulders×2 / hips×2），统计 raycast 命中比例 → none / partial / full |
| `get_terrain_at(pos)` | 查 cell `terrain` 列表 | `point-in-mesh` 测试，返回该点所在的 primitive 列表 |
| `validate_move(from, to, M, type)` | cell pathfind + cost | A* on nav_graph，边权含 movement_cost + climb cost + dangerous + falling trigger |
| `valid_charge_paths(model, target)` | stub: dist + LOS | A* 最短路径 + interposing enemy 检测 + ≤12" + LOS 起点验证 |
| **新**：`valid_move_area(model_id, M, dash?)` | — | Dijkstra 从模型当前位置，返回所有可达点 polygon（给 UI 高亮用） |

### C.2 `get_los` 详细算法

```python
def get_los(from_pos, to_pos, match_name) -> dict:
    """
    眼位 = pos.z + model_height_mm/25.4 - 0.2  (距头顶 ~5mm，模拟眼睛位置)
    raycast from shooter_eye → target_eye via trimesh scene.intersects_first()
    返回：{
      state: "clear" | "partial_cover" | "full_cover" | "blocked",
      blocker_id: str | None,
      hit_pos: [x, y, z] | None,
      cover_modifier: -1 | -2 | None  # 套用到 Success Roll
    }
    """
```

- `clear`：raycast 不命中任何 terrain → 无修正
- `partial_cover`：≥50% < 100% 的采样 raycast 命中 cover-type terrain → -1 DICE
- `full_cover`：100% 命中 cover → -2 DICE（PDF 部分武器忽略）
- `blocked`：100% 命中 LOS-blocking terrain（如实心墙） → 不能射击

### C.3 `valid_move_area` 给 UI 用

```python
def valid_move_area(model_id, match_name, include_dash=False) -> dict:
    """
    从模型当前位置 Dijkstra，nav_graph 节点间距 0.5"
    返回：{
      reachable_polygons: [          # 按 z 层分组，方便 UI 画多层 mesh
        {z: 0.0, polygon: [...]},     # 地面可达
        {z: -3.0, polygon: [...]},    # 战壕底可达
        {z: 3.0, polygon: [...]},     # 屋顶可达
      ],
      max_movement: 6.0,              # 模型 M characteristic
      with_dash: 12.0                 # 含 Dash 总距离
    }
    """
```

UI 拿这个数据画半透明地毯 mesh overlay。

### C.4 `validate_move` 现在变成 nav_graph 查询

```python
def validate_move(model_id, to_pos, move_type, match_name) -> dict:
    """
    A* on nav_graph from model.pos to to_pos
    返回：{
      valid: bool,
      path: [(x,y,z), ...],            # 实际走的路径（UI 可画虚线预览）
      movement_used: float,
      triggers: ["risky_climb", "falling_3in", "dangerous_barbed_wire"]
    }
    """
```

Risky climb / falling 触发自动产生 trigger，AI 看到 trigger 知道要调对应 dice 工具。

### C.5 测试

`tests/test_coord_v3.py`：

- **LOS / cover 矩阵**（10 用例）：trench wall 边缘豁免 / ruin 角后 partial cover / open ground clear / 烟雾穿过 / 多层 ruin 屋顶看下来
- **valid_move_area**（5 用例）：M=6 平地圆形 / 含 trench 自动绕路 / 含梯子可上屋顶 / 含 dangerous 边权高 / dash 多倍距离
- **valid_charge_paths**（5 用例）：直线 / interposing enemy 阻挡 / LOS 阻挡 / 超 12" / 终点 1" within
- **回归**：旧 cell-based 测试改写成 float-input，逐条对照（保留 PDF spec 案例）

### C.6 完成判定

- [ ] 4 个工具升级 + 1 个新增（`valid_move_area`）
- [ ] 删除旧 stub 代码 + 文档标注
- [ ] tests pass + 覆盖率 ≥85%
- [ ] AI 在 sample turn 中调用新工具，结果与玩家在浏览器看到的一致

### C.7 风险

- **trimesh raycast perf**：单次 raycast ~0.1ms（BVH），AI 一个 turn 调几十次没问题
- **nav_graph 重建**：terrain 不变就缓存，单 match 一次性建图 ~30s（5000 nodes Dijkstra）；可接受
- **climb-aid 建模**：v0.3 用 cell-level `climb_aids: [{at_pos, target_pos}]` 标注，A* 把这对节点加 0-cost 边（梯子免 Risky）
- **既有 third-blood 现场迁移**：z=-1 旧坐标 → z=-3.0 新坐标；模型位置批量重算需写脚本

---

## Phase D — Three.js 纯预览层（2-3 工作日）

**目标**：浏览器自跑 raycast + A*，鼠标点击 / hover 即时显示，零后端调用。

### D.1 新模块

```
tools/mcp-server/src/render_three.py  ← 扩展
  + 嵌入 nav_graph.json（B phase 输出的简化版，浏览器 A* 用）
  + 注入新前端 JS 代码（见 D.2）
```

或者拆出 JS bundle：

```
tools/mcp-server/src/three_assets/
  ├── viewer.js              ← 现有 inline JS 提到这里
  ├── raycast_preview.js     ← 新
  ├── pathfind.js            ← 新（A* on nav_graph）
  └── hud.js                 ← 新（HUD 坐标显示）
```

### D.2 三个交互

**(1) Click model → 高亮可达区**

```js
function onModelClick(modelId) {
  const moveArea = computeMoveArea(modelId);  // 浏览器本地 A*
  drawReachableOverlay(moveArea);              // 半透明地毯 mesh
  drawDashOverlay(moveArea, {dashColor: true}); // dash 区另一颜色（条件）
}

// ESC / click empty → clear
function clearOverlays() { ... }
```

可达区表示：用 Convex Hull 或 Marching Squares 把 reachable nodes 转成多边形 mesh，半透明叠加。多 z 层各画一层。

**(2) Hover target → 画射击 ray**

```js
function onTargetHover(shooterId, targetId) {
  const result = browserRaycast(shooter.eye, target.eye);
  drawRayLine(shooter.eye, target.eye, {
    color: {clear: 0x00ff00, partial_cover: 0xffff00, blocked: 0xff0000}[result.state],
    dashed: result.state === 'blocked'
  });
  showTooltip(result);  // "Clear · estimate -0 DICE"
}
```

**(3) HUD 实时坐标**

右下角小框：
```
📍 (15.3, 22.0, 0.0)        ← 鼠标 world pos（投射到地面）
🎯 yeoman_1 → distance 4.2" ← 选中模型 + 鼠标点距离
[copy coords]               ← 一键复制粘 chat
```

### D.3 交互不动 state

**所有预览仅渲染，不调任何 MCP**。玩家"决定"还是要回 chat 说"move yeoman to (15.3, 22.0)"。

### D.4 完成判定

- [ ] Click model 1 秒内显示可达区高亮
- [ ] Hover target 显示彩色 ray + cover 提示
- [ ] HUD 显示坐标 + 复制按钮
- [ ] ESC 清空所有 overlay
- [ ] 在 third-blood 迁移版上跑通

### D.5 风险

- **浏览器 A* perf**：5000-node graph A* < 50ms，无感知
- **多 z 层 overlay 视觉乱**：默认只显示当前选中模型所在 z 层的 reachable；其他层按住 Alt 才显示
- **Three.js raycaster vs trimesh 差**：B phase 已经测过一致性；D phase 用同 mesh，结果应一致

---

## Phase E — 迁移测试 + 文档回填（1 工作日）

### E.1 步骤

1. 跑迁移脚本把 third-blood final state 转 v0.3
2. 在新 viewer 里打开，肉眼核对：trench 位置 / model 位置 / ruin 形状对得上
3. 跑一个 sample turn（AI 激活一个模型），日志对比 v0.2 和 v0.3 的 distance / LOS 结果
4. 把所有"v0.2 实操陷阱"过一遍，确认 v0.3 是否消除：
   - validate_move v0.5 stub → ✅ 消除（A* 真实现）
   - get_terrain_at 签名变化 → 用 float
   - MCP cache reload → 不变
   - 武器 Range 编码 → 不变
5. 更新 `CLAUDE.md`：
   - "v0.2 实操陷阱" → 留作历史，新加 "v0.3 实操陷阱"
   - 坐标 / LOS 说明改写
6. 更新 `coordinate-system.md` §1-8（旧版本归档）

### E.2 完成判定

- [ ] third-blood 迁移版可玩（AI 能继续出招）
- [ ] CLAUDE.md / coordinate-system.md 更新
- [ ] v0.2 → v0.3 changelog 写好（给玩家看的）
- [ ] 旧 cell-based 文档归档（不删，加 deprecation banner）

---

## 2. 风险点 / 决策点

1. **schema 不兼容**：v0.2 yaml 不能读，必须走迁移脚本——MCP server 启动时检测版本字段，拒绝 v0.2 文件并提示。**third-blood 迁移失败 = 整个 v0.3 滞后**，A 阶段务必先把迁移脚本搞稳
2. **trimesh / Three.js 几何不一致**：B phase 加单测两端对比 10 采样点；不一致就 rollback compile 流程
3. **nav_graph 内存**：5000 nodes × edges + cache pickle ~5MB，单 match 可接受；多 match 切换要清缓存
4. **UI overlay 视觉超载**：多 z 层全显示乱，默认按选中模型层；Alt 切换
5. **Mesh BVH 性能**：trimesh 默认有 BVH，单 raycast 0.1ms；AI 一 turn ~50 raycast，总 5ms，OK
6. **v0.4 UI 直驱 state**：暂不做，但 schema 要预留 — 模型 `pos` 必须是 server-authoritative，浏览器只读

---

## 3. v0.3 不做但要记得的

- **GLB 导入支持**（v0.4）：允许 terrain primitive 指向外部 .glb 文件（复杂建筑 / 战车），不只是 box/cylinder
- **WebSocket UI driver**（v0.4）：浏览器直接 commit state；要解决 AI 同步通知
- **多 match 并行**：v0.3 仍假设单 match 在打；多 match 切换 nav cache 清理
- **战场编辑器**：v0.3 用户手写 terrain yaml；v0.5 加 web 编辑器
- **复杂 cover 规则**：PDF 有"防御工事 Defended Obstacle"概念，v0.3 仅用 partial/full 二分；v0.4 细化

---

## 4. v0.4+ Backlog（v0.2 顺延 + v0.3 新增）

**v0.2 顺延**：
- 4 待导 faction（Pilgrims / Iron Sultanate / Black Grail / Court Serpent）
- Campaign Rules（Patrons / Trauma / Promotions / Glory Items）
- 剩余 10 scenarios
- Mercenaries
- 多 AI 对战

**v0.3 新增**：
- UI → MCP 直驱（WebSocket / HTTP bridge）
- GLB 导入
- 战场编辑器
- 复杂 cover / 防御工事
- 烟雾扩散 / 风向（基于体积体随 turn 漂移）

---

## 5. 启动检查清单（Phase A 开工前）

- [ ] third-blood 比赛已结束（main worktree 干净，没有进行中的 match-state.yaml 变更）
- [ ] v0.2 已知遗留确认：valid_charge_paths stub / validate_move z 漏洞 都会在 v0.3 Phase C 消除
- [ ] 决定 worktree 名：建议 `.claude/worktrees/v0.3-continuous-coords`
- [ ] 在新 worktree 装 `trimesh` + `pyglet`（trimesh 可视化用）
- [ ] 在新 worktree 跑通现有 146 tests 作 baseline
- [ ] 读本文件 Phase A 准备实施
- [ ] **不要**在 main worktree 改 schema（会污染未来比赛回归）

---

## 6. 阶段验收 demo 脚本（可选，给非工程评估用）

每 phase 结束跑一个 30 秒 demo：

- **Phase A**：`/usr/bin/python3 scripts/migrate_v02_to_v03.py matches/third-blood/match-state.yaml` 输出新 yaml + diff
- **Phase B**：compile terrain，打开 trimesh viewer 看战场 mesh
- **Phase C**：MCP 调 `get_los(trench_inside, behind_ruin)` 返 blocked + blocker_id
- **Phase D**：浏览器 click 模型，看到可达区高亮；hover 敌人，看到红色 ray
- **Phase E**：third-blood 复刻完整跑一个激活
