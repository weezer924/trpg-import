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
  movement: 6      # M（英寸，PDF Profile 第一字段）
ranged: 0          # +/- DICE 修正（PDF Profile 第二字段）
melee: 0           # +/- DICE 修正
armour: 0          # -INJURY MODIFIER（无装甲为 0）
keywords: [NEW ANTIOCH, FIRETEAM]    # 单位 keyword 列表（ALL-CAPS 保留）
base_size: [1, 1]                    # grid 占用（仅正方形 v0.1）
base_shape: circle                   # 视觉：circle / oval / square（默认 circle 可省）
base_dimensions_mm: [25, 25]         # 视觉：实际基座尺寸 mm（默认 [28,28] 可省）
```

> **重要**：TC 用 Injury Roll 决胜负，**没有 HP / AC**——曾经的示例字段是误导，已按 PDF v1.0.2 Profile 字段修正。详见 [[Pass 1 base 契约 §5]] 三层基座语义。

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

### 3.7 中英术语锚定表（必读，Pass 2-13 所有作者共用）

**目的**：多 agent 并行导入时保证术语一致。任何 rules / warbands / narrative / errata 章节的中文翻译必须与下表锚定；首次出现给 `中文（English）` 对照，其后用英文原文（保留官方大小写）。

**通用约定**：
- ✅ **保留英文原文**（**不译**）：单位名、武器名、特殊规则名、faction 名的英文形式、ALL-CAPS 关键词、装备型号
- ✅ **首次给对照**：核心机制术语、阶段名、战斗动作、判定类型、地形大类
- ✅ **后续可省**：在同一文件中已给过对照的术语，后文用英文或中文皆可，保持一致

#### A. 核心机制（首次给对照）

| English | 中文锚定 | 备注 |
|---|---|---|
| Warband | 战团 | 双方各 1 个 |
| Faction | 派系 | 6 大派系 + Mercenaries |
| Activation | 激活 | 一次激活 1 个模型 |
| Initiative | 先手 / 主动权 | 模型少者持 |
| Movement Characteristic (M) | 移动值（M） | 模型属性 |
| Armour Characteristic | 装甲值 | 模型属性 |
| Cost (👑) | 招募成本（👑 Ducat） | 👑 不译，符号保留 |
| Glory Points (☼) | 荣耀点数（☼） | ☼ 不译，符号保留；单场 = 完成 Glorious Deed × 10 VP |
| Glorious Deeds | 荣耀事迹 | 剧本指定 |
| Victory Points (VP) | 胜利点数（VP） | 用于胜负判定 |

#### B. 阶段与动作（首次给对照）

| English | 中文锚定 | 备注 |
|---|---|---|
| Initiative Phase | 先手阶段 | 回合阶段 1 |
| Activation Phase | 激活阶段 | 回合阶段 2 |
| Morale Phase | 士气阶段 | 回合阶段 3 |
| Move ACTION | 移动行动 | 标准移动 |
| Charge ACTION | 冲锋行动 | M + d6，需 12" 内见敌 |
| Retreat ACTION | 撤退行动 | 离开 melee；敌方免费 melee |
| Dash ACTION | 疾行行动 | Risky；同回合可两次 |
| Shoot ACTION | 射击行动 | 远程攻击 |
| Fight ACTION | 近战行动 | 近战攻击 |

#### C. 判定与骰子（首次给对照）

| English | 中文锚定 | 备注 |
|---|---|---|
| Success Roll | 成功判定 | 2d6 ≥ 7 |
| Risky Success Roll | 风险判定 | 失败立即结束激活 |
| Critical Success | 大成功 | 12 = injury +1 dice |
| +X DICE / -X DICE | +X 骰 / -X 骰 | 多投取高/取低 |
| Action Success Chart | 成功判定表 | 7+ 成功 / 12 大成功 / 6- 失败 |
| Injury Roll | 受伤判定 | 命中后投 |
| Injury Roll Table | 受伤表 | 2-6 / 7-8 / 9+ |
| Bloodbath Roll | 血浴判定 | 3d6 全加（DEADLY 时 4d6） |
| INJURY DICE | 伤害骰 | 加在 injury roll |
| INJURY MODIFIER | 伤害修正 | 加在 injury 结果（最低 -3） |
| Rolling Off | 掷骰决断 | d6 平手时重投 |

#### D. 标记与状态（首次给对照）

| English | 中文锚定 | 备注 |
|---|---|---|
| Blood Marker | 血液标记 | 攻方花，目标 action -1 dice 或 injury +1 dice |
| Blessing Marker | 祝福标记 | 防方花，反向修正 |
| Down | 倒下 | 7-8 结果；激活立即结束；起身后 M 减半 |
| Out of Action | 出局 | 9+ 结果；移出战场 |
| Shaken | 动摇 | 士气失败选项；所有 action 变 risky |
| Minor Hit | 轻伤 | 2-6 结果 |
| Falling | 坠落 | 3"+ 触发 injury，每 3" +1 dice |

#### E. 战斗修正（首次给对照）

| English | 中文锚定 | 备注 |
|---|---|---|
| Line of Sight (LOS) | 视线（LOS） | 见 `matches/coordinate-system.md` §6 |
| Cover | 掩体 | -1 DICE ranged |
| Partial Line of Sight | 部分视线 | LOS state = partial_cover |
| Elevated Position | 高地 | 高 3"+ → +1 DICE ranged |
| Short Range / Long Range | 近射程 / 远射程 | 一半射程为界；Long -1 DICE |
| Defended Obstacle | 掩护障碍 | 近战时 ½" 障碍 -1 DICE |
| Off-Hand Weapon | 副手武器 | -1 DICE |
| Diving Charge | 俯冲冲锋 | 跳下 3"+ 后 charge，成功 +1 DICE 下次 melee |

#### F. 地形（首次给对照）

| English | 中文锚定 | 关键词 |
|---|---|---|
| Open terrain | 开阔地形 | — |
| Difficult Terrain | 崎岖地形 | `DIFFICULT TERRAIN` |
| Dangerous Terrain | 危险地形 | `DANGEROUS TERRAIN` |
| Impassable Terrain | 不可通行地形 | `IMPASSABLE TERRAIN` |
| Trench | 战壕 | z=-1 |
| Ruins | 废墟 | 可攀爬 |
| Hill | 山丘 | high ground 来源 |
| Abandoned Corner | 废弃角落 | 杂物堆 |
| Landmark | 地标 | 剧本目标 |

#### G. Faction 名称（首次给对照）

| English | 中文锚定 | v0.1 含 |
|---|---|---|
| New Antioch (Principality of) | 新安提阿（公国） | ✅ |
| Heretic Legions | 异端军团 | ✅ |
| Trench Pilgrims | 战壕朝圣者 | ❌ v0.2 |
| The Sultanate of the Iron Wall | 钢墙苏丹国 | ❌ v0.2 |
| The Cult of the Black Grail | 黑圣杯邪教 | ❌ v0.2 |
| The Court of the Seven-Headed Serpent | 七首蛇圣庭 | ❌ v0.2 |
| Mercenaries | 雇佣兵 | ❌ v0.2 |

#### H. 不译条目（保留英文原文 + 官方大小写）

- **单位名**：Yeoman / Lieutenant / Anchorite Shrine / Heretic Trooper / Heretic Death Commando / Heretic Priest / Brazen Bull / Plague Knight / Wretched / Trench Pilgrim …
- **武器名**：Bolt-Action Rifle / Musket / Tank-Splitter Sword / Holy Smoke / Infernal Bomb / Blessed Revolver / Blessed Sabre / Bayonet / Trench Knife …
- **装备**：Trench Shield / Standard Armour / Reinforced Armour / Machine Armour
- **ALL-CAPS 关键词**：`PENETRATING (X)` / `CLEAVE (X)` / `TOUGH` / `DEADLY` / `RELIABLE` / `ASSAULT` / `BLAST` / `DIFFICULT TERRAIN` / `DANGEROUS TERRAIN` / `IMPASSABLE TERRAIN` / `COVER` / `BLOOD MARKER` / `BLESSING MARKER`（保留大小写不变）
- **特殊规则名**、**Skill 名**、**Patron 名**：均保留英文

#### I. 工作流约定

1. 每个 Pass 作者**写完后搜索**自己文件，确保用到的术语都能在本表 A-G 找到锚定；若引入新术语，在 PR 描述里报上来，统一回填本表
2. ALL-CAPS 关键词（PDF 原文用大写）**任何位置都用 `` ` `` 反引号包**（`` `PENETRATING (1)` ``），与普通英文区分
3. 不确定翻译时：保留英文 + 加 `[术语待锚定]` 注释（占位），不要自创翻译
4. ☼ 👑 等 PDF 原文符号**直接复制保留**，不要替换为 ASCII

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

> **⚠️ Pass 2-12 通用硬性规范（rules/* 全适用）**：
> 凡涉及**距离测量 / Line of Sight / Cover / 地形属性 / base size / 坐标**的描述，
> **直接引用** `matches/coordinate-system.md` 对应 §（参见该文件 §9 实施 checklist 表），
> **不要散文复述**——避免规则漂移、保证单一信息源（SSoT）。
> 例：`rules/02` 写 ranged attack 时只写"判定 LOS（→ `matches/coordinate-system.md` §6）"，
> 不要重写 PDF "cover 三问" 的散文版本。

| 阶段 | 文件 | 来源 | 备注 |
|---|---|---|---|
| 框架 | 指南 + 状态表更新 | — | 当前 |
| Pass 1 | `matches/coordinate-system.md` + `matches/match-template.yaml` | 本指南 §4 | 先写契约，rules 章节会引用 |
| Pass 2 | `rules/01-core-rules.md` | PDF p.14-21 | 速览版；遵守 Pass 2-12 硬性规范（见上方框） |
| Pass 3 | `rules/02-comprehensive-rules.md` | PDF p.22-51 | 详细规则（长，分 2 节做） |
| Pass 4 | `rules/03-keywords-glossary.md` | PDF p.52-57 | 关键词词典（PDF p.58+ 已是 Terrain 章节） |
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

### 5.1 交叉校验：Core Rules 视频 transcript

Pass 2-4 完成后（rules/01 + rules/02 + rules/03），**必须**用 `output/TrenchCrusade/_references/core-rules-video-transcript.md` §3 校验清单逐条核对：

- 14 条关键规则要点（成功阈值 / 移动三种 / +dice 取高/−dice 取低 / Cover 三问 / Long range 定义 / Injury 阈值 2-6/7-8/9+ / 装甲减伤数值 / Tough 仅首次 / Bloodbath 累加 / Blood marker 不能反向修自 injury / Morale 半数触发 / Shaken=所有 action 变 risky）
- 数值/阈值若与 PDF v1.0.2 冲突 → **以 PDF 为准**，在 transcript 文件该条目加注修正

视频是简化教学，可能漏边界条件，但**新玩家最易混淆的几条**（Blood Marker 不能反向修自身 injury、Tough 仅首次、Bloodbath 累加 4d6）视频明确指出，rules/02 写到这些时**必须加注释提示**。

## 6. 校验检查清单（每文件）

- [ ] **完整性**：源 PDF 对应页码区间是否全部覆盖？
- [ ] **数值准确**：抽查 5 个关键数值（M / AC / HP / 射程 / 伤害 / Cost）与 PDF 原文对照
- [ ] **YAML 块完整**：每个单位/武器都有结构化 yaml 块，字段齐全
- [ ] **关键词大小写**：`PENETRATING (1)` / `CLEAVE (2)` 等保留原文大写格式
- [ ] **flavor 文本保留**：单位/武器/特殊规则的 lore flavor 段（1-3 句）不能砍
- [ ] **跨文件引用**：用相对路径 `→ rules/03-keywords-glossary.md#penetrating`
- [ ] **无乱码**：PDF 提取残留的特殊符号（如 `ª` `≠` ``` ` `` `👑` `☼`）按需保留或转换说明

## 7. sibling 项目（v0.2 Phase A 已建）

**状态**：v0.2 Phase A 完成，`/Users/jack/Projects/trpg-projects/TrenchCrusade/` 已建（commit `0d9e5e9`）。Phase B-E 待补 MCP server / AI prompt / CLI / 试玩。

### 当前结构

```
TrenchCrusade/
├── rules/       → symlink dnd-rules-import/output/TrenchCrusade/rules/
├── warbands/    → symlink
├── narrative/   → symlink
├── lore/        → symlink
├── errata/      → symlink
├── matches/
│   ├── coordinate-system.md → symlink
│   ├── match-template.yaml  → symlink
│   ├── roster-template.md   → symlink
│   └── test-match/          ← 本地可写（match-state.yaml 测试用）
├── rule books/  → symlink Rule Books/Trench Crusade/（PDF + txt 原文，歧义回查）
├── tools/mcp-server/  ← Phase B 填实际 Python MCP server
├── .mcp.json    ← 注册 trenchcrusade server（Phase B 才生效）
├── .claude/CLAUDE.md  ← AI 启动指令（Opponent + Battle Narrator 定位）
└── README.md
```

### v0.2 后续 Phase 待补

- **Phase B**（1.5-2d）：Python MCP server v0 — 6 coord 接口 + 6 骰子 + 7 yaml CRUD + roster 校验
- **Phase C**（1d）：AI master prompt（独立 `tools/ai-opponent-prompt.md`）
- **Phase D**（1d）：`match-cli` CLI 文本 UI
- **Phase E**（1-2d）：试玩 Scenario I + friction 回填
- **v0.3+**：`web-ui/` HTML 战场 UI（暂缓）

### 与 TTRPG sibling 的差异

- **不需要** `saves/{role}-notes.md`、`{theme}-log.md`、`.active` 等 TTRPG 存档约定
- **需要** `matches/{name}/match-state.yaml` 替代 saves；每场对战独立目录
- **AI 角色不是 Warden/Keeper**，而是 **"Opponent + Battle Narrator"**（对手玩家 + 战斗描述员）
- 不需要 `characters/`，改用 `warbands/`（战团列表）+ `matches/roster-template.md`（战团构建模板）

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
| 模型成本 VP 计算 | ~~草拟时以为有 `👑÷10、☼÷3` 公式，PDF Scenario Format p.144-150 实际无此公式~~（属 Campaign Rules，v0.2.A 才覆盖）。v0.1 各 scenario 的 VP 直接由该 scenario 明列条目给出（Objective / Mark / Asset / Glorious Deed） |
| 战团 Shaken / 逃跑（Morale Phase） | `rules/02`（Morale Phase） |
| Glory Points (☼) + Glorious Deeds 框架 | `rules/08`（Scenario Format 含简化版：**每完成 1 项 Glorious Deed = 1 VP**，由 Pass 12 对照 PDF p.153/156/160 校正）|
| 击倒他们（3" 高度坠落） | `rules/02`（Climbing & Jumping / Jumping Down） |
| 孤注一掷（同回合 2 次 Risky Success） | `rules/02`（Dash ACTION 触发） |
| 神枪手（远程 + 远距修正 + 掩体修正命中） | `rules/02`（Combat / Ranged Attack Modifiers） |
| 游戏长度 | `rules/08`：**各 scenario 固定回合数**（Scenario I = 4 回合 / Scenario II = 5 回合）；草拟时以为有"第 5 回合末 d6 决定继续"机制——PDF 中无此通用机制。Scenario II 的 d6 用于每回合开始的 Unforeseen Events（5-6 触发），与游戏长度无关 |

**关键洞察**：Glory Points (☼) 完整定义在 Campaign Rules（p.99），**但 Scenario Format 章节（v0.1 已含，p.144-150）有单场可用的简化用法**——每完成 1 项 Glorious Deed = **1 VP**（不是 10 VP，PDF p.153/156/160 已核实）。所以 **v0.1 单场对战不需要 Campaign Rules**。

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
