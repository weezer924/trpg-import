# Chapter 3: Combat System 战斗系统

> 来源：Record of Lodoss War Companion I（1989, Group SNE）PDF p.34–37
> 译本：英文同人翻译版

While combat is not everything in a fantasy TTRPG, it certainly occupies an important part. This chapter explains the Lodoss RPG combat system with a focus on the use of skills.

## Index

- [Round Procedure 回合流程](#round-procedure-回合流程)
- [Initiative Determination 先攻判定](#initiative-determination-先攻判定)
- [Actions 行动种类](#actions-行动种类)
- [Hit & Damage 命中与伤害](#hit--damage-命中与伤害)
- [Critical Hit 致命一击](#critical-hit-致命一击)
- [Number of Attacks 攻击次数表](#number-of-attacks-攻击次数表)
- [Example: First combat with goblins](#example-first-combat-with-goblins-范例--与哥布林的初战)

---

## Round Procedure 回合流程

Combat progresses by repeating a series of actions called **rounds**. **One round = 30 seconds** and follows the procedure below.

```
1. Initiative Determination     先攻判定
        ↓
2. First Side Acts              先攻方行动
        ↓
3. Second Side Acts             后攻方行动
        ↓
4. Sheet Recording              记录变化
```

### 1. Initiative Determination 先攻判定

Determine which side acts first — the character side or the monster side.

- Each monster has an **Initiative Value (IV)** from **1 to 10**.
- The GM or player rolls **D10**: if the result is **≥ monster's IV**, the character side goes first.
- The higher the IV, the faster the monster moves.
- When monsters with different IVs are mixed, **use the highest value**.

### 2. First Side Acts / 3. Second Side Acts

Each side acts in turn. Order of actions within a side:

- **PCs**: in **TS (Thief Skill) order** — higher TS acts earlier.
- **Monsters**: in **Initiative Value order**.

> You are free to **delay your action**. For example, you can wait for a mage to cast Enchant Weapon on your weapon before striking a monster.

### 4. Sheet Recording

Record changes in **LP and MP** on the character sheet.

---

## Actions 行动种类

During combat, you can choose **only one** of the following actions per round.

### Movement 移动

Two types of movement:

| 类型                    | 速度          |
| ----------------------- | ------------- |
| Running 全速奔跑        | 100 + AG 米/回合 |
| Combat movement 战斗移动 | 最多 40 米/回合 |

In either case, it is possible to move more slowly.

> **Monster movement** is indicated as human-level or human × some multiplier. Assume **human-level AG = 10**.

### Attack 攻击

You can attack **one enemy per round** with your equipped weapon — striking the enemy.

- **Number of attacks** varies by class and level (see [Table 3.1](#table-31-number-of-attacks)).
- Even when you can attack multiple times, you can only attack **one target** per round.
- **Ranged weapons basically remain at 1 attack/round.**

### Moving Attack 移动攻击

You can move and attack within your **combat movement range**. However, in that case:

- **Your Fighting Skill is halved.**
- **Damage is calculated normally.**

### Magic 施法

You cast spells that you know — see **Chapter 4: Magic**.

### Defensive Stance 防御姿态

You do nothing but focus entirely on protecting yourself. This grants:

- **DE + 20, RE + 20**

This action can also be declared **when the monster acts if the monster side has initiative**. For example, after a monster decides to attack you, you can declare a defensive stance for this round. The defensive stance is also maintained during your own action phase.

### Other 其他

Any action that can be performed in reality is possible — for example, unlocking a door while your companions protect you. In such cases, make a **skill check** for the relevant skill (see Chapter 5).

---

## Hit & Damage 命中与伤害

### Hit Determination 命中判定

After making an attack, determine whether it hit.

- **Hit Rate (%) = Your FS − Opponent's DE**
- Roll **D100**: if the result is ≤ hit rate, the attack hits.
- DE represents the ability to avoid attacks and reduces the hit rate of all attacks against you.
- **Floor rule:** Even if hit rate becomes ≤ 10% (or negative), a D100 roll of **10 or less still hits**.

### Damage 伤害

If the attack hits, determine damage:

1. Roll the weapon's damage dice (e.g., D8 or D10+2)
2. Add the attacker's **Damage Bonus (DB)** → this is the total damage
3. **Subtract the enemy's Armor Value (AV)** from total damage
4. Subtract the result from the enemy's **LP**
5. If LP ≤ 0, the enemy is **defeated**
6. If AV ≥ damage → **"It didn't hurt a bit!"** (no wound)

> 公式：`实际扣 LP = max(0, 武器伤害骰 + DB − 敌方 AV)`
>
> AV（Armor Value 装甲值）：来自盔甲或皮甲，会先吸收伤害。

---

## Critical Hit 致命一击

If a D100 roll hits at **1/10 or less of the hit rate**, it becomes a **critical hit (effective hit)** — you've struck a weak point in the enemy's armor or hide.

- **Effect:** Enemy's Armor Value is **completely ignored** — total damage subtracts directly from LP.
- **Floor rule:** If the hit rate is less than 10%, a critical hit only occurs when the D100 roll is **exactly 1**.

> 例：FS-DE = 50% 命中率 → ≤ 5 是致命一击。命中率 < 10% 时仅 01 致命。

---

## Number of Attacks 攻击次数表

### Table 3.1 Number of Attacks

| Level | Warrior / Knight | Priest / Scout / Shaman | Sorcerer / Wizard |
| ----: | ---------------- | ----------------------- | ----------------- |
|     1 | 1/round          | 1/round                 | 1/round           |
|     3 | 2/round          | 1/round                 | 1/round           |
|     5 | 3/round          | 2/round                 | 1/round           |
|     7 | 4/round          | 2/round                 | 2/round           |

> 「level 7 Warrior」相比早期 D&D 多次攻击系统更显著——本系统鼓励高级战士多挥几剑。

---

## Example: First combat with goblins 范例 — 与哥布林的初战

> 来源：PDF p.36（Chapter 3 末尾示例，Greevus / Garrack / Spark 队伍）

Having just reached **level 2**, the party encountered a band of goblins. Since the enemy seemed ready to attack, we decided to take them on.

**1. Initiative roll** — Spark (for once!) rolled **10** on D10 → party goes first.

**2. Greevus attacks** — readied halberd for a move-and-attack:

- Hit rate = (FS ÷ 2) − enemy DE = 22 − 5 = **17%**
- Rolled D100 = **01** → ≤ 1/10 of 17% → **critical hit!**
- Damage rolled: **12 damage**, ignoring AV.

**3. Garrack** also took down one goblin in a single round.

**4. Goblin counterattack** — they used moving attack too. *"Don't forget my defense is 30, GM."* They **missed**.

**5. Next round, enemy initiative** — their attack **hit** for **7 damage**.

- *"This chainmail armor absorbs up to 7 damage, so it doesn't hurt one bit!"*

**6. After 10 rounds**, half the goblins fell and the rest fled. Greevus took down 4 with the halberd; Garrack got 3.
