# Trench Crusade 1.0.2 导入指南

> **系统**：Trench Crusade（Tuomas Pirinen 等，v1.0.2，2024+）
> **类型**：**战棋游戏 wargame**（非 TTRPG，对称双方对战）
> **源 PDF**：`Rule Books/Trench Crusade/`
> **输出目录**：`output/TrenchCrusade/`
> **系统简称**：TrenchCrusade / TC
> **语言**：英文原文为主，关键术语附中文注释；叙事 flavor 章节中英皆可

---

## 0. 系统背景与设计取向

- Trench Crusade 是 **WW1 战壕战 + 神圣战争 + 地狱降临** 的 grimdark 战棋
- 双方各控一个**战团（warband）**（6-10 个模型），按 scenario 胜负条件对战
- 核心机制：D6 success roll（5+ 命中）/ +dice 与 -dice / Blood Markers / Blessing Markers / Injury Roll Table
- 三阶段回合：Initiative Phase → Activation Phase → Morale Phase
- **不是 TTRPG**：无 GM、无叙事推动、信息对称、双方都按规则出招
- **本项目的特殊用途**：玩家 vs AI 对战。AI 作为对手玩家通过 MCP 操纵战团；玩家通过 HTML UI 操纵自己的战团。AI 不主持剧情，只按规则出招 + 提供战斗 flavor 描述

### 与 TTRPG 导入的关键差异

| 维度 | TTRPG 导入 | TC 战棋导入 |
|---|---|---|
| AI 角色 | GM / 监守 / Warden | **对手玩家** |
| 信息对称 | GM 多于玩家 | **双方对等** |
| 叙事 | GM 推剧情 | **仅战斗事件 flavor**，不推剧情 |
| 状态主体 | 角色 + 剧情进展 | **战场状态**（棋子位置/HP/标记） |
| 输出目录 | `characters/`、`saves/{role}-notes.md` | **`warbands/`（战团列表）+ `matches/`（战场状态）** |
| 战役 | 模组 = 剧情线 | 战役 = 战团跨场进化（暂不导入） |

## 1. 导入范围（v0.1，不含扩展包）

**包含**：
- `Trench Crusade - Digital Rulebook v1.0.2.pdf`（197p）— 核心规则
- `Warbands of Trench Crusade v1.0.2.pdf`（186p）— 6 faction + Mercenaries（**先只做 2 派**：New Antioch + Heretic Legions）
- `Trench Crusade Rules Commentaries v1.0.2.pdf`（8p）— 官方 errata
- `Warband Roster Sheet.pdf`（2p）— 仅作 roster 模板设计参考，不输出

**排除（扩展/社区）**：
- `New Antioch - Prussian Stosstruppen v1.0.2.pdf`
- `Prussian Stosstruppen Warband.pdf`
- `New Antioch - Sniper Priests v1.0.2.pdf`
- `The Great Hunger v1.0.2.pdf`
- `The Red Brigade v1.5 (Westfalia).pdf`
- `Trench Crusade Changelog v1.0.2.pdf`

**暂缓**（v0.2+）：
- Campaign Rules（patrons / trauma / promotion / exploration / quartermaster / glory items）
- 其他 4 个 faction（Trench Pilgrims / Iron Sultanate / Black Grail / Court of Seven-Headed Serpent）
- Mercenaries（仅 campaign 用）

## 2. 输出文件结构

```
output/TrenchCrusade/
├── rules/                              # 核心规则（拆 Digital Rulebook）
│   ├── 00-overview.md                  # 简介 + 双方对战说明（精简，跳过 World in Flames 详细时间线）
│   ├── 01-core-rules.md                # 速览：行动/战斗/士气阶段
│   ├── 02-comprehensive-rules.md       # 详细：核心概念/判定/标记/侧写/动作/移动/战斗/受伤/士气
│   ├── 03-keywords-glossary.md         # 关键词词典
│   ├── 04-battlefield-terrain.md       # 战场原型 + 地形规则
│   ├── 05-battlekit.md                 # 远程/近战/手雷/护盾/装备全表（结构化）
│   └── 08-scenarios.md                 # 12 个剧本（MVP 先导前 2-3 个简单的）
├── warbands/                           # 战团（每 faction 一文件 + 共享 keywords）
│   ├── 00-warband-keywords.md          # Warbands 合集独有的 keyword（与 rules/03 去重后剩余）
│   ├── 01-new-antioch.md               # 新安提阿公国
│   └── 02-heretic-legions.md           # 异端军团
├── errata/
│   └── rules-commentaries.md           # 官方 FAQ/裁决（整本 8 页）
├── narrative/                          # 叙事调色板（AI 战斗描述用）
│   ├── world-primer.md                 # 2-3 页世界观精要（不是时间线，是"调子"）
│   ├── tone-guide.md                   # 文风指引：用词倾向 / 感官意象 / 禁区
│   ├── injury-flavor.md                # Injury Roll Table 6 个结果 × 武器类别 的描述模板
│   └── event-triggers.md               # Bloodbath / Critical / Down / Out of Action / Charge 等事件描述钩子
├── matches/                            # 战场状态（替代 TTRPG 的 saves/）
│   ├── match-template.yaml             # 战场状态 schema + 默认 36×36 战场模板
│   ├── coordinate-system.md            # 坐标 / 距离 / LOS / 地形 规约（MCP server 接口契约）
│   └── roster-template.md              # 战团构建模板（招募规则 + 装备槽）
└── lore/                               # 可选 lore（AI 不主动读，玩家想看时翻）
    └── timeline.md                     # World in Flames 简略时间线（仅作 flavor 参考）
```

## 3. 写作规范

### 3.1 通用

- **英文原文为主**（PDF 是英文），关键术语首次出现附中文注释：`Blood Marker（血液标记）`
- 单位/武器/特殊规则名保留**原文大写格式**（如 `Tank-Splitter Sword`、`Holy Smoke`）—— 这些是 AI 描述战斗时的"调色板词汇"，不能改名
- 数值精确：M / AC / HP / Cost / 武器射程 / 伤害骰 / 关键词 全部不可有误
- 数值表格用 markdown 表格，数字列右对齐
- 每个文件开头：`#` 标题 + `>` 引用块（源 PDF + 页码 + 版本）+ `## Index`

### 3.2 单位侧写 unit profile 结构化格式（强制）

**所有单位**必须用以下统一格式（让 MCP / AI 可解析）：

````markdown
### Yeoman

> **Faction**: New Antioch · **Type**: Troops · **Cost**: 30 👑 · **Limit**: 0–5

```yaml
profile: yeoman
stats:
  movement: 6
  ac: 12
  hp: 1
keywords: [Trooper, Mortal, Faithful]
base_size: [1, 1]
```

**Equipment slots**:
- 1× ranged (from Armoury Tier 1-2)
- 1× melee (from Armoury Tier 1)
- 0–1 grenade
- 0–1 shield

**Lore**（保留原文 1-3 句 flavor）:
> The common soldiery of the Principality, equipped with mass-produced
> blessed firearms and an iron resolve to die for their God-Emperor.

**Special rules** (如有):
- ...
````

YAML 块必须紧跟在标题下，便于 MCP 直接 parse。

### 3.3 武器/装备结构化格式（强制）

```yaml
weapon: bolt-action-rifle
type: ranged
range:
  short: 12       # +dice 加成范围（如适用）
  long: 24        # 最大射程
attacks: 1
damage: 1
keywords: [Penetrating, Reliable]
cost: 5
armoury_tier: 1
```

散文描述（特殊规则触发条件、flavor）放 YAML 后。

### 3.4 关键词词典

`rules/03-keywords-glossary.md` 是**索引文件**：每个 keyword 一节，定义 + 触发时机。`warbands/00-warband-keywords.md` 只放 Warbands 合集独有的（与 rules/03 去重）。

### 3.5 叙事调色板（narrative/）规范

这是本项目特殊章节，对应"AI 提供战斗 flavor 描述"需求。

- `world-primer.md`：**不是时间线**，是 2-3 页的"调子"——TC 世界的关键意象（战壕、毒气、机械教士、地狱蝗虫、亵渎圣物、教廷狂热）。AI 描述战斗时调用这些意象。
- `tone-guide.md`：明确写出
  - ✅ **允许**：血腥、宗教狂热、机械教士、地狱意象、毒气、泥泞战壕、亵渎圣物、神迹
  - ❌ **禁区**：现代俚语、玩笑、推翻骰子结果、超出当前战场的剧情发展、PG-13 化的描述
- `injury-flavor.md`：Injury Roll Table 的 6 个结果 × 武器类别（远程齐射 / 重型近战 / 圣火 / 手雷 / 异端魔法）= 描述模板矩阵。每个 cell 给 1-3 个示例句。AI 套模板生成。
- `event-triggers.md`：关键事件（Charge 接触、Bloodbath、Critical Hit、Down、Out of Action、Morale 失败、Bless 触发）的描述钩子。

**核心原则**：叙事**始终后于规则结算**。骰子先出结果，AI 根据结果套描述，不能反过来用描述影响骰子。

### 3.6 文件头模板

```markdown
# rules/02-comprehensive-rules: Comprehensive Rules

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.22-51
> 版本：v1.0.2

## Index

- [What You Need To Play](#what-you-need-to-play)
- [Core Concepts](#core-concepts)
- ...

---
```

## 4. 坐标系与战场状态契约（v0.1 决议）

详细规约见 `matches/coordinate-system.md`，此处给摘要。**整个项目所有规则、单位、武器的数值描述都以此为基础**。

| 维度 | 决议 |
|---|---|
| 单位尺度 | 1" = 1 格（PDF 所有数值直接套用） |
| 默认战场 | 36×36 格（3'×3'，入门）；可扩 48×48 |
| 棋子位置 | 整数 `(x, y, z)` |
| 高度 z | 离散层级：0=地面、1=二楼/丘陵顶、2=屋顶、-1=战壕凹陷；每层默认 3" 高（场地设备中可调） |
| 距离测量 | 3D 欧几里得 `√((Δx)² + (Δy)² + (Δz)²)`，保留 1 位小数。**MCP server 计算**，AI 不心算 |
| LOS 判定 | MCP server 算射线 + 高度，返回 `clear` / `partial_cover` / `blocked` |
| 地形表示 | 形状区域（rect/polygon）+ 属性：`{type, bounds, height, blocks_los, cover, movement_cost, dangerous}` |
| 棋子基座 | 默认 1×1 格；大型单位（Anchorite Shrine / Brazen Bull 等）标 2×2 |
| 模型上限 | 单方推荐 6-10 个（控制状态复杂度） |

### match-state.yaml 示例骨架

```yaml
battlefield:
  size: [36, 36]
  layer_height: 3      # 每个 z 层等于多少英寸（垂直距离用）

terrain:
  - type: building
    bounds: [12, 8, 18, 14]
    height: 2
    blocks_los: true
    cover: full
  - type: trench
    bounds: [4, 20, 28, 22]
    height: -1
    cover: partial
  - type: forest
    bounds: [22, 4, 28, 10]
    blocks_los: partial
    movement_cost: 2

scenario: claim-no-mans-land
turn: 2
phase: activation
initiative: red

models:
  - id: red.lieutenant
    side: red
    profile: lieutenant
    pos: [6, 6, 0]
    base_size: [1, 1]
    hp: 3
    markers: []         # blood / blessing / down / shaken 等
    activated: false
    equipment:
      ranged: blessed-revolver
      melee: blessed-sabre
  - id: red.yeoman_1
    side: red
    profile: yeoman
    pos: [7, 6, 0]
    base_size: [1, 1]
    hp: 1
    markers: []
    activated: false
    equipment:
      ranged: bolt-action-rifle
      melee: bayonet
  - id: blue.heretic_priest
    side: blue
    profile: heretic-priest
    pos: [30, 30, 0]
    ...
```

## 5. 章节优先级与分对话计划

每对话 1-2 文件，完成后立即校验。**MVP 目标**：能玩第一场 New Antioch vs Heretic Legions 的 "Claim No Man's Land"。

| 阶段 | 文件 | 来源 | 备注 |
|---|---|---|---|
| 框架 | 指南 + 状态表更新 | — | 当前 |
| Pass 1 | `matches/coordinate-system.md` + `matches/match-template.yaml` | 本指南 §4 | 先写契约，rules 章节会引用 |
| Pass 2 | `rules/01-core-rules.md` | PDF p.14-21 | 速览版 |
| Pass 3 | `rules/02-comprehensive-rules.md` | PDF p.22-51 | 详细规则（长，分 2 节做） |
| Pass 4 | `rules/03-keywords-glossary.md` | PDF p.52-64 | 关键词词典 |
| Pass 5 | `rules/04-battlefield-terrain.md` | PDF p.60-67 | 地形规则 |
| Pass 6 | `rules/05-battlekit.md` | PDF p.68-86 | 武器/装备全表（结构化） |
| Pass 7 | `errata/rules-commentaries.md` | Commentaries PDF | 整本 8 页 |
| Pass 8 | `warbands/00-warband-keywords.md` + `warbands/01-new-antioch.md` | Warbands p.15-20, 21-46 | New Antioch 全派 + 共享 keywords |
| Pass 9 | `warbands/02-heretic-legions.md` | Warbands p.103-124 | Heretic Legions 全派 |
| Pass 10 | `narrative/world-primer.md` + `narrative/tone-guide.md` | Digital Rulebook p.7-13 + 自撰 | 调子 + 文风 |
| Pass 11 | `narrative/injury-flavor.md` + `narrative/event-triggers.md` | 自撰（基于规则） | 战斗描述模板 |
| Pass 12 | `rules/08-scenarios.md`（Scenario Format 通用框架 + 1-2 个简单 scenario） | PDF **p.144-160** | MVP 先做 Scenario Format（含 Glorious Deeds + Glory Points 通用规则） + "Claim No Man's Land" + "Hunt for Heroes"。注意 Glory Points (☼) 概念定义虽然主体在 Campaign Rules，但 Scenario Format 章节有单场可用的简化用法（完成一项 Glorious Deed = 10 VP），单场对战不需要完整 Campaign |
| Pass 13 | `rules/00-overview.md` + `matches/roster-template.md` + `lore/timeline.md` | PDF p.7-13 | 收尾 |

**v0.1 完成判定**：以上 13 个 Pass 全部完成 → 能跑第一局完整对战（详细规则覆盖验证见 §9.1）。

**v0.2+ 详细 backlog 见 §9.2**。

## 6. 校验检查清单（每文件）

- [ ] **完整性**：源 PDF 对应页码区间是否全部覆盖？
- [ ] **数值准确**：抽查 5 个关键数值（M / AC / HP / 射程 / 伤害 / Cost）与 PDF 原文对照
- [ ] **YAML 块完整**：每个单位/武器都有结构化 yaml 块，字段齐全
- [ ] **关键词大小写**：`PENETRATING (1)` / `CLEAVE (2)` 等保留原文大写格式
- [ ] **flavor 文本保留**：单位/武器/特殊规则的 lore flavor 段（1-3 句）不能砍
- [ ] **跨文件引用**：用相对路径 `→ rules/03-keywords-glossary.md#penetrating`
- [ ] **无乱码**：PDF 提取残留的特殊符号（如 `ª` `≠` ``` ` `` `👑` `☼`）按需保留或转换说明

## 7. sibling 项目（v0.2+，规则稳定后再建）

待 v0.1 完成且实际玩过几局后，再考虑建 `/Users/jack/Projects/trpg-projects/TrenchCrusade/`。结构：

- `rules/` → symlink 到 `dnd-rules-import/output/TrenchCrusade/rules/`
- `warbands/` → symlink
- `narrative/` → symlink
- `matches/` → symlink
- `tools/mcp-server/` — 关键工具：
  - 距离查询 / LOS 查询 / 移动合法性 / 战团构建校验 / 骰子 / 战场状态 CRUD
  - 推荐 Python MCP（参考 Mothership sibling 的 `tools/mcp-server/`）
- `web-ui/` — **新增**：HTML 战场 UI，玩家拖动棋子。与 MCP server 共享 match-state.yaml

**与 TTRPG sibling 的差异**：
- **不需要** `saves/{role}-notes.md`、`{theme}-log.md`、`.active` 等 TTRPG 存档约定
- **需要** `matches/{name}/match-state.yaml` 替代 saves；每场对战独立目录
- **AI 角色不是 Warden/Keeper**，而是 "Opponent"（对手）

## 8. 注意事项

1. **不要混扩展**：v0.1 严格只导核心 + Warbands 合集中的 New Antioch + Heretic Legions。`The Great Hunger`、`Red Brigade`、Stosstruppen 独立扩展全部不动。
2. **不要把 AI 写成 GM**：所有 narrative/ 文件、tone-guide、event-triggers 都要明确"AI = 对手玩家 + 战斗描述员，不是叙事推动者"。
3. **数值格式统一**：所有单位/武器用 YAML 块结构化（§3.2 §3.3）。MCP server 解析依赖此格式，散文格式会破坏 v0.2 工程化。
4. **保留单位/武器命名**：`Tank-Splitter Sword` / `Holy Smoke` / `Wretched` / `Plague Knight` 等原文名是叙事调色板，不能改名/汉化掉。
5. **页码标注**：每个大章节开头标 PDF 页码范围，便于校对。

---

## 9. v0.1 完整度验证 与 v0.2+ Backlog

### 9.1 v0.1 不缺核心规则 — 用 "Claim No Man's Land" 剧本验证

实际对照剧本规则需求 → v0.1 文件，全部覆盖：

| 剧本规则需求 | v0.1 覆盖文件 |
|---|---|
| 无人区 battlefield archetype + 7 种地形类型 | `rules/04-battlefield-terrain.md` |
| 地形 8" 视作 2 块 / 6" 间距等设置规则 | `rules/04` |
| Rolling Off（掷骰决定） | `rules/02`（Other Rules Principles） |
| 标准部署 / 战团模型数量多者先部署 | `rules/08`（Scenario Format 通用框架） |
| Infiltrator（渗透者）特殊部署 | `rules/03`（Keywords Glossary） |
| Out of Action（击倒出局）判定 | `rules/02`（Injury Roll Table） |
| 模型成本 VP 计算（👑÷10、☼÷3 向上取整） | `warbands/01,02` + `rules/05`（装备成本） |
| 战团 Shaken / 逃跑（Morale Phase） | `rules/02`（Morale Phase） |
| Glory Points (☼) + Glorious Deeds 框架 | `rules/08`（Scenario Format 含简化版：完成 1 项 Glorious Deed = 10 VP） |
| 击倒他们（3" 高度坠落） | `rules/02`（Climbing & Jumping / Jumping Down） |
| 孤注一掷（同回合 2 次 Risky Success） | `rules/02`（Dash ACTION 触发） |
| 神枪手（远程 + 远距修正 + 掩体修正命中） | `rules/02`（Combat / Ranged Attack Modifiers） |
| 第 5 回合末掷 D6 决定游戏长度 | `rules/08`（scenario 特定规则） |

**关键洞察**：Glory Points (☼) 完整定义在 Campaign Rules（p.99），**但 Scenario Format 章节（v0.1 已含，p.144-150）有单场可用的简化用法**——完成一项 Glorious Deed = 10 VP。所以 **v0.1 单场对战不需要 Campaign Rules**。

### 9.2 v0.2+ Backlog（按优先级）

#### v0.2.A — Campaign Rules（战团长线进化）

PDF p.87-143（56 页），新增 2 个 rules 文件：

| 子系统 | PDF 页码 | 内容 |
|---|---|---|
| Patrons（赞助人） | p.87-94 | 8 种赞助人（Temporal Lord / Warrior Saint / Learned Saint / Infernal Noble / Sublime Gate / Order of the Fly / Mammon / Antipope of Avignon） |
| Campaign Games | p.95-99 | 战役框架下的 scenario 选择 + Glory Points 完整规则 |
| Trauma Step | p.101-103 | 战后伤亡判定（永久损伤/死亡/恢复表） |
| Promotions & Experience | p.104-111 | 单位升级 4 类技能：Melee&Strength / Ranged / Stealth&Speed / Wildcard |
| Reinforcements | p.112 | 补充新单位 |
| Exploration | p.113-122 | 3 张地点表：Common / Rare / Legendary |
| Quartermaster | p.123-124 | 战间补给采购 |
| Glory Items | p.125-143 | 晋升装备完整表（19 页） |

输出文件：`rules/06-campaign-rules.md` + `rules/07-glory-items.md`

#### v0.2.B — 剩余 4 个 Faction

| Faction | PDF 页码 | 备注 |
|---|---|---|
| Trench Pilgrims | Warbands p.47-70 | 朝圣战士狂热者 |
| The Sultanate of the Iron Wall | Warbands p.71-102 | 伊斯兰系战团 + Goetic/Alchemist 子系统 |
| The Cult of the Black Grail | Warbands p.125-143 | 瘟疫膜拜 |
| The Court of the Seven-Headed Serpent | Warbands p.144-170 | **含 Goetic Powers 子系统（7 种罪恶魔法列表）— 最复杂** |

#### v0.2.C — Mercenaries（雇佣兵）

Warbands p.172-186。原 §1 标"campaign 才用"——**待复核**：Scenario Format 章节是否允许单场用 ☼ 雇佣。如允许则可提前到 v0.1.5。

#### v0.2.D — 剩余 10 个 Scenario

PDF p.154-197。v0.1 只导 Scenario I (Claim No Man's Land) + II (Hunt for Heroes)。剩：

- III Relic Hunt / IV Trench Warfare（标准战场）
- V Armoured Train / VI Dragon Hunt（异形战场，复杂特殊规则）
- VII Supply Raid / VIII From Below / IX Fields of Glory / X Don't Breathe / XI The High Ground / XII Great War

### 9.3 待复核问题（导入前先查 PDF）

1. **Mercenaries 单场可用性**：PDF Warbands p.172 "Mercenary Special Rules" 应明确触发条件。若允许单场 skirmish 雇佣，则 §1 暂缓列表中 Mercenaries 应移到 v0.1.5。
2. **Faction Variants 完整度**：每个 faction 下 3-5 个 variants（如 New Antioch 5 个：Papal States / Éire Rangers / Alba / Stosstruppen / Abyssinia）。v0.1 的 `warbands/01-new-antioch.md` 必须包含主战团 **+ 全 variants**（约 26 PDF 页）。Pass 8 实际工作量需按此评估，可能需拆 2 次对话。
3. **Goetic Powers 子系统**（Court of Seven-Headed Serpent）：v0.2.B 中此 faction 含 7 种罪恶魔法列表（p.154-161），结构复杂，建议单独一个 Pass。
