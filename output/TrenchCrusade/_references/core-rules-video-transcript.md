# Core Rules 视频教学 transcript

> **来源**：YouTube 视频，未署名教学频道（提及 Discord / Patreon / TTS battle reports）
> **目的**：v0.1 Pass 2-4 完成后做 sanity check；rules/02-comprehensive-rules.md 写完后对照
> **版本不确定**：视频未注明对应 PDF 版本。**数值若与 PDF v1.0.2 冲突以 PDF 为准**。
> **重要约定**：本文件 `_` 前缀目录，不进 sibling symlink，仅作内部参考资料

---

## 1. 结构化规则要点（grep-friendly）

### 1.1 Turns & Activations

- 每回合双方**交替激活**模型，每次激活 1 个，轮流直到双方所有模型激活完
- **谁先激活**：当前回合开始时模型数少的玩家选；平手 d6（最高选）
- 一次激活内可做**多种动作**，但**同一动作不能重复**（除非模型规则另有说明）
- 基础动作：**Move / Ranged Attack / Melee Attack / Dash**

### 1.2 Movement（三选一，每激活只能选一种）

| 类型 | 规则 |
|---|---|
| **Standard Move** | 直接移动到 Movement 值（英寸），无骰子 |
| **Charge** | 选择 12" 内可视敌方模型 → 沿最短直线移动 → Movement + d6 inches；进入 1" = 锁入 melee；**距离不够也必须用满移动尽量靠近**；**已做过 ranged attack 不能 charge**（除非武器有 `ASSAULT` keyword） |
| **Retreat** | 可离开 melee，移动到 Movement 值；**每个 engaged 敌方在你出发前可免费 melee 攻击一次**；若被 down 或 out 则原地不动 |

### 1.3 Dice Modifiers（核心机制）

- 基础所有判定 **2d6**
- **+X dice** = 多投 X 个，**取最高 2 个**
- **−X dice** = 多投 X 个，**取最低 2 个**
- 修正来源：模型 ranged / melee 侧写值 + 情境修正
- 示例：Heretic Death Commando（+1 ranged / +2 melee）→ 远程投 3d6 取 2 高、近战投 4d6 取 2 高
- 反向示例：cover 给攻击方 −1 dice → 攻击方投 3d6 取 2 低

### 1.4 Action Success Chart

| 2d6 结果（修正后两高/两低之和） | 判定 |
|---|---|
| **7+** | 成功 |
| **6−** | 失败 |
| **12** | **大成功（Critical Success）**：injury roll +1 dice |

### 1.5 Failed Actions vs Risky Actions

- 标准动作（ranged/melee attack）失败 → **激活继续**
- **Risky actions**（如 dash、charging without line of sight）失败 → **激活立即结束**
- Shaken 状态下所有 action 都变 risky（见 §1.10）

### 1.6 Ranged Combat

- 需要：**有 LOS** + **不在 melee**
- 流程：declare weapon → check range → apply modifiers → roll
- **常见 ranged 修正**：

| 情境 | 修正 |
|---|---|
| 攻击者比目标高 2"+ | +1 dice（high ground） |
| 目标在 cover | −1 dice |
| Long range | −1 dice |

- **Long range 定义**：超过武器射程的**一半**（例：bolt-action rifle 24" → 12" 以上算 long range）
- **Cover 三问**（全 yes 才算受 cover）：
  1. 模型是否触碰 cover？
  2. cover 是否与模型 base **等宽或更宽**？
  3. 模型是否有**任何部分**被遮蔽？

### 1.7 Melee Combat

- 需要：激活模型在敌方 1" 内
- 流程：选 melee 武器 → declare 目标 → roll
- **常见 melee 修正**：

| 情境 | 修正 |
|---|---|
| 攻防之间有 0.5" 高障碍 | −1 dice（defended obstacle） |
| 用副手武器（off-hand） | −1 dice |

### 1.8 Injury Chart（命中后投）

基础 **2d6**，按 gear/traits/conditions 修正：

| 结果 | 效果 |
|---|---|
| **1−** | 无效果 |
| **2-6** | **Minor hit** → 目标加 1 个 blood marker |
| **7-8** | **Down** → 目标加 1 个 blood marker + 任何对它的后续 injury roll +1 dice；下次激活时可起身但 Movement 减半；再次 down → 加 2 blood markers |
| **9+** | **Out of Action** → 移出战场（本局不归） |

**装甲减 injury**：

| 装甲 | injury roll 减 |
|---|---|
| Trench shield | −1 |
| Standard armor | −1 |
| Reinforced armor | −2 |
| Machine armor | −3 |

**`TOUGH` keyword**：第一次本该 9+ out of action → 只 down 不 out。**仅第一次有效**。

### 1.9 Blood Markers & Bloodbath & Blessings

**Blood markers**：

- 来源：每次 minor hit / down 给目标加
- **对方激活时**，你可以花对方身上的 blood marker，每个 = action roll −1 dice
- 对方对你 injure 时，**你（攻击者）可以花防御者身上的 blood marker**：每个 = injury roll +1 dice
- ⚠️ **常见误解（视频明确警告）**：injury roll **不是 action**，所以**不能用 blood marker 反向修正 injury roll 自己**（被攻击方不能用自己身上的 blood marker 减 injury dice）。但能 +1 dice 让 injury 对自己更惨——这是攻击方的事

**Bloodbath（特殊 injury roll）**：

- 标准 injury 是 2d6 取 2 个值；**Bloodbath 改为 3d6 全部加总**
- 若武器自带 boost（如 Infernal Bomb）→ Bloodbath 时 **4d6 全部加总**
- Bloodbath 下若有 −1 dice 罚 → 4d6 取**最低 3 个**加总

**Blessing markers**（反向 blood marker，更稀有，只能从特定能力获得）：

- 我方激活时花 blessing marker → action roll +1 dice
- 对方对我方 injure 时花 blessing marker → 对方 injury roll −1 dice

### 1.10 Ending the Turn（Morale）

- 双方所有模型都激活完 → 回合结束
- **Morale test 触发**：若**半数或以上**模型处于 **down 或 out of action**
- 投 2d6
  - 失败 → warband 撤退，或选择继续战斗但带 **`SHAKEN`** 状态
  - **Shaken 含义**：所有 action 变 **risky action**（失败立即结束激活）

---

## 2. 视频时间戳 → 主题快速索引

| 时间 | 主题 | §|
|---|---|---|
| 0:25 | Turns and Actions | 1.1 |
| 1:18 | Movement 三种 | 1.2 |
| 2:21 | TTS Movement 示例 | — |
| 3:48 | Dice modifiers | 1.3 |
| 5:33 | Action Success Chart | 1.4 |
| 5:33 | Combat | 1.6-1.7 |
| 7:21 | Melee modifiers | 1.7 |
| 8:00 | Injury chart | 1.8 |
| 8:52 | Armor / Tough | 1.8 |
| 9:18 | Blood markers | 1.9 |
| 10:21 | TTS Blood marker 示例 | — |
| 11:35 | Bloodbath | 1.9 |
| 12:07 | Blessings | 1.9 |
| 12:32 | Morale / Ending Turn | 1.10 |

---

## 3. 校验提示（导 rules/01-02 时对照）

写 `rules/02-comprehensive-rules.md` 时，以下视频要点**必须**能在 PDF 中找到对应原文，且数值一致：

- [ ] 7+ 成功、12 大成功 → PDF Core Concepts / Success Rolls
- [ ] +dice 取高 / −dice 取低 → PDF +Dice and −Dice
- [ ] Charge = Movement + d6, 12" 内 → PDF Charging
- [ ] Retreat 触发对方 free melee → PDF Retreating
- [ ] Long range = 武器射程一半以上 → PDF Ranged Attacks
- [ ] Cover 三问 → PDF Ranged Attack Modifiers
- [ ] Injury 阈值 2-6 / 7-8 / 9+ → PDF Injuries / Injury Roll Table
- [ ] 装甲减 −1/−1/−2/−3 → PDF Equipment / Armour
- [ ] Tough keyword 仅第一次 → PDF Keywords Glossary
- [ ] Bloodbath 3d6 加总（+武器 boost = 4d6）→ PDF Bloodbath Rolls
- [ ] Blood marker 不能反向修正自身 injury → PDF Blood Markers
- [ ] Morale 触发：半数 down/out → PDF Morale Phase
- [ ] Shaken = 所有 action 变 risky → PDF Shaken Warbands

发现**任何数值/阈值不符**时：**以 PDF v1.0.2 为准**，在 rules/02 中明确导入 PDF 原文，并在本文件相应条目加注 "[v1.0.2 修正：PDF 说 X，视频说 Y]"。

---

## 4. 原 transcript（保留时间戳）

```
0:00 Trench Crusade is a brutal skirmish style war game of blood, fire, and
faith. Set in the ashes of a war torn earth, we fight for the forces of heaven
or hell. Whether you're a grizzled veteran or a fresh recruit to wargaming,
this video will help you gain an understanding of the core rules. Let's
get into it.

[Music — Turns and Actions]

0:30 Trench Crusade is played in turns. Each turn, players take alternating
activations in which you will activate one model, then your opponent activates
one of theirs, and so on until every model on both sides has been activated
once. At the start of each turn, the player with fewer models remaining
chooses who activates first. If you're tied, roll a d6. Highest wins the
choice.

During a model's activation, it can perform a series of actions. The basic
actions that pretty much every model can do are move, ranged attack, melee
attack, and dash. You can perform as many different actions as you want, but
you can't repeat the same one twice, unless your model's rules state
otherwise.

1:16 Let's talk movement before we get into the other actions of the game.
You can choose one of three options when declaring a move. First up, the
standard move. It's simple. Just move the model up to its movement stat in
inches. No dice, no roll, just go.

Alternatively, you can charge if you want to get into melee combat with a
model. To charge, you must pick an enemy you see within 12 in, then move your
model towards them using the shortest, most effective path and add a bonus d6
in to your movement. Even if you do not have enough movement to get into
melee range, you must use the full movement to get as close as possible. If
you get within one inch, you're now locked in melee combat. But remember, you
can't charge if you've already made a ranged attack, unless it was with a
ranged weapon that has the assault keyword.

2:07 The final choice for movement is the retreat option. To retreat, you
must move up to your full movement stat, and you're allowed to leave melee
combat. However, there is a risk. Every enemy you're engaged with gets a free
melee attack before you go.

2:21 [TTS demonstration — standard move, charge with d6 bonus example
(Heretic Trooper M6 + d6=5 = 11" charge), retreat with Trench Pilgrim free
swing before disengage.]

3:48 Most other actions are rolled with a base two dice. There are a variety
of modifiers you can get to make odds better or worse, which will read as
plus one dice or minus one dice in the rules. The most common bonuses you
will see will be in your character sheets under the ranged and melee
profiles.

Let's break down how dice modifiers work by using a heretic death commando as
an example. When you're performing an action like making a ranged attack or
melee attack, you always start by rolling two dice and then you either add or
subtract extra dice based on your character stats or the situation. For
instance, this death commando has a plus one dice to ranged and a plus two
dice to melee. That means when he makes a ranged attack, he rolls three dice
total and takes the two highest results. In melee, it's even better. He rolls
four dice and again takes the two highest.

4:45 Now, those same dice modifiers can also work against you. Let's say an
enemy model is trying to shoot someone who's in cover. that shooter now takes
a minus one dice penalty to their ranged attack. For example, imagine a
heretic trooper is taking the shot. His base range stat is zero. So under
normal conditions, he just roll the standard two dice and take the best two.
But because the target is in cover, he's hit with a minus one dice penalty.
That means he rolls three dice total, but this time he takes the two lowest
results.

5:21 Failing standard actions like a ranged or melee attack allow you to
continue your activation after failing. Others like dashing or charging
without line of sight are risky actions which will end your activation
immediately if failed.

5:33 To complete any action in the game, you must roll on the action success
chart. No matter what action you are doing, you will always roll on this
chart, which makes things very easy to understand. A successful action is the
result of seven or higher when rolled on the chart. Six or lower is a fail,
and a 12 is a critical success, which gives you a bonus dice to ranged or
melee attacks when rolling on the injury table.

[Combat]

6:06 The combat system is simple yet effective, unlike other war games that
have a ton of weird, intricate rules that you often forget. When making a
ranged attack, models can shoot if they have line of sight and are not in
melee. Declare your weapon, check range, apply modifiers, and roll on the
action success chart.

6:30 Here are some common range modifiers. If your model is 2 in higher than
its target, then you would be shooting from high ground, which grants you
plus one dice. Is the target behind cover? Minus one dice. Are you in long
range? another minus one dice.

6:48 To see if a model has cover, ask yourself these three questions. One, is
the model touching cover? Two, is that cover as wide or wider than its base?
Three, is any part of the model obscured? If you answer yes to all three of
these, then the model is receiving the benefits of cover.

7:05 Long range is simply classified as over half of the ranged weapons
range. So, if you were firing a bolt-action rifle with a range of 24 in, then
anything higher than 12 in would be considered long range, and you would
suffer the penalty to hit.

7:21 Melee attacks can be made if the activated model is within 1 in of one
or more enemies. Select a melee weapon the model is equipped with, and
declare what model you are attacking. Then, roll on the action success chart
and add any modifiers to the hit.

7:38 Here are some common melee modifiers. If there is at least a halfinch
high obstacle in between the attacking and defending model in melee combat,
then you would get a minus one dice to hit for defended obstacle. When an
attack is made with a second melee weapon, you would suffer the penalty for
off-hand weapons, which is a minus one dice to hit.

8:00 If either of your ranged or melee attacks result in a successful action,
it is time to roll on the injury chart. 2d6 again modified by gear traits and
conditions.

Here's a breakdown of the injury chart. On a one or less, there is no effect.
On a 2 to six, it will be a minor hit, which adds a blood marker to the
model. On a 7 to 8, the model goes down, in which a blood marker will be
placed, and you will receive a bonus plus one dice when rolling an injury
against the downed model. At the start of the downed model's activation, they
can stand back up, but their movement is cut in half. If a downed model
suffers an additional down result, they will take two more blood markers.
Finally, on a result of nine or higher, the model is taken out of action in
which it is removed from the board for the rest of the game.

8:52 Armor can reduce the result from the injury role. A trench shield
subtracts one to injury rolls. Standard armor subtracts one to injury roles.
Reinforced armor subtracts two. And machine armor subtracts three. If the
model has the keyword tough, they do not go out of action on a 9up. They only
go down instead. The tough ability is only used during the first time a model
would go out of action.

[Blood Markers and Blessings]

9:19 Blood markers can seem a bit confusing at first, as I see a lot of new
players getting this rule wrong. So, pay close attention and I'll try to
explain it to the best of my ability. Blood markers represent physical damage
that can be received from taking a minor injury. As we discussed before,
every time the wounded model takes an action, your opponent can spend one or
more blood markers to apply minus one dice per marker on the action roll. If
the model with a blood marker on it is receiving an injury roll, those same
markers can be spent to add plus one dice to the injury chart rule, making it
much more likely that they perish. Keep in mind that you cannot use blood
markers when an enemy is making an injury roll against you, as an injury roll
is not an action.

10:21 [TTS demonstration — Trench Pilgrim ranged attack on Heretic Trooper
with blood marker spent for −1 dice (3d6 take 2 lowest, result 6 = fail);
then engagement reversed, Heretic charges in and lands hit, spends Trench
Pilgrim's blood marker to add +1 dice to injury roll, takes 2 highest, result
= Out of Action.]

11:35 There is however one more mechanic to blood markers that gets a little
bit more in-depth. Blood bath lets you supercharge your injury roll. Instead
of rolling the standard 2d6, you roll 3d6 and add them all together. And if
you're using a weapon that already boosts your roll like that, such as the
infernal bomb, you stack it. That's 4 d6 total, all added together. If you
are at a minus one dice to injure on a blood bath, you would roll 4d6 and
take the three lowest.

12:07 Blessing markers are essentially inverse blood markers. They are a lot
more rare than blood markers, though, as you can only get them through a few
special abilities. When an ally model takes an action, you can spend a
blessing marker to add plus one dice to your dice pool on the action success
chart. If an opponent is rolling an injury against you, you can give them a
minus one dice penalty to make the odds worse for them.

[Ending a Turn]

12:32 Once both players have activated all of their models, the turn ends.
But it's not quite over yet. If half of your warb band is down or out of
action, you must roll for a morale test. Roll 2d6. If you fail, your warb
band flees or you choose to keep fighting with the shaken status. The shaken
status means every time you roll for an action, it becomes a risky action.
Morale is something definitely to keep in the back of your mind as it could
easily become a win condition if the battle gets bloody enough.

13:05 [Outro — Discord, Patreon, TTS battle reports plug.]
```
