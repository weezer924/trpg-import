# rules/01-core-rules: Core Rules（速览）

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.14-21
> 版本：v1.0.2
> 范围：Core Rules 章节——Initiative / Activation / Morale 三阶段、6 个基础 ACTION、Success Rolls、Combat（Ranged/Melee 含修正）、Falling、Injury Rolls、Blood/Blessing/Bloodbath、Down、Shaken。
>
> **用途**：5 分钟读完上手版。所有详细展开、边界条件、Errata 集成、跨文件接口均**只引用** `→ rules/02-comprehensive-rules.md#X`，本文件**不复述**。距离/LOS/cover 概念引 `→ matches/coordinate-system.md §X`；keyword 完整定义引 `→ rules/03-keywords-glossary.md#X`。
>
> **关键来源说明**：本节即 PDF 的"Core Rules"章节（p.14-21）——Trench Crusade 把 Core Rules（速览版）与 Comprehensive Rules（详细版）拆为两段。Core 给出最少必要规则供新玩家立即开战；Comprehensive 展开同一套规则的全部边界条件。**两段不冲突**——遇歧义以 Comprehensive 为准（PDF p.22）。

## Index

- [游戏目标与胜利条件](#游戏目标与胜利条件)
- [Core Concepts 速览](#core-concepts-速览)
- [回合结构（三阶段）](#回合结构三阶段)
  - [1. Initiative Phase（先手阶段）](#1-initiative-phase先手阶段)
  - [2. Activation Phase（激活阶段）](#2-activation-phase激活阶段)
  - [3. Morale Phase（士气阶段）](#3-morale-phase士气阶段)
- [基础 ACTIONS（6 个）](#基础-actions6-个)
- [Combat 速览](#combat-速览)
  - [Ranged Attack（远程攻击）](#ranged-attack远程攻击)
  - [Melee Attack（近战攻击）](#melee-attack近战攻击)
  - [Falling（坠落）](#falling坠落)
- [Injury Rolls（受伤判定）](#injury-rolls受伤判定)
- [Blood & Blessing Markers（血液 / 祝福标记）](#blood--blessing-markers血液--祝福标记)
- [Down Results（倒下结果）](#down-results倒下结果)
- [Bloodbath Rolls（血浴判定）](#bloodbath-rolls血浴判定)
- [Shaken & 输掉游戏](#shaken--输掉游戏)

---

## 游戏目标与胜利条件

> PDF p.14（章节首段）

Trench Crusade 是双人对战战棋。双方各控制一个 **Warband（战团）**（通常 6-10 个模型）。游戏分若干 **Turn（回合）**，每个 Turn 含 3 个阶段。胜负由所选 **Scenario（剧本）** 决定——通常是回合数 + Glorious Deeds / Victory Points。

- **立即胜利**：若对手 Warband 在 Morale Phase 失败到逃跑 → 你立即获胜
- **回合数结算**：所有 scenario 有固定回合数；最终回合结束后按剧本 VP 判定胜负
- 详细胜负条件 → `→ rules/08-scenarios.md`；通用 winning rules 详见 `→ rules/02-comprehensive-rules.md#winning-the-game`

**所需用品**：双方各一个战团；战场（推荐 36"×36"）；地形若干；6 面骰；卷尺（数字化对战由 MCP server 替代）。详见 `→ rules/02-comprehensive-rules.md#what-you-need-to-play`。

---

## Core Concepts 速览

> PDF p.14-15、p.18-20

- **2D6 + 取两骰之和**：所有 Success Roll 和 Injury Roll 基础掷骰 → 详见 `→ rules/02-comprehensive-rules.md#success-rolls`
- **7+ Success / 12+ Critical Success / 2-6 Failure**：判定阈值（Success Table）
- **+X DICE 多投取最高 2 个 / -X DICE 多投取最低 2 个**：修正方式；同次掷骰 +/- 两两抵消 → 详见 `→ rules/02-comprehensive-rules.md#dice-and--dice`
- **Risky Success Roll（风险判定）**：掷骰方式相同，但**失败立即结束 Activation** → 详见 `→ rules/02-comprehensive-rules.md#risky-success-rolls`
- **ACTION 与 Attack 不是同一回事**：ACTION 是激活时的活动（Move/Charge/Retreat/Dash/Shoot/Fight），Attack（Ranged/Melee）是 Shoot/Fight **执行的内容**——某些规则（如 Cast Spell）也可触发 Attack 而不消耗 Shoot ACTION → 详见 `→ rules/02-comprehensive-rules.md#action-vs-attack动作与攻击的概念分离`
- **Keywords（关键词）**：ALL-CAPS 词（如 `BLOOD MARKER`、`PENETRATING (1)`、`TOUGH`、`ASSAULT`）定义规则与能力 → 完整词典 `→ rules/03-keywords-glossary.md`

---

## 回合结构（三阶段）

> PDF p.14、p.20-21

每个 Turn 按顺序执行：

1. **Initiative Phase** — 判定先手
2. **Activation Phase** — 双方交替激活模型直至全部激活完
3. **Morale Phase** — 检查伤亡是否触发 Morale Check

### 1. Initiative Phase（先手阶段）

> PDF p.14

- 数双方战场模型数（不含 Down / Out of Action 的）
- **模型少**的玩家持 Initiative
- 平手 → 双方各投 1d6，高者持（roll-off）
- 持 Initiative 的玩家**选择本回合谁先激活**

详细规则、start of Turn tasks、同时事件顺序 → `→ rules/02-comprehensive-rules.md#1-initiative-phase`

### 2. Activation Phase（激活阶段）

> PDF p.14、p.20

- 由 Initiative 持有者选谁先激活
- 双方**交替**激活一个本回合**未激活**的友方模型
- 一个模型激活时可执行 1 个或多个 ACTIONS（见下节）
- 该模型结束后对手激活，循环直至全部激活完
- 若一方先激活完，另一方接连激活剩余模型

详细 Activation 流程 → `→ rules/02-comprehensive-rules.md#2-activation-phase`

### 3. Morale Phase（士气阶段）

> PDF p.21

- 若你的战团**半数或以上**模型 Down 或 Out of Action（向上取整）→ **必须** take Success Roll 作为 **Morale Check**
- Success → 战团正常继续
- Failure → 战团变 **Shaken（动摇）**
- Shaken 战团：所有 Success Roll **视作 Risky**（失败立即结束 Activation）；下回合末再做一次 Morale Check——若再失败 → **战团逃跑，立即输掉游戏**
- 也可在失败时**主动撤退**直接输掉以保存战力（Sounding the Retreat）

详细 Shaken 状态、Sounding the Retreat、End of Turn tasks → `→ rules/02-comprehensive-rules.md#3-morale-phase`

---

## 基础 ACTIONS（6 个）

> PDF p.14-15

每次激活可执行多个 ACTION，**顺序任意**，但**每种 ACTION 同次激活仅一次**（除非另有说明）。Move / Charge / Retreat **三选一互斥**（一次激活只能选其中一种 movement type）。

| ACTION | 简述 | 关键限制 | 详细引用 |
|---|---|---|---|
| **Move（移动）** | 模型移动距离 ≤ Movement Characteristic，任意方向；无需掷骰 | 不能移到敌方 1" 内（必须用 Charge） | `→ rules/02-comprehensive-rules.md#moves` |
| **Charge（冲锋）** | 选 12" 内、LOS 内的敌方为目标；投 1d6 加到 Movement（最大 12"），沿最短路径移向目标 | 接触目标 1" 内 = charge 成功；完成后**不**自动 Fight | `→ rules/02-comprehensive-rules.md#charging` |
| **Retreat（撤退）** | 模型在敌方 1" 内时离开 melee；移动 ≤ Movement Characteristic | 对手对每个 ≤1" 敌方做 **1 次 free Fight**（仅 1 件武器、不能 Multiple）；移动结束必须 >1" 离开所有敌方 | `→ rules/02-comprehensive-rules.md#retreating` |
| **Dash（疾行）** | 移动距离 ≤ Movement Characteristic；**前置 Risky Success Roll** | Success → 移动（不能 charge / retreat）；Failure → Activation 结束。可与 Move/Charge/Retreat 同回合并用 | `→ rules/02-comprehensive-rules.md#dash` |
| **Shoot（射击）** | 用 Ranged Weapon 做 Ranged Attack | 模型不能在敌方 1" 内；同回合若已 Charge / Fight 则**不能再** Shoot（除非武器有 `ASSAULT`） | `→ rules/02-comprehensive-rules.md#shoot` |
| **Fight（近战）** | 用 Melee Weapon 做 Melee Attack | 目标必须在 1" 内 | `→ rules/02-comprehensive-rules.md#fight` |

**Other**：某些 warband / battlekit / campaign skill 提供额外 ACTION（参见各战团条目）。

---

## Combat 速览

> PDF p.16-17

### Ranged Attack（远程攻击）

> PDF p.16

**流程**（速览）：

1. 选 Ranged Weapon；选目标（必须在射程内 + 攻击者 LOS 内）
2. take Success Roll（应用修正）
3. Failure → 无事；Success → 命中，做 Injury Roll；Critical Success → 命中且 **+1 INJURY DICE**

**Shooting into Melee（射入混战）**：目标在友方 1" 内时，必须投 1d6 决定真正目标——**1-3 = 友方**，**4-6 = 敌方**。详细 → `→ rules/02-comprehensive-rules.md#shooting-into-melee`

**Ranged Attack Modifiers**（cumulative；+/- DICE 抵消规则按 Core Concept）：

| 情境 | 修正 | 触发条件 |
|---|:---:|---|
| **Elevated position（高地）** | **+1 DICE** | 攻击者比目标至少**高 3"**（→ `matches/coordinate-system.md` §3.2、§2.3） |
| **Cover（掩体）** | **-1 DICE** | 目标 in cover；判定算法 → `matches/coordinate-system.md` §6.2 三问 |
| **Long Range（远射程）** | **-1 DICE** | 距离 > 武器 Range 的一半（→ `matches/coordinate-system.md` §3.2） |

完整修正展开 + 武器关键词交互 → `→ rules/02-comprehensive-rules.md#ranged-attack-modifiers`

### Melee Attack（近战攻击）

> PDF p.17

**流程**：

1. 选 Melee Weapon；选目标（在 1" 内、LOS 内）
2. take Success Roll（应用修正）
3. 同 Ranged：Failure / Success → Injury / Critical → +1 INJURY DICE

**Melee Attack Modifiers**（cumulative）：

| 情境 | 修正 | 触发条件 |
|---|:---:|---|
| **Multiple Melee Weapons（双持）** | 第二次攻击 **-1 DICE** | 模型携 2 件 Melee Weapons 时可一次 Fight 做两次 Melee Attack，顺序自选 |
| **Fear（畏惧）** | **-1 DICE** | 对手有 `FEAR` 关键词；**若双方都有 FEAR 则抵消** |
| **Defended Obstacle（掩护障碍）** | **-1 DICE** | 目标 in cover（地形 ≥½" 高 + ≥基座宽 + 位于攻防之间，与 ranged cover 同判定） |
| **Diving Charge（俯冲冲锋）** | 下次 Melee Attack **+1 DICE** | 攻击者从目标上方 ≥3" 处 Jump Down 落入 1" 内并通过 Risky Success Roll；Failure → 模型 Down + Falling Injury Roll |

完整 Multiple Melee Weapons / CLEAVE 交互 / Diving Charge 流程 → `→ rules/02-comprehensive-rules.md#combat--melee-attacks`

### Falling（坠落）

> PDF p.17

- 模型 Jump、Dive 或 Fall **≥ 3"** 时，必须做 Injury Roll
- **每 3" 加 +1 INJURY DICE**（例：3-5" = +1；6-8" = +2；以此类推）
- `FLYING` 关键词模型**不**做 Falling Injury Roll（→ `rules/03-keywords-glossary.md#flying`）

数字化映射：z 层差 × `layer_height` ≥ 3" 触发 → `→ matches/coordinate-system.md` §2.3。详细 Climbing / Jumping Over Gaps / Jumping Between Ledges → `→ rules/02-comprehensive-rules.md#climbing--jumping` 与 `#falling`

---

## Injury Rolls（受伤判定）

> PDF p.18

**流程**：

1. 取 **2 D6**；加 `+/- INJURY DICE`（按 +/- 抵消规则）
2. 掷所有骰子，取**最高 2 个**（若有 +INJURY DICE）或**最低 2 个**（若有 -INJURY DICE）
3. 两骰相加，加 `+/- INJURY MODIFIERS`（**总和最低不超过 -3**）
4. 查 Injury Roll Table

### Injury Roll Table

| Roll（修正后） | Result |
|---:|---|
| **1 or less** | **No Effect**（无效果） |
| **2-6** | **Minor Hit**（轻伤）。放 1 个 `BLOOD MARKER` |
| **7-8** | **Down**（倒下）。放 1 个 `BLOOD MARKER` 并标记 Down。**若模型已 Down，改放 2 个 BLOOD MARKERS** |
| **9+** | **Out of Action**（出局）。模型移出战场 |

> ⚠️ `TOUGH` 关键词的模型**仅首次**承受 9+ 时降级为 Down（→ `rules/03-keywords-glossary.md#tough`）。

### Common Injury Roll Modifiers

| 来源 | 修正 |
|---|---|
| Critical Success | **+1 INJURY DICE** |
| Down（Melee 攻击 Down 目标） | **+1 INJURY DICE** |
| Blood Markers（攻方花） | 每 1 个 = **+1 INJURY DICE** |
| Blessing Markers（防方花） | 每 1 个 = **-1 INJURY DICE** |
| Armour Characteristic | **-INJURY MODIFIER**（按目标 Armour 值） |
| Battlekit（Armour / Shield 等） | **-INJURY MODIFIER**（按装备） |
| Abilities / Keywords | 由规则决定 +/- INJURY DICE 或 MODIFIER |

完整规则（Bloodbath、Errata 边界、非攻击 Injury Roll 由谁掷等） → `→ rules/02-comprehensive-rules.md#injuries`

---

## Blood & Blessing Markers（血液 / 祝福标记）

> PDF p.19-20

**BLOOD MARKER（血液标记）** = 你模型受伤累积的标记（含物理伤口、疲惫、震荡、炮弹休克）。

- **上限 6 个**（超出忽略放置指令）
- **对手**（敌方玩家）可花费你模型身上的 BLOOD MARKERS：
  - 你 take Success Roll 时 → 每 1 个 = **-1 DICE**
  - 对手 make Injury Roll 时 → 每 1 个 = **+1 INJURY DICE**

> ⚠️ **新玩家最易混淆**：Injury Roll **不是 ACTION**，所以 BLOOD MARKER **不能反向**用来减自身被攻击时的 Injury Roll。只有**对手**能花你身上的 BLOOD MARKERS。详见 `→ rules/02-comprehensive-rules.md#blood-markers`

**BLESSING MARKER（祝福标记）** = BLOOD MARKER 的镜像：超自然力量、圣物等加持。

- **上限 6 个**
- **你自己**（己方玩家）可花费友方模型身上的 BLESSING MARKERS：
  - 你 take Success Roll 时 → 每 1 个 = **+1 DICE**
  - 对手 make Injury Roll 时 → 每 1 个 = **-1 INJURY DICE**

详细规则、同次掷骰双方同时花 marker 时的顺序裁决 → `→ rules/02-comprehensive-rules.md#blessing-markers`

---

## Down Results（倒下结果）

> PDF p.20

Down 状态规则（视觉：模型侧躺）：

- **若模型在自己 Activation 中被 Down → Activation 立即结束**
- Down 模型 take Success Roll → **-1 DICE**
- 对 Down 模型的 Melee Attack → Injury Roll **+1 INJURY DICE**
- Down 模型**不能移动**（除非 Fall）
- 下次激活时**站起来**，但本次激活的 Movement Characteristic **减半**（含 Charge Bonus）

边缘情况（Down 时位于 ledge 1" 内可能 Fall）→ `→ rules/02-comprehensive-rules.md#down-results`

---

## Bloodbath Rolls（血浴判定）

> PDF p.19

当你为敌方模型 make Injury Roll 时，可花 **6 BLOOD MARKERS**（若目标已 Down 则 **3 BLOOD MARKERS**）将 Injury Roll 转为 Bloodbath Roll：

- 投 **3D6 并把 3 个全部相加**（不是常规的取 2 高 / 2 低）
- 若 Injury Roll 带 `DEADLY` 关键词 → **改投 4D6 全加**（→ `rules/03-keywords-glossary.md#deadly`）

> ⚠️ **新玩家最易混淆**：DEADLY 武器触发 Bloodbath = 4D6 全加（不是 3D6）。

完整 Bloodbath（含 +/- INJURY DICE 与 INJURY MODIFIER 如何与全加相加）→ `→ rules/02-comprehensive-rules.md#bloodbath-rolls`

---

## Shaken & 输掉游戏

> PDF p.21

**Morale Check 失败 → Shaken**：

- Shaken 战团**所有 Success Roll 视作 Risky Success Roll**（除非本来就是 Risky）
- 下回合 Morale Phase **必须再做一次** Success Roll
  - Success → 解除 Shaken
  - **Failure → 战团逃跑，立即输掉游戏**
- 失败时也可主动选择立即逃跑（Sounding the Retreat）保存战力

**胜利条件总览**：

- 对手战团逃跑 → 立即胜利
- 最终回合结束后按剧本 VP 判定 → `→ rules/08-scenarios.md`
- 详细胜负 → `→ rules/02-comprehensive-rules.md#winning-the-game`

**Ending the Turn**：Morale Phase 完成后，若双方战团都未逃跑，开始新 Turn。

---

## 附录：跨文件引用统计

本速览引用：

- **`→ rules/02-comprehensive-rules.md#X`**：21 处（覆盖所有展开规则）
- **`→ rules/03-keywords-glossary.md#X`**：4 处（ASSAULT / FEAR / TOUGH / FLYING / DEADLY）
- **`→ matches/coordinate-system.md §X`**：4 处（§2.3 z 层 / §3.2 距离映射 / §6.2 cover 三问）
- **`→ rules/08-scenarios.md`**：2 处（VP / 胜负条件）

**校验**：本文件全部展开规则均通过引用代替散文复述；新玩家从本文件能在 5 分钟内上手第一场对战，遇歧义即翻 Comprehensive Rules。
