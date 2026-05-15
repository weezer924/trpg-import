# matches/coordinate-system: 坐标系 / 距离 / LOS / 地形 契约

> 源：本项目自创契约（Trench Crusade v1.0.2 PDF 未规定数字坐标系）
> 语义映射：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.30-49
> 版本：v0.1（与 PDF v1.0.2 配套）

## Index

- [1. 范围与用途](#1-范围与用途)
- [2. 坐标系统](#2-坐标系统)
- [3. 距离测量](#3-距离测量)
- [4. 战场默认](#4-战场默认)
- [5. 棋子基座](#5-棋子基座)
- [6. 视线判定算法规约（LOS）](#6-视线判定算法规约los)
- [7. 地形模型](#7-地形模型)
  - [7.1-7.3 v0.4 bounds-based（语义参考 + 7 类对照）](#71-bounds-两种格式)
  - [**7.4 v0.5 cell-keyed schema（实际 yaml + edge 模型）**](#74-v05-cell-keyed-schema实际-yaml-形式)
- [8. MCP server 接口草案](#8-mcp-server-接口草案)
- [9. 实施 checklist（给 Pass 2+ rules 作者）](#9-实施-checklistgive-pass-2-rules-作者)

---

## 1. 范围与用途

本文件是 **MCP server / web UI / AI 对手** 三方对战场状态的**契约**，先于 `rules/*` 任何章节导入。

为什么先写：

- PDF v1.0.2 用**实体卷尺测距 + 蹲下检查视线**作为裁判方式（p.30-31「stoop down and take a look」）；
  数字化对战必须用**数学规约**替代这两个动作，否则 MCP 没法仲裁、AI 没法计算。
- 所有 `rules/*` 章节里的"12 英寸内冲锋""半射程 long range""−1 dice cover"等数值，
  最终都要落到本文件定义的 `get_distance` / `get_los` / `is_in_range` 上。
- 任何后续规则文件若与本契约语义冲突，**以 PDF v1.0.2 为准修正本契约**，
  本文件被改后所有引用它的 rules 章节需重新校对。

**适用范围**：

| 消费者 | 用本契约的什么 |
|---|---|
| MCP server | §8 的 6 个接口签名（实现层依据） |
| Web UI（玩家拖动棋子） | §4 战场默认 + §5 基座 + §7 地形 schema |
| AI 对手 | §3 距离 + §6 LOS 三态 → 决策时不心算，调 MCP |
| 战场存档 `matches/{name}/match-state.yaml` | §7 terrain schema + §4 battlefield 顶层字段 |

---

## 2. 坐标系统

### 2.1 单位尺度

- **1 格 = 1 英寸（inch）**。PDF 所有距离数值（M / 武器射程 / charge 12" / cover ½" 等）直接套用，无需换算。
- 位置用整数三元组 `(x, y, z)`。**亚格位置（如 0.5 格）不允许**——所有移动/部署落到整数格中心点。
  > 损失少量精度，换取 LOS 算法与战场可视化的稳定性。PDF p.30「Within」定义距离用最近点测量，整数离散化后误差 ≤ 0.5 格。

### 2.2 原点与轴向

- 原点 `(0, 0, 0)` 在**战场左下角，z=0 层（地面）**。
- `x` 轴向右、`y` 轴向上、`z` 轴向上（垂直方向）。
- 默认战场范围：`x ∈ [0, 35]`、`y ∈ [0, 35]`（36×36 格）。

### 2.3 z 轴：离散层级（非连续高度）

| z 值 | 含义 | 默认高度差（"） |
|---:|---|---:|
| `2` | 屋顶（多层建筑顶） | 6 |
| `1` | 二楼 / 丘陵顶 | 3 |
| `0` | 地面（默认） | 0 |
| `-1` | 战壕凹陷 / 弹坑底 | -3 |

- 每个 z 层级对应的实际英寸高度由顶层字段 `layer_height` 控制，**默认 3"**，[v0.1 默认，可调]。
- 单个地形（如双层建筑）可在自身 yaml 中用 `layer_height` 字段 override：

  ```yaml
  - type: building
    bounds: [10, 10, 16, 16]
    height: 2          # 顶部在 z=2
    layer_height: 4    # 这栋楼每层 4"（不是默认的 3"）
  ```

- **为什么离散**：PDF 没有连续高度概念，只用"½" 高""3" 高""6" 高"等离散坎。把 z 离散化让 MCP 可以稳定计算高低差，且匹配 PDF "elevated +1 DICE 要求高 3"+ "（p.43）的判定。

### 2.4 坐标合法性

- 模型 `pos = (x, y, z)` 合法当且仅当：
  - `0 ≤ x < battlefield.size[0]`、`0 ≤ y < battlefield.size[1]`
  - z 存在对应的可站立表面（地面 z=0 永远可站；z=1/2 需有 building/hill 在该 (x,y) 提供；z=-1 需有 trench 在该 (x,y) 提供）
- 基座占多格时，**所有占据格**都必须满足上述条件。

---

## 3. 距离测量

### 3.1 算法：3D 欧几里得

```
distance(A, B) = √((Bx - Ax)² + (By - Ay)² + ((Bz - Az) · layer_height)²)
```

- 结果保留 **1 位小数**（向下截断到 0.1）。
- z 层差乘以 `layer_height`（默认 3"）换算成英寸后参与欧式距离。
- 模型基座 > 1×1 时，**取双方基座间最近点距离**（PDF p.30「distance between the nearest points」）。
  → 在数字网格上落地为：`min(distance(a, b) for a in A.cells for b in B.cells)`。
- 完全相同的 (x, y, z) → 距离 0；同格不同 z → 距离 = `layer_height`。

### 3.2 与 PDF 的语义映射

| PDF 术语 | 本契约 |
|---|---|
| Within X" of（p.30）| `get_distance(A, B) ≤ X` |
| In contact（p.30）| `get_distance(A, B) ≤ 0` 或基座格相邻且距离 ≤ 1.0（基座间隙） |
| Within 1" of enemy（locked in melee，p.36）| `get_distance ≤ 1.0` |
| Short Range（≤ 半射程，p.43）| `get_distance ≤ weapon.range / 2` |
| Long Range（> 半射程，p.43）| `get_distance > weapon.range / 2` |
| Elevated +1 DICE（高 3"+，p.43）| `(attacker.z - target.z) · layer_height ≥ 3` |

### 3.3 测试用例

| # | 用例 | 输入 A | 输入 B | 期望距离 | 备注 |
|---|---|---|---|---:|---|
| 1 | 纯平面相邻 | `(5, 5, 0)` | `(8, 5, 0)` | `3.0` | 横向 3 格 |
| 2 | 平面对角 | `(0, 0, 0)` | `(3, 4, 0)` | `5.0` | 3-4-5 三角 |
| 3 | 同列上下 | `(10, 10, 0)` | `(10, 10, 1)` | `3.0` | z 差 1 × layer_height 3 |
| 4 | 立体复合 | `(0, 0, 0)` | `(4, 0, 1)` | `5.0` | √(16+0+9) = 5 |
| 5 | Charge 12" 临界 | `(6, 6, 0)` | `(15, 14, 1)` | `12.4` | √(81+64+9)≈12.4 → **不可冲锋**（PDF p.36 「visible and within 12」） |
| 6 | 战壕下射上方 | `(5, 5, -1)` | `(5, 12, 1)` | `9.2` | z 差 2 层 = 6"，平面 7"，√(49+0+36)≈9.2 |

> **注意用例 5**：M6 模型 charge 总移动可达 6 + d6（最大 12"），但 `is_in_range(..., 12)` 在距离 12.4" 时返回 false，**不能宣告冲锋目标**。
> 这是离散化的代价；PDF 用卷尺实测会有类似的边缘案例。AI 若想 charge 应优先调 `is_in_range(target, 12)` 而不是心算。

---

## 4. 战场默认

| 字段 | v0.1 默认 | 备注 |
|---|---:|---|
| `battlefield.size` | `[36, 36]` | 3'×3' 入门战场，PDF 推荐尺寸 |
| `battlefield.size`（扩展） | `[48, 48]` | 4'×4'，多人或大战团用 |
| `battlefield.layer_height` | `3` | 每个 z 层等多少英寸 [v0.1 默认，可调] |
| 单方模型数 | 6–10 | 控制状态复杂度；PDF Warbands 章节标准战团规模 |
| 部署区 | 战场左右 12" 内 | 实际由 scenario 决定，本字段仅作默认 |

战场顶层 yaml schema：

```yaml
battlefield:
  size: [36, 36]       # [width, height] in 1" cells
  layer_height: 3      # inches per z level
  deployment:
    red: [0, 0, 12, 36]   # 左侧 12 格
    blue: [24, 0, 36, 36] # 右侧 12 格
```

`deployment` 的 bounds 是 `[x_min, y_min, x_max, y_max]`，与地形 `bounds` 字段同格式。

---

## 5. 棋子基座（base size）

### 5.1 两层语义（grid 占用 vs 视觉/物理）

base 的描述**分两层**，解耦 grid 占用与视觉形状：

| 层 | 字段 | 用途 |
|---|---|---|
| **Grid 占用** | `base_size: [w, h]` | 决定占哪些格 / snap / 不可重叠判定 / 距离中心点 |
| **视觉与物理** | `base_shape` + `base_dimensions_mm` | UI 渲染基座 + 未来 edge-to-edge 精确判定（v0.1 不强制） |

**v0.1 grid 占用仅正方形** —— `[1, 1]` 或 `[2, 2]`。引入长方形（`[1, 2]` 等）会强制 facing 朝向规则；TC 原版允许 free pivot（PDF p.35「Moves」），v0.1 不引入 facing。详见 §5.6 Open Questions。

### 5.2 三档分类表（按实际基座尺寸）

| 实际 base | `base_size` | `base_shape` | 典型单位 |
|---|:---:|---|---|
| ≤32mm 圆 | `[1, 1]` | `circle` | 步兵、精英 |
| 40mm 圆 / 25×50mm 椭圆 | `[1, 1]` 或 `[2, 2]`（按最大边） | `circle` / `oval` | 重型步兵、骑兵、机械化重装 |
| ≥50mm 圆 / 30×60mm 椭圆 | `[2, 2]` | `circle` / `oval` | 大型怪物、构造体 |

**40mm 归档判断**：单边超过 1.5"（约 38mm）则升 `[2, 2]`，避免占用过紧。具体单位由 Pass 8-9 在各 warband profile 中标注。

**取消 `[3, 3]` 一档**：Brazen Bull 等"非常巨大"单位实际基座约 60mm = 2.36"，2×2 (2") 已能容纳（视觉层用 `base_dimensions_mm: [60, 60]` 表达精确大小）。3×3 是过度设计。

### 5.3 字段定义

| 字段 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `base_size` | `[int, int]` | `[1, 1]` | grid 占用宽 × 深；v0.1 仅正方形 |
| `base_shape` | enum `circle` / `oval` / `square` | `circle` | 视觉形状 |
| `base_dimensions_mm` | `[int, int]` | `[28, 28]` | 实际基座宽 × 深，mm；圆形时 W=D=直径 |

**`base_shape` 与 `base_dimensions_mm` 是可选视觉字段** —— v0.1 逻辑判定（距离、LOS、近战触发、占格）**只看 `base_size`**。视觉字段供：

1. UI 渲染基座圆/椭圆（让玩家一眼分辨步兵/骑兵/怪物）
2. 未来 edge-to-edge 精确判定扩展（如骑兵 charge 12" 临界，可选升级到边到边而非中心到中心）

### 5.4 实际基座归档（Pass 8-9 已回填）

PDF v1.0.2 没有"基座尺寸表"，各单位实际基座按 PDF Warbands 章节侧写中的 mm 标注归档。v0.1 已确认：

| 单位 | Faction | `base_size` | `base_shape` | `base_dimensions_mm` | 来源 |
|---|---|:---:|---|:---:|---|
| Mechanized Heavy Infantry | New Antioch | `[1, 1]` | `circle` | `[40, 40]` | PDF Warbands p.33；40mm 仍在 1.5" 阈值内（§5.2） |
| War Wolf Assault Beast | Heretic Legions | `[2, 2]` | `oval` | `[50, 50]` | PDF Warbands p.113；50mm 椭圆 → §5.2 升 `[2,2]` |
| Tank Palanquin rig (Heretic Priest, Trench Ghosts variant) | Heretic Legions | `[2, 2]` | `circle` | `[50, 50]` | PDF Warbands p.119 "Bulky: 50mm base" |

**v0.1 仅以上 3 个单位 base 非默认 `[1, 1]` 28mm**；其余主战团（NA 9 单位 + HL 8 单位 + variants）全部 `[1, 1]` circle，差别只在 dimensions（25mm Trooper / 32mm Elite）。

**v0.2+ 候选**（Warbands 扩展导入时回填）：
- Brazen Bull（Iron Sultanate v0.2.B） — 预测 `[2, 2]` circle
- Lord of Tumours（Black Grail v0.2.B） — 预测 `[2, 2]` circle

> **注**：导入前曾预测 Anchorite Shrine 为 `[2, 2]` 候选，Pass 8 实际导入发现 PDF Warbands p.21 仅在 lore 段提到 "wall-embedded battle shrines"，**v1.0.2 NA Warbands p.21-46 范围内没有可玩 Anchorite Shrine 单位**——预测错误已剔除。

### 5.5 占格规则

- 基座 `[w, h]` 的模型在 `pos = (x, y, z)` 占据格 `(x..x+w-1, y..y+h-1, z)`
- 这些格不能与另一模型基座或 `IMPASSABLE` 地形重叠（PDF p.31「Model Placement」）
- 1×1 模型的"contact"（PDF p.30）= 基座相邻（曼哈顿距离 1）
- 2×2 模型的"contact" = 任意一个占据格相邻

### 5.6 Open Questions（v0.1.5+）

- **长方形 / 椭圆精确占用**：v0.1 椭圆基座视为最大边等效正方形（25×50mm 椭圆按 50mm 归档）。v0.2+ 引入骑兵冲锋专属规则时再决定：
  - 是否引入 `facing: 0/90/180/270` 字段
  - 是否支持 `base_size: [1, 2]` 长方形 grid 占用
  - 自由旋转 vs 离散 4 方向的取舍
- **40mm 边缘归档阈值**：当前 1.5" 是经验值。Pass 8-9 实测后调整
- **edge-to-edge 距离判定**：v0.1 用中心到中心距离（简洁）。若 charge 12" / 近战 1" 临界场景出现误差感，未来可升级到使用 `base_dimensions_mm` 的边到边距离

---

## 6. 视线判定算法规约（LOS）

### 6.1 接口契约

```
get_los(from_pos, to_pos) -> { state: "clear" | "partial_cover" | "blocked", blockers: [terrain_id, ...] }
```

- 输入：两个 `(x, y, z)` 三元组。PDF 规定测量 line of sight 时**不算 target 的 base / hands / feet / 武器**（p.30）——
  数字化简化为：from = 攻击方基座中心，to = 目标基座中心。
- 输出三态对应 PDF 语义：

| 输出 state | PDF 映射 | TC ranged attack 修正 |
|---|---|---|
| `clear` | 射线沿途无任何 terrain.blocks_los | 无修正 |
| `partial_cover` | 射线擦过 `blocks_los: partial` 的地形 / 目标 in cover | **−1 DICE**（PDF p.43 Cover 修正） |
| `blocked` | 射线被 `blocks_los: true` 的实体阻断 | **不可射**（PDF p.42「target must be in the Line of Sight」） |

### 6.2 算法描述（射线遍历 + 高度比较）

```
def get_los(A, B):
    blockers = []
    # 1. 沿 A→B 在 xy 平面用 Bresenham（或 DDA）取经过的格序列
    cells = bresenham_xy(A.xy, B.xy)
    # 2. 对每个中间格 c（不含 A、B 自身格），查该格 (cx, cy) 处所有 terrain
    for c in cells[1:-1]:
        for t in terrain_at(c):
            if not t.blocks_los:
                continue
            # 3. 高度比较：地形是否伸到射线在该格的高度？
            #    射线高度 = lerp(A.z, B.z, progress) × layer_height
            ray_z_inches = interpolate_z(A, B, c) * layer_height
            terrain_top_inches = (t.base_z + t.height) * layer_height
            terrain_bottom_inches = t.base_z * layer_height
            if terrain_bottom_inches < ray_z_inches < terrain_top_inches:
                blockers.append(t.id)
                if t.blocks_los == True:
                    return { state: "blocked", blockers }
                # blocks_los == "partial" → 继续遍历，但记下
    # 4. 检查 target 是否 in cover（PDF p.38 三问改造）
    if any(t.blocks_los == "partial" for t in blockers):
        return { state: "partial_cover", blockers }
    # 5. 也要看 target 本身是否站在 cover 地形里（PDF p.38）
    if target_in_cover(B):
        return { state: "partial_cover", blockers: cover_pieces_around(B) }
    return { state: "clear", blockers: [] }
```

**target_in_cover(B)** 实现 PDF p.38 的"三问"：

1. B 是否触碰至少 ½" 高的 terrain piece？（接触 = B 占据格与 terrain 占据格相邻或重叠）
2. 该 terrain piece 是否与 B 基座等宽或更宽？（terrain bounds 宽度 ≥ B 基座宽度）
3. 该 terrain piece 是否位于 B 与攻击方之间？（terrain 中心点在 A→B 线段附近，垂直距离 ≤ 1 格）

三问全 yes → `partial_cover`。

### 6.3 测试用例

| # | 场景 | A | B | 地形 | 期望 state | 备注 |
|---|---|---|---|---|---|---|
| 1 | 穿过双层楼 | `(2, 5, 0)` | `(20, 5, 0)` | `building bounds=[10,3,14,7], height=2, blocks_los=true` | `blocked` | 楼挡死 |
| 2 | 跨过低矮丘陵 | `(2, 5, 0)` | `(20, 5, 1)` | `hill bounds=[10,3,14,7], height=1, blocks_los=true` | `clear` | A 在 z=0 看 B 在 z=1（丘陵顶），射线终点高过丘陵顶 |
| 3 | 烟雾（partial） | `(2, 5, 0)` | `(20, 5, 0)` | `smoke bounds=[10,3,14,7], height=2, blocks_los=partial` | `partial_cover` | 烟挡视线但允许射，−1 DICE |
| 4 | 目标在战壕（cover） | `(2, 5, 1)` | `(20, 5, -1)` | `trench bounds=[18,3,22,7], height=-1` 在 B 周围 | `partial_cover` | target_in_cover 三问 yes |

---

## 7. 地形模型

> **导读**：§7.1-7.3 是 v0.4 bounds-based 的 PDF 语义对照（7 类地形 + 7 字段），保留作历史参考。**实际 yaml 是 v0.5 cell-keyed**：直接跳 [§7.4](#74-v05-cell-keyed-schema实际-yaml-形式)。adapter 层（match.py::cells_to_legacy_terrain）让 coord.py 仍按 §7.2 的 bounds-shape 工作。

### 7.1 bounds 两种格式

- **矩形（rect）**：`bounds: [x_min, y_min, x_max, y_max]`（4 个整数）→ 默认假设矩形地形。
- **多边形（polygon）**：`bounds_polygon: [[x1,y1], [x2,y2], ...]` → 非矩形（如不规则废墟）用此。

矩形是首选；polygon 仅在矩形拟合损失太大时用。

### 7.2 通用属性表

| 字段 | 类型 | 说明 |
|---|---|---|
| `type` | enum | 见 §7.3 七类 |
| `bounds` 或 `bounds_polygon` | rect/polygon | 占据格范围 |
| `base_z` | int（默认 0）| 地形底面 z 层 |
| `height` | int | 地形顶面与底面的 z 层差（如 building height=2 意为 2 层楼高） |
| `layer_height` | int（可选 override）| 该地形每层 z 等多少英寸；缺省继承 `battlefield.layer_height` |
| `blocks_los` | `true` / `false` / `partial` | 三态视线规约（§6） |
| `cover` | `none` / `partial` / `full` | 是否给在其内/旁的模型提供 cover keyword |
| `movement_cost` | float（默认 1）| 进入此地形每格消耗的移动力；`DIFFICULT TERRAIN` 通常 2 |
| `dangerous` | bool（默认 false）| 触发 PDF p.38 「DANGEROUS TERRAIN」keyword（移动时风险判定） |
| `impassable` | bool（默认 false）| 触发 PDF p.38 「IMPASSABLE TERRAIN」keyword（不能进入） |
| `climbable` | bool（默认 false）| 是否允许从此地形侧面 Climb（PDF p.39） |

> **⚠ 命名警告**：`cover: full / partial / none` 是描述地形给 in/on 模型提供的 cover **强度档**，但 v1.0.2 PDF 中 cover 关键词的**唯一机制效果**是 -1 DICE（不论 full/partial）。命名继承 PDF 表述，不代表数值差异。'full cover' 不等于'阻断射击'——阻断由 blocks_los: true 控制。

### 7.3 七类地形（对应 PDF p.38 + Battlefield archetype 章节）

> 中英对照 + 一行 PDF 语义 + yaml 例。

#### 7 类地形对照表

> 各类的**典型默认值**（每个 instance 可在 yaml 里 override 任一字段）。`mv_cost` 是每格基础移动消耗；`cover` 仅描述强度档，机制效果均为 -1 DICE（见 §7.2 命名警告）；`blocks_los` 三态见 §6。

| Type | z / Height | blocks_los | cover | mv_cost | climbable | dangerous | impassable | 备注 |
|---|---|---|---|---:|:---:|:---:|:---:|---|
| **A. trench**（战壕）| z=-1 / h=1 | false | partial | 1 | — | — | — | 凹陷 1"；进入或贴边获 cover；高度差 ≤3" 不触发 fall_3in |
| **B. ruins**（废墟）| z=0 / h=2 | partial | full | 1 | ✓ | — | — | 多层结构，可登顶；窗洞透视；登顶后从顶面射击算 high ground |
| **C. abandoned_corner**（废弃角落）| z=0 / h=1 | partial | partial | 1 | — | — | — | 破车 / 铁丝团 / 弹药箱；可作 cover 但不可登顶 |
| **D. hill**（山丘）| z=0 / h=1 | false | none | 1 | ✓ | — | — | 高地；丘顶赋 high ground +1 DICE（PDF p.43）|
| **E. dangerous**（危险地形）| z=0 / h=0 | false | none | 2 | — | ✓ | — | 铁丝网 / 雷区 / 毒气 / 烈焰；进入或穿越触发 Injury Roll |
| **F. difficult**（崎岖地形）| z=0 / h=0 | false | partial | **2** | — | — | — | 弹坑 / 泥潭 / 岩堆；触发 DIFFICULT TERRAIN（移动 2× 加权）|
| **G. landmark**（地标）| z=0 / h=0 | false | none | 1 | — | — | — | 旗 / 圣物 / 补给箱；纯 scenario 用途，无机制效果 |

> **混合地形提示**：同一格 cell 可叠多地形（例如 trench + dangerous_gas）。`get_terrain_at()` 返回全部，机制效果按各 keyword 叠加（见 [`tools/mcp-server/src/coord.py`](../../../../TrenchCrusade/tools/mcp-server/src/coord.py)）。

#### A. 战壕（Trench）

凹陷 z=-1 的长条结构，进入提供 cover。

```yaml
- id: trench_central
  type: trench
  bounds: [4, 17, 32, 19]      # 横贯战场的战壕
  base_z: -1
  height: 1                    # 顶面回到地面 z=0
  blocks_los: false            # 战壕本身不挡视线（只挡里面的人）
  cover: partial               # 在内或紧贴的模型获 cover
  movement_cost: 1
```

#### B. 废墟（Ruins）

破损建筑残骸，多层可攀爬，部分挡视线。

```yaml
- id: ruin_north
  type: ruins
  bounds: [10, 28, 16, 34]
  height: 2                    # 残存两层楼
  blocks_los: partial          # 透过窗洞能看见
  cover: full
  climbable: true
  movement_cost: 1
```

#### C. 废弃角落（Abandoned Corner）

无主物件堆（破车、铁丝团、弹药箱），通常 1 层。

```yaml
- id: junk_pile_a
  type: abandoned_corner
  bounds: [22, 8, 24, 10]
  height: 1
  blocks_los: partial
  cover: partial
  movement_cost: 1
```

#### D. 山丘（Hill）

高地，无遮挡但提供 high ground +1 DICE（PDF p.43）。

```yaml
- id: hill_east
  type: hill
  bounds: [28, 12, 34, 22]
  height: 1                    # 丘顶 z=1
  blocks_los: false            # 开阔丘陵不挡视线
  cover: none
  climbable: true              # 边坡可爬
  movement_cost: 1
```

#### E. 危险地形（Dangerous Terrain）

铁丝网 / 雷区 / 毒气 / 烈焰，触发 PDF `DANGEROUS TERRAIN` keyword。

```yaml
- id: barbed_wire_north
  type: dangerous
  subtype: barbed_wire         # 备选：minefield / poison_gas / fire
  bounds: [12, 16, 20, 18]
  height: 0
  blocks_los: false
  cover: none
  movement_cost: 2
  dangerous: true              # 移动进入时触发 Injury Roll
```

#### F. 崎岖地形（Difficult Terrain）

弹坑、泥潭、岩石堆，触发 PDF `DIFFICULT TERRAIN` keyword（移动减半）。

```yaml
- id: crater_field
  type: difficult
  subtype: craters             # 备选：mud / rocks / swamp
  bounds: [16, 8, 24, 14]
  height: 0
  blocks_los: false
  cover: partial               # 弹坑内可蹲
  movement_cost: 2
```

#### G. 地标（Landmark）

剧本目标点（旗、圣物、补给箱），通常无碰撞但有 scenario 意义。

```yaml
- id: relic_objective
  type: landmark
  subtype: relic               # 备选：flag / supply_crate / shrine
  bounds: [17, 17, 19, 19]     # 中央 2×2 区域
  height: 0
  blocks_los: false
  cover: none
  movement_cost: 1
  scenario_tag: claim_objective
```

---

### 7.4 v0.5 cell-keyed schema（实际 yaml 形式）

> v0.4 用 `terrain[]` + bounds 矩形；v0.5 改为 `battlefield.cells[]` per-cell 字典 + 顶层 `objectives[]`。本节是 **实际 yaml 形式 + edge 模型**，§7.1-7.3 仍保留作 PDF 语义参考。

#### 7.4.1 动因：cover 有两个来源

PDF Cover 规则（v1.0.2 p.38，见 `rules/04-battlefield-terrain.md` §3）混合了两个机制：

| 来源 | 触发 | 方向 | yaml 字段 |
|---|---|---|---|
| **Area cover**（在地形里） | 模型 base >50% 在 terrain bounds 内 → COVER keyword | **不分方向** | `cell.cover_area` |
| **Edge cover**（掩体在攻击线上） | terrain piece ≥½" 高 + ≥ base 宽 + 在 ray 上 + partially blocks LOS | **按攻击方向分** | `cell.edges.{N,E,S,W}` |

两者机械效果都是 **-1 DICE**，但触发条件完全不同。v0.4 把所有 cover 塞进单一 `cover:` 字段，无法表达 "沙袋只挡南面" 或 "Wolf 整体在掩体里"。v0.5 把两者拆开。

#### 7.4.2 yaml schema

```yaml
battlefield:
  size: [36, 36]
  layer_height: 3
  deployment: {...}
  cells:                          # ← 新：per-cell 字典列表（替代 terrain[]）
    - pos: [9, 4]                 # (x, y) 单格坐标
      stack: 0                    # 地面叠加层（hill=1-2, ruins=1, trench=0）
      depth: 1                    # 下沉深度（trench=1, 否则 0）
      types: [trench]             # 该 cell 上叠加的原始 type 列表
      subtypes: []                # 可选：[poison_gas, barbed_wire, pillbox, ...]
      cover_area: half            # area cover 强度（half / none）
      blocks_los: none            # ray 穿过此 cell 的 LOS 影响（none / partial / full）
      atmospheric: gas            # 可选：smoke / gas（穿过即 partial LOS）
      edges:                      # 四条边的"线性掩体"高度
        N: none                   # none / half / full
        E: none
        S: none
        W: none
      mv_cost: 1                  # 进入该 cell 每格消耗（PDF DIFFICULT TERRAIN 用 2）
      dangerous: false            # 标志位（barbed wire / poison gas → true）
      difficult: false
      climbable: false
      impassable: false
      source_ids: [red_front_line]  # 追溯：本 cell 来自哪些 v0.4 terrain instance

objectives:                       # ← 新：landmark 从 terrain 提出来
  - id: objective_relic
    pos: [17, 17]
    type: relic
    holder: null
    scenario_tag: claim_objective
    bounds_note: [17, 17, 18, 18]  # 可选：原 bounds 留作参考
```

**开阔地**：不在 `cells[]` 里（节省 36×36=1296 cell 的常见情况）。`get_terrain_at()` 对未在 cells 的 pos 返回 open 默认。

#### 7.4.3 type → preset 映射表（migration 用）

| v0.4 type | stack | depth | cover_area | blocks_los | 标志 | 备注 |
|---|---:|---:|---|---|---|---|
| `trench` | 0 | 1 | `half` | `none` | — | 战壕沉 -1"，模型在内获 cover |
| `ruins` | 1 | 0 | `half` | `partial` | climbable | 残墙模型透视 |
| `ruins`+subtype=`pillbox` | 1 | 0 | `half` | `partial` | climbable | **外缘 edges 自动 `full`**（碉堡墙，邻格不是 pillbox 时） |
| `abandoned_corner` | 1 | 0 | `half` | `partial` | — | 破车 / 弹药箱 |
| `dangerous` | 0 | 0 | `none` | `none` | dangerous | barbed wire 默认 |
| `dangerous`+subtype=`poison_gas` | 0 | 0 | `none` | `partial` | dangerous, **atmospheric:gas** | 穿过 ray 衰减 |
| `difficult` | 0 | 0 | `half` | `none` | difficult | crater 蹲身 cover |
| `hill` | 1-2 | 0 | `none` | `none` | climbable | 高地无遮蔽 |
| `landmark` | — | — | — | — | — | 不进 cells，进 `objectives[]` |

> **z 转换**：v0.4 `base_z`/`height` 与 v0.5 `stack`/`depth` 满足 `base_z = -depth`、`height = stack + depth`。adapter 双向无损。

#### 7.4.4 edge model：facing cover for 线性掩体

> 这一节是 v0.5 的核心新增能力。Phase 1 只 pillbox 用；沙袋 / 半墙等线性 feature 是未来的扩展点。

**契约**：边是 **cell 的属性**，不是 model 的属性。每个 cell 存 4 条边的高度（`none` / `half` / `full`），与邻 cell **物理共享**（cell A 的 E 边 = cell B 的 W 边，迁移脚本保证两侧一致）。

**结算算法**（攻击方 A → 目标 B）：

1. **取 ray 主方向**（8 离散方向 N/NE/E/SE/S/SW/W/NW）
2. **取 B 的投影边集合**（B's base 在主方向外缘的边集）：
   - B 单格 25mm → 投影 1 条边（正方向）或 2 条边（斜方向）
   - B 多格 2×2 50mm → 投影 2 条边（正方向）或 4 条边（斜方向）—— `coordinate-system.md` §5.5 多格 base 外缘
3. **判定**：
   - 全部 `none` → no cover（投影空）
   - 至少一条 `half` 且无 `full` → cover (-1 DICE)
   - 至少一条 `full` 且其余 ≥ `half` → cover (-1 DICE)（**松裁决**：见 §7.4.5）
   - 全部 `full` → blocks LOS（不能瞄准）

**Wolf 2×2 base × edges**：Wolf 占 4 cell，外缘 8 条边，内边 4 条。**内边对自己的攻击结算无效**——内边只在 Wolf 移走后影响别的模型。

**攻击发起**：Wolf 射击时，**任一占用 cell 能画出 clear LOS 即可**（攻击端取最宽，对偶防御端取最严）。

#### 7.4.5 边角裁决（约定俗成）

| 情形 | 裁决 | 备注 |
|---|---|---|
| 投影一边 `full` 一边 `half` | **算 cover**（松） | 与 PDF "见到一部分就 cover" 精神一致 |
| Ray 恰好穿过 cell 顶点（45° / 135° 之类） | **取较严** 的相邻边 | 占位裁决，未来查 PDF errata 可调 |
| 攻击方向夹在两个 8-方向区间正中（如 22.5°） | 取**更严**的那个 facing | 同上 |

#### 7.4.6 模型高度

**规则数据**：模型自己多高 **不进 yaml**。PDF Cover 规则只引用 base 宽度 + 掩体高度，不引用模型高度。

**视觉数据**：渲染层按 `model.profile` 查表得视觉高度（圆柱高），**纯美术**。

**eye_height**：高地视野 LOS（Phase 2 才做）统一用 `eye_height = 1.0"`，不分模型。Phase 1 只用 `edges` 档位结算 cover/blocks，不算 ray-vs-height。

#### 7.4.7 atmospheric (smoke / gas)

`cell.atmospheric ∈ {gas, smoke}` 是 cell 内的雾气体积，**不是边上的墙**。LOS ray 穿过 atmospheric cell 即按 `blocks_los: partial` 处理（已在 migration 脚本里固化为 cell.blocks_los=partial）。Phase 1 不区分穿过 1 vs 2 vs 3 cell 的累计衰减，Phase 2+ 再考虑。

#### 7.4.8 adapter 层（coord.py 不动）

`tools/mcp-server/src/match.py::cells_to_legacy_terrain(state)`：

```python
def cells_to_legacy_terrain(state: dict) -> list[dict]:
    """v0.5 cell-keyed → v0.4 bounds-shape（per-cell 单格 bounds [x,y,x,y]）"""
    if "terrain" in state:                       # idempotent：测试 fixture 用 v0.4 直接返回
        return list(state["terrain"] or [])
    for c in state["battlefield"]["cells"]:
        yield {
            "id": c["source_ids"][0],
            "type": c["types"][0],
            "bounds": [x, y, x, y],
            "base_z": -c["depth"],
            "height": c["stack"] + c["depth"],
            "blocks_los": {"none": False, "partial": "partial", "full": True}[c["blocks_los"]],
            "cover": c["cover_area"],
            "movement_cost": c["mv_cost"],
            # ... 标志位
        }
```

调用点：`server.py` 4 处 + `match_cli.py` 5 处 + `render_html.py` 1 处。 coord.py 完全不知道有 v0.5——它继续按 v0.4 bounds-based 算法跑。

> 当我们要真正用 edges / atmospheric / facing-cover（Phase 2 重写 coord.py）时,把 adapter 退役。

#### 7.4.9 migration 工具

一次性脚本：`tools/migrate_terrain_v2.py`（已 commit `9c804aa`）。

```bash
.venv/bin/python tools/migrate_terrain_v2.py matches/{name}/match-state.yaml
# 输出: matches/{name}/match-state.v2.yaml（不动原文件）
```

逻辑：
1. 展开 `bounds` → cells list
2. 按 type preset（§7.4.3）填字段
3. 同 type 邻格之间的内边 = `none`
4. pillbox 外缘自动 = `full`
5. landmark → 顶层 `objectives[]`
6. 多个 instance 叠到同 cell → merge（stack/depth 取 max，cover/blocks_los 取 max 档位，flags 取 OR，types/subtypes 取 union）

已迁移：first-blood / second-blood / third-blood（commit `9c804aa`）。

---

## 8. MCP server 接口草案

仅函数签名 + 一行语义，**不写实现**。Pass v0.2 实际建 MCP server 时（参考 Mothership Python MCP）按此签名搭。

```python
# 1. 距离查询：欧氏 3D 距离（§3 算法），用于 within/range 判定
def get_distance(from_pos: tuple, to_pos: tuple) -> float: ...

# 2. 视线查询：返回三态 + 阻挡物列表（§6 算法）
def get_los(from_pos: tuple, to_pos: tuple) -> dict:
    # returns: {"state": "clear"|"partial_cover"|"blocked", "blockers": [str, ...]}
    ...

# 3. 射程内判定：组合距离 + 武器 short/long 信息
def is_in_range(from_pos: tuple, to_pos: tuple, weapon_range: int) -> dict:
    # returns: {"in_range": bool, "band": "short"|"long"|"out_of_range"}
    # 用于 PDF p.43 Short/Long Range 判定
    ...

# 4. 合法冲锋路径：枚举从 model 到 target 的可达路径（PDF p.36-37 charge 规则）
def valid_charge_paths(model_id: str, target_id: str) -> list:
    # returns: [path, ...]; path = [(x,y,z), ...]
    # 检查 LOS + 12" + interposing enemy（PDF p.36）+ shortest direct route（p.37）
    # 若无合法路径返回 []
    ...

# 5. 地形查询：返回某格上叠加的所有地形
def get_terrain_at(pos: tuple) -> list:
    # returns: [terrain_dict, ...]
    # 用于 cover / dangerous / movement_cost / impassable 检查
    ...

# 6. 移动合法性：给定起点 + 目标 + 移动类型，返回是否合法 + 实际消耗
def validate_move(model_id: str, to_pos: tuple, move_type: str) -> dict:
    # move_type ∈ {"move", "charge", "retreat", "dash"}
    # returns: {"valid": bool, "reason": str, "movement_used": float, "triggers": [...]}
    # triggers 含：dangerous_terrain_injury / fall_3plus / risky_success_needed 等
    ...
```

**实现优先级（v0.2 MCP server 建立时）**：
`get_distance` > `get_terrain_at` > `is_in_range` > `get_los` > `validate_move` > `valid_charge_paths`

---

## 9. 实施 checklist（给 Pass 2+ rules 作者）

写各 rules 章节时**必须引用**本文件对应节，不要重复定义、不要心算距离：

| 你要写的章节 | 涉及概念 | 引本文件哪节 | 提醒 |
|---|---|---|---|
| `rules/01-core-rules.md` | 基础回合 / 移动概览 | §3.2 PDF 术语映射表 | 用 `get_distance` / `is_in_range` 而非散文"测量距离" |
| `rules/02-comprehensive-rules.md` Movement 段 | Move / Charge / Retreat / Dash | §3、§5（基座占格）、§8 (`validate_move`) | Charge 12" 临界、interposing enemy 全靠 MCP 仲裁 |
| `rules/02` Ranged Combat | LOS / Short-Long Range / Cover / Elevated | §3.2 映射表、§6 LOS 三态、§6 target_in_cover 三问 | **绝对不要重复定义 LOS**，引 §6；Cover −1 DICE 来自 `state=partial_cover` |
| `rules/02` Melee Combat | within 1" / defended obstacle | §3.2（within 1" = `get_distance ≤ 1.0`）、§7 地形 height ≥ ½" | Defended obstacle 需查 §7 地形 height |
| `rules/02` Climbing & Jumping | 3" 高度坎、Falling | §2.3 z 层级、§3 距离 | Jumping Down ≥ 3" 触发 falling injury → PDF p.40-41 |
| `rules/03-keywords-glossary.md` | DIFFICULT / DANGEROUS / IMPASSABLE / COVER keywords | §7.2 通用属性表的字段语义 | keyword 定义里直接写"`movement_cost: 2`""`dangerous: true`"映射 |
| `rules/04-battlefield-terrain.md` | 七类地形 + battlefield archetype | §7.3 完整七类 yaml 例 | **直接引用本文件 §7.3**，不要重写 yaml 例；本节只写战场摆放规则 |
| `rules/05-battlekit.md` | 武器 range 字段 | §3.2 short/long range 映射 | YAML 武器块的 range.short / range.long 字段意义来自 PDF p.43 一半射程定义 |
| `rules/08-scenarios.md` | 部署区 / 地标 / VP | §4 battlefield.deployment / §7.3.G landmark | Scenario 用 landmark + scenario_tag 表示目标 |
| `warbands/*.md` | 单位 base_size + 视觉字段 | §5.2 三档分类 / §5.3 字段定义 / §5.4 待定回填 | 非 `[1, 1]` 或非 `circle` 时 yaml 块必须显式写出；回填 §5.4 候选表；遇骑兵/椭圆基座按"视觉 oval + grid 最大边等效"处理（不引入 facing） |
| `narrative/event-triggers.md` | LOS 阻挡时的 flavor | §6 三态 | "blocked" → 描述模型被掩体遮挡；"partial_cover" → 描述子弹擦过 |

**校验**：写完任一 rules 文件后，搜索文中是否包含"距离 / line of sight / cover 三问"等概念散文复述。若有，**改为引用本文件 §X**，避免规则漂移。

---

> 本文件后续若有数值调整（如 `layer_height` 默认值改变、第八个地形类引入），需同步更新所有引用本文件的 rules/* 章节。变更日志写入本文件顶部 `> 版本：` 行。
