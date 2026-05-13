# rules/08-scenarios: Scenarios

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.144-157
> 版本：v1.0.2
> v0.1 范围：Scenario Format 通用框架 + Scenario I (Claim No Man's Land) + Scenario II (Hunt for Heroes)。
> 其余 10 个 scenarios（III–XII，PDF p.158-197）属 v0.2.D backlog。

---

## Index

- [1. Scenario Format 通用框架](#1-scenario-format-通用框架)
  - [1.1 准备对战 Preparing to Play](#11-准备对战-preparing-to-play)
  - [1.2 部队 Forces](#12-部队-forces)
  - [1.3 战场 The Battlefield](#13-战场-the-battlefield)
  - [1.4 部署 Deployment](#14-部署-deployment)
  - [1.5 特殊规则 Special Rules](#15-特殊规则-special-rules)
  - [1.6 游戏长度 Game Length](#16-游戏长度-game-length)
  - [1.7 胜利条件 Victory Conditions](#17-胜利条件-victory-conditions)
  - [1.8 荣耀事迹 Glorious Deeds](#18-荣耀事迹-glorious-deeds)
  - [1.9 荣耀点数 Glory Points (Campaign 用)](#19-荣耀点数-glory-points-campaign-用)
- [2. Scenario I — Claim No Man's Land](#2-scenario-i--claim-no-mans-land)
- [3. Scenario II — Hunt for Heroes](#3-scenario-ii--hunt-for-heroes)

---

## 1. Scenario Format 通用框架

> PDF p.144-150。所有剧本（scenario）共享这套结构。

### 1.1 准备对战 Preparing to Play

要玩一场 Trench Crusade，必须先：

1. 招募战团（Warband）—— 见 `warbands/` 章节
2. 找到对手
3. 双方选择要玩的剧本（scenario）

**单场对战 vs 战役**：

- **Campaign**（战役）模式下，剧本由战役规则决定（v0.2.A backlog，本 v0.1 不含）
- **One-off**（单场）模式下双方协商；不能达成一致 → **roll-off**（掷骰决断，见 `rules/02-comprehensive-rules.md#other-rules-principles`），赢家选剧本

#### 单场对战推荐预算（PDF p.145）

| 经验阶段 | 建议预算 | 备注 |
|---|---|---|
| 新手第一场 | **700 👑** | 此场可计入后续战役第一局 |
| 有经验后 | **800 👑 + 6 ☼** | 提供足够选择不至于战团失控 |

**☼ 使用约定**：双方在开局前必须**约定**单场是否允许花 ☼ 招募 Mercenaries（雇佣兵）/ 购买 Battlekit / 购买 Glory Items（v0.2.A 内容）。v0.1 默认 **不允许花 ☼**（因为 Mercenaries/Glory Items v0.2 才导入）。

### 1.2 部队 Forces

每场比赛使用的不是整个战团，而是从中挑选的**部队（Force）**。

- **单场对战**：通常可使用战团内**所有模型**
- **战役模式**：Force 必须符合战团的 Threshold Value 和 Field Strength（v0.2.A）

**关键规则**：一旦选定 Force，**只有 Force 内的模型**在该场比赛中算作战团成员。规则若说"若该模型属于你的战团，可如何如何"——该模型未入 Force 即不可触发。

部分剧本会增加额外的 Force 限制（如 Scenario II 要求"必须包含尽可能多的 ELITE 模型"），写在该剧本的 FORCES 段。

### 1.3 战场 The Battlefield

#### 战场尺寸

多数剧本可在普通餐桌上玩；少数（异形战场剧本）要求 36" 或 48" 方阵。本项目数字化默认 **36×36 格**，详见 `→ matches/coordinate-system.md §4`。

#### Battlefield Archetypes（战场原型）

剧本会指定使用哪个 battlefield archetype（如 No Man's Land 无人区）。地形规则与七类地形 yaml schema 详见 `→ rules/04-battlefield-terrain.md` 与 `→ matches/coordinate-system.md §7`。地图上画的地形是**示意**，实际无需复制。

#### Markers（标记）

某些剧本要求设置一个或多个 **Markers**（标记物）。

- 在地图上 Marker 位置用**白色十字**标出
- 在 **'Midpoint'**（中点）的 Marker → 中心置于战场正中心
- 物理代币：纸板、木质、塑料、旗子、最大 40mm 的散件地形
- Marker **不阻碍移动也不影响 LOS**（除非本身也是地形件）
- 若地形件覆盖了 Marker 位置 → 把 Marker 放在地形件上任意点

**本项目数字化**：Marker 用 `landmark` 类地形表示，引用 `→ matches/coordinate-system.md §7.3.G`。每个 Marker 在 `match-state.yaml` 的 `terrain` 列表中作为 `type: landmark` 项，带 `scenario_tag` 字段。

#### Blocking Terrain（堵塞地形禁忌）

地形摆放**不得**导致任何模型无法离开自己部署区或抵达任意 Marker。若开局后发现，被堵塞的模型视该地形为 Open terrain（开阔地）穿过——LOS 阻挡仍然有效。

### 1.4 部署 Deployment

部署一般流程：

1. 双方 roll-off，赢家选自己的 Deployment Zone（部署区）
2. 双方**交替**部署模型，**每次一个**
3. 第一个部署的：**战团模型数较多者**（平 → roll-off）
4. 模型必须**完全位于自己的部署区内**（不能跨边）
5. 一方先部署完所有模型 → 另一方一次性连续部署剩余所有模型
6. 双方部署完毕 → 部署结束，游戏第 1 回合开始

**部署区数字表示**：`[x_min, y_min, x_max, y_max]`，详见 `→ matches/coordinate-system.md §4`。

#### Infiltrators（渗透者）

具有 `INFILTRATOR` 关键词（→ `rules/03-keywords-glossary.md#infiltrator`，Pass 4 在写）或类似特殊规则的模型，可以在其他模型之后部署，或在部署区**之外**部署。

- 剧本会明确写"Infiltrators must deploy normally" 或 "can use their special deployment rules"
- "deploy normally" → **不允许**任何模型在部署区外部署
- 部署顺序中，"after other models" 指**双方所有非渗透模型都部署完之后**
- 若双方都有渗透模型：先把非渗透部完（短数方先用尽）；再按渗透部署，仍遵守"模型多者先部署"原则

**PDF 示例**：Gary 9 个模型（含 1 渗透），Christina 7 个（含 3 渗透）。
- 非渗透：Gary 8 vs Christina 4。两人交替部 4 轮（Gary 先因总数 9>7），Christina 用尽
- Gary 继续部完剩余 4 个非渗透模型
- 然后部渗透：Gary 1 vs Christina 3。**Christina 先部**（因 Gary 部了最后一个非渗透）
- 双方交替直到完成

### 1.5 特殊规则 Special Rules

#### Pre-Game Activities（开局前行动）

许多 Abilities / Skills / Battlekit 特殊规则允许在游戏开始前执行。

- 每个 pre-game activity 自带触发时机
- "before X" / "after X" → 紧贴 X 之前/之后发生
- 多个同时触发 → roll-off 决定结算顺序

#### Secret Information（秘密信息）

某些剧本要求**秘密写下信息**（如 Scenario II 的 Marks & Assets）。

- 写下内容必须清晰可辨
- 揭示时必须**出示给对手看**

### 1.6 游戏长度 Game Length

剧本指定游戏持续的**回合数**（多数 4 或 5 回合）。详细的回合阶段（Initiative / Activation / Morale）见 `→ rules/02-comprehensive-rules.md`。

### 1.7 胜利条件 Victory Conditions

#### Victory Points (VP)（胜利点数）

多数剧本用 VP 决定胜负。VP 相同 → 平局。

每个剧本明确列出可获 VP 的条件 + 时机。

**回合末结算顺序**：游戏结束时，**先**结算最后一个回合末的 VP，**再**结算"游戏结束时"才结算的 VP。

#### 即胜条件

部分剧本（如 I、II）规定：若一方在战场上无敌方模型，或敌方战团**逃跑**（Morale Phase 见 `→ rules/02-comprehensive-rules.md#morale-phase`），该方立即获胜。

### 1.8 荣耀事迹 Glorious Deeds

每个剧本附带一组独特的 **Glorious Deeds**（荣耀事迹）。完成后授予 VP（具体 VP 数写在该剧本的 Victory Points 列表中，**默认 1 VP / Deed**）。

#### 完成判定

- 每个 Deed 有标题 + condition（条件）
- 一旦条件**首次**被满足 → 该 Deed 完成
- 除非另注，每个 Deed **每场只能完成一次**
- 双方同时完成同一 Deed → roll-off 决定归属
- **单个模型可同时完成多个 Deeds**

#### 条件因果链规则（关键）

PDF 给出两个对照例子，定义"满足条件"的因果界：

| Deed | 条件 | 是否满足？ |
|---|---|---|
| **Protect the Relic** | 致使敌方圣物 1" 内模型 Out of Action | ✅ 攻击让对方 Down，对方坠崖 Out of Action — **算**（你的攻击因果导致 OoA） |
| **Sniper** | 远程攻击（Long Range + Cover）须 Out of Action 目标 | ❌ 攻击让对方 Down，对方坠崖 OoA — **不算**（OoA 是 Fall 造成的，不是 Ranged Attack） |

**核心原则**：Deed 条件具体写"由 X 类型攻击造成 OoA"时，OoA 必须**直接**来自该攻击；若仅写"造成 OoA"则间接因果（如击 Down 后 Fall）也算。

### 1.9 荣耀点数 Glory Points (Campaign 用)

> ⚠️ **v0.1 单场对战不使用本节**。完整的 Glory Points (☼) 规则属 Campaign Rules（v0.2.A backlog）。本节仅作概念占位与跨场扩展引用。

战役模式下，完成一项 Glorious Deed 让你在战后获得：

- **1 ☼**（Glory Point）—— 可花在招募 Mercenaries / 购买 Battlekit / 购买 Glory Items
- 完成该 Deed 且**带 `ELITE` 关键词**的模型获得 **1 Experience Point**（→ Promotions & Experience，v0.2.A）
  - 若 Deed 由整个 Warband 或玩家完成（非具体模型） → **不**授予经验点
- 每完成一项 Deed → 战后 Promotion Pool **+1 D6**

**v0.1 用法**：单场比赛中，Glorious Deeds **仅作为 VP 来源**（按剧本 Victory Points 列表数值，通常 1 VP / Deed）。战后不结算 ☼ / Experience / Promotion Pool。

---

## 2. Scenario I — Claim No Man's Land

> PDF p.151-153。
> **Battle for control over a stretch of land and drive away your foes.**
> 争夺一片无人区的控制权，把敌人赶出去。

### 2.1 Forces

无特殊限制。

### 2.2 The Battlefield

- 战场原型：**No Man's Land**（无人区） — 见 `→ rules/04-battlefield-terrain.md`
- 双方 roll-off，赢家摆放地形

#### 地图（PDF p.151）

```
                        24" (战场宽度)
  ┌────────────────────────────────────────────────────┐
  │ DEPLOYMENT ZONE                                    │
  │ (6" 深)                                            │   红方部署区
  ├────────────────────────────────────────────────────┤
  │                                                    │
  │                                                    │
  │                  ※ MIDPOINT ※                      │   中央无人区
  │                                                    │   (5 个 Objective)
  │                                                    │
  ├────────────────────────────────────────────────────┤
  │ DEPLOYMENT ZONE                                    │
  │ (6" 深)                                            │   蓝方部署区
  └────────────────────────────────────────────────────┘
```

数字化映射（36×36 战场，假设战场 y 轴 36" 满 = PDF 标 24"，差值非比例缩放，部署区按 6" 字面值）：

```yaml
battlefield:
  size: [36, 36]
  layer_height: 3
  deployment:
    red:  [0,  0,  36, 6]    # 下侧 6" 深部署区
    blue: [0,  30, 36, 36]   # 上侧 6" 深部署区
```

> 引用 `→ matches/coordinate-system.md §4`。

#### Objective Markers（5 个）

- 地图中央散布 **5 个 Objective Markers**（白色十字）
- 摆放地形时，**前 5 件地形必须覆盖**这 5 个 Marker 起始位置
- **必须使用 Ruined Building 地形件**（如手头有）
- Objective Marker 在所有地形摆完后再放，放在覆盖它的地形件上任意点
- **整个地形件**被视为该剧本的 Objective，**不可被摧毁或移除**

数字化表示（`landmark` 子类型）：

```yaml
terrain:
  - id: objective_1
    type: landmark
    subtype: objective
    bounds: [10, 14, 14, 18]
    base_z: 0
    height: 2                   # 覆盖它的 Ruined Building 高度
    blocks_los: partial
    cover: full
    scenario_tag: claim_objective_i
  # ... objective_2..objective_5 同构
```

#### 控制 Objective

某玩家**控制**一个 Objective 地形件当且仅当：

- 该地形件**上 / 内 / 1" 内**的友方模型数 > 敌方模型数
- **特例**：若一方有任何模型**站在地形件上**而对方没有 → 该方控制，**即使**对方在 1" 内更多

> "within 1"" 数字定义：`get_distance ≤ 1.0`（`→ matches/coordinate-system.md §3.2`）。

### 2.3 Deployment

通用规则（见 §1.4）。

#### Infiltrators

**Infiltrators must deploy normally**（必须按正常规则部署，**不能**用特殊渗透规则）。

### 2.4 Game Length

**4 回合**。

### 2.5 Victory Conditions

#### 即胜

战场上无敌方模型 / 敌方战团逃跑（Morale 失败 → flee） → 立即获胜。

#### Victory Points

| 时机 | VP |
|---|---:|
| 每回合末 — 每控制一个 Objective | **2 VP** |
| 游戏末 — 每完成一项 Glorious Deed | **1 VP** |

### 2.6 Glorious Deeds（7 项）

| Deed | 条件 |
|---|---|
| **Bloodletting**（放血）| 友方攻击导致敌方旁放下第 6 个 `BLOOD MARKER` |
| **Cast Them Down**（推下高地）| 友方致使敌方从 **≥ 3"** 高处 Fall（如击 Down 在崖边 / 推下崖）。3" 阈值见 `→ matches/coordinate-system.md §2.3`（z 层差 × layer_height 3） |
| **Hold Your Ground**（坚守阵地）| 本场**首位**通过 Morale Check 的战团。授 1 VP；战役模式额外给战团内带 `LEADER` 的 ELITE 模型 1 EXP + Glory Points + Promotion D6 |
| **Lord of War**（战神）| 友方模型在**单个回合**内用 **Melee Attack** 击 Out of Action **2 个敌方模型** |
| **Resist and Bite**（垂死反扑）| 友方模型**开始激活时处于 Down 状态**，在同一激活中击 Out of Action 一个敌方模型 |
| **Sniper**（神枪手）| 友方模型用带 **Long Range + Cover modifiers** 的 Ranged Attack 击 Out of Action 一个**敌方 ELITE 模型**（Long Range / Cover 见 `→ matches/coordinate-system.md §3.2` 和 §6） |
| **Suicidal Bravery**（自杀式英勇）| 友方模型用**同一个 charge 动作**成功冲锋**两个**敌方模型（Charge 12" 临界与多目标见 `→ matches/coordinate-system.md §3` 和 `→ rules/02-comprehensive-rules.md` Charge ACTION） |

---

## 3. Scenario II — Hunt for Heroes

> PDF p.154-157。
> **Hunt down the enemy leaders while protecting your own.**
> 猎杀敌方领袖，同时保护自己的领袖。

### 3.1 Forces

**双方必须包含尽可能多的 ELITE 模型**（不允许故意留下 ELITE 不上场）。

### 3.2 The Battlefield

- 战场原型：**No Man's Land**
- 双方 roll-off，赢家摆地形

#### 地图（PDF p.154）

```
        7"             10"      10"       7"
   ┌─────────┬───────────────────────┬─────────┐
   │         │      DEPLOYMENT       │         │
   │         │           ZONE        │   M     │
   │   ※     ├──────── 10" ──────────┤   ※     │
   │  (Obj)  │  Defense Works        │  (Obj)  │
   │         │  placements Area      │         │
   ├─────────┤                       ├─────────┤
   │   G     │                       │         │
   │   ※     │   5"     ※ MIDPOINT   │   G     │
   │  (DW)   │              5"  ※    │   ※     │
   │         │              (Obj)    │  (DW)   │
   ├─────────┤   5"  ※               ├─────────┤
   │         │              5"  ※    │         │
   │   ※     │              (Obj)    │   M     │
   │  (Obj)  │  Defense Works        │   ※     │
   │         │  placements Area      │  (DW)   │
   │         │ ───── 10" ────────────│         │
   │         │      DEPLOYMENT       │         │
   │   ※     │           ZONE        │         │
   │  (Obj)  │                       │  (Obj)  │
   └─────────┴───────────────────────┴─────────┘

说明：
※（白十字）= Objective Marker（4 个，角落附近）
G = Defence Works Marker with Gun Battery（2 个）
M = Defence Works Marker with Machine Gun Emplacement（2 个）
MIDPOINT = 战场中心
```

#### Objective Markers（4 个）

- 地图上 4 个白十字
- 摆地形时，**前 4 件地形**覆盖 Objective Marker 起始位置
- **必须用 Ruined Building**（如有）
- 地形完毕后放 Marker；**整个地形件**算 Objective
- 控制判定同 Scenario I（多于敌方友模在内/上/1"内）

#### Defence Works Markers（4 个）

地图上标 `G` 或 `M` 的 Marker：

- `G` → **Gun Battery**（炮台）— 视作 Sultanate Grand Cannon 固定炮台（详见 Warbands of Trench Crusade — Defenders of the Iron Wall 章节，v0.2.B faction backlog）。**任何模型**可操作
- `M` → **Machine Gun Emplacement**（机枪阵地）— 在 1" 内的模型视作携带标准 Battlekit 列表中的 Machine Gun（→ `rules/05-battlekit.md#machine-gun`）。**每回合最多用一次**；若 Marker 1" 内有**敌方模型**则**不可使用**

摆放规则：

- 4 个 Objective 摆完之后，**接下来 4 件地形**覆盖 Defence Works Marker 位置
- 必须用 Ruined Building 地形件（如有）
- 地形完毕后放 Marker

```yaml
terrain:
  # 4 Objectives
  - id: obj_i
    type: landmark
    subtype: objective
    scenario_tag: claim_objective_ii
    # ...
  # 2 Gun Batteries
  - id: defence_works_g_1
    type: landmark
    subtype: gun_battery
    scenario_tag: defence_works_gun
    # ...
  # 2 Machine Gun Emplacements
  - id: defence_works_m_1
    type: landmark
    subtype: machine_gun_emplacement
    scenario_tag: defence_works_mg
    # ...
```

> Landmark schema 见 `→ matches/coordinate-system.md §7.3.G`。

### 3.3 Deployment

通用规则（见 §1.4）。

#### Infiltrators

**Infiltrators 可正常部署或使用渗透特殊规则**。**但**：用渗透规则时，**不得在任意 Objective 8" 内**部署。

> 8" 数字定义：`get_distance(infiltrator_pos, objective_pos) > 8.0`（`→ matches/coordinate-system.md §3.2`）。

#### Marks & Assets（部署后秘密信息）

部署完成后，双方**秘密写下**（见 §1.5 Secret Information）：

- **最多 3 个**敌方 `ELITE` 模型作为 **Marks**（猎杀目标）
- **1 个**友方 `ELITE` 模型作为 **Asset**（己方资产）

游戏结束时揭示，影响 VP 结算（见 §3.6）。

### 3.4 Unforeseen Events（突发事件）

第 1 回合后，**每回合开始时**，一名玩家掷 **1 D6**：

- **1-4**：无事发生
- **5-6**：发生一次 Unforeseen Event；掷 **1 D3** 查表

> 一回合内**只触发一次**（D6 出 5-6 后不再重投）。

#### D3 表（PDF p.156）

| D3 | 事件 | 效果 |
|:--:|---|---|
| **1** | **Rising Fog**（升起浓雾）| 本回合 + 下回合，所有 **Ranged Weapons 的 Range 减半**（short range 为减半后 Range 的一半） |
| **2** | **Rain, Mud, and Guts**（雨、泥、肠子）| 本回合 + 下回合，所有 **Melee Attack** rolls **−2 DICE** |
| **3** | **Deep Craters**（深陷弹坑）| 双方 roll-off，从赢家开始**轮流**摆放 Crater Markers，共摆 **6 个**。Crater Markers 不能放在部署区内 / 不能距地形件或模型 **2" 内**。Crater Marker 中心 2" 范围内的开阔地形视为深坑（陡壁，深度 **D3+3"**，每个 Marker 独立投）。模型可 Jump Down / Fall 进入，需 Climb 才能离开。Crater Marker 用最大 4" 的合适地形件代表 |

> Crater 深度 D3+3" → 数字化为 z=-2 层（z 层差 × layer_height 3" = 6"，对应 D3+3 范围 4-6"）。Jump Down ≥ 3" 触发 Falling injury（PDF p.40-41）见 `→ rules/02-comprehensive-rules.md` Climbing & Jumping。

### 3.5 Game Length

**5 回合**。

### 3.6 Victory Conditions

#### 即胜

战场上无敌方模型 / 敌方战团逃跑 → 立即获胜。

#### Victory Points

| 时机 | VP |
|---|---:|
| 每回合末 — 每个 Objective 1" 内有自己 ≥ 1 模型 | **1 VP** |
| 每回合末 — 每控制一个 Objective | **1 VP** |
| 游戏末 — 每完成一项 Glorious Deed | **1 VP** |
| 游戏末 — 每个被击 Out of Action 的敌方 Mark | **2 VP** |
| 游戏末 — 若友方 Asset **未被** Out of Action | **3 VP** |

> 注意：同一 Objective 上控制 + 1" 内有模型 → 同时拿 1 VP + 1 VP = 2 VP（与 Scenario I 单次 2 VP 等价，但通过不同条件累计）。

### 3.7 Glorious Deeds（5 项）

| Deed | 条件 |
|---|---|
| **Sharpshooter**（神射手）| 友方模型**在 cover 中**，用带 **Long Range modifier** 的 Ranged Attack 击 Out of Action 一个**敌方 ELITE 模型** |
| **Dangerous Fall**（致命坠落）| 友方致使敌方模型坠入一个 **Crater**（见 Unforeseen Events D3=3） |
| **Death From Above**（天降神威）| 友方模型用带 **Diving Charge modifier** 的 Melee Attack 击 Out of Action 一个敌方模型（Diving Charge 见 `→ rules/02-comprehensive-rules.md` — 跳下 3"+ 后冲锋） |
| **High Risk, High Reward**（高风险高回报）| 一个 **Asset** 击 Out of Action 一个敌方 **Mark**。要求玩家**先揭示**该友模是 Asset 且该敌模是 Mark |
| **Kill their Leaders**（斩首）| 击 Out of Action **所有**敌方 Marks。要求玩家**先揭示**哪些敌模是 Marks。**取最后一个 Mark Out of Action 的模型**算完成此 Deed |
