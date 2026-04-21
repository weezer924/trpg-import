# Cairn 2e — Core Rules, Combat, Scars & Magic

> Source: *Cairn* 2nd Edition Player's Guide, Section 3 (pp.62–67). Text licensed under CC BY-SA 4.0.
> Covers: attributes, saves, healing, deprivation, armor, reactions, morale, hirelings, die of fate, combat, critical damage, scars, magic.
> Procedures (dungeon, wilderness, downtime) live in `cairn2e-procedures.md`.

## Index

1. [Core Rules](#core-rules)
2. [Combat](#combat)
3. [Scars Table](#scars-table)
4. [Magic](#magic)

---

## Core Rules

### Attributes

*(Players' Guide p.62)*

Each of the three attributes is used in different circumstances (see **Saves**).

- **Strength (STR)** — Used for saves requiring physical power, like lifting gates, bending bars, resisting poison, etc.
- **Dexterity (DEX)** — Used for saves requiring poise, speed, reflexes, dodging, climbing, sneaking, balancing, etc.
- **Willpower (WIL)** — Used for saves to persuade, deceive, interrogate, intimidate, charm, provoke, manipulate spells, etc.

### Saves

- A save is a roll to avoid negative outcomes from risky choices. Characters roll a **d20** and compare the result to the appropriate attribute. If they roll **equal to or under** that attribute, they succeed. Otherwise, they fail. **A 1 is always a success, and a 20 is always a failure.**
- If two opponents are each trying to overcome the other, **whoever is most at risk should save**.
- If two characters need to take an action together, **whoever is most at risk should save** (usually the character with the lowest relevant attribute).

### Healing & Recovery

- Resting for a few moments and having a drink of water restores lost HP but may leave the party exposed. **Bandages** can stabilize a character that has taken **Critical Damage**.
- Attribute loss (see **Critical Damage**) can usually be restored with a week's rest, facilitated by a healer or other appropriate source of expertise.
- Some healing services are free, while magical or more expedient means of recovery may come at a cost.

### Deprivation & Fatigue

- A PC that lacks a crucial need (such as food or rest) is ***Deprived***. Anyone Deprived for more than a day adds **Fatigue** to their inventory, one for each day. A Deprived PC cannot recover HP, attributes, or item slots from Fatigue.
- A PC may also be forced to add Fatigue after casting spells or due to events occurring in the fiction. Each Fatigue **occupies one slot** and lasts until the PC is able to recuperate (such as with a full night's rest in a safe spot).
- If a character is forced to add Fatigue but they have no free slots, they must **drop an item** from their inventory.

### Armor

*(Players' Guide p.63)*

- Before calculating damage to HP, **subtract the target's Armor value** from the result of damage rolls.
- Shields and similar armor provide a bonus defense (e.g. +1 Armor), but only while the item is held or worn. Some may also provide additional benefits, depending on the fiction.
- A PC, NPC, or monster **cannot have more than 3 Armor**.

### Reactions

When the PCs encounter an NPC whose reaction to the party is not obvious, the Warden may roll **2d6** and consult the following table:

| 2d6 | 2 | 3–5 | 6–8 | 9–11 | 12 |
|---|:-:|:-:|:-:|:-:|:-:|
| Reaction | Hostile | Wary | Curious | Kind | Helpful |

### Morale

- Enemies must pass a **WIL save** to avoid fleeing when they take their first casualty and again when they lose half their number.
- Some groups may use their **leader's WIL** in place of their own. Lone foes must save when they're reduced to 0 HP.
- **Morale does not affect PCs.**

### Hirelings

- Adventuring parties can recruit hirelings, relying on their unique skills, knowledge, and training to aid in expeditions.
- To create a hireling, choose an appropriate role from the **Hirelings** table in the Marketplace (`cairn2e-character-creation.md`). Roll **3d6** for each attribute and **1d6** for HP. Give them equipment appropriate to their station, then roll on the Character Traits tables to further flesh them out.
- Alternatively, choose an appropriate **background** and name from the Character Creation guide. Roll (or choose from) the tables for that background. Then roll for Rations, Gold Pieces, Attributes, HP, and age.

### Die of Fate

- Optionally, roll **1d6** whenever the outcome of an event is uncertain or to simulate an element of randomness and chance.
- A roll of **4 or more** generally favors the PCs; a roll of **3 or under** usually means bad luck for the PCs.

---

## Combat

### Rounds

*(Players' Guide p.64)*

- A **round** is roughly ten seconds of in-game time and proceeds with each side taking turns. Each round starts with all PCs that are able to act, followed by their opponents. *The result of each side's actions occur simultaneously.*
- During the **first round of combat**, each PC must make a **DEX save** in order to act. Special circumstances, abilities, items, or skills may negate this requirement. PCs that fail their save **lose their turn** for this round.
- Their opponents then take their turn, and the first round ends. The next round begins with the PCs taking their turn, followed by their opponents, and so on until combat has ended with one side defeated or fled.

### Actions

- On their turn, a character may move up to **40 ft** and take up to **one action**. This may be casting a spell, attacking, moving for a second time, or some other reasonable action. Each round, the PCs declare what they are doing before dice are rolled. If a character attempts something risky, the Warden calls for a save for appropriate players or NPCs.

### Attacking & Damage

- The attacker rolls their weapon die and subtracts the target's Armor, then deals the remaining total to their opponent's HP. **Attacks in combat automatically hit.**
- If multiple attackers target the same foe, roll all damage dice and **keep the single highest result**. All actions are declared before being resolved.
- If an attack would take a PC's HP **exactly to 0**, refer to the **Scars** table to see how they are uniquely impacted.

### Attack Modifiers

- If fighting from a position of weakness (such as through cover or with bound hands), the attack is ***Impaired***, and the attacker must roll **1d4 damage** regardless of the attack's damage die. **Unarmed attacks always do 1d4 damage.**
- If fighting from a position of advantage (such as against a helpless foe or through a daring maneuver), the attack is ***Enhanced***, allowing the attacker to roll **1d12 damage** instead of their normal die.
- Attacks with the ***Blast*** quality affect all targets in the noted area, rolling separately for each affected character. This can be anything from explosions to a dragon's breath or the impact of a meteorite. If unsure how many targets can be affected, roll the related damage die for a result.
- If attacking with two weapons at the same time, roll both damage dice and **keep the single highest result** (denoted with a plus symbol, e.g. d8+d8).

### Critical Damage

*(Players' Guide p.65)*

- Damage that reduces a target's HP **below zero** is subtracted from their **STR** by the amount of damage remaining. The target must then immediately make a STR save (using their **new** STR score) to avoid taking **Critical Damage**. On a success, the target is still in the fight (albeit with a lower STR score) and must continue to make Critical Damage saves when incurring damage.
- Any PC that suffers Critical Damage cannot do anything but crawl weakly, grasping for life. If given aid (such as bandages), they will stabilize. If left untreated, **they die within the hour**. NPCs and monsters that fail a Critical Damage save are considered dead, per the Warden's discretion. Some enemies have special abilities or effects triggered when their target fails a Critical Damage save.

### Attribute Loss

- If a PC's **STR** is reduced to 0, they **die**. If their **DEX** is reduced to 0, they are **paralyzed**. If their **WIL** is reduced to 0, they are **delirious**. Complete DEX and WIL loss renders the character unable to act until they are restored through extended rest or by extraordinary means.
- If a PC takes damage **outside of combat**, they should instead receive damage to an attribute, typically STR.

### Character Death

- When a character dies, the player should create a new character or take control of a hireling. They immediately join the party in order to reduce downtime.

### Detachments

- Large groups of similar combatants fighting together are treated as a single **Detachment**. When a detachment takes Critical Damage, it is routed or significantly weakened. When it reaches 0 STR, it is destroyed.
- Attacks against detachments by individuals are ***Impaired*** (excluding *Blast* damage).
- Attacks against individuals by detachments are ***Enhanced*** and deal *Blast* damage.

### Retreat

- Running away from a dire situation always requires a successful **DEX save**, as well as a safe destination to run to.

### Ranged Attacks

- Ranged weapons can target any enemy near enough to "see the whites of their eyes." Attacks against especially distant targets are ***Impaired***.
- **Ammunition is not tracked unless otherwise specified.**

---

## Scars Table

*(Players' Guide p.66) — if damage to a PC would reduce their HP to **exactly 0**, look up the result on the table below based on the **HP lost in that attack** (e.g. went from 3 HP to 0 HP → entry #3 Walloped).*

| HP Lost | Scar | Effect |
|---:|---|---|
| 1 | **Lasting Scar** | Roll 1d6 \| 1: Neck, 2: Hands, 3: Eye, 4: Chest, 5: Legs, 6: Ear. Roll 1d6. If the total is higher than your max HP, take the new result. |
| 2 | **Rattling Blow** | You're disoriented and shaken. Describe how you refocus. Roll 1d6. If the total is higher than your max HP, take the new result. |
| 3 | **Walloped** | You're sent flying and land flat on your face, winded. You are *deprived* until you rest for a few hours. Then, roll 1d6. Add that amount to your max HP. |
| 4 | **Broken Limb** | Roll 1d6 \| 1–2: Leg, 3–4: Arm, 5: Rib, 6: Skull. Once mended, roll 2d6. If the total is higher than your max HP, take the new result. |
| 5 | **Diseased** | You're afflicted with a gross, uncomfortable infection. When you get over it, roll 2d6. If the total is higher than your max HP, take the new result. |
| 6 | **Reorienting Head Wound** | Roll 1d6 \| 1–2: STR, 3–4: DEX, 5–6: WIL. Roll 3d6. If the total is higher than your current attribute, take the new result. |
| 7 | **Hamstrung** | You can barely move until you get serious help and rest. After recovery, roll 3d6. If the total is higher than your max DEX, take the new result. |
| 8 | **Deafened** | You cannot hear anything until you find extraordinary aid. Regardless, make a WIL save. If you pass, increase your max WIL by 1d4. |
| 9 | **Re-brained** | Some hidden part of your psyche is knocked loose. Roll 3d6. If the total is higher than your max WIL, take the new result. |
| 10 | **Sundered** | An appendage is torn off, crippled, or useless (the Warden will tell you which). Then make a WIL save. If you pass, increase your max WIL by 1d6. |
| 11 | **Mortal Wound** | You are deprived and out of action. You die in one hour unless healed. Upon recovery, roll 2d6. Take the new result as your max HP. |
| 12 | **Doomed** | Death seemed ever so close, but somehow you survived. If your next save against Critical Damage is a fail, you die horribly. If you pass, roll 3d6. If the total is higher than your max HP, take the new result. |

---

## Magic

### Spellbooks

*(Players' Guide p.67)*

- Spellbooks contain a single spell and take up one slot. They cannot be easily transcribed or created; instead they are recovered from places like tombs, dungeons, and manors.
- Spellbooks sometimes display unusual properties or limitations, such as producing a foul or unearthly smell when opened, possessing an innate intelligence, or being legible only when held in moonlight.
- Spellbooks will attract the attention of those who seek the arcane power within, and it is considered dangerous to display them openly.

### Casting Spells

- Anyone can cast a spell by holding a Spellbook in **both hands** and reading its contents aloud. They must then add a **Fatigue** to inventory.
- Given time and safety, PCs can ***enhance*** a spell's impact (e.g., affecting multiple targets, increasing its power, etc.) without any additional cost.
- If the PC is *deprived* or in danger (such as during combat), the Warden may require a **WIL save** to avoid any ill-effects from casting the spell. Consequences of failure are on par with the intended effect and may result in added Fatigue, the destruction of the Spellbook, injury, and even death.

### Scrolls

Scrolls are similar to Spellbooks, however:

- They are ***petty***.
- They do not cause Fatigue.
- They disappear after one use.

### Relics

- Relics are items imbued with a magical spell or power. They do **not** cause Fatigue. Relics usually have limited uses, as well as a **Recharge** condition.

> **Note:** the 2e Player's Guide does not include a spell list — the 100 spells from 1e are reused. See `cairn1e-spells.md` for the d100 Spellbook table and individual spell descriptions.
