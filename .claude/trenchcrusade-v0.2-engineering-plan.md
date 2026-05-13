# Trench Crusade v0.2 工程化计划

> **前置**：v0.1 已完成（13/13 Pass，~14000 行 markdown 规则文档 + 数字化契约 + 战团数据）。详见 [[trenchcrusade-import-guide]]。
> **v0.2 目标**：把 v0.1 文档转成**最小可玩对战环境**——完成一局完整的 Claim No Man's Land（New Antioch vs Heretic Legions）。
> **本文版本**：v0.2 plan v0.1（与 import guide §9.2 配套，扩展工程化部分）
> **总估时**：5-7 个工作日

---

## 0. v0.1 → v0.2 缺口表

v0.1 完成的是**纸面规则**，"开打"还差工具链：

| 缺口 | 原因 | v0.2 补位 |
|---|---|---|
| MCP server | coord §8 只列了 6 个接口**签名**，没实现 | Phase B |
| AI 不能心算契约 | coord §1 硬规："AI 不心算距离，调 MCP" → MCP 没建则 AI 必心算 | Phase B + C |
| match-state.yaml 工具 | schema 写了，没 CRUD 工具 | Phase B |
| 战团构建校验 | `roster-template.md` 给规范 + 自查清单，没自动校验器 | Phase B |
| AI 出招逻辑 | system prompt 完全没写 | Phase C |
| 战场可视化 | 玩家手编 yaml 体验差 | Phase D |
| sibling 项目 | import guide §7 写明 v0.2+ 才建 | Phase A |
| 实际试玩 | 第一局必暴露盲点 | Phase E |

---

## 1. Phase 概览

| Phase | 内容 | 依赖 | 估时 | 产出 |
|---:|---|---|---:|---|
| **A** | sibling 项目脚手架 | v0.1 ✅ | 0.5d | sibling 目录 + symlinks + .mcp.json 占位 |
| **B** | Python MCP server v0 | A | 1.5-2d | 6 接口 + 骰子工具 + yaml CRUD + roster 校验 |
| **C** | AI master prompt | B | 1d | system prompt + 决策树 + 拒绝违规请求护栏 |
| **D** | match-cli（CLI 文本 UI） | B | 1d | 玩家可看 / 移动 / 触发 AI 回合 |
| **E** | 试玩 + 文档回填 | A-D | 1-2d | 1 局完整 + friction 报告 + v0.1 文档增补 |

**v0.3+ 暂缓**：HTML 战场 UI / 多 scenario 测试 / campaign 模式 / 4 个待导 faction。

---

## Phase A — sibling 项目脚手架（0.5 工作日）

**目标**：建 `/Users/jack/Projects/trpg-projects/TrenchCrusade/`，让所有 v0.1 markdown 可被 AI 通过 symlink + .mcp.json 访问。

### A.1 目录骨架

```
TrenchCrusade/
├── rules/           → symlink dnd-rules-import/output/TrenchCrusade/rules/
├── warbands/        → symlink ...
├── matches/         → 不 symlink（本地需可写 match-state.yaml）
│   ├── coordinate-system.md → symlink ...
│   ├── match-template.yaml  → symlink ...
│   ├── roster-template.md   → symlink ...
│   └── test-match/          → 本地，测试用
├── narrative/       → symlink ...
├── lore/            → symlink ...
├── errata/          → symlink ...
├── rule books/      → symlink Rule Books/Trench Crusade/（PDF + txt 原文，AI 歧义回查用——无 md files/ 子目录）
├── tools/
│   └── mcp-server/  （Phase B 填）
├── .mcp.json        （Phase B 填，cwd 指向 sibling）
├── .claude/
│   └── CLAUDE.md    （sibling 项目说明 + AI 角色定位）
└── README.md        （人类玩家用：怎么开 AI、怎么开始一局）
```

### A.2 步骤

1. `mkdir -p TrenchCrusade/{tools/mcp-server,matches/test-match,.claude}`
2. 创建所有 symlinks（参考 Mothership sibling 的 ln -s 命令）
3. `matches/` **不能整体 symlink**——内部 markdown 和 schema 是 symlink，但 `test-match/` 必须本地可写
4. 写 sibling `.claude/CLAUDE.md`（~50 行）：
   - 项目身份 + AI 角色（Opponent + Battle Narrator，不是 GM）
   - 入口 → `rules/00-overview.md`
   - 必读 → `narrative/tone-guide.md`（语气）+ `narrative/world-primer.md`（意象）
5. 写 sibling `README.md`（~30 行）：玩家如何启动一局
6. `git init` + first commit

### A.3 完成判定

- [ ] `cd TrenchCrusade/ && ls rules/` 显示 7 个文件（00-overview / 01-core-rules / 02-comprehensive / 03-keywords / 04-terrain / 05-battlekit / 08-scenarios）
- [ ] `.claude/CLAUDE.md` 给清晰 AI 角色定位
- [ ] `matches/test-match/match-state.yaml` 可写（非 symlink）

### A.4 风险

- **Mothership sibling 是 Python MCP 唯一模板**（其他系统用 Node/TS）——参考它的 uv 配置 + .mcp.json 结构

---

## Phase B — Python MCP server v0（1.5-2 工作日）

**目标**：实现 coordinate-system §8 的 6 接口 + 骰子工具 + match-state.yaml CRUD + roster 校验。

### B.1 项目结构

```
tools/mcp-server/
├── pyproject.toml          （uv-managed, fastmcp + pyyaml）
├── README.md
├── src/
│   ├── __init__.py
│   ├── server.py           （MCP server 入口，注册 tools）
│   ├── coord.py            （§8 6 接口）
│   ├── dice.py             （骰子工具）
│   ├── match.py            （match-state.yaml CRUD）
│   └── roster.py           （roster 校验）
└── tests/
    ├── test_coord.py       （coord §3.3 6 距离 + §6.3 4 LOS 用例）
    ├── test_dice.py        （骰子分布测试）
    └── test_match.py       （yaml CRUD 集成测试）
```

### B.2 6 个 coord 接口实现

参考 `output/TrenchCrusade/matches/coordinate-system.md` §8 签名：

| 函数 | 输入 | 输出 | v0 实现要点 |
|---|---|---|---|
| `get_distance` | from, to | float | 3D 欧氏（§3.1 公式），保留 1 位小数 |
| `get_los` | from, to | `{state, blockers}` | Bresenham + 高度比较（§6.2 算法） |
| `is_in_range` | from, to, range | `{in_range, band}` | wrap distance + short/long 判定 |
| `get_terrain_at` | pos | `list[dict]` | 查 match-state.yaml `terrain` 节，返回该格的所有地形 |
| `valid_charge_paths` | model_id, target_id | `list[path]` 或 `[]` | LOS + ≤12" + interposing enemy + shortest direct route。**v0 可先 stub**（仅校验 distance + LOS，complex pathing 留 v0.5） |
| `validate_move` | model_id, to_pos, move_type | `{valid, reason, movement_used, triggers}` | 综合 distance + terrain cost + dangerous trigger 等 |

### B.3 骰子工具（6 个）

| 函数 | 用途 | 对应 PDF |
|---|---|---|
| `roll_2d6_success(plus_dice, minus_dice)` | Success Roll | rules/02 §1.4 |
| `roll_injury(plus_dice, minus_dice, modifier)` | Injury Roll | rules/02 §10 |
| `roll_bloodbath(plus_dice, minus_dice, deadly, modifier)` | Bloodbath Roll | rules/02 §11 |
| `roll_d6()` | 通用 d6（Rolling Off / Shooting Into Melee） | rules/02 §2 |
| `roll_charge_bonus()` | Charge d6 | rules/02 §4 |
| `roll_falling(distance_inches)` | Falling Injury Roll（自动算 +INJURY DICE） | rules/02 §6 |

**关键**：所有骰子返回 `{rolls: [...], picked: [...], total: N, result: "Success" | "Failure" | "Critical" | injury_label}` —— 让 AI 能解释为什么是这个结果，且 narrative 套描述时能引用具体骰值。

### B.4 match-state.yaml CRUD（5-7 个）

| 函数 | 用途 |
|---|---|
| `load_match(name)` | 读 `matches/{name}/match-state.yaml` |
| `save_match(name, state)` | 写（含 schema 校验） |
| `move_model(name, model_id, new_pos)` | 修改位置 |
| `add_marker(name, model_id, marker_type)` | 加 blood / blessing / down / shaken / out |
| `remove_marker(name, model_id, marker_type)` | 删除（如花 blood marker） |
| `append_event(name, event)` | 追加事件日志 |
| `set_phase(name, phase)` | 切换 initiative / activation / morale 阶段 |

### B.5 roster 校验

实现 `validate_roster(roster_yaml) -> {valid, errors: list[str]}`，按 `matches/roster-template.md` 10 条 self-check：

1. 总成本 ≤ 预算（700/800 👑 + 6 ☼）
2. 模型数 6-10
3. Leader 必选且只能 1 个
4. Troops / Elites limit 符合 faction 表
5. 每个单位 equipment 在自己 slot 内
6. 武器价格与 rules/05-battlekit + warbands armoury 一致
7. 非默认 base 显式标 base_shape + dimensions_mm
8. faction-specific keyword 不混搭
9. yaml schema 完整（id / side / profile / pos / ...）
10. v0.1 仅允许 NA + Heretic Legions

### B.6 MCP 注册

`.mcp.json`（sibling 根）：

```json
{
  "mcpServers": {
    "trenchcrusade": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.server"],
      "cwd": "/Users/jack/Projects/trpg-projects/TrenchCrusade/tools/mcp-server"
    }
  }
}
```

### B.7 完成判定

- [ ] 6 coord 接口 + 6 骰子 + 7 yaml CRUD + 1 roster 校验全部 pytest 通过
- [ ] coord §3.3 的 6 个距离用例 + §6.3 的 4 个 LOS 用例 ✓（数值层 sanity check）
- [ ] Claude Code 启动后 `/mcp` 看到 trenchcrusade server，能调用任意 tool

### B.8 风险点

1. **`valid_charge_paths` 完整算法复杂**（LOS + 路径 + interposing + shortest），v0 用 stub 暂返回 `validate_move` 调用结果，v0.5 再优化
2. **yaml schema drift**：MCP 写 yaml 时若 schema 与 `match-template.yaml` 不一致，AI 读取会错位。建议 server 启动时**校验** template 与代码的 schema 是否同步
3. **骰子可重现性**：测试需固定 seed，生产环境用真随机

---

## Phase C — AI master prompt（1 工作日）

**目标**：写 AI 对手的 system prompt（或 sibling `.claude/CLAUDE.md` 扩展段），让 Claude 能按规则出招、调 MCP、套描述模板。

### C.1 文件选择

两种方案：

- **方案 a（推荐）**：`tools/ai-opponent-prompt.md` 独立文件，sibling `.claude/CLAUDE.md` 引用之
- 方案 b：直接写在 sibling `.claude/CLAUDE.md`

推荐 a，因为 prompt 会迭代很多次，独立文件方便 diff + 版本化。

### C.2 内容大纲（300-500 行）

1. **角色定位**（开头硬规）：
   - 你是 Opponent + Battle Narrator
   - 你不是 GM / Warden / Keeper（引 narrative/tone-guide.md）
   - 你的玩家是人类，对手是你
2. **必读文件清单**（启动时读，按顺序）：
   - `rules/00-overview.md`（文件地图）
   - `narrative/tone-guide.md`（语气）
   - `narrative/world-primer.md`（意象）
   - 自己战团的 warband 文件（NA 或 HL）
3. **激活回合 7-step 决策树**（参考 rules/00-overview §7）：
   - 读 match-state.yaml
   - 选要激活的模型（评估剩余 activations + 战略目标）
   - 评估目标 + **调 MCP get_distance / get_los**（**禁止心算**）
   - 选 ACTION（Move / Charge / Shoot / Fight / Dash）
   - **调 MCP validate_move / valid_charge_paths**
   - 调骰子工具（roll_2d6_success → roll_injury 或 bloodbath）
   - 套描述模板（按 injury 结果查 `narrative/injury-flavor.md` 矩阵；按事件查 `event-triggers.md`）
   - 调 MCP move_model / add_marker / append_event 更新状态
4. **拒绝违规请求的护栏**：
   - 玩家提议非规则的行动 → 引规则文档拒绝
   - 玩家提议推翻骰子结果 → 拒绝（tone-guide.md §"禁区"）
   - 玩家提议超出当前战场的剧情 → 拒绝（不在 AI 职责）
5. **边界条件**：
   - 哪些情况问玩家（如规则歧义、scenario 特殊判定）
   - 哪些情况自决（己方激活内的所有 ACTION 选择）
6. **描述长度规范**（引 tone-guide §"描述长度规范"表）
7. **错误恢复**：MCP 调用失败 / yaml schema 错位 时如何降级
8. **自检 prompt**：每个激活前自问"我准备心算了吗？是否该调 MCP？"

### C.3 测试

用 Phase D 的 CLI 触发一个 sample turn：

```
match-cli new claim-no-mans-land --red-roster roster-a.yaml --blue-roster roster-b.yaml
match-cli activate red.yeoman_1 move [10, 16]
match-cli ai-turn   # 触发 AI 激活，观察输出
```

期望 AI 输出含：
- 选了哪个模型 + 为什么
- 调用了哪些 MCP（log 应可见）
- 投了什么骰
- 描述（1-3 段，按 tone-guide 风格）

### C.4 完成判定

- [ ] Prompt 300-500 行
- [ ] CLI sample turn 跑通，AI 输出含 MCP 调用 log + 描述
- [ ] AI 至少 5 次激活内**没有心算**距离（log 全是 MCP 调用）

---

## Phase D — match-cli（CLI 文本 UI，1 工作日）

**目标**：最小命令行工具让玩家能完整跑完一局。

### D.1 命令集

| 命令 | 用途 |
|---|---|
| `match-cli new <scenario> --red-roster X.yaml --blue-roster Y.yaml` | 新建战场 |
| `match-cli show [--grid]` | 显示战场状态（ASCII grid 或 yaml） |
| `match-cli move <model_id> <pos>` | 玩家移动自己的棋子 |
| `match-cli activate <model_id> <action> [target]` | 触发一次 ACTION（含投骰） |
| `match-cli ai-turn` | 触发 AI 激活己方所有未激活模型 |
| `match-cli end-turn` | 结束当前回合，进入 Morale Phase |
| `match-cli history` | 显示事件日志 |
| `match-cli quit` | 保存并退出 |

### D.2 ASCII grid 渲染

36×36 战场，字符代表：

```
. = 开阔
T = 战壕
R = 废墟（z=1）
H = 山丘（z=1）
* = 危险地形
~ = 崎岖地形
@ = 地标
1-9 = 红方模型 ID 缩写
A-Z = 蓝方模型 ID 缩写
```

20-30 行的 ASCII 战场图（横向压缩 1:1，纵向 0.5:1 因终端字符长方）。

### D.3 内部架构

所有命令通过 MCP server 调用 —— CLI 是 thin wrapper：

```python
# match-cli show
state = mcp.call("load_match", "test-match")
render_ascii(state)

# match-cli activate red.yeoman_1 shoot blue.heretic_trooper_1
result = mcp.call("validate_move", ...)
roll = mcp.call("roll_2d6_success", ...)
if roll.success:
    injury = mcp.call("roll_injury", ...)
    mcp.call("add_marker", "blue.heretic_trooper_1", "blood")
mcp.call("append_event", ...)
```

### D.4 完成判定

- [ ] 8 个命令实现
- [ ] ASCII grid 渲染 5 类地形 + 双方棋子
- [ ] AI turn 触发后输出 AI 的描述（来自 Phase C prompt）

---

## Phase E — 试玩 1 局 + 文档回填（1-2 工作日）

**目标**：完整跑 Scenario I "Claim No Man's Land"（NA vs HL），记录所有 friction，回填到对应文档。

### E.1 试玩流程

1. 加载 `matches/roster-template.md` §7 的两个示例 roster
2. 用 scenario I battlefield archetype（rules/04-battlefield-terrain.md + rules/08-scenarios.md §2）
3. 部署 → 4 回合 → 比 VP
4. 玩家操作己方，AI 操作对方
5. **过程中持续记录 friction**

### E.2 Friction 分类与回填

| Friction 类型 | 回填目标 |
|---|---|
| PDF 规则盲点（文档没覆盖） | `rules/02-comprehensive-rules.md` 增补 |
| yaml schema 不够 | `matches/coordinate-system.md` §7 + `match-template.yaml` |
| AI 决策错（心算 / 不调 MCP / 描述错语气） | `tools/ai-opponent-prompt.md` |
| 描述模板套用问题 | `narrative/injury-flavor.md` / `event-triggers.md` |
| MCP server 边界 case | `tools/mcp-server/src/*` + 加测试 |
| 武器/单位数值错 | `warbands/*` 或 `rules/05-battlekit.md` |

### E.3 完成判定

- [ ] 一局完整跑完（4 回合或胜利）
- [ ] 至少 5 条 friction 回填对应文档
- [ ] **第二局测试基本无新 friction**（v0.2 finalized）

---

## 2. 风险点 / 决策点

1. **MCP server 复杂度爆炸**：`valid_charge_paths` 涉及多步规则。v0 stub 简化，v0.5 优化
2. **AI 心算诱惑**：prompt 必须**反复强调**调 MCP。Phase C 应有"自检 prompt"段
3. **描述漂移**：试玩中 AI 可能用现代俚语 / 抒情过度。tone-guide 已写严格，但有效性需试玩验证
4. **schema drift**：MCP server 与 match-template.yaml 必须 schema 同步。Phase B 应有 schema 自检
5. **战团构建 vs 单场**：roster-template 是单场（700 👑），campaign（v0.2+ Glory Items）暂不考虑

---

## 3. v0.1 文档已知待回填（不阻塞 v0.2）

由 Pass 11 + Pass 13 标注的 backflow：

- 异端魔法（Goetic）武器类别在 `injury-flavor.md` W8 列仍是 placeholder
- Heretic Priest 法术列表细节
- Wretched ALL-CAPS keyword 名
- Tank-Splitter Sword keyword 确认（DEADLY？）
- Heretic-side BLESSING MARKER 机制（是否反向存在）

这些不阻塞 Phase A-E。Phase E 试玩遇到时再回填即可。

---

## 4. v0.3+ Backlog（暂缓）

- HTML 战场 UI（web-ui/）
- 4 个待导 faction（Trench Pilgrims / Iron Sultanate / Black Grail / Court of Seven-Headed Serpent，import guide §9.2.B）
- Campaign Rules（Patrons / Trauma / Promotions / Glory Items，§9.2.A）
- 剩余 10 个 scenarios（§9.2.D）
- Mercenaries（§9.2.C）
- 多 AI 对战（红 vs 蓝双 AI 测试压力）

---

## 5. 启动检查清单（Phase A 开工前）

- [ ] v0.1 全部 commit 入 main（已 ✅，14 commits 在 `eb6562d` 及之前）
- [ ] CLAUDE.md TrenchCrusade 行已更新为 "v0.1 完成（v0.2 工程化中）"（已 ✅）
- [ ] 读 Mothership sibling 项目获取 Python MCP 模板：`/Users/jack/Projects/trpg-projects/Mothership/tools/mcp-server/`
- [ ] 阅读本文件 Phase A 准备实施
