# rules/02-comprehensive-rules: Comprehensive Rules

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.22-51
> 版本：v1.0.2
> 范围：Comprehensive Rules 章节——Core Concepts、Other Rules Principles、Game Turns（Initiative/Activation/Morale）、Movement、Climbing & Jumping、Falling、Combat（Ranged/Melee）、Injuries、Bloodbath、Winning。本节不改变 Core Rules，但展开细则与示例。
>
> **强制规范**：所有涉及**距离测量 / Line of Sight / Cover / 地形属性 / base size / 坐标**的描述一律引用 `→ matches/coordinate-system.md §X`，**不散文复述**。Keyword 完整定义引 `→ rules/03-keywords-glossary.md`。武器具体数据引 `→ rules/05-battlekit.md`。官方裁决引 `→ errata/rules-commentaries.md`。

## Index

- [What You Need To Play](#what-you-need-to-play)
- [Core Concepts](#core-concepts)
  - [Keywords](#keywords)
  - [Success Rolls](#success-rolls)
  - [Risky Success Rolls](#risky-success-rolls)
  - [+DICE and -DICE](#dice-and--dice)
  - [Injury Dice](#injury-dice)
  - [Blood Markers](#blood-markers)
  - [Blessing Markers](#blessing-markers)
  - [Profiles](#profiles)
  - [ACTION vs Attack（动作与攻击的概念分离）](#action-vs-attack动作与攻击的概念分离)
- [Other Rules Principles](#other-rules-principles)
  - [Fractions](#fractions)
  - [Measuring Distances](#measuring-distances)
  - [Line of Sight](#line-of-sight)
  - [Points on the Battlefield or Terrain Pieces](#points-on-the-battlefield-or-terrain-pieces)
  - [Model Accuracy](#model-accuracy)
  - [Model Placement](#model-placement)
  - [Pre-Measuring](#pre-measuring)
  - [Re-rolls](#re-rolls)
  - [Rolling Off](#rolling-off)
- [Game Turns](#game-turns)
  - [The Sequence of Play](#the-sequence-of-play)
  - [1. Initiative Phase](#1-initiative-phase)
  - [2. Activation Phase](#2-activation-phase)
  - [ACTIONS](#actions)
- [Movement](#movement)
  - [Moves](#moves)
  - [Charging](#charging)
  - [Retreating](#retreating)
- [Terrain（在 Movement 中的引用）](#terrain在-movement-中的引用)
- [Climbing & Jumping](#climbing--jumping)
  - [Climbing Sheer Surfaces](#climbing-sheer-surfaces)
  - [Jumping Over Gaps](#jumping-over-gaps)
  - [Jumping Between Ledges of Unequal Heights](#jumping-between-ledges-of-unequal-heights)
  - [Jumping Down](#jumping-down)
- [Falling](#falling)
- [Combat — Ranged Attacks](#combat--ranged-attacks)
  - [Ranged Attack Sequence](#ranged-attack-sequence)
  - [Shooting into Melee](#shooting-into-melee)
  - [Measuring the Range](#measuring-the-range)
  - [Short Range & Long Range](#short-range--long-range)
  - [Ranged Attack Modifiers](#ranged-attack-modifiers)
  - [Ranged Attack Success Roll](#ranged-attack-success-roll)
- [Combat — Melee Attacks](#combat--melee-attacks)
  - [Melee Attack Sequence](#melee-attack-sequence)
  - [Melee Attack Modifiers](#melee-attack-modifiers)
  - [Multiple Melee Weapons](#multiple-melee-weapons)
  - [Diving Charge](#diving-charge)
- [Injuries](#injuries)
  - [Injury Rolls](#injury-rolls)
  - [Bloodbath Rolls](#bloodbath-rolls)
  - [Making an Injury Roll](#making-an-injury-roll)
  - [Injury Roll Table](#injury-roll-table)
  - [Common Injury Roll Modifiers](#common-injury-roll-modifiers)
  - [Down Results](#down-results)
  - [Out of Action](#out-of-action)
- [3. Morale Phase](#3-morale-phase)
  - [Shaken Warbands](#shaken-warbands)
  - [Ending the Turn](#ending-the-turn)
  - [Sounding the Retreat](#sounding-the-retreat)
- [Winning the Game](#winning-the-game)

---

## What You Need To Play

> PDF p.22 · **TL;DR**：双人对战；每方 1 战团（6-20 模型）；战场 36-48"² 方；测量单位英寸（数字化由 MCP 计算）；首场推荐 Scenario 1（Claim No Man's Land）。

Comprehensive Rules 章节扩展 Core Rules，提供更深入的解释、附加规则和示例，但**不改变** Core Rules。

- **PLAYERS**：本规则书按双人对战编写；多人对战剧本见 trenchcrusade.com。
- **WARBANDS & MODELS**：每位玩家指挥一个 Warband（战团），通常含 6-20 个模型（详见 Warbands of Trench Crusade — Starting a Warband 章节）。
  - **Friendly & Enemy Models（友方与敌方模型）**：你战团内的模型为 friendly models，对手战团内的为 enemy models。规则中"you"指指挥该模型所属战团的玩家。"Take a roll"是为自家模型掷骰；"make a roll"是对敌方模型掷骰。
- **Profiles**：每个模型有 Profile 描述其战斗能力与所携 Weapons（详见 Profiles 节）。
- **BATTLEFIELD**：战场尺寸标准为 30" 以上宽度；标准对战 36"×36" 或 48"×48"。具体见 `→ rules/08-scenarios.md` 与 `→ matches/coordinate-system.md` §4。
- **TERRAIN**：地形必需且多多益善——位置与战术是 TC 的核心。详见 `→ rules/04-battlefield-terrain.md` 与 `→ matches/coordinate-system.md` §7。
- **TAPE MEASURE OR RULER**：所有测量单位为英寸（Imperial）。数字化对战中**距离由 MCP server 计算**，见 `→ matches/coordinate-system.md` §3。
- **DICE (D6s & D3s)**：每位玩家需若干 6 面骰。
  - **D3 Rolls**：投 1d6 然后除以 2 向上取整：1-2=1、3-4=2、5-6=3。
- **SCENARIO**：游戏前选一个剧本。剧本决定地形布置、部署区、回合数与胜负判定。首次对战推荐 Scenario 1: Claim No Man's Land（详见 `→ rules/08-scenarios.md`）。

---

## Core Concepts

> PDF p.23-29 · **TL;DR**：Success Roll = 2D6 ±DICE，取 2 个加权后骰；2-6 Failure / 7-11 Success / 12+ Critical（Critical 命中 +1 INJURY DICE）。Risky Success Roll 失败直接结束 Activation。BLOOD MARKERS 始终**不利于**持有者（仅对手可花，每个 ±1 DICE），BLESSING MARKERS 始终**有利于**持有者。

本节解释支配 Trench Crusade 玩法的核心原则。

### Keywords

> PDF p.23

规则中大写字母词（如 `ACTION`、`BLOOD MARKER`）称为 Keywords（关键词），定义核心能力、规则、兵种与伤害类别。所有 Keywords 完整定义见 `→ rules/03-keywords-glossary.md`。

### Success Rolls

> PDF p.24

游戏中常需为模型做 **Success Roll（成功判定）** 并在表上查结果，以判断模型是否成功执行任务（如远程攻击是否命中）。规则会说明何时需做 Success Roll，以及结果含义。

例如：Ranged Attack 的 Success Roll 结果 = **Failure** → 攻击落空；= **Success** → 命中，做 Injury Roll；= **Critical Success** → 命中且额外加成（见下方 Success Roll Table 12+ 行）。

#### Success Roll 流程

1. 取 **2D6**
2. 加任意 +DICE 或 -DICE（详见下文 [+DICE and -DICE](#dice-and--dice)）
3. 掷所有骰子
4. 若加了 +DICE → 取**最高 2 个**；若加了 -DICE → 取**最低 2 个**
5. 两骰相加，对照 Success Roll Table

#### Success Roll Table

| Roll 结果（修正后两骰之和） | 判定 |
|---:|---|
| 2-6 | **Failure**（失败） |
| 7-11 | **Success**（成功） |
| 12+ | **Critical Success**（大成功）。Ranged Attack 或 Melee Attack 时，Injury Roll **+1 INJURY DICE** |

> **Errata 裁决**：并非所有 ACTION 都要做 Success Roll。**需要 Success Roll 的 ACTION 在该 ACTION 的规则正文中明确说明**（如 Dash / Shoot / Fight 等通用 ACTION 在本章 Comprehensive Rules 段中说明）。（→ `errata/rules-commentaries.md` Core Rules Q8）

### Risky Success Rolls

> PDF p.24

**Risky Success Roll（风险判定）** 的掷骰方式与普通 Success Roll 完全相同，但若**失败**：
- 该模型的 Activation **立即结束**（详见 [Activation Phase](#2-activation-phase)）
- 若 Risky Success Roll 是某 ACTION 的一部分但发生**在该模型 Activation 之外**，则该 ACTION 立即结束。

适用于 Success Roll 的所有规则同样适用于 Risky Success Roll。

### +DICE and -DICE

> PDF p.25

规则常要求向掷骰加额外骰子，格式为 `+1 DICE` 或 `-1 DICE`（如：从高地射击时 +1 DICE）。

- **+DICE**：每 1 个 +DICE 多加 1 个骰子，掷完取**最高 2 个**。例：+2 DICE → 投 4 个骰，取 2 高。
- **-DICE**：每 1 个 -DICE 多加 1 个骰子，掷完取**最低 2 个**。例：-2 DICE → 投 4 个骰，取 2 低。

#### Combining +DICE and -DICE（相互抵消）

同次掷骰若同时存在 +DICE 与 -DICE，**两两抵消**直至只剩一种。例：+2 DICE 与 -1 DICE 同时存在 → 1 个 +DICE 抵消 1 个 -DICE → 余下 1 个 +DICE。

#### 示例（PDF p.26）

> Trench Pilgrim 用 Bolt-Action Rifle 射击 Heretic。Heretic 在 cover（-1 DICE）。投 3D6 = 5、5、1。取 2 低（5 和 1）= **6**。失败（< 7），未命中。
>
> Heretic Trooper（Ranged +1 DICE）射击 Pilgrim（cover -1 DICE）。+1 与 -1 互相抵消，投 2D6 = 4、3 = **7**。命中！

### Injury Dice

> PDF p.25

`+/- INJURY DICE` 与 `+/- DICE` 工作原理相同，但**作用于 Injury Roll**（受伤判定）而非 Success Roll（详见 [Injury Rolls](#injury-rolls)）。

#### Dice 与 Injury Dice 的区分

- 模型 / Battlekit 的 `+/- DICE` 关键词 **仅** 作用于 Success Roll，**不**作用于 Injury Roll。
- 模型 / Battlekit 的 `+/- INJURY DICE` 关键词 **仅** 作用于 Injury Roll，**不**作用于 Success Roll。

### Blood Markers

> PDF p.27-28

战斗中你的战士可能因攻击、超自然力量、坠落等受伤。Trench Crusade 用 `BLOOD MARKERS（血液标记）`表示伤害——除物理伤口外亦表示疲惫、震荡、炮弹休克、精神紧张等。

#### Placing Blood Markers

- 每次你的模型受伤，在模型旁放 1 个 `BLOOD MARKER`。
- 模型上 `BLOOD MARKERS` **不能超过 6 个**——到达 6 个后忽略放置指令，直到数量降回 6 以下。

#### Spending Blood Markers

**对手**（即"敌方玩家"）可花费你模型身上的 `BLOOD MARKERS`：

- **你为友方模型 take Success Roll 时**：对手可宣告花 1 个或多个 `BLOOD MARKERS`，每个 = Success Roll **-1 DICE**。被花的标记从模型上移除。例：模型有 3 个 BLOOD MARKERS → 对手可花 1/2/3 个 → -1/-2/-3 DICE。
- **对手为你的模型 make Injury Roll 时**：对手可花 1 个或多个 `BLOOD MARKERS`，每个 = Injury Roll **+1 INJURY DICE**（详见 [Injury Rolls](#injury-rolls)）。

> ⚠️ **新玩家最易混淆条目（视频教学明确警告）**：Injury Roll **不是 ACTION**，所以 `BLOOD MARKER` **不能**用于反向修正被攻击方自己的 Injury Roll——即**你不能用自己模型身上的 blood marker 来减自己被攻击时的 injury dice**。BLOOD MARKER 只能由**对手**花掉（让你的模型行动失败 / 受伤更重）。
>
> 范例：你的 Pilgrim 身上有 3 个 BLOOD MARKERS。当 Heretic 攻击该 Pilgrim 命中、做 Injury Roll 时，**Heretic 玩家**可花掉 Pilgrim 身上的 3 个 BLOOD MARKERS 让伤害更重；**你不能**花 Pilgrim 自己身上的 markers 来让伤害减轻。

#### Gameplay Example（PDF p.27）

> Trench Pilgrim 已有 1 个 BLOOD MARKER。Heretic Trooper 用 Bolt-Action Rifle 射击 Pilgrim，得 8 命中。Heretic 玩家决定花掉 Pilgrim 身上的 BLOOD MARKER 加大伤害概率。投 3D6（2D6 + 1 INJURY DICE）= 5、1、4。取 2 高 = **9**。Pilgrim out of action！

### Blessing Markers

> PDF p.28

`BLESSING MARKERS（祝福标记）` 是 `BLOOD MARKERS` 的镜像：超自然力量、圣物等可授予模型。

#### Placing Blessing Markers

- 每次你的模型获得 blessing，在旁放 1 个 `BLESSING MARKER`。
- 上限同样 **6 个**——超出忽略放置指令。

#### Spending Blessing Markers

**你自己**（"己方玩家"）可花费友方模型身上的 `BLESSING MARKERS`：

- **你为友方模型 take Success Roll 时**：可宣告花 1 个或多个，每个 = Success Roll **+1 DICE**。
- **对手为你的模型 make Injury Roll 时**：可宣告花 1 个或多个，每个 = Injury Roll **-1 INJURY DICE**。

#### Tracking Blood & Blessing Markers

可用不同颜色的骰子或方块计数（如红色骰记 BLOOD MARKERS、黄色骰记 BLESSING MARKERS）。

> **Errata 裁决**：当两位玩家要对**同一次掷骰**同时应用 `BLOOD MARKER` 与 `BLESSING MARKER` 时，由持有 **Initiative** 的玩家决定执行顺序。（→ `errata/rules-commentaries.md` Core Rules Q1）

### Profiles

> PDF p.29

每个模型有 Profile 定义其战斗能力。此外 Battlekit Profiles 涵盖模型可携带的 Weapons、Armour、Equipment。

- Model Profile 详解见 Warbands of Trench Crusade — Starting a Warband 章节（`→ matches/roster-template.md` 与 `→ warbands/*`）
- Battlekit Profile 详解见 `→ rules/05-battlekit.md`

Profile 含字段：Cost（👑）/ Movement / Ranged / Melee / Armour / Base / Keywords / Lore。

### ACTION vs Attack（动作与攻击的概念分离）

> 本节为 v0.1 整理（基于 PDF 多处 + Errata），用于澄清新玩家最常误解的概念差。

`ACTION` 与 `Attack` 在 Trench Crusade 规则中**不是同一回事**：

- **ACTIONS** 是模型在 Activation 时可执行的活动，例如 `Move ACTION` / `Charge ACTION` / `Retreat ACTION` / `Dash ACTION` / `Shoot ACTION` / `Fight ACTION`。**同类型 ACTION 每次 Activation 仅一次**（除非规则另有说明）。
- **Ranged Attack / Melee Attack** 是攻击行为，**不是** ACTION 本身。它们是 Shoot ACTION 或 Fight ACTION **执行的内容**——但许多其他规则（如 Cast Spell 法术 ACTION、Goetic Power 等）也可触发 Ranged Attack 或 Melee Attack。

**关键含义**：

1. **"每次 Activation 同类型 ACTION 仅一次"** 的限制**只适用 ACTION**，不适用 Attack。例：Sorcerer 可在同一 Activation 中先做 Cast Spell ACTION（产生一次 Ranged Attack），再做 Shoot ACTION（产生另一次 Ranged Attack）。
2. **某些 marker / 修正规则** 按"ACTION"字面应用——例如 BLOOD MARKER 的"每次模型 take Success Roll 时可花一个"针对 ACTION 的 Success Roll（而 Injury Roll 不是 ACTION，故被攻击方不能花自己身上的 marker 反向减 injury dice，见 [Blood Markers](#blood-markers) ⚠️ 警告）。
3. **"ACTION 触发的 Injury Roll"与"Attack 触发的 Injury Roll"也不同**：见 [Injury Rolls](#injury-rolls) 与 Errata Core Q9。

> **Errata 裁决**：**Ranged（与 Melee）Attack 不是 ACTION**——只有 ACTION 才被限定为"每次激活同类型仅一次"（除非另有说明）。（→ `errata/rules-commentaries.md` The Court Q1，揭示通用规则）
>
> **Errata 裁决**：**所有 ACTION 都需要 Success Roll 吗？不**。**需要 Success Roll 的 ACTION 在该 ACTION 的规则正文中明确说明**。（→ `errata/rules-commentaries.md` Core Rules Q8）

---

## Other Rules Principles

> PDF p.30-31 · **TL;DR**：分数一律**向上取整**；测距走英寸（数字化由 MCP `get_distance` 计算，3D 欧氏）；LOS 三态 clear / partial_cover / blocked；同一骰子只能 re-roll 一次；Pre-Measuring 允许（任何时候可量）。

### Fractions

规则提到分数时：

- 若被修正的值是**距离**（如武器射程、模型移动距离）→ **保留分数**
- 其他情况 → **向上取整**至最近整数

### Measuring Distances

距离测量规则（散文版 PDF p.30）：

> **数字化映射**：所有距离测量、`within X"`、`in contact` 判定一律按 `→ matches/coordinate-system.md` §3 中定义的 3D 欧氏距离算法处理。**MCP server 仲裁**，AI 不心算。具体语义映射见该文件 §3.2 PDF 术语映射表。

- **Within**：A within X" of B 等价 `get_distance(A, B) ≤ X`（→ coord §3.2）
- **In contact**：基座接触；数字化映射 `get_distance ≤ 0` 或基座格相邻（→ coord §3.2、§5.5）

### Line of Sight

> PDF p.30

**完全交由坐标系契约判定**：

- 判定算法、partial / clear / blocked 三态、cover 三问 → `→ matches/coordinate-system.md` §6
- 不在此散文复述

**关键语义保留**：

- 模型 360° 全向视野，做 LOS 判定前可自由 pivot
- 测量 Line of Sight 时**不算 target 的 base、hands、feet、携带物（如武器或旗帜）**——`get_los` 的输入是基座中心点
- **Partial Line of Sight**：射击方能见目标的部分而非全部 → MCP `get_los` 返回 `partial_cover`

> **Errata 裁决**：模型对自己**有** Line of Sight。（→ `errata/rules-commentaries.md` Misc Q7）

### Points on the Battlefield or Terrain Pieces

> PDF p.30

需对战场上或地形上的一个**点**做 LOS 判定时：

- 该点视作 **1mm × 1mm × 1mm 高**（→ coord §6 的 partial-cover 判定按此尺寸处理）

> **Errata 裁决**：检测 LOS 到点时，**能看到该点的任何部分**即算 LOS。**该点视作 1mm 高**。（→ `errata/rules-commentaries.md` Keywords Q7）

### Model Accuracy

> PDF p.30

确保战场上的模型与其声明的尺寸、实际装备（武器、护甲）一致时，遵循这一格言：

> *"Be strict with yourself but lenient with others."*（对自己严格，对他人宽容。）

实操含义：

- 自己的模型应当与所选 profile / battlekit **视觉一致**（装备槽体现在 miniature 上）
- 对手模型若视觉与 profile 略有出入，**默认按 profile 数据处理**，不要纠缠

> **数字化对战项目说明**：本项目以 `match-state.yaml` 为权威——模型 profile / equipment 字段就是裁决依据，无视觉一致性问题。该条 PDF 规则在实体桌游中相关，数字化场景下作为历史背景保留。

### Model Placement

> PDF p.31

- 部署或移动模型时，基座**不能**与 `IMPASSABLE` 地形或其他模型基座重叠（→ `rules/03-keywords-glossary.md#impassable-terrain`）
- 可让基座部分悬空，**只要超过一半在战场或地形上**
- 经对手同意，可将模型移至附近安全位置（仍视作在原位）
- **Deployment & Redeployment**：部署 / 重新部署不视作 move

**穿越空间的判定**：

> **Errata 裁决**：模型**不能**穿越任何小于其基座尺寸的空间（如窗户、走廊、地形件之间的缝）。若模型基座两维不等（如 30mm × 60mm），判定能否穿越某空间时**取较小一维**。（→ `errata/rules-commentaries.md` Core Rules Q7）

> ⚠️ **Base size 阈值方向不一致**（与上条对照阅读）：另一条 Errata 在判定"按 Base size 给予不同效果"（如小于/大于 40mm）的规则时，**取较大一维**（如 30×60mm 模型按 60mm 处理）。（→ `errata/rules-commentaries.md` Misc Q1）
>
> **两条裁决方向相反**：
> - 穿越空间（窗户/狭缝）→ 取**较小**一维（Core Q7）
> - 按尺寸阈值套用规则 → 取**较大**一维（Misc Q1）
>
> 字面应用即可：穿越是"能否塞过去"问题（看最瘦的一边），阈值是"模型规格上属于哪一档"问题（看最大维代表的尺寸级别）。

### Pre-Measuring

> PDF p.31

除非规则明确禁止，可在**任何时候**测量距离（如检查是否在射程内、是否能 charge 等）。

### Re-rolls

> PDF p.31

- Re-roll = 重投同次掷骰使用的骰子
- 同一颗骰子**不能 re-roll 两次以上**
- 若 re-roll 一次 XD6（如 2D6、3D6 等），**必须重投全部骰子**

### Rolling Off

> PDF p.31

各玩家投 1D6，最高者获胜。

- 不能 re-roll 或修正 roll-off 的骰子
- 平手则**重投**

---

## Game Turns

> PDF p.32-34 · **TL;DR**：每 Turn 三阶段 — ① **Initiative**（roll-off d6 决先手）→ ② **Activation**（双方轮流激活模型，每次激活可做多个 ACTION，但同类 ACTION 一激活只能做 1 次）→ ③ **Morale**（伤亡过半 take Morale Check）。Turn 总数 + 胜负条件由 scenario 定。

Trench Crusade 游戏分为若干 Turn（回合）。剧本指定回合数与胜负判定（→ `rules/08-scenarios.md`）。

### The Sequence of Play

每个 Turn 分三阶段：

1. **Initiative Phase**：判定哪位玩家持 Initiative，执行 start of Turn tasks
2. **Activation Phase**：双方**交替激活**模型，每次一个，直到双方所有模型都激活一次
3. **Morale Phase**：若某玩家半数或以上模型 Down 或 Out of Action，须做 Morale Check；**连续 2 个 Turn 失败则输掉游戏**。然后执行 end of Turn tasks，开始新 Turn。

### 1. Initiative Phase

> PDF p.32

每个 Turn 开始时，判定 Initiative（先手 / 主动权），并执行 start of Turn tasks。**持 Initiative 的玩家选择哪方先 Activate**。

#### Determining the Initiative

- 数双方战场上模型数（**不计** Down 或 Out of Action 的模型）
- **模型少**的玩家持 Initiative
- 若平手 → roll-off（投 D6 高者持）

#### Start of Turn Tasks

若有多个 start of Turn task 同时触发，由持 Initiative 的玩家决定执行顺序。

#### Simultaneous Activities

若两件事同时发生，由持 Initiative 的玩家决定执行顺序。

> **Errata 裁决**：当两位玩家要对同一次掷骰应用 BLOOD MARKER 与 BLESSING MARKER 时，由持 Initiative 的玩家决定顺序——通用裁决条款。（→ `errata/rules-commentaries.md` Core Rules Q1）这条裁决在剧本场景下（如 Armoured Train 中 King of the Hill 同时完成）同样适用（→ Scn Q2）。

### 2. Activation Phase

> PDF p.33

双方**交替** Activating 模型，每次一个。持 Initiative 的玩家选哪方先 Activate。

#### Carrying Out Activations

- 轮到你时，选一个本回合**未激活**的友方模型 Activate
- 用该模型 take ACTIONS（详见下文 [ACTIONS](#actions)）
- 该模型 Activation 结束后，对手 Activate 一个他们的模型
- 若一方模型用完，另一方接连激活剩余模型直到全部激活
- 全部激活完成后进入 Morale Phase

可在模型旁放小标记表示已激活，便于跟踪。

### ACTIONS

> PDF p.34

激活模型时，可 take 一个或多个 ACTIONS。**ACTIONS 顺序任意**——但**每种 ACTION 同次激活仅一次**（除非另有说明）。

例：可 Shoot → Move → Dash；或 Dash → Charge → Fight；但**不能** Shoot → Dash → Shoot。

#### Common Actions

所有模型可执行的通用 ACTIONS：

##### Move / Charge / Retreat（**三选一互斥**）

> **Errata 裁决**：Move ACTION / Charge ACTION / Retreat ACTION 是**不同类型**的 ACTION——但**模型在同一次 Activation 中不能 take 其中超过一个**。若想让模型移动两次以上，必须改用 Dash ACTION。（→ `errata/rules-commentaries.md` Core Rules Q2）

- **Move**：移动模型距离不超过其 Movement Characteristic（详见 [Moves](#moves)）。Move ACTION **不能**用于移动到敌方 1" 内（必须用 Charge ACTION）。
- **Charge**：选定 12" 内、在自己 LOS 内的敌方模型，投 1D6 + Movement，最大 12"，沿最短直线移向目标（详见 [Charging](#charging)）。**Shoot ACTION 后不能再 Charge 或 Fight**（除非武器有 `ASSAULT` 关键词，→ `rules/03-keywords-glossary.md#assault`）。
- **Retreat**：模型在敌方 1" 内时离开 melee 的特殊移动（详见 [Retreating](#retreating)）。

##### Dash

可让模型移动距离至 Movement Characteristic，**但需先 take Risky Success Roll**：

- Success → 移动（**不能** charge 或 retreat）
- Failure → Activation 结束

Dash 可与 Move / Charge / Retreat ACTION **同回合并用**，前后顺序任意。例：Dash → Shoot → Move。

> **同回合 2 次 Risky Success**：Dash 本身含 Risky Success Roll；若先 Dash 后 Move ACTION 进入 Dangerous terrain（触发 Risky Success Roll，见 `→ rules/03-keywords-glossary.md#dangerous-terrain`），即出现"同回合 2 次 Risky Success"。

##### Shoot

允许模型做 Ranged Attack（详见 [Combat — Ranged Attacks](#combat--ranged-attacks)）。

##### Fight

允许模型做 Melee Attack（详见 [Combat — Melee Attacks](#combat--melee-attacks)）。

#### Warband / Battlekit / Skill 专属 ACTIONS

某些模型有 Warband Entry / Battlekit 特殊规则 / Campaign Skill 描述的额外 ACTIONS。这些 ACTIONS 与上述通用 ACTIONS **并存**，但同样**每种每次激活仅一次**。

---

## Movement

> PDF p.35-37 · **TL;DR**：4 个移动 ACTION — **Move**（基础，距离 ≤ M）/ **Dash**（前置 Risky Success → +½M）/ **Charge**（≤12"，roll Charge Bonus d6 接 Melee）/ **Retreat**（脱离 melee 触发 enemy 自由攻击）。地形 `movement_cost` 决定每格消耗。Difficult terrain 2× 加权。"Move"（大写 = ACTION），"move"（小写 = 动作）。

Move、Charge、Retreat、Dash ACTION 都让你拿起一个模型移动它。Move 与 Dash 移动方式相同（Dash 多一个前置 Risky Success Roll）；Charge 与 Retreat 移动方式有特殊规则。

> **术语区分**：大写 "Move"（ACTION）指 **Move ACTION**；小写 "move"（动词）指**移动模型**这个动作。

### Moves

> PDF p.35

移动方法：

- 拿起模型沿路径在战场或地形上移动
- 路径**不能超过 Movement Characteristic**（除非另有说明）
- 可任意方向 / 组合方向移动
- 可在移动中**自由 pivot**任意朝向（v0.1 不引入 facing 字段 → `matches/coordinate-system.md` §5.6）

**附加规则**：

- 模型只能**穿过**友方模型，**前提是**有足够的剩余移动力完整穿过
- 模型只能在规则明确允许时离开战场
- 模型只能通过 **Charge** ACTION 移动到敌方 1" 内
- 若一个模型 move 开始时已在敌方 1" 内，则只能：
  - **整个 move 全程**保持在所有开始时 ≤1" 距离的敌方 1" 内，或
  - 做 **Retreat**（→ [Retreating](#retreating)）
- 移动结束时模型基座任何部分**不能**距起始位置超过 Movement Characteristic 的英寸数

> **数字化测量**：基座占格、模型间距、Movement Characteristic 的 1" = 1 格语义 → `→ matches/coordinate-system.md` §3、§5

### Charging

> PDF p.36-37

Charge ACTION 让模型做一种特殊移动——**charge**——以接近至敌方 1" 内。

- **进入敌方 1" 内**（基座间测量）**只能**通过 Charge 实现
- 适用所有敌方模型，包括 Down 状态的、或已在另一友方 1" 内的敌方

#### Declare Charge

宣告 Charge ACTION 后：

- 选一个**对你模型可见**（LOS 内）且在 **12" 之内**的敌方模型为目标
- LOS 与距离判定 → `→ matches/coordinate-system.md` §3.2、§6

#### Interposing Enemy Models（阻隔敌方模型）

若到达目标的路径会让 charging 模型在到达目标 1" 前先进入**其他敌方模型** 1" 内：

- **必须**改选该阻隔敌方为 charge 目标，或**不进行 charge**

合法 charge 路径枚举由 MCP 仲裁 → `→ matches/coordinate-system.md` §8 `valid_charge_paths`

#### Charge Bonus

选定目标后：

- 投 1D6 加到 Movement Characteristic 上（**最大 Movement Characteristic 为 12"**）
- 该 D6 即 Charge Bonus

#### Charge Moves

按 Charge Bonus 加成后的距离向目标移动，附加规则：

- 必须沿**最短直接路径**指向目标
- Climbing、Jumping、Jumping Down 或穿过 Dangerous terrain **可选**（前提是绕开的路径仍最短）
- 模型接触目标时**必须停下**——**除非**继续移动可保持与目标接触并落入其他敌方 1" 内

**结果判定**：

- charge 完成后若在目标 1" 内 → **charge 成功**
- 未达到 → **charge 失败**，模型停在 charge move 完成处
- **注意**：完成 charge 并**不自动**允许 Fight。要做 Melee Attack 需另做 Fight ACTION（前提是模型允许）

### Retreating

> PDF p.37

Retreat ACTION 让在敌方 1" 内的模型移开。

**关键流程**：

1. 在 retreating 模型实际移动前，**对手为每个**与该模型距离 ≤1" 的敌方模型 take 1 次 Fight ACTION（攻击 retreating 模型）
   - 每个攻击模型**只能用 1 件武器做 1 次 Melee Attack**（不能 Multiple Melee Weapons），但若武器带 `CLEAVE (X)` 关键词，CLEAVE 仍生效（→ `rules/03-keywords-glossary.md#cleave-x`）
2. 攻击结算后，若 retreating 模型**未** Down 或 Out of Action（→ [Injuries](#injuries)），玩家可移动该模型
3. retreating 移动距离 = Movement Characteristic
4. 移动结束时 retreating 模型必须 **> 1"** 离开所有敌方模型
5. 若无法做到 → **完全不能移动**

**Redeploying 不算 retreat move**。

> **Errata 裁决**：模型即便**无法移动**仍可宣告 Retreat ACTION。然而，**即便模型无法移动，它仍如同已 Retreat 一样会受到攻击**（除非另有说明）——即对手仍可对其做 1 次免费 Fight ACTION。（→ `errata/rules-commentaries.md` Core Rules Q3）

---

## Terrain（在 Movement 中的引用）

> PDF p.38 · **TL;DR**：4 个移动主类 — **Open**（默认）/ **Difficult**（2× mv_cost）/ **Dangerous**（进入或穿越触发 Injury Roll）/ **Impassable**（不可进入）+ **Cover** 修饰符（-1 DICE 对其内/旁模型的攻击）。Schema 详见 [`matches/coordinate-system.md`](../matches/coordinate-system.md) §7 七类对照表。

地形类型完整规则在 `→ rules/04-battlefield-terrain.md`（Pass 5）。本节仅给出 Movement 视角下需引用的概念：

- **Open / Difficult / Dangerous / Impassable** 四种主类型 + **Cover** 修饰符
- 各类完整 keyword 定义：
  - `DIFFICULT TERRAIN` → `rules/03-keywords-glossary.md#difficult-terrain`
  - `DANGEROUS TERRAIN` → `rules/03-keywords-glossary.md#dangerous-terrain`
  - `IMPASSABLE TERRAIN` → `rules/03-keywords-glossary.md#impassable-terrain`
  - `COVER` → `rules/03-keywords-glossary.md#cover`
- **七类地形 yaml schema 与示例** → `→ matches/coordinate-system.md` §7.3（Trench / Ruins / Abandoned Corner / Hill / Dangerous / Difficult / Landmark）

**Moving into Terrain**：模型 "in" 一块地形当且仅当其基座**一半以上**在该地形边界内（PDF p.38）。

**Cover** 概念由坐标系契约的 `target_in_cover(B)` 三问算法判定（→ `matches/coordinate-system.md` §6.2）。本节**不重复**散文版的 cover 三问——若需查询完整三问 → 坐标系契约 §6.2。Cover 触发 ranged `-1 DICE` 修正（→ [Ranged Attack Modifiers](#ranged-attack-modifiers)）。

---

## Climbing & Jumping

> PDF p.39-40 · **TL;DR**：**Climb sheer surface** 需 Risky Success Roll（失败 fall 回起点）；**Jump across** 距离 ≤ Movement，作为正常移动一部分；**Jump down** 是 free movement（不耗 M），但落差 ≥3" 触发 Falling Injury Roll。Climbing 距离按垂直高度算入总 Movement。

### Climbing Sheer Surfaces

> PDF p.39

- 1" 以下的地形、3" 以下的 Trench Walls（战壕墙）、梯子 / 坡道 / 绳索 / 楼梯等专门为攀爬设计的设备 → 视作 **Open terrain**（无须判定）
- 其他**垂直 sheer surface**（如墙）需 Climb：
  - 若模型移动到 sheer surface 1" 内可宣告 Climb
  - 必须有**足够的剩余移动力**爬完整个垂直高度（不能停在墙中段）
  - 在到达 sheer surface 时 take **Risky Success Roll**
  - Success → 模型直接上 / 下到顶端 / 底端；可用剩余移动力继续移动
  - Failure → 不能再移动，Activation 结束

### Jumping Over Gaps

> PDF p.40

可宣告模型在 move 中 Jump：

- 跨越缝隙宽度**不超过 Movement Characteristic 的一半**
- "到缝隙前的移动距离 + 缝隙宽度" 之和 **≤ Movement Characteristic**
- 例：Movement 6" 模型 → 可移动 3" 再跳过 3" 宽缝隙

**流程**：

1. 移动到缝隙边
2. take **Risky Success Roll**
3. Success → 把模型放到对岸，可用剩余移动力继续移动
4. Failure → 模型 **Falls**（详见 [Falling](#falling)），Activation 结束（对手选模型从哪一侧 Fall 下）

> **Errata 裁决**：将模型放到缝隙对岸所需的额外移动（含基座占位）视为 **free movement（自由移动）**——**只要"到缝隙前的移动 + 缝隙本身的距离"之和 ≤ Movement Characteristic**。例：Movement 6" 模型可移动 3" 再跳 3"，让基座完整落到对岸的额外位移是 free。（→ `errata/rules-commentaries.md` Core Rules Q4）

### Jumping Between Ledges of Unequal Heights

> PDF p.40

跨越不等高 ledges 的缝隙：

- 若**跳出方**较高 → 按 **Jumping Down** 规则结算（→ [Jumping Down](#jumping-down)）
- 若**降落方**较高 → 把额外高度加到水平距离上（可能导致跳跃**不可能**完成，若加后超过模型可移动距离）

### Jumping Down

> PDF p.40

模型移动中可 Jump Down：

- **Jumping Down 本身不消耗移动**（"free"）
- 但若 Jump Down **≥ 3"**，视作 **Falling**，必须做 Injury Roll 才能继续移动（→ [Falling](#falling)）

---

## Falling

> PDF p.41 · **TL;DR**：模型落到下方第一个可占据平面；按下落距离做 Injury Roll，**每 3" +1 INJURY DICE**；落点被占则推到最近空格。MCP `roll_falling(distance_inches, modifier?)` 自动计算 dice 数。

当模型 Fall 时：

- 从当前位置移到下方第一个可占据的平面
- 若 Fall **≥ 3"**，必须为模型做一次 Injury Roll：
  - 每 **3"** 加 **+1 INJURY DICE**
  - 例：Fall 3-5" → +1 INJURY DICE；Fall 6-8" → +2 INJURY DICE；以此类推

> 数字化映射：z 层差 × `layer_height`（默认 3"）≥ 3" 时触发 → `→ matches/coordinate-system.md` §2.3

**例外**：`FLYING` 关键词模型 Fall 时**不**做 Injury Roll（→ `rules/03-keywords-glossary.md#flying`）。

---

## Combat — Ranged Attacks

> PDF p.42-44 · **TL;DR**：Shoot ACTION → 选 in-range（short ≤ R_short，long > R_short 且 ≤ R_long，-1 DICE）+ LOS 目标 → Success Roll（cover -1 / high-ground +1 / 射入混战时 1d6 随机选目标）→ 命中 → Injury Roll。Critical Success → Injury Roll +1 INJURY DICE。

Shoot ACTION 让模型做 Ranged Attack；Fight ACTION 让模型做 Melee Attack。本节规则讲解各类攻击如何进行。

**Ranged Attack 前提**：

- 模型必须有 **Ranged Weapon**（→ `rules/05-battlekit.md`）
- 模型**不能**在敌方 1" 内
- 模型若本次 Activation 已 take Charge 或 Fight ACTION，**不能再** take Shoot ACTION 做 Ranged Attack——**除非**武器带 `ASSAULT` 关键词（→ `rules/03-keywords-glossary.md#assault`）

### Ranged Attack Sequence

1. **Choose Weapon**
2. **Pick Target**
3. **Check Line of Sight**
4. **Check Range**
5. **Determine Modifiers**
6. **Take Success Roll** for attacking model

#### Choosing the Weapon

从模型 Profile 上的 Ranged Weapon 中选 1 件。

#### Picking the Target

- 选 1 个敌方模型作目标
- 目标必须**在攻击模型的 LOS 内**（→ `matches/coordinate-system.md` §6）
- 目标必须**在武器射程内**（→ [Measuring the Range](#measuring-the-range)）

### Shooting into Melee

> PDF p.42

若想射击在**任一**友方模型 1" 内的敌方目标：

- **必须投 1D6 决定真正目标**：
  - **1-3**：必须以**友方模型**为目标
  - **4-6**：可以以**敌方模型**为目标

**关键约定（PDF p.42 注释）**：

- 仅当一个 Ranged Attack 的目标在**友方** 1" 内时才需要随机化目标
- 但其他随机化情形**不发生**——例：用 `BLAST` 武器命中后，在爆破半径内的友方模型**不需要**随机化各自的 Injury Roll；BLOOD MARKER 放置时也不需要随机化

> **Errata 裁决**：当射入混战、掷出 1-3 须以友军为目标时，**只能**选**对攻击模型可见、且在所用武器射程内**的友军。若无这样的友军，攻击**作废**。（→ `errata/rules-commentaries.md` Core Rules Q5）

### Measuring the Range

> PDF p.43

- 距离从攻击模型基座**最近点**量到目标模型基座**最近点**
- 目标 in range ⟺ 该距离 **≤ 武器 Range**
- 数字化映射 → `→ matches/coordinate-system.md` §3.2

### Short Range & Long Range

> PDF p.43

- 距离 **≤ 武器 Range 的一半** → **Short Range**
- 距离 **> 武器 Range 的一半** → **Long Range**
- **Long Range** 攻击 → Success Roll **-1 DICE**

某些武器与 Skills 对 Short / Long Range 有特殊效果（如 `SHOTGUN` 关键词，→ `rules/03-keywords-glossary.md#shotgun`）。

数字化映射 → `→ matches/coordinate-system.md` §3.2（`is_in_range` 返回 `band: short / long / out_of_range`）

### Ranged Attack Modifiers

> PDF p.43

**通用修正（cumulative，相互之间按 +/- DICE 抵消规则处理）**：

| 情境 | 修正 | 触发条件 |
|---|:---:|---|
| **Elevated position（高地）** | **+1 DICE** | 攻击者比目标至少**高 3"**（按基座测量） |
| **Cover** | **-1 DICE** | 目标在 cover；判定 → `matches/coordinate-system.md` §6.2 三问 |
| **Long Range** | **-1 DICE** | 距离 > 武器 Range 的一半 |

> **关键说明**：
> - "高 3"+" → 由 z 层差 × `layer_height` 计算（→ `matches/coordinate-system.md` §3.2、§2.3）
> - Cover 触发条件、cover 三问算法 → `matches/coordinate-system.md` §6.2，**不在此重复**
> - Long Range 距离判定由 `is_in_range` 返回的 `band` 字段决定（→ coord §3.2）

#### 示例（PDF p.43）

> Trench Pilgrim 用 Musket 射击 Heretic Trooper（in cover）。Cover 加 -1 DICE。投 3D6 = 5、5、1，取 2 低 = **6**。失败（< 7），未命中。

### Ranged Attack Success Roll

> PDF p.44

最后做 Success Roll：

- **Failure** → 攻击落空，无事发生
- **Success** → 命中目标，做 Injury Roll（→ [Injuries](#injuries)）
- **Critical Success** → 命中目标，Injury Roll **+1 INJURY DICE**

---

## Combat — Melee Attacks

> PDF p.45 · **TL;DR**：Fight ACTION（前提：已贴脸 1" 内）→ Success Roll → 命中 → Injury Roll。Down 目标 +1 INJURY DICE。**Multiple Melee Weapons**：同 Activation 内每件 melee weapon 只能用一次，但可用多件（含 chainsaw / bayonet 等额外 INJURY DICE 武器）。

**Melee Attack 前提**：

- 模型必须有 **Melee Weapon**（→ `rules/05-battlekit.md`）
- 模型必须在目标 **1" 内**（→ `matches/coordinate-system.md` §3.2 within 1"）

### Melee Attack Sequence

1. **Choose Weapon**
2. **Choose Target**
3. **Determine Modifiers**
4. **Take Success Roll** for attacking model

#### Choosing the Weapon

从模型 Profile 上的 Melee Weapon 中选 1 件。

#### Choosing the Target

- 目标必须在攻击模型的 **1" 内**且在其 LOS 内（→ `matches/coordinate-system.md` §3.2、§6）

### Melee Attack Modifiers

> PDF p.45

| 情境 | 修正 | 触发条件 |
|---|:---:|---|
| **Diving Charge** | **+1 DICE** | 攻击者做 Diving Charge（→ [Diving Charge](#diving-charge)） |
| **Defended Obstacle** | **-1 DICE** | 目标 in cover **且** 提供 cover 的地形位于其与攻击者之间 |
| **Off-Hand Weapon** | **-1 DICE** | 攻击者用 Off-Hand Weapon 攻击（→ [Multiple Melee Weapons](#multiple-melee-weapons)） |

> **Defended Obstacle 触发条件**：地形 height ≥ ½"，且其位于攻防之间。完整地形 height 字段语义 → `matches/coordinate-system.md` §7.2。

> **跳过 Off-Hand 修正的途径**：模型若带 `IGNORE OFF-HAND WEAPON` 关键词（由 Promotion Skill **Berserker** / **Gunslinger** 赋予，→ `rules/06-campaign-rules.md` §4 Skill Tables），则用 Off-Hand Weapon 做 Melee Attack 时**不**受 `-1 DICE` 修正。该关键词是 `IGNORE [MODIFIER]` 的实例（→ `rules/03-keywords-glossary.md#ignore-modifier`）。

### Multiple Melee Weapons

> PDF p.45

带 2 件 Melee Weapons 的模型，可用一次 Fight ACTION 做**两次** Melee Attacks（一次一件，顺序自选）：

- 第二次攻击所用武器称 **Off-Hand Weapon**（触发 Off-Hand `-1 DICE`，详见 [Melee Attack Modifiers](#melee-attack-modifiers)）
- 两次攻击可指向**同一**或**不同**目标
- 若一件或两件武器带 `CLEAVE` 关键词（→ `rules/03-keywords-glossary.md#cleave-x`）：
  - 选其中一件先做 Melee Attack；若该件带 CLEAVE，连续做完所有 CLEAVE 攻击
  - 然后选另一件 Melee Attack（用 Off-Hand 修正）；若该件带 CLEAVE，连续做完所有 CLEAVE 攻击（仍带 Off-Hand 修正）

#### Melee Attack Success Roll

- **Failure** → 攻击落空
- **Success** → 命中，做 Injury Roll
- **Critical Success** → 命中，Injury Roll **+1 INJURY DICE**

### Diving Charge

> PDF p.46

可将友方模型的 charge 转为 **Diving Charge**——前提是该模型在 charge 中 **Jump Down ≥ 3"** 并落在目标 **1" 内**。

**流程**：

1. 模型 Jump Down 至少 3" 后落在目标 1" 内
2. 为该模型 take **Risky Success Roll**：
   - **Failure** → 模型被 take Down，并须做 Falling Injury Roll（→ [Falling](#falling)）
   - **Success** → **不用**做 Falling Injury Roll；该模型**下次** Melee Attack 的 Success Roll **+1 DICE**

---

## Injuries

> PDF p.46-49 · **TL;DR**：**Injury Roll** = 2D6 ±INJURY DICE ± modifier → ≤1 **No Effect** / 2-6 **Minor Wound**（+1 BLOOD MARKER）/ 7-8 **Down** / 9+ **Out of Action**。**Bloodbath**：对 Down 目标再受伤、或攻击方花 ≥3 BLOOD MARKERS / 触发 Concentrated Attack → 升级为 3D6（DEADLY 武器 4D6）。Armour 提供负 INJURY MODIFIER；IGNORE ARMOUR 无视之。

游戏中模型可能因攻击、坠落、穿越 Dangerous terrain 受伤。无论来源，**敌方模型受伤时**你必须为该模型做 **Injury Roll**。

### Injury Rolls

> PDF p.46

Injury Roll 类似 Success Roll：

1. 取 **2D6**
2. 加 `+/- INJURY DICE` 而非 `+/- DICE`
3. 掷骰
4. 加 `+/- INJURY MODIFIERS`
5. 查 Injury Roll Table

**关键定义**：

- `INJURY DICE` 加入 Injury Roll 的方式与 `DICE` 加入 Success Roll 相同
- `INJURY MODIFIERS` 加在 Injury Roll **结果**上（投完骰后 ± 修正值）
- **最大 `-INJURY MODIFIER` 不能超过 -3**（总和上限）

#### 示例（PDF p.46）

> Injury Roll 有 +1 INJURY DICE 与 -1 INJURY MODIFIER。投 3D6 = 2、4、5。取 2 高 = **9**。应用 -1 MODIFIER = **8**。查表 → **Down**。

**注**：若规则说某模型被 taken **Down** 或 **Out of Action**，按 Injury Roll Table 完整应用对应结果（**包括**放 BLOOD MARKER）。

> **Errata 裁决**：以"非 Injury Roll 来源"被打 Down 的模型（如 Eire Trench Cleric 的 *Away, Serpents!* 异能）**仍要**在旁边放 BLOOD MARKER——"被打 Down"与"受到 Injury Table 的 Down 结果"同义。（→ `errata/rules-commentaries.md` Core Rules Q10）

> **Errata 裁决**：当模型因**非攻击来源**（如某些异能效果）承受 Injury Roll 时：**你始终为敌方模型掷 Injury Roll**，花掉**敌方模型身上**的 BLOOD / INFECTION MARKER 与**友方模型身上**的 BLESSING MARKER。同理对手为你的模型掷。（→ `errata/rules-commentaries.md` Core Rules Q9）

> **Errata 裁决**：某些规则文本说 `INJURY DICE` / `INJURY MODIFIER` "for a model" 时，指**对该模型做的 Injury Roll**——**不**指该模型**发动**的 Injury Roll。例：*Artificial Life* 的 "Add -1 INJURY DICE to Injury Rolls for a Lion of Jabir" 适用于**对 Lion of Jabir 做的** Injury Roll。（→ `errata/rules-commentaries.md` Core Rules Q6）

### Bloodbath Rolls

> PDF p.47

当你为敌方模型做 Injury Roll 时，可花 **6 BLOOD MARKERS**（若目标 Down 则 **3 BLOOD MARKERS**）将该 Injury Roll 转换为 **Bloodbath Roll**：

- 投 **3D6 并把 3 个全部相加**（不是常规的 "取 2 个相加"）
- 加 `+/- INJURY DICE` 与 `+/- INJURY MODIFIERS` 的方式与普通 Injury Roll 相同
- 但池中取**最高 3 个**或**最低 3 个**（而非通常的 2 个）
- 若 Injury Roll 带 `DEADLY` 关键词（→ `rules/03-keywords-glossary.md#deadly`）→ **改投 4D6 并把 4 个全部相加**

> ⚠️ **新玩家最易混淆条目（视频教学明确警告）**：Bloodbath 累加 4D6 当武器自带 boost——例如 Infernal Bomb 等 `DEADLY` 武器触发 Bloodbath 时是 **4D6 全加**（而非 3D6）。-1 DICE 罚 + DEADLY Bloodbath → 投 4D6 取**最低 3 个**加总。

### Making an Injury Roll

> PDF p.48

完整步骤：

1. 取 **2 D6**
2. 加 `+/- INJURY DICE`（按 +DICE/-DICE 抵消规则处理）
3. 掷所有骰子
4. 取**最高 2 个**（若有 +INJURY DICE）或**最低 2 个**（若有 -INJURY DICE）
5. 两骰相加
6. 加 `+/- INJURY MODIFIERS`（总和最低 -3）
7. 查 Injury Roll Table

### Injury Roll Table

> PDF p.48

| Roll 结果（修正后） | Result |
|---:|---|
| **1 or less** | **No Effect**（无效果）。模型未受伤。 |
| **2-6** | **Minor Hit**（轻伤）。在模型旁放 1 个 `BLOOD MARKER`。 |
| **7-8** | **Down**（倒下）。在模型旁放 1 个 `BLOOD MARKER` 并标记为 Down。**若模型已经 Down，改放 2 个 `BLOOD MARKERS`**。 |
| **9+** | **Out of Action**（出局）。模型严重受伤或死亡，**移出战场**。 |

> ⚠️ **新玩家最易混淆条目（视频教学明确警告）**：`TOUGH` 关键词的模型**仅首次**承受 Out of Action（9+）时，将该结果改为 **Down**。**第二次及以后**的 9+ 结果**不再降级**（→ `rules/03-keywords-glossary.md#tough`）。
>
> 若该模型还有 Machine Armour 的 Standfast 规则，可按 Errata Keywords Q5 的"逐条字面套用"顺序进一步降级——但 TOUGH 自身只生效一次。

### Common Injury Roll Modifiers

> PDF p.48

以下修正可叠加（cumulative），但 **`-INJURY MODIFIER` 总和不能超过 -3**：

| 来源 | 修正 |
|---|---|
| **Blessing Markers** | 每花 1 个 → **-1 INJURY DICE**（由防御方花） |
| **Blood Markers** | 每花 1 个 → **+1 INJURY DICE**（由攻击方花） |
| **Critical Success** | **+1 INJURY DICE** |
| **Down**（Melee Attack 时目标 Down） | **+1 INJURY DICE** |
| **Abilities or Keywords** | 由规则 / Keyword 决定 +/- INJURY DICE 与 +/- INJURY MODIFIERS |
| **Armour Characteristic** | 加目标 Armour 的 -INJURY MODIFIER |
| **Battlekit**（Armour / Shield 等） | 加 Battlekit 的 -INJURY MODIFIER |

#### Gameplay Example（PDF p.48）

> Heretic Trooper 远程攻击命中 Trench Pilgrim Castigator（2 BLOOD MARKERS + Standard Armour）。Heretic 玩家花掉两个 BLOOD MARKERS。投 4D6（2D6 + 2 INJURY DICE）= 2、5、4、1。取 2 高 = **9**。Standard Armour 提供 -1 INJURY MODIFIER → 修正后 = **8**。查表 → **Down**！

### Down Results

> PDF p.49

Down 状态规则：

- **若模型在自己的 Activation 中被 take Down，Activation 立即结束**
- 为 Down 模型做 Success Roll → **-1 DICE**
- 对 Down 模型的 Melee Attack → Injury Roll **+1 INJURY DICE**
- Down 模型**不能因任何原因被移动**，除非它 Fall
- 下次被 Activate 时模型**站起来**，但**该 Activation 内 Movement Characteristic 减半**（含 Charge Bonus）
- 若 Down 时模型在 ledge 1" 内 → 可能 **Fall off the ledge**：
  - 在标记为 Down **之前**为模型做 Success Roll
  - Success → 标记 Down，**不** Fall
  - Failure → 模型从最近 ledge **Fall**，然后标记为 Down（→ [Falling](#falling)）

> **注**：Down 模型在被激活时（≥ ① 选模型这一步），down marker 立即移除，模型站起。本激活内的任何 Success Roll / Risky Success Roll 都**不**再适用 Down 模型 -1 DICE 修正（因为 down 状态已解除）。Activation 期间被打回 Down 才重新生效。

**视觉表示**：可在模型旁放 marker，或将模型**侧躺**（侧躺时模型中心应在原基座中心位置）。测距时 Down 模型可从模型任何部分量起（不限基座）。

### Out of Action

> PDF p.48

**Out of Action** 模型严重受伤或死亡——**移出战场，本局不归**。

> **Errata 裁决**：`TOUGH` 与其他防 Down 规则的叠加按**字面顺序、逐条套用**。例：带 TOUGH 与 Machine Armour 的 Lieutenant 第一次被 9+ → ① TOUGH 改为 Down → ② Machine Armour 的 Standfast 把 Down 改为 Minor Wound → ③ 结果是 Minor Wound。第二次被 9+ 时，TOUGH 仅生效首次，故直接 Out of Action。（→ `errata/rules-commentaries.md` Keywords Q5）

---

## 3. Morale Phase

> PDF p.50 · **TL;DR**：战团 **½ 或以上模型 Down/OoA**（向上取整）→ take **Morale Check**（Success Roll；LEADER 在场 +1 DICE）。Failure → 战团进入 **Shaken** 状态（次 Turn 起激活数受限）。**连续 2 Turn Morale 失败 → 直接输掉游戏**。

战团可能因伤亡过重撤离战场。Morale Phase 中：

- 若你的战团中**半数或以上**模型 Down 或 Out of Action（**向上取整**）→ 必须 take 一种特殊 Success Roll 称 **Morale Check**
- Morale Check 的掷骰方式与 Success Roll 相同：
  - **Success** → 战团正常继续
  - **Failure** → 战团进入 **Shaken** 状态

> **半数取整说明（PDF p.50 注释）**：5 个模型的战团需 3 个 Down 或 Out of Action 才触发 Morale Check（5÷2 = 2.5，向上取整 = 3）。

### Shaken Warbands

> PDF p.50

Shaken 战团的所有规则：

- **所有 Success Rolls 视作 Risky Success Rolls**（除非本来已是 Risky Success Roll）——失败立即结束 Activation
- 在**下一回合末**的 Morale Phase 中**必须再做一次** Morale Check（即使此时少于半数 Down 或 Out of Action）
  - Success → 解除 Shaken（未来仍可能再次进入 Shaken）
  - Failure → **战团逃跑，立即输掉游戏**

> **设计含义（连续 2 回合失败 = 输）**：第一次 Morale Check 失败 → Shaken；第二回合再失败 → 输。这就是"连续 2 个 Turn 失败"在玩法层的实际表现。

### Ending the Turn

> PDF p.50

只要双方战团**都未**逃跑，玩家可执行 end of Turn tasks，然后开始新 Turn。

#### End of Turn Tasks

若有多个 end of Turn task 同时触发，由持 Initiative 的玩家决定执行顺序。

### Sounding the Retreat

> PDF p.50

若 Morale Check 失败，可**主动**选择立即逃跑、输掉游戏，**而非**变 Shaken——有时主动撤退保存实力比拼到最后一兵一卒更明智。

---

## Winning the Game

> PDF p.51 · **TL;DR**：对手战团逃跑（连续 2 Turn Morale 失败 / 全 OoA） → **立即胜利**；否则最终 Turn 末按 scenario 判定（Turn 数、Glorious Deeds、VP / objective control 等）。

- 若对手战团逃跑 → **立即胜利**
- 否则在最终回合结束后判定胜负
- 胜负条件由剧本决定：回合数 / Glorious Deeds / VP 等 → `→ rules/08-scenarios.md`

---

## 附录 A：视频 transcript §3 14 条要点核对

> 用 `_references/core-rules-video-transcript.md` §3 校验清单逐条对照。**冲突时以 PDF v1.0.2 为准**。

| # | 视频要点 | PDF 对应位置 | 核对结果 |
|---:|---|---|---|
| 1 | 7+ 成功、12 大成功 | PDF p.24 Success Roll Table | ✅ 一致（PDF 表述：7-11 Success、12+ Critical Success） |
| 2 | +dice 取高 / -dice 取低 | PDF p.25 +DICE and -DICE | ✅ 一致 |
| 3 | Charge = Movement + d6，12" 内 | PDF p.36 Declare Charge + Charge Bonus | ✅ 一致（最大 Movement 12"） |
| 4 | Retreat 触发对方 free melee | PDF p.37 Retreating | ✅ 一致（但 PDF 明确每个攻击仅 1 件武器 1 次 Melee Attack，不能 Multiple Melee Weapons；CLEAVE 仍生效——视频未提此细节） |
| 5 | Long range = 武器射程一半以上 | PDF p.43 Short Range & Long Range | ✅ 一致 |
| 6 | Cover 三问 | PDF p.38 + Errata Keywords Q7 / Misc Q7 | ✅ 一致——但**本文件不复述三问**，引 `matches/coordinate-system.md` §6.2 |
| 7 | Injury 阈值 2-6 / 7-8 / 9+ | PDF p.48 Injury Roll Table | ✅ 一致（注意 PDF 多出 1 or less = No Effect 一档，视频简化未提） |
| 8 | 装甲减 -1/-1/-2/-3 | PDF p.48 Common Injury Roll Modifiers + `→ rules/05-battlekit.md`（Pass 6） | ✅ 数值在 battlekit；本文件只引概念框架 |
| 9 | TOUGH 仅首次有效 | PDF Keywords p.52-64（→ `rules/03-keywords-glossary.md#tough`）+ Errata Keywords Q5 | ✅ 一致，本文件在 Injury Roll Table 处加显著 ⚠️ 警告 |
| 10 | Bloodbath 3d6 加总（武器自带 boost = 4d6） | PDF p.47 Bloodbath Rolls | ✅ 一致，本文件加显著 ⚠️ 警告（DEADLY 武器触发 4D6） |
| 11 | Blood marker 不能反向修自身 injury | PDF p.27-28 + 视频 §1.9 + Errata Core Q9（非攻击 Injury 由对手掷） | ✅ 一致，本文件在 Blood Markers 节加显著 ⚠️ 警告 |
| 12 | Morale 触发：半数 down/out | PDF p.50 Morale Phase | ✅ 一致（PDF 明确"向上取整"，5 模型战团需 3 个 Down/Out 触发） |
| 13 | Shaken = 所有 action 变 risky | PDF p.50 Shaken Warbands | ✅ 一致 |
| 14 | 连续 2 回合失败 = 输 | PDF p.32 Morale Phase + p.50 Shaken Warbands | ✅ 一致——表述：Shaken 后下回合再失败立即输 |

**[v1.0.2 修正说明]**：视频要点全部在 PDF 中找到原文，无重大数值冲突。视频简化了边界细节（如 No Effect 一档、Retreating 攻击不能 Multiple Melee Weapons、TOUGH 与其他防 Down 规则的叠加顺序）——PDF v1.0.2 是权威，本文件以 PDF 为准并辅以 Errata 澄清边界。

---

## 附录 B：Pass 7 Errata 集成索引

本文件已内联以下 Errata 条目（Core Rules Q1-Q10、Keywords Q5/Q7、Misc Q1/Q7）：

| Errata 条目 | 集成位置 | 主题 |
|---|---|---|
| Core Q1（同时事件由 Initiative 决定顺序） | [Blessing Markers](#blessing-markers) + [1. Initiative Phase](#1-initiative-phase) | Simultaneous activities |
| Core Q2（Move/Charge/Retreat 互斥） | [ACTIONS](#actions) Move/Charge/Retreat 节 | 一次激活只能选一种 movement type |
| Core Q3（不能动也能宣告 Retreat） | [Retreating](#retreating) | 仍受 free melee |
| Core Q4（Jumping Over Gap 的 free movement） | [Jumping Over Gaps](#jumping-over-gaps) | 缝隙对岸落位是 free |
| Core Q5（误伤友军必须在 LOS+射程内） | [Shooting into Melee](#shooting-into-melee) | 否则攻击作废 |
| Core Q6（"for a model" 指对该模型做的 Injury Roll） | [Injury Rolls](#injury-rolls) | 方向澄清 |
| Core Q7（不能穿越小于基座的空间） | [Model Placement](#model-placement) | 取较小一维 vs Misc Q1 取较大一维（方向相反，已显式对照） |
| Core Q8（仅文本指明的 ACTION 才掷 Success Roll） | [Success Rolls](#success-rolls) + [ACTION vs Attack](#action-vs-attack动作与攻击的概念分离) | ACTION 不必都掷骰 |
| Core Q9（非攻击 Injury Roll 仍由对手掷） | [Injury Rolls](#injury-rolls) | 标记花费方向 |
| Core Q10（非 Injury Roll 来源的 Down 也放 BLOOD MARKER） | [Injury Rolls](#injury-rolls) | "被打 Down" = "Down 结果" |
| Keywords Q5（TOUGH 与其他防 Down 叠加按字面顺序） | [Out of Action](#out-of-action) | Lieutenant 范例 |
| Keywords Q7（LOS 到点：能见任何部分即算，点视作 1mm 高） | [Points on the Battlefield or Terrain Pieces](#points-on-the-battlefield-or-terrain-pieces) | LOS 到点判定 |
| Misc Q1（30×60mm 非正方基座按较大维处理） | [Model Placement](#model-placement) | vs Core Q7 显式对照 |
| Misc Q7（模型对自己有 LOS） | [Line of Sight](#line-of-sight) | LOS 自指 |

未集成到本文件但与本章相关的 Errata 条目（已在 `errata/rules-commentaries.md` 中）：

- Camp Q3（Trench Dog 不计入 Morale Check）→ 主体在 Campaign Rules（v0.2.A）；本文件 Morale Phase 暂不引用
- Misc Q2（"Friendly models within X" 包含自己）→ 与本文件多处距离判定相关；细节在 `rules/03-keywords-glossary.md` / `rules/05-battlekit.md`（Pass 6）

---

## 附录 C：跨文件引用统计

为方便人工校验，本文件出现的所有跨文件引用：

### → `matches/coordinate-system.md`

- §2.3（z 层级 / Falling 触发 3" 阈值）
- §3（距离测量算法）
- §3.2（PDF 术语映射表 / within / Short / Long Range / Elevated 3"）
- §4（战场默认 / 部署区）
- §5（基座占格）、§5.5（contact 定义）、§5.6（v0.1 不引入 facing）
- §6（LOS 三态）、§6.2（target_in_cover 三问与算法）
- §7（地形 schema）、§7.2（cover 字段语义 / height ≥ ½"）、§7.3（七类地形 yaml 例）
- §8（MCP server 接口：is_in_range / valid_charge_paths）

### → `rules/03-keywords-glossary.md`

- `#assault`（Shoot 后允许 Charge/Fight）
- `#cleave-x`（Retreat 触发的 free melee 仍触发 CLEAVE）
- `#cover`、`#dangerous-terrain`、`#difficult-terrain`、`#impassable-terrain`
- `#deadly`（Bloodbath 4D6）
- `#flying`（Fall 不做 Injury Roll）
- `#shotgun`（Long Range 的特殊修正）
- `#tough`（TOUGH 仅首次）

### → `rules/05-battlekit.md`

- 武器（Ranged Weapon / Melee Weapon）profile 与 range 字段
- Armour 与 Shield 的 -INJURY MODIFIER 数值
- ASSAULT / CLEAVE / DEADLY 等 keyword 应用的具体武器

### → `rules/04-battlefield-terrain.md`

- 七类地形完整规则（Pass 5）

### → `rules/08-scenarios.md`

- 剧本部署 / 回合数 / 胜负判定
- Glorious Deeds 框架

### → `errata/rules-commentaries.md`

- Core Rules Q1-Q10（全部 10 条）
- Keywords Q5、Keywords Q7
- Misc Q1、Misc Q7
- The Court Q1（"Attack 不是 ACTION" 通用裁决）

### → `matches/roster-template.md`、`→ warbands/*`

- Profile 字段含义（Pass 13 / Pass 8-9）

---

## 附录 D：不确定项 / 待锚定占位

无重大不确定项。本文件所有术语已在导入指南 §3.7 锚定表 A-G 找到对应中文锚定，未引入新术语；ALL-CAPS 关键词均按规范用反引号包围。

> 若 Pass 5/6 完成后发现地形 / 武器具体数据与本文件引用不一致，需回流校正本文件相关引用。
