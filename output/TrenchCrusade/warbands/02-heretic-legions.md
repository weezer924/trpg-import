# warbands/02-heretic-legions: Heretic Legions（异端军团）

> 源：`Rule Books/Trench Crusade/Warbands of Trench Crusade v1.0.2.pdf` p.103-124
> 版本：v1.0.2
>
> Faction：**Heretic Legions（异端军团）** · Alignment：**Fallen** · Patron：依 variant 而定（默认无；Knights of Avarice → Mammon）

## Index

- [Faction Overview](#faction-overview)
- [Warband Creation](#warband-creation)
- [Special Rules](#special-rules)
- [Armoury Tables](#armoury-tables)
  - [Ranged Weapons](#ranged-weapons)
  - [Melee Weapons](#melee-weapons)
  - [Grenades](#grenades)
  - [Shields](#shields)
  - [Armour](#armour)
  - [Equipment](#equipment)
- [Heretic Legions Battlekit (unique)](#heretic-legions-battlekit-unique)
  - [Blasphemous Staff](#blasphemous-staff)
  - [Hellblade](#hellblade)
  - [Sacrificial Blade](#sacrificial-blade)
  - [Tartarus Claws](#tartarus-claws)
- [Elite Warband Entries — The Devil's Own](#elite-warband-entries--the-devils-own)
  - [Heretic Priest](#heretic-priest)
  - [Death Commando](#death-commando)
  - [Chorister](#chorister)
- [Troop Warband Entries — Legionnaires of Hell](#troop-warband-entries--legionnaires-of-hell)
  - [Heretic Trooper / Heretic Legionnaire](#heretic-trooper--heretic-legionnaire)
  - [War Wolf Assault Beast](#war-wolf-assault-beast)
  - [Wretched](#wretched)
  - [Anointed Heavy Infantry](#anointed-heavy-infantry)
  - [Artillery Witch](#artillery-witch)
    - [Infernal Bomb](#infernal-bomb)
- [Warband Variants](#warband-variants)
  - [Trench Ghosts](#trench-ghosts)
    - [Trench Ghost Battlekit](#trench-ghost-battlekit)
      - [Sarcophagus Mine](#sarcophagus-mine)
      - [Tank Palanquin](#tank-palanquin)
  - [Knights of Avarice](#knights-of-avarice)
    - [Knights of Avarice Battlekit](#knights-of-avarice-battlekit)
      - [Coin Hammer](#coin-hammer)
      - [Golden Calf Altar](#golden-calf-altar)
      - [Gas Bombs](#gas-bombs)
      - [Standard of Mammon](#standard-of-mammon)
      - [Tarnished Armour](#tarnished-armour)
  - [Heretic Naval Raiders](#heretic-naval-raiders)
- [Base Size Summary](#base-size-summary)
- [Cross-References](#cross-references)

---

## 数值速查表（Model Profiles at a Glance）

> 单位：M / Ranged / Melee = DICE 修正；Armour = INJURY MODIFIER；Base = 逻辑 base_size × 视觉 mm；Limit = warband 招募上限。
> 详细 special rules / battlekit slots / lore 见下方对应章节。Variant warband（Trench Ghosts / Knights of Avarice / Heretic Naval Raiders）不在此表（详见 [Warband Variants](#warband-variants)）。

### Elite（精英）

| Model | Cost | M | R | Me | Armour | Base | Keywords | Limit |
|---|---:|---:|---:|---:|---:|---|---|---|
| [Heretic Priest](#heretic-priest) | 80 👑 | 6 | +2 | +2 | 0 | 1×1 / 32mm | HERETIC, ELITE, LEADER, TOUGH | **1（required）** |
| [Death Commando](#death-commando) | 90 👑 | 6 | +1 | +2 | 0 | 1×1 / 32mm | HERETIC, ELITE, INFILTRATOR | 0–1 |
| [Chorister](#chorister) | 65 👑 | 6 | -2 | +2 | 0 | 1×1 / 32mm | HERETIC, ELITE, FEAR | 0–1 |

### Troops（部队）

| Model | Cost | M | R | Me | Armour | Base | Keywords | Limit |
|---|---:|---:|---:|---:|---:|---|---|---|
| [Heretic Trooper / Legionnaire](#heretic-trooper--heretic-legionnaire) | 30 / 40 👑 | 6 | 0 | 0 | 0 | 1×1 / 25mm | HERETIC | 无上限 |
| [War Wolf Assault Beast](#war-wolf-assault-beast) | 145 👑 | **8** | — | +2 | -3 | **2×2 / 50mm** | HERETIC, ARTIFICIAL, FEAR, NEGATE DIFFICULT TERRAIN, TOUGH | 0–1 |
| [Wretched](#wretched) | 25 👑 | 6 | -1 | -1 | 0 | 1×1 / 25mm | HERETIC | 无上限 |
| [Anointed Heavy Infantry](#anointed-heavy-infantry) | 95 👑 | 6 | +1 | +1 | -2 | 1×1 / 32mm | HERETIC, STRONG | 0–5 |
| [Artillery Witch](#artillery-witch) | 100 👑 | 6 | 0 | -1 | 0 | 1×1 / 32mm | HERETIC, ARTIFICIAL, NEGATE FEAR, NEGATE GAS | 0–1（≥1000👑 时 0–2）|

> **特殊数值提示**：
> - **War Wolf** 不能 Ranged Attack（`ranged: null`），Movement = 8，base = 2×2 逻辑格（与 [`matches/coordinate-system.md`](../matches/coordinate-system.md) §1 base 渲染相关）。
> - **Heretic Legionnaire**（40 👑）是 Heretic Trooper 的 upgrade，profile = `heretic-legionnaire`，stats 与 Trooper 同表但 battlekit 选项不同。
> - **Mandatory battlekit**：Anointed = Reinforced Armour + Infernal Brand；Artillery Witch = Infernal Bomb。

---

## Faction Overview

> *A shroud of darkness blankets the world. Smoke and brimstone spew from the yawning Gates of Inferno, enveloping the lands where people have abandoned God and openly wage war against His Creation. ... The main satanic military force on Earth are the Heretic Legions, raised from amongst these citizens of the damned.*
> — Warbands p.103

In domains where men worship demons and kneel before the altars of the Golden Calf, mortal followers — flanked by the abhorrent progeny of the underworld — muster beneath the banners of mighty archdevils. Initiation requires an unholy pilgrimage to the burning bronze Gates of Hell; those who survive the Valley of Tears are branded with the mark of the demon lord that has claimed them. The **Anointed** push further still — to the very Gate and beyond — and are forever scarred by abyssal fires, granted strength to wield Gehenna armour and weapons no mortal could lift. The Legions are reinforced by **War Beasts** of captured and possessed creatures, and by dreaded **Artillery Witches** who act as mobile artillery.

---

## Warband Creation

```yaml
faction: heretic-legions
alignment: Fallen
starting_budget: 700      # 👑
patron: null              # default; see Knights of Avarice variant
```

You have **700 👑** to recruit a Heretic Legions Warband for a campaign (▶ see `matches/roster-template.md`). The Heretic Legions are **Fallen**.

---

## Special Rules

**No special rules apply** to a standard Heretic Legions Warband. (Variants below add their own.)

---

## Armoury Tables

Battlekit marked **[•]** is **unique to Heretic Legions** — full rules in [Heretic Legions Battlekit (unique)](#heretic-legions-battlekit-unique) below. All other items follow standard Battlekit rules in `→ rules/05-battlekit.md`.

### Ranged Weapons

| Item                  | Restrictions / Notes              | Cost   |
| --------------------- | --------------------------------- | -----: |
| Anti-Materiel Rifle   | Limit: 1                          |    3 ☼ |
| Automatic Rifle       | Bayonet Lug, Limit: 2             |    2 ☼ |
| Automatic Shotgun     | Bayonet Lug, Shield Combo         |   15 👑 |
| Bolt-Action Rifle     | Bayonet Lug                       |   10 👑 |
| Flamethrower          | Limit: 3                          |   30 👑 |
| Grenade Launcher      | Limit: 2                          |   30 👑 |
| Heavy Flamethrower    | Limit: 2                          |   55 👑 |
| Machine Gun           | Limit: 1                          |   50 👑 |
| Pistol                | —                                 |    6 👑 |
| Semi-Automatic Rifle  | Bayonet Lug                       |   15 👑 |
| Shotgun               | Bayonet Lug, Shield Combo         |   10 👑 |
| Silenced Pistol       | `ELITE` only                      |   15 👑 |
| Submachine Gun        | Bayonet Lug, Shield Combo         |    2 ☼ |

### Melee Weapons

| Item                   | Restrictions / Notes                            | Cost   |
| ---------------------- | ----------------------------------------------- | -----: |
| Bayonet                | Shield Combo                                    |    2 👑 |
| **• Blasphemous Staff** | `ELITE` only                                    |    2 ☼ |
| Great Hammer/Maul      | —                                               |   10 👑 |
| Great Sword/Axe        | —                                               |   12 👑 |
| **• Hellblade**         | Limit: 2                                        |    1 ☼ |
| Polearm                | Shield Combo                                    |    7 👑 |
| **• Sacrificial Blade** | `ELITE` only, Limit: 2                          |   23 👑 |
| Sword/Axe              | —                                               |    4 👑 |
| **• Tartarus Claws**    | Death Commando only                             |   15 👑 |
| Trench Club            | —                                               |    3 👑 |
| Trench Knife           | —                                               |    1 👑 |

### Grenades

| Item                | Restrictions | Cost  |
| ------------------- | ------------ | ----: |
| Frag Grenades       | —            |  7 👑 |
| Gas Grenades        | —            | 10 👑 |
| Incendiary Grenades | —            | 15 👑 |

### Shields

| Item          | Notes        | Cost  |
| ------------- | ------------ | ----: |
| Trench Shield | Shield Combo | 10 👑 |

### Armour

| Item              | Restrictions                  | Cost  |
| ----------------- | ----------------------------- | ----: |
| Reinforced Armour | Anointed & `ELITE` only       | 40 👑 |
| Standard Armour   | —                             | 15 👑 |

### Equipment

| Item                       | Restrictions / Notes                                     | Cost  |
| -------------------------- | -------------------------------------------------------- | ----: |
| Binoculars                 | `ELITE` only                                             | 10 👑 |
| Combat Helmet              | Headgear                                                 |  5 👑 |
| Gas Mask                   | —                                                        |  5 👑 |
| Hellbound Soul Contract    | Heretic Troopers & Heretic Legionnaires only, Limit: 3   |  5 👑 |
| Incendiary Ammunition      | Consumable, Limit: 1                                     | 15 👑 |
| Infernal Brand             | —                                                        |  5 👑 |
| Mountaineer Kit            | Limit: 2                                                 |  3 👑 |
| Musical Instrument         | Limit: 1                                                 | 15 👑 |
| Shovel                     | —                                                        |  5 👑 |
| Troop Flag                 | Limit: 1                                                 |  1 ☼ |
| Unholy Relic               | —                                                        | 15 👑 |
| Unholy Trinket             | Consumable                                               | 15 👑 |

> All non-unique items: see `→ rules/05-battlekit.md` for full rules.
> Note: **Hellbound Soul Contract** and **Infernal Brand** have full rules in
> `→ rules/05-battlekit.md#hellbound-soul-contract` and
> `→ rules/05-battlekit.md#infernal-brand`.

---

## Heretic Legions Battlekit (unique)

The following Battlekit items are **unique to the Heretic Legions Warband**. Rules for all other items are in the standard Battlekit section (`→ rules/05-battlekit.md`).

### Blasphemous Staff

> *Crafted in mockery of the rod carried by the prophet Aaron, this evil staff unleashes searing hellfire, causing excruciating pain with the slightest touch.*

```yaml
weapon: blasphemous-staff
type: melee
hands: 1
range: melee
keywords: [CRITICAL, FIRE]
restrictions: ELITE only
cost: 2 ☼
```

- **Evil Power**: Add `+1 DICE` to Success Rolls or Risky Success Rolls for a model with a Blasphemous Staff, **apart from** the Success Rolls for a Ranged or Melee Attack, or the Risky Success Roll to take a Dash ACTION.

> `→ rules/03-keywords-glossary.md#critical`, `→ rules/03-keywords-glossary.md#fire`

### Hellblade

> *Crafted from iron ore from the mines of Dis in Inferno, this weapon burns with the unquenchable fires of Hell.*

```yaml
weapon: hellblade
type: melee
hands: 2
range: melee
keywords: ["+1 INJURY DICE", FIRE]
limit: 2
cost: 1 ☼
```

> `→ rules/03-keywords-glossary.md#injury-dice`, `→ rules/03-keywords-glossary.md#fire`

### Sacrificial Blade

> *Terrifying blades blessed by the hand of a greater devil, these knives are used in Heretic rituals to sacrifice captives to the dark powers of Hell. They simply need to touch their opponents to cause indescribable pain, and even the most minor wound often proves fatal from the agony alone. They are risky even to their wielders, as the merest scratch wounds friend and foe alike.*

```yaml
weapon: sacrificial-blade
type: melee
hands: 1
range: melee
keywords: ["+2 INJURY MODIFIER", RISKY]
restrictions: ELITE only
limit: 2
cost: 23 👑
```

> `→ rules/03-keywords-glossary.md#injury-modifier`, `→ rules/03-keywords-glossary.md#risky`

### Tartarus Claws

> *Made from severed hands of Malebranche, the Tartarus claws are granted by archdevils only to those whose hearts are blackened with the sin of Wrath.*

```yaml
weapon: tartarus-claws
type: melee
hands: 2
range: melee
keywords: [CLEAVE 2, CRITICAL, CUMBERSOME]
restrictions: Death Commando only
cost: 15 👑
```

- **Harrowing Assault**: If the target is taken Down or Out of Action by a Melee Attack made with Tartarus Claws, you can immediately move the model up to **3"**. You can use this move to move within 1" of another enemy model, and if you do so, this model can take another **Fight ACTION**. However, it cannot make the 3" move if the second attack takes the target Down or Out of Action.

> `→ rules/03-keywords-glossary.md#cleave-x`, `→ rules/03-keywords-glossary.md#critical`, `→ rules/03-keywords-glossary.md#cumbersome`, `→ rules/02-comprehensive-rules.md#fight-action`

---

## Elite Warband Entries — The Devil's Own

### Heretic Priest

> **Faction**: Heretic Legions · **Type**: Elite · **Cost**: 80 👑 · **Required**: 1 (Warband must include 1)

```yaml
profile: heretic-priest
stats:
  movement: 6           # "/Infantry
  ranged: +2 DICE
  melee: +2 DICE
  armour: 0
keywords: [HERETIC, ELITE, LEADER, TOUGH]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
```

**Battlekit**: A Heretic Priest can have any Battlekit from the Heretic Legions Armoury Tables.

**Lore**:
> These fallen Priests wield unholy magics, summoning petrifying demons and creatures through their Goetic spells. Often pledged to a demon lord in Hell, such as Pazuzu or Guison, the profane gospels they recite strike fear into Church forces, causing ears to bleed and eyeballs to burst in their sockets.

**Abilities**:

- **Puppet Master ACTION**: A Heretic Priest can take a *Puppet Master ACTION*. If they do so, take a Risky Success Roll for the model. If the roll is a Failure, the Heretic Priest's Activation ends immediately. If the roll is a Success or Critical Success, pick 1 model (friend or foe) that is within 12" of the Heretic Priest and in their Line of Sight, apart from the Heretic Priest themselves. You can move the model D6". The move must be in a straight line, but can be in any direction, and can be used to make the model move within 1" of an enemy, make a Retreat move, Climb, Jump, or Jump Down. The model cannot make a Diving Charge and does not count as charging if it finishes the move within 1" of an enemy model.

> Distance / LOS: `→ matches/coordinate-system.md §3`, `→ matches/coordinate-system.md §6`
> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#elite`, `→ rules/03-keywords-glossary.md#leader`, `→ rules/03-keywords-glossary.md#tough`

---

### Death Commando

> **Faction**: Heretic Legions · **Type**: Elite · **Cost**: 90 👑 · **Limit**: 0–1

```yaml
profile: death-commando
stats:
  movement: 6           # "/Infantry
  ranged: +1 DICE
  melee: +2 DICE
  armour: 0
keywords: [HERETIC, ELITE, INFILTRATOR]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
```

**Battlekit**: A Death Commando can have Battlekit from the Heretic Legions Armoury Tables. The only **Ranged Weapons** they can have are *Silenced Pistols* and *Tormentor Chains* (▶ see Glory Items in the Trench Crusade Digital Rulebook — v0.2+), and the only **Grenades** they can have are *Gas Grenades*. No restrictions apply to any other Types of Battlekit. (Tartarus Claws are Death Commando-only.)

**Lore**:
> These terrifying infiltrators are silent killers, equipped with stealth generators that hide them from the Eyes of God. They have been known to eliminate entire enemy squads single-handedly.

**Abilities**:

- **Stealth Generator**: Add `-1 DICE` to rolls for Ranged Attacks that target a Death Commando.
  > **Errata clarification**: *Stealth Generator* applies **only when the attack directly targets the Death Commando**. It does **not** apply to a `BLAST` attack that targets a point on the ground (the Death Commando may still be caught in the blast). `→ errata/rules-commentaries.md#heretic-legions-q2--death-commando-的-stealth-generator-对-blast-的效力`
- **Hide ACTION**: A Death Commando can take a *Hide ACTION* if they are in contact with a terrain piece that is at least **½"** high. If they do so, take a Risky Success Roll for the model and add `+1 DICE` to the roll. If the roll is a Failure, the Death Commando's Activation ends immediately. If the roll is a Success or Critical Success, enemy models cannot choose the Death Commando as the target for a Ranged Attack or Charge until the Death Commando moves, charges, retreats, makes a Ranged Attack, or an enemy model moves within **1.5"** of them. The Death Commando can be hit if they are within the blast radius of a Weapon with the `BLAST` Keyword.

> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#elite`, `→ rules/03-keywords-glossary.md#infiltrator`, `→ rules/03-keywords-glossary.md#blast-x`

---

### Chorister

> **Faction**: Heretic Legions · **Type**: Elite · **Cost**: 65 👑 · **Limit**: 0–1

```yaml
profile: chorister
stats:
  movement: 6           # "/Infantry
  ranged: -2 DICE
  melee: +2 DICE
  armour: 0
keywords: [HERETIC, ELITE, FEAR]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
```

**Battlekit**: A Chorister can have any Battlekit from the Heretic Legions Armoury Tables.

**Lore**:
> Choristers sacrifice themselves upon black altars, and if worthy, rise after nine days, finishing their own beheading as their severed heads begin to sing. Their hymns conjure visions of Hell, sapping the strength and resolve of all who hear, the Chorister's cold blood forming diabolic symbols in rhythm with their unholy chorus.

**Abilities**:

- **Unholy Hymns**: Add `-1 DICE` to Success Rolls taken for enemy models that are within **8"** of one or more Choristers.

> Distance: `→ matches/coordinate-system.md §3`
> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#elite`, `→ rules/03-keywords-glossary.md#fear`

---

## Troop Warband Entries — Legionnaires of Hell

### Heretic Trooper / Heretic Legionnaire

> **Faction**: Heretic Legions · **Type**: Troops · **Cost**: 30 👑 (Trooper) / 40 👑 (Legionnaire upgrade)

**Heretic Trooper profile**:

```yaml
profile: heretic-trooper
stats:
  movement: 6           # "/Infantry
  ranged: +0 DICE
  melee: +0 DICE
  armour: 0
keywords: [HERETIC]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [25, 25]
```

**Heretic Legionnaire profile** (upgrade from Trooper, +10 👑):

```yaml
profile: heretic-legionnaire
stats:
  movement: 6           # "/Infantry
  ranged: see-below     # choose +1 DICE on ranged OR melee
  melee: see-below
  armour: 0
keywords: [HERETIC]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [25, 25]
upgraded_from: heretic-trooper
upgrade_cost: 10 👑
```

**Battlekit**: A Heretic Trooper or Heretic Legionnaire can have any Battlekit from the Heretic Legions Armoury Tables.

**Lore**:
> These soldiers make up the bulk of the Heretic forces. Heretic Legionnaires have witnessed the Gate of Hell and survived; they are damned for all eternity.

**Abilities**:

- **Heretic Legionnaires (upgrade)**: You can upgrade Heretic Troopers in your Warband to Heretic Legionnaires, at a cost of `+10 👑` each. You **cannot** upgrade a Heretic Trooper if doing so would result in there being more Heretic Legionnaires in your Warband than there are Heretic Troopers. When you upgrade a Heretic Trooper to a Heretic Legionnaire, you can change **either** their Ranged Characteristic **or** their Melee Characteristic from 0 to **+1**.

> Keywords: `→ rules/03-keywords-glossary.md#heretic`

---

### War Wolf Assault Beast

> **Faction**: Heretic Legions · **Type**: Troops · **Cost**: 145 👑 · **Limit**: 0–1

```yaml
profile: war-wolf-assault-beast
stats:
  movement: 8           # "/Infantry
  ranged: null          # cannot make Ranged Attacks
  melee: +2 DICE
  armour: -3
keywords: [HERETIC, ARTIFICIAL, FEAR, NEGATE DIFFICULT TERRAIN, TOUGH]
base_size: [2, 2]
base_shape: oval
base_dimensions_mm: [50, 50]  # 50mm base per PDF p.113
```

**Battlekit**: A War Wolf **always** has a *Chainsaw Mouth* and *Shredding Claws*. These weapons are part of the War Wolf and cannot be removed or lost throughout the campaign for any reason. It **cannot** have any other Battlekit.

**Lore**:
> This abomination charges through miles of barbed wire, clearing a path for the Heretic infantry. Its uniquely formed head is designed to cut cleanly through it. War Wolves wear unique armour forged in the factories of Hell, as seen by the maker's marks stamped upon it.

**Abilities**:

- **Assault Beast**: A War Wolf is armed with two Melee Weapons (its *Chainsaw Mouth* and *Shredding Claws*). When it makes a Melee Attack, it can attack **once** using either its Chainsaw Mouth or Shredding Claws, **or twice**, first with the Chainsaw Mouth and second with its Shredding Claws (the **Off-Hand Weapon** modifier applies to the attack made with the Shredding Claws). Note that **both** Weapons have the `RISKY` keyword, which means that the War Wolf's Activation ends immediately if the Success Roll for an attack made with either weapon is a Failure.
- **Loping Dash**: Add `+1 DICE` to the Risky Success Roll for a War Wolf that is taking a **Dash ACTION**.

**Built-in Weapons**:

```yaml
weapon: chainsaw-mouth
type: melee
hands: special           # integral to model
range: melee
keywords: ["+1 DICE", "+1 INJURY DICE", IGNORE ARMOUR, RISKY]
restrictions: War Wolf Assault Beast only
```

```yaml
weapon: shredding-claws
type: melee
hands: special           # integral to model
range: melee
keywords: ["+1 INJURY DICE", CUMBERSOME, RISKY]
restrictions: War Wolf Assault Beast only
```

> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#artificial`, `→ rules/03-keywords-glossary.md#fear`, `→ rules/03-keywords-glossary.md#negate-keyword`, `→ rules/03-keywords-glossary.md#difficult-terrain`, `→ rules/03-keywords-glossary.md#tough`, `→ rules/03-keywords-glossary.md#ignore-armour`, `→ rules/03-keywords-glossary.md#cumbersome`, `→ rules/03-keywords-glossary.md#risky`
> Off-Hand Weapon: `→ rules/02-comprehensive-rules.md#off-hand-weapon`
> Base sizing: `→ matches/coordinate-system.md §5`

---

### Wretched

> **Faction**: Heretic Legions · **Type**: Troops · **Cost**: 25 👑

```yaml
profile: wretched
stats:
  movement: 6           # "/Infantry
  ranged: -1 DICE
  melee: -1 DICE
  armour: 0
keywords: [HERETIC]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [25, 25]
```

**Battlekit**: Wretched can have any Battlekit from the Heretic Legions Armoury Tables **that costs up to 10 👑**. A Wretched **must** have at least 1 Weapon (they cannot be sent into battle completely unarmed).

**Lore**:
> Many unfortunates fall into the hands of Heretic warbands, captured in raids, purchased from the slave markets, or seized by watchful patrols. Such Wretched are branded with cursed flesh-eating tattoos as a safeguard against escape and heavily drugged to degrade and dull their will, while still leaving their aggression intact.

**Abilities**:

- **Chattel**: In a campaign, Wretched can be sold in the Quartermaster Step for `25 👑` plus half the cost in 👑 of any Battlekit they have. (v0.2+ Campaign Rules)
- **Dark Blessing**: When a Wretched is taken Out of Action, place **1 BLESSING MARKER** next to the nearest friendly model with the `ELITE` and `HERETIC` Keywords. If two or more eligible models are equally close to the Wretched, you can choose which receives the BLESSING MARKER.
- **Law of Hell**: If an attack made by a Wretched takes an enemy model with the `ELITE` Keyword **Out of Action**, the Wretched model gains its freedom and is immediately **removed from the game**. It no longer counts as being part of the Warband for the purposes of Morale Checks and is removed from the Warband Roster.

> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#elite`, `→ rules/03-keywords-glossary.md#blessing-marker`

---

### Anointed Heavy Infantry

> **Faction**: Heretic Legions · **Type**: Troops · **Cost**: 95 👑 · **Limit**: 0–5

```yaml
profile: anointed-heavy-infantry
stats:
  movement: 6           # "/Infantry
  ranged: +1 DICE
  melee: +1 DICE
  armour: -2            # Reinforced Armour already factored in
keywords: [HERETIC, STRONG]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
mandatory_battlekit: [reinforced-armour, infernal-brand]
```

**Battlekit**: An Anointed Heavy Infantry **always** has **Reinforced Armour** and an **Infernal Brand** (`→ rules/05-battlekit.md#reinforced-armour`, `→ rules/05-battlekit.md#infernal-brand`). This Battlekit cannot be removed or lost throughout the campaign for any reason. The Injury Modifier for the Armour is already included in the model's Profile above. They can also have any Battlekit from the Heretic Legions Armoury Tables.

**Lore**:
> Heavily armed and armoured assault troops. Their skin is burned and blistering from their ordained pilgrimages to Hell and back.

**Abilities**: None

> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#strong`

---

### Artillery Witch

> **Faction**: Heretic Legions · **Type**: Troops · **Cost**: 100 👑 · **Limit**: 0–1 (0–2 if Warband ≥ 1,000 👑)

```yaml
profile: artillery-witch
stats:
  movement: 6           # "/Infantry
  ranged: +0 DICE
  melee: -1 DICE
  armour: 0
keywords: [HERETIC, ARTIFICIAL, NEGATE FEAR, NEGATE GAS]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
mandatory_battlekit: [infernal-bomb]
```

**Battlekit**: An Artillery Witch **always** has *Infernal Bombs* (see [Infernal Bomb](#infernal-bomb) below). She can have Battlekit from the Heretic Legions Armoury Tables **except for** Ranged Weapons or Grenades.

**Lore**:
> Artillery Witches stalk the battlefields, hurling ordnance assembled in the death factories of Hell's Third Circle. They are completely mute, and no one has ever seen their faces, leading some to question if they are even alive. Rumours suggest that they too, were manufactured in Hell. They can call forth an endless number of Infernal bombs from a portal to Hell that they manifest at will, summoning them to their hands from a gate of midnight blackness.

**Abilities**:

- **Abiotic Life**: Add `-1 INJURY DICE` to rolls for an Artillery Witch that has been hit by an attack with the `GAS` Keyword.
- **Artillery Witch Battery**: You may include **0–2** Artillery Witches in a Warband if the total cost of all of the other models in the Warband (including their Battlekit, etc.) adds up to **1,000 👑 or more**.
- **Levitate**: You do **not** have to take a Risky Success Roll for an Artillery Witch when they Climb or Jump, or an Injury Roll if they Fall.

> Keywords: `→ rules/03-keywords-glossary.md#heretic`, `→ rules/03-keywords-glossary.md#artificial`, `→ rules/03-keywords-glossary.md#negate-keyword`, `→ rules/03-keywords-glossary.md#fear`, `→ rules/03-keywords-glossary.md#gas`

#### Infernal Bomb

> *Bombs summoned from a portal to Hell.* Mandatory weapon of the Artillery Witch.

```yaml
weapon: infernal-bomb
type: ranged
hands: 1
range:
  max: 36              # inches; flat profile (no short/long split — IGNORE LONG RANGE)
keywords: [BLAST 3", IGNORE COVER, IGNORE ELEVATED POSITION, IGNORE LONG RANGE, RELOAD, SCATTER, SHRAPNEL]
restrictions: Artillery Witch only
included_with: artillery-witch
```

- **Duck**: Add `-1 INJURY DICE` to the roll for a model that is hit by an Infernal Bomb if it is in contact with a terrain piece that is at least **½"** tall **and** that lies in between it and the target point.
- **Infernal Strike**: If the Success Roll for a Ranged Attack with an Infernal Bomb that targets an enemy model is a Success or a Critical Success, **or** if the attack is a Failure and the target point scatters onto a model's base, apply the effect of the `DEADLY` Keyword to the Injury Roll for that model. Injury Rolls for other models caught in the Infernal Bomb's `BLAST` are made normally.
- **Mighty Explosion**: If a model that has been hit by an Infernal Bomb is not taken Out of Action by the Injury Roll, it is blown away **D3"** in a straight line by the explosion, even if the model has been taken Down by the Injury Roll. Roll separately for each model to see how far it is blown away. If the model was the target of the attack, it is blown directly away from the Artillery Witch. If the model was caught in the Blast of the weapon, it is blown directly away from the target point. The model stops if it is blown into another model, Impassable terrain, or terrain it cannot cross without having to Climb.

> `→ rules/03-keywords-glossary.md#blast-x`, `→ rules/03-keywords-glossary.md#ignore-modifier`, `→ rules/03-keywords-glossary.md#reload`, `→ rules/03-keywords-glossary.md#scatter`, `→ rules/03-keywords-glossary.md#shrapnel`, `→ rules/03-keywords-glossary.md#deadly`
> Distance / LOS / target point: `→ matches/coordinate-system.md §3`, `→ matches/coordinate-system.md §6`

---

## Warband Variants

### Trench Ghosts

> *Sometimes, when Heretic troopers die upon a hallowed ground or in the presence of an uncorrupted holy relic, they become trapped between planes of existence. Claimed by neither Heaven nor Hell, the Trench Ghosts become undead. They are doomed to fight a war without an end, attacking both the Faithful and Heretic alike, hating all life, and obeying commands that no living can hear.*
> — Warbands p.118

```yaml
variant: trench-ghosts
base_faction: heretic-legions
patron: null
```

**Trench Ghost Special Rules**:

- **Barbed Wire Banshee**: A Trench Ghost Warband can include a **Barbed Wire Banshee** instead of a Chorister. The Barbed Wire Banshee has the **same Profile and Cost** as a Chorister (65 👑, M 6, Ranged -2 DICE, Melee +2 DICE, Armour 0, base 32mm; keywords `HERETIC, ELITE, FEAR`), but **instead of** the *Unholy Hymns* Ability, **add `+1 INJURY DICE` to rolls for enemy models that are within 8" of a Barbed Wire Banshee**.
- **Enemies of All**: A Trench Ghost Warband **cannot** include Mercenaries.
- **Lost Souls**: A Trench Ghost Warband **cannot** include models with the `ARTIFICIAL` Keyword (i.e. no War Wolf, no Artillery Witch), and models in a Trench Ghost Warband **cannot** have *Hellbound Soul Contracts* or *Infernal Brands*. The Warband **can** include Anointed Heavy Infantry, but they do **not** have their Infernal Brand and still cost **95 👑**.
- **Semi-corporeal**: Add `-1 INJURY DICE` for Injury Rolls caused by Ranged Attacks that hit a model from a Trench Ghost Warband.
- **Slow and Creeping**: Treat a Trench Ghost model as having a Movement Characteristic of **3"/Infantry** when it takes a **Dash ACTION**. In addition, add `-1 DICE` to the Success Roll for an attack made by a Trench Ghost model on an enemy model that is making a **Retreat**.
- **Undead Horror**: Models in this Warband have the `FEAR`, `NEGATE DIFFICULT TERRAIN`, and `NEGATE GAS` Keywords.

```yaml
variant_profile: barbed-wire-banshee
stats:
  movement: 6
  ranged: -2 DICE
  melee: +2 DICE
  armour: 0
keywords: [HERETIC, ELITE, FEAR]
base_size: [1, 1]
base_shape: circle
base_dimensions_mm: [32, 32]
cost: 65 👑
replaces: chorister
ability_override: barbed-wire-banshee-aura   # +1 INJURY DICE for enemies within 8"
```

#### Trench Ghost Battlekit

The following pieces of Battlekit are available to a Trench Ghost Warband.

##### Sarcophagus Mine

> *Heretic Troopers can be encased in suits of thick armour that have been filled with explosives, which can be triggered by the Trooper when the enemy draws close.*

```yaml
battlekit: sarcophagus-mine
type: armour
keywords: ["-3 INJURY MODIFIER", BLAST 3"]
restrictions: Heretic Troopers only (Trench Ghost variant)
limit: 2
cost: 30 👑
```

- **Walking Bomb**: A model that has a Sarcophagus Mine **cannot have any other Battlekit**. A model with a Sarcophagus Mine can take a **Trigger ACTION** (see below). In addition, if an enemy model finishes a move within **3"** of a model with a Sarcophagus Mine, you can interrupt its Activation and detonate the Sarcophagus Mine without having to take a Trigger ACTION.
- **Trigger ACTION**: When a model with a Sarcophagus Mine takes a Trigger ACTION, you must take a Risky Success Roll for the model with `+1 DICE`. If the roll is a Failure, nothing happens (but you can try again the next time the model is Activated). If the roll is a Success or Critical Success, the Sarcophagus Mine detonates as described below.
- **Detonation**: When a Sarcophagus Mine detonates, all models (friend or foe) within **3"** of the model carrying the Sarcophagus Mine **and** in its Line of Sight are hit by a Ranged Attack with the `SHRAPNEL` Keyword. Add `+1 INJURY DICE` to the Injury Rolls for models that are within **1"** of the model carrying the Sarcophagus Mine. The model carrying the Sarcophagus Mine is then taken **Out of Action**.

> `→ rules/03-keywords-glossary.md#blast-x`, `→ rules/03-keywords-glossary.md#shrapnel`, `→ matches/coordinate-system.md §6` (LOS)

##### Tank Palanquin

> *Trench Ghost Heretic Priests sometimes ride into battle standing on top of an armoured platform called a Tank Palanquin. From their lofty vantage point, they rain destruction upon the foe.*

```yaml
battlekit: tank-palanquin
type: armour
keywords: ["-3 INJURY MODIFIER", STRONG]
restrictions: Heretic Priest only (Trench Ghost variant)
cost: 60 👑
forces_base_size: [2, 2]
forces_base_dimensions_mm: [50, 50]   # 50mm base per "Bulky" rule
```

- **Bulky**: A model that has a Tank Palanquin **must be mounted on a 50mm base** and **cannot be equipped with a Shield**. In addition, it has a **Charge Bonus of D3"** instead of D6".
- **Death From On High**: Add **3"** to the height of a model that has a Tank Palanquin when determining if it receives the **Elevated Position** modifier for any Ranged Attacks that it makes.
- **Standfast**: When a model that has a Tank Palanquin suffers a **Down** result on the Injury table, it is treated as a **Minor Hit** result instead.

> `→ rules/03-keywords-glossary.md#strong`, `→ matches/coordinate-system.md §5` (base size), `→ rules/02-comprehensive-rules.md#injury-roll-table`

---

### Knights of Avarice

> *Warbands who follow the Prince of Greed call themselves the Knights of Avarice. ... In combat, they favour hammers and clubs that break bones but leave flesh and blood intact, alongside poison gas and highly accurate rifles. They scorn crude and destructive fire or explosive weapons that could damage any objects of value.*
> — Warbands p.120

```yaml
variant: knights-of-avarice
base_faction: heretic-legions
patron: Mammon
```

**Knights of Avarice Special Rules**:

- **Corrupt Merchants**: When you create your starting Warband, you can purchase **1 piece of Battlekit from the New Antioch Armoury**, and **1 piece of Battlekit from the Iron Sultanate Armoury**. Any stipulations that apply to it must still be followed (so there is little point in taking the Assassin's Dagger, for example, as it can only be used by Assassins). You can repurchase the Battlekit later during the campaign if it is lost for any reason.
- **Gas Bombs**: Artillery Witches in a Knights of Avarice Warband **replace** their Infernal Bombs with **Gas Bombs** (see [Gas Bombs](#gas-bombs) below).
- **Goetic Warlocks**: Goetic Warlocks are creations of Mammon. A Knights of Avarice Warband can include up to **2 Goetic Warlocks** as Mercenaries (v0.2+ Mercenaries). In addition, the **first** Goetic Warlock to be recruited in a Knights of Avarice Warband costs **110 👑 instead of its normal cost in ☼**.
  > **Errata clarification**: This rule's intent is to **allow the Warband to recruit two Goetic Warlocks** — the 👑 path does **not** block also recruiting one via ☼. `→ errata/rules-commentaries.md#heretic-legions-q1--knights-of-avarice-的-goetic-warlock-双重招募`
- **Infernal Rivalry**: Mammon is a rival of Beleth, who is the Patron of Death Commandos. A Knights of Avarice Warband **cannot include Death Commandos**.
- **Mammon's Chosen**: A Knights of Avarice Warband **cannot include a model if the cost of the model and its Battlekit is less than 80 👑**, unless the model is a Wretched.
- **Preserve the Loot**: Models in a Knights of Avarice Warband **cannot have Battlekit that has, or would give another piece of Battlekit, the `FIRE` and/or `SHRAPNEL` Keywords**. Grenade Launchers **can** be taken, but replace the `SHRAPNEL` Keyword with the `-1 INJURY DICE`, `GAS`, and `IGNORE ARMOUR` Keywords.
- **Price of Greed**: A Heretic Priest in a Knights of Avarice Warband has the following **Price of Greed ACTION instead of the Puppet Master ACTION**.
  - **Price of Greed ACTION**: Worldly wealth becomes the target of this curse, gradually crushing its victim under its weight. A Knights of Avarice Heretic Priest can take a Price of Greed ACTION. If they do so, take a Risky Success Roll for the model. If the roll is a Failure, the Knights of Avarice Heretic Priest's Activation ends immediately. If the roll is a Success or Critical Success, make an **Injury Roll** for an enemy model that is within **12"** of the model taking the Price of Greed ACTION and in its Line of Sight. Add `+1 INJURY DICE` to the roll if the Success Roll was a Critical Success, **and add `+1 INJURY DICE` to the roll for each `-1 INJURY MODIFIER` that applies to the target** (the `-1 INJURY MODIFIER` still applies). For example, if the target had Standard Armour with a `-1 INJURY MODIFIER`, you would add `+1 INJURY DICE` and a `-1 INJURY MODIFIER` to the roll.
- **Worship Mammon**: The Patron of a Knights of Avarice Warband is always **Mammon**.

#### Knights of Avarice Battlekit

##### Coin Hammer

> *This double-handed hammer bears the rune of Mammon on its head. Its strike burns through even the heaviest armour, leaving a permanent, painful scar in the shape of the rune.*

```yaml
weapon: coin-hammer
type: melee
hands: 2
range: melee
keywords: ["+1 INJURY DICE", HEAVY]
restrictions: Knights of Avarice variant only
limit: 2
cost: 20 👑
```

- **Rune of Mammon**: If the Injury Roll for an attack made by a Coin Hammer results in 1 or more `BLOOD MARKERS` being placed next to the target, place **1 BLESSING MARKER** next to the model using the Coin Hammer.

> `→ rules/03-keywords-glossary.md#heavy`, `→ rules/03-keywords-glossary.md#blood-marker`, `→ rules/03-keywords-glossary.md#blessing-marker`

##### Golden Calf Altar

> *This portable altar of Mammon creates illusions of immense wealth, taking the form of whatever its target covets most.*

```yaml
battlekit: golden-calf-altar
type: equipment
keywords: [DEPLOYABLE, HEAVY]
restrictions: Knights of Avarice variant only
limit: 3
cost: 20 👑
deployed_terrain:
  height_inches: 0.5
  base_mm: 25
  passability: impassable
```

A Golden Calf Altar, if deployed, is represented by a terrain piece that is about **½"** high and which is mounted on a **25mm base**. It is **Impassable terrain**.

- **Illusions**: Enemy models treat Open ground and all terrain within **3"** of a model with a Golden Calf Altar (or a Golden Calf Altar terrain piece) as being **Difficult terrain** (if it is not already), **even if they have the `FLYING` Keyword**.
- **Place Altar ACTION**: A model with a Golden Calf Altar can take a *Place Altar ACTION*. If they do so, deploy the Golden Calf Altar anywhere within **1"** of the model. Once deployed, the model that had the Golden Calf Altar is not considered to be carrying it for the rest of the game. In addition, the Golden Calf Altar is **lost at the end of the game** and removed from your Warband Roster.

> `→ rules/03-keywords-glossary.md#deployable`, `→ rules/03-keywords-glossary.md#heavy`, `→ rules/03-keywords-glossary.md#difficult-terrain`, `→ rules/03-keywords-glossary.md#flying`, `→ rules/03-keywords-glossary.md#impassable-terrain`, `→ matches/coordinate-system.md §7` (terrain model)

##### Gas Bombs

> *Artillery Witches in a Knights of Avarice Warband replace their Infernal Bombs with equally deadly Gas Bombs. Doing so ensures that valuable loot will not be damaged.*

```yaml
weapon: gas-bombs
type: ranged
hands: 1
range:
  max: 36              # inches; IGNORE LONG RANGE
keywords: ["-1 INJURY DICE", BLAST 3", GAS, IGNORE ARMOUR, IGNORE COVER, IGNORE ELEVATED POSITION, IGNORE LONG RANGE, RELOAD, SCATTER]
restrictions: Artillery Witch in Knights of Avarice variant only
cost: included with Artillery Witch
replaces: infernal-bomb
```

- **Choking Gas**: If a model that has been hit by a Gas Bomb is **not** taken Out of Action by the Injury Roll, it staggers **D3"** in a straight line trying to get away from the gas cloud. Roll separately for each model to see how far it staggers. If the model was the target of the attack, it staggers in a direction **chosen by the player making the attack**. If the model was caught in the Blast of the weapon, it staggers directly away from the target point. The model stops if it staggers into another model, Impassable terrain, or a terrain piece it cannot cross without having to Climb.

> `→ rules/03-keywords-glossary.md#blast-x`, `→ rules/03-keywords-glossary.md#gas`, `→ rules/03-keywords-glossary.md#ignore-armour`, `→ rules/03-keywords-glossary.md#ignore-modifier`, `→ rules/03-keywords-glossary.md#reload`, `→ rules/03-keywords-glossary.md#scatter`

##### Standard of Mammon

> *The Battle Standards of Mammon are opulently decorated works of art, icons and banners created in mockery of the virtues of Charity and Temperance.*

```yaml
battlekit: standard-of-mammon
type: equipment
keywords: [HELD, LEADER]
restrictions: Knights of Avarice variant only
limit: 1
cost: 25 👑
```

- **Kneel Before Me**: An enemy model that is **Down** and within **1"** of a model with the Standard of Mammon **cannot stand back up**. In addition, the opposing player must take a Success Roll for any of their models that **finish a charge within 1"** of a model with the Standard of Mammon. If the roll is a Failure, the enemy model is marked as being **Down**. If the roll is a Success or a Critical Success, the enemy model stays on its feet.

> `→ rules/03-keywords-glossary.md#held`, `→ rules/03-keywords-glossary.md#leader`

##### Tarnished Armour

> *This suit of armour, gilded with gleaming gold, comes with a helmet often adorned with a beautiful, cherub-like face, corrupted in some way with grotesque detailing such as inhuman eyes or a face twisted upside-down.*

```yaml
battlekit: tarnished-armour
type: armour
keywords: ["-2 INJURY MODIFIER", NEGATE GAS]
restrictions: Knights of Avarice variant only
limit: 1
cost: 25 👑
```

- **Target of Wrath**: An enemy model **must** choose a model that has Tarnished Armour as the target of the charge **if** the model is in its Line of Sight, **not already** within 1" of an enemy model, **and** can be reached without the charging model having to Climb, Jump, make a Diving Charge, or move across Dangerous terrain.

> `→ rules/03-keywords-glossary.md#negate-keyword`, `→ rules/03-keywords-glossary.md#gas`, `→ rules/03-keywords-glossary.md#dangerous-terrain`, `→ matches/coordinate-system.md §6` (LOS for charge legality)

---

### Heretic Naval Raiders

> *The Heretic fleet operates as a semi-autonomous entity under the command of its High Captain and other admirals. The Heretics have their own marine infantry, which often operate in small bands, striking deep behind enemy lines and executing smash-and-grab missions.*
> — Warbands p.124

```yaml
variant: heretic-naval-raiders
base_faction: heretic-legions
patron: null
```

**Heretic Naval Raiders Special Rules**:

- **Close Assault Weapons**: Submachine Guns cost **25 👑** for a Heretic Naval Raiders Warband (instead of 2 ☼).
- **Fast as Lightning**: Add `+1 DICE` to the Risky Success Roll for models from a Heretic Naval Raiders Warband that are taking a **Dash ACTION**.
- **Let Sleeping Dogs Lie**: This Warband **cannot include a War Wolf**.
- **Light Troops**: A Heretic Naval Raiders Warband **cannot have more than two Anointed models or more than 1 Artillery Witch** (even if the Warband has a value of 1,000 👑 or more).
- **Unseen Advance**: Up to **three models without the `ELITE` Keyword** in a Heretic Naval Raiders Warband can be given the `INFILTRATOR` Keyword at a cost of `+10 👑` each.

> Keywords / actions: `→ rules/03-keywords-glossary.md#elite`, `→ rules/03-keywords-glossary.md#infiltrator`, `→ rules/02-comprehensive-rules.md#dash-action`

---

## Base Size Summary

Models with `base_size != [1, 1]` (per `→ matches/coordinate-system.md §5`):

| Unit / variant rig                 | `base_size` | `base_shape` | `base_dimensions_mm` | Source                       |
| ---------------------------------- | :---------: | :----------: | :------------------: | ---------------------------- |
| War Wolf Assault Beast             |   `[2, 2]`  |    `oval`    |      `[50, 50]`      | PDF p.113 (50mm base)        |
| Heretic Priest w/ **Tank Palanquin** (Trench Ghosts) |   `[2, 2]`  |  `circle`   |      `[50, 50]`      | PDF p.119 ("must be mounted on a 50mm base") |

All other Heretic Legions models use the default `base_size: [1, 1]`. Their `base_shape: circle` and `base_dimensions_mm` are listed in each unit's yaml block (25mm for Troopers/Legionnaires/Wretched; 32mm for Elites, Anointed, Artillery Witch).

---

## Cross-References

- Distance / LOS / cover / terrain → `→ matches/coordinate-system.md` §3, §6, §7
- All-caps keywords (HERETIC, ELITE, TOUGH, FEAR, INFILTRATOR, ARTIFICIAL, STRONG, RISKY, CRITICAL, FIRE, CLEAVE (X), CUMBERSOME, BLAST (X), DEADLY, SHRAPNEL, SCATTER, RELOAD, GAS, IGNORE [MODIFIER], IGNORE ARMOUR, HELD, LEADER, HEAVY, DEPLOYABLE, DIFFICULT TERRAIN, IMPASSABLE TERRAIN, FLYING, BLOOD MARKER, BLESSING MARKER, NEGATE [KEYWORD]) → `→ rules/03-keywords-glossary.md`
- Standard battlekit (rifles, pistols, grenades, armour, gear referenced in Armoury Tables) → `→ rules/05-battlekit.md`
- Combat & actions (Charge, Dash, Fight, Shoot, Retreat, Off-Hand, Injury Roll Table, Morale, Climb/Jump, Falling, Elevated Position) → `→ rules/02-comprehensive-rules.md`
- Errata:
  - Heretic Legions Q1 (Knights of Avarice Goetic Warlock dual recruitment) → `→ errata/rules-commentaries.md#heretic-legions-q1--knights-of-avarice-的-goetic-warlock-双重招募`
  - Heretic Legions Q2 (Death Commando Stealth Generator vs Blast) → `→ errata/rules-commentaries.md#heretic-legions-q2--death-commando-的-stealth-generator-对-blast-的效力`
- Warband-specific shared keywords (if any) → `→ warbands/00-warband-keywords.md` (Pass 8 — may not yet exist; reference only)
