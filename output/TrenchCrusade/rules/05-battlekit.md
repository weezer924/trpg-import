# rules/05-battlekit: Battlekit (Weapons / Armour / Shields / Grenades / Equipment)

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.68-86
> 版本：v1.0.2
> 关键词定义详见：`rules/03-keywords-glossary.md`
> 距离 / Short-Long Range 语义：`matches/coordinate-system.md` §3.2

## Index

- [About This Chapter](#about-this-chapter)
- [General Rules](#general-rules)
  - [Battlekit Profile Fields](#battlekit-profile-fields)
  - [Weapon Dice & Injury Dice](#weapon-dice--injury-dice)
  - [Battlekit Limits](#battlekit-limits)
  - [Shields (carry restrictions)](#shields-carry-restrictions)
  - [Dual-Purpose Battlekit](#dual-purpose-battlekit)
  - [Two Hands, One Head and a Body](#two-hands-one-head-and-a-body)
- [Ranged Weapons](#ranged-weapons)
  - [Anti-Materiel Rifle](#anti-materiel-rifle)
  - [Automatic Pistol](#automatic-pistol)
  - [Automatic Rifle](#automatic-rifle)
  - [Automatic Shotgun](#automatic-shotgun)
  - [Blunderbuss](#blunderbuss)
  - [Bolt-Action Rifle](#bolt-action-rifle)
  - [Flamethrower](#flamethrower)
  - [Grenade Launcher](#grenade-launcher)
  - [Heavy Flamethrower](#heavy-flamethrower)
  - [Heavy Shotgun](#heavy-shotgun)
  - [Machine Gun](#machine-gun)
  - [Musket](#musket)
  - [Pistol](#pistol)
  - [Semi-Automatic Rifle](#semi-automatic-rifle)
  - [Shotgun](#shotgun)
  - [Silenced Pistol](#silenced-pistol)
  - [Sniper Rifle](#sniper-rifle)
  - [Submachine Gun](#submachine-gun)
- [Melee Weapons](#melee-weapons)
  - [Anti-Tank Hammer](#anti-tank-hammer)
  - [Bayonet](#bayonet)
  - [Flail/Scourge](#flailscourge)
  - [Great Hammer/Maul](#great-hammermaul)
  - [Great Sword/Axe](#great-swordaxe)
  - [Misericordia](#misericordia)
  - [Polearm](#polearm)
  - [Sword/Axe](#swordaxe)
  - [Trench Club](#trench-club)
  - [Trench Knife](#trench-knife)
- [Grenades](#grenades)
  - [Frag Grenades](#frag-grenades)
  - [Gas Grenades](#gas-grenades)
  - [Incendiary Grenades](#incendiary-grenades)
  - [Molotov Cocktail](#molotov-cocktail)
  - [Satchel Charge](#satchel-charge)
- [Shields](#shields)
  - [Trench Shield](#trench-shield)
- [Armour](#armour)
  - [Standard Armour](#standard-armour)
  - [Reinforced Armour](#reinforced-armour)
- [Equipment](#equipment)
  - [Armour-Piercing Bullets](#armour-piercing-bullets)
  - [Binoculars](#binoculars)
  - [Blessed Icon](#blessed-icon)
  - [Combat Helmet](#combat-helmet)
  - [Dum-Dum Bullets](#dum-dum-bullets)
  - [Field Shrine](#field-shrine)
  - [Gas Mask](#gas-mask)
  - [Hellbound Soul Contract](#hellbound-soul-contract)
  - [Holy Relic](#holy-relic)
  - [Incendiary Ammunition](#incendiary-ammunition)
  - [Infernal Brand](#infernal-brand)
  - [Martyrdom Pills](#martyrdom-pills)
  - [Medi-kit](#medi-kit)
  - [Mountaineer Kit](#mountaineer-kit)
  - [Musical Instrument](#musical-instrument)
  - [Shovel](#shovel)
  - [Tracer Bullets](#tracer-bullets)
  - [Troop Flag](#troop-flag)
  - [Unholy Relic](#unholy-relic)
  - [Unholy Trinket](#unholy-trinket)

---

## About This Chapter

This chapter catalogues all **common Battlekit** (装备/战具) defined in the core Digital Rulebook p.68-86 — the **shared library** of weapons, grenades, armour, shields and equipment available across Factions. Faction-exclusive Battlekit is documented in each `warbands/*.md`.

**Cost (👑) and Armoury Tier are intentionally omitted from YAML blocks** in this file, because the core Digital Rulebook lists no economic prices for the common Battlekit — costs are defined per-Faction inside the Warbands document (e.g. a Bolt-Action Rifle costs different ducats for New Antioch vs Heretic Legions, and each Faction has its own Armoury tier table). When MCP server consumes weapon yaml for **roster construction**, it must look up `cost` / `armoury_tier` from the relevant `warbands/*.md` armoury table for the model's Faction.

**Notation in this file**:

- `range.short` / `range.long`: in inches. PDF lists a single `Range` value = the **long range** (maximum). **Short range = long range ÷ 2** (PDF p.43 "half range"). See `matches/coordinate-system.md` §3.2.
- For Melee weapons, `range = "Melee"` (attacks against targets within 1", per PDF p.30).
- For Dual-purpose weapons (e.g. `12"/Melee`), both `range.long` (12) and a `melee: true` flag are set.
- `keywords`: ALL-CAPS keyword strings preserved verbatim from PDF. Numeric keyword parameters (e.g. `BLAST 2"`, `AUTOMATIC 2`, `BLESSED 1`) included in the string.
- `attacks` / `damage` fields from §3.3: Trench Crusade does **not** use those D&D-style fields. Attacks-per-activation derive from the `AUTOMATIC X` keyword (X attacks) and from each weapon's special rules. Damage is resolved by **Injury Roll** (PDF Comprehensive Rules), modified by `+N INJURY DICE` and `+N INJURY MODIFIER` keywords. The yaml therefore omits these two fields and reflects the actual TC mechanic in `keywords`.

---

## General Rules

> **Errata 裁决（BK Q1，为何不列 stipulation）**：本章及 `rules/07-glory-items.md`（Glory Items）**故意不列 stipulation 字段**（如 `ELITE only` / `Limit: X` 等）——这些 stipulation **由每个 Faction 的 Armoury Table 单独定义**，相同 Battlekit 在不同 Faction 下可能 stipulation 不同（例：Bolt-Action Rifle 在 New Antioch 有 Bayonet Lug，在 Heretic Legions 无此限）。stipulation 数据**位于 `warbands/*.md` 的 Armoury 章节**。（→ `errata/rules-commentaries.md` BK Q1）

### Battlekit Profile Fields

Each piece of Battlekit (PDF p.68) has:

- **Name**
- **Description** (lore)
- **Type**: `1-Handed` / `2-Handed` / `Grenade` / `Armour` / `Shield` / `Equipment` / `Special`
- **Range**:
  - Numeric value (e.g. `12"`) → **Ranged Weapon** (Ranged Attacks; → `rules/02-comprehensive-rules.md` Ranged Combat)
  - `Melee` → **Melee Weapon** (Melee Attacks against targets within 1"; → `rules/02-comprehensive-rules.md` Melee Combat)
  - `12"/Melee` → **Dual-purpose** (both Ranged and Melee)
  - `-` → cannot be used to make an attack
- **Keywords**:
  - Weapon Keywords (1-Handed / 2-Handed / Grenade): apply to attacks made by the model that has the weapon (ignore at all other times)
  - Armour & Shield Keywords: apply to Injury Rolls for the model that has the Armour and/or Shield (ignore at all other times)
  - Other Battlekit Keywords: added to the Keywords found on the model's Profile; apply all of the time unless stated otherwise
- **Special Rules**: where present, listed below the Profile.

### Weapon Dice & Injury Dice

> PDF p.69:
> If a Weapon has the `+/- DICE` Keyword, then the Keyword **only** applies to **Success Rolls** for attacks made by the weapon. It does not apply to any other sort of Success Roll, or to Injury Rolls.
> By the same token, if a Weapon has the `+/- INJURY DICE` Keyword, then the Keyword **only** applies to **Injury Rolls** for attacks made by the weapon. It does not apply to any other sort of Injury Roll, or to Success Rolls.

### Battlekit Limits

Unless otherwise stated a model is limited to:

- One 2-Handed Ranged Weapon **or** two 1-Handed Ranged Weapons.
- One 2-Handed Melee Weapon **or** two 1-Handed Melee Weapons.
- One **type** of Grenade.
- One suit of Armour.
- One Shield (see additional restrictions below).
- Any number of pieces of Equipment or Special Battlekit. A Model cannot have two or more pieces of Equipment or Special Battlekit with the same Name.

### Shields (carry restrictions)

A Shield requires one hand to carry and cannot be unequipped. As a result, if a model has a Shield:

- It may carry a maximum of **one 1-Handed Melee** and **one 1-Handed Ranged Weapon**.
- It cannot carry a 2-Handed Weapon **unless** the Weapon and the Shield both have the **Shield Combo** stipulation (→ see `warbands/`).

A Shield does **not** block Line of Sight to the model that is carrying it.

### Dual-Purpose Battlekit

A Dual-Purpose weapon (e.g. a Pistol) can be used as Ranged or Melee, but still only counts as a single 1-Handed (or 2-Handed) Weapon when totalling weapon slots.

### Two Hands, One Head and a Body

Unless otherwise stated, a model is assumed to have:

- Two hands to carry weapons and equipment.
- One head for wearing a helmet.
- One body that can be covered by armour.
- Enough belts, backpacks and pouches to carry Grenades and any other Equipment it possesses.

A model may freely switch between Ranged and Melee Weapons between ACTIONS, slinging unused weapons over the shoulder or stowing them in a holster or scabbard.

---

## Ranged Weapons

Ranged Weapons can be used to perform a **Ranged Attack** (→ `rules/02-comprehensive-rules.md` Ranged Combat). They cannot make Melee Attacks unless the Range entry includes "Melee".

### Anti-Materiel Rifle

```yaml
weapon: anti-materiel-rifle
type: ranged
hands: 2
range:
  short: 18
  long: 36
melee: false
keywords: ["+1 INJURY DICE", "CRITICAL", "HEAVY", "IGNORE ARMOUR"]
cost: null            # see warbands/{faction} armoury
armoury_tier: null    # see warbands/{faction} armoury
```

Enormous long rifles designed to take out heavily armoured targets, vehicles and strongpoints. With the powerful armour available to the armies of the Great War, these terrifying weapons are much in demand. A downside is their enormous weight and terrifying recoil — they are most often used by Communicants or Anointed who possess the supernatural strength to wield such weapons.

### Automatic Pistol

```yaml
weapon: automatic-pistol
type: ranged
hands: 1
range:
  short: 6
  long: 12
melee: true                  # 12"/Melee (dual-purpose)
keywords: ["ASSAULT", "AUTOMATIC 2", "PISTOL"]
cost: null
armoury_tier: null
```

Automatic pistols are symbols of prestige owing to their rarity and cost. They are excellent weapons when storming trenches or fighting in hand-to-hand combat. They boast a high rate of fire, though they can be hard to control even for the best sharpshooters since they usually lack a stock.

### Automatic Rifle

```yaml
weapon: automatic-rifle
type: ranged
hands: 2
range:
  short: 12
  long: 24
melee: false
keywords: ["ASSAULT", "AUTOMATIC 2"]
cost: null
armoury_tier: null
```

A marvel of modern engineering, only a few prototypes exist. It has a high rate of fire and can be quickly re-loaded.

- **Focused Fire**: When this Weapon is used to make 2 Ranged Attacks, the same enemy model must be the target of both attacks.

### Automatic Shotgun

```yaml
weapon: automatic-shotgun
type: ranged
hands: 2
range:
  short: 6
  long: 12
melee: false
keywords: ["+1 DICE", "ASSAULT", "SHOTGUN"]
cost: null
armoury_tier: null
```

This shotgun is equipped with an auto-loader, a recent invention by the Prussian engineering corps of Königsberg. It is ideal for close quarter combat thanks to its high rate of power and accuracy. The technology has not been perfected, however, and sometimes leads to misfeeds and jams.

### Blunderbuss

```yaml
weapon: blunderbuss
type: ranged
hands: 2
range:
  short: 5
  long: 10
melee: false
keywords: ["SHRAPNEL"]
cost: null
armoury_tier: null
```

A firearm of a bygone era, loaded with rusty nails, lead shot, grenade shrapnel and shell pieces.

### Bolt-Action Rifle

```yaml
weapon: bolt-action-rifle
type: ranged
hands: 2
range:
  short: 12
  long: 24
melee: false
keywords: []
cost: null
armoury_tier: null
```

The workhorse of the Great War. Sturdy, highly reliable and reasonably accurate — it is no surprise that most of the infantry of the Great War carry this battlefield classic.

### Flamethrower

```yaml
weapon: flamethrower
type: ranged
hands: 2
range:
  short: 4
  long: 8
melee: false
keywords: ["-1 INJURY DICE", "FIRE", "FLAMETHROWER", "IGNORE ARMOUR"]
cost: null
armoury_tier: null
```

A flamethrower is a terrifying Weapon capable of projecting great streams of fire and flammable liquids at a distance. It is ideal for clearing bunkers, trenches and other fortifications, killing in a most horrific way. Consequently, it is greatly favoured by the Heretic forces.

### Grenade Launcher

```yaml
weapon: grenade-launcher
type: ranged
hands: 2
range:
  short: 18
  long: 36
melee: false
keywords: ["BLAST 3\"", "HEAVY", "IGNORE COVER", "SHRAPNEL"]
cost: null
armoury_tier: null
```

Modifications of great siege rifles designed to lob grenades over long distances.

### Heavy Flamethrower

```yaml
weapon: heavy-flamethrower
type: ranged
hands: 2
range:
  short: 5
  long: 10
melee: false
keywords: ["-1 INJURY DICE", "AUTOMATIC 2", "FIRE", "FLAMETHROWER", "HEAVY", "IGNORE ARMOUR"]
cost: null
armoury_tier: null
```

These massive flamethrowers are normally mounted on armoured vehicles, but those possessing uncanny strength may use them as infantry weapons.

### Heavy Shotgun

```yaml
weapon: heavy-shotgun
type: ranged
hands: 2
range:
  short: 6
  long: 12
melee: false
keywords: ["+1 DICE", "+1 INJURY DICE", "HEAVY", "SHOTGUN"]
cost: null
armoury_tier: null
```

This massive 8 bore shotgun is used to take down extremely powerful and large opponents at short range. It is known as a "Wolf-Killer" in New Antioch as it is the weapon favoured by the soldiery of the Duke to take down the Heretic War Wolf Assault Beasts. Heavy shotguns use tungsten-orichalcum alloy shot which explains their enormous stopping power at short ranges.

- **Tungsten-orichalcum Alloy Shot**: Add `+1 INJURY DICE` to rolls for Ranged Attacks made by this Weapon at **Short Range**.

### Machine Gun

```yaml
weapon: machine-gun
type: ranged
hands: 2
range:
  short: 18
  long: 36
melee: false
keywords: ["AUTOMATIC 3", "HEAVY", "RELOAD"]
cost: null
armoury_tier: null
```

Machine guns are lethal fully-automatic firearms, capable of mowing down entire ranks of infantry from afar. The firing rate depends on the lock assembly used but averages 500 rounds per minute.

### Musket

```yaml
weapon: musket
type: ranged
hands: 2
range:
  short: 9
  long: 18
melee: false
keywords: ["-1 INJURY DICE"]
cost: null
armoury_tier: null
```

A primitive weapon from a bygone age, the musket is a smooth bore long rifle that shoots lead balls. It still sees widespread use due to its simple construction and low price.

### Pistol

```yaml
weapon: pistol
type: ranged
hands: 1
range:
  short: 6
  long: 12
melee: true                  # 12"/Melee (dual-purpose)
keywords: ["PISTOL"]
cost: null
armoury_tier: null
```

Pistols come in a staggering variety, ranging from revolvers to semi-automatic pistols. Heretic forges produce their own, often highly elaborate sidearms. They see extensive use in close-quarter combat.

### Semi-Automatic Rifle

```yaml
weapon: semi-automatic-rifle
type: ranged
hands: 2
range:
  short: 12
  long: 24
melee: false
keywords: ["ASSAULT"]
cost: null
armoury_tier: null
```

Semi-automatic rifles are said to be an invention of Marbas, the Devil who holds great wisdom and knowledge in mechanical arts. They are excellent both at long range and in assault, combining accuracy and high rate of fire, though they are prone to jamming.

### Shotgun

```yaml
weapon: shotgun
type: ranged
hands: 2
range:
  short: 6
  long: 12
melee: false
keywords: ["+1 DICE", "SHOTGUN"]
cost: null
armoury_tier: null
```

Short-barrelled pump action shotgun loaded with six rounds containing antimony hardened 00 buckshot, the combat shotgun is ideal for short-range engagements, clearing trenches and taking out lightly-armoured infantry. Often featuring stocks made of walnut or other rare wood, it is a custom of the troops to decorate these arms with carvings and inscriptions.

> **PDF marker**: `PW` (Prussian / Westfalia source flag — present in PDF margin).

### Silenced Pistol

```yaml
weapon: silenced-pistol
type: ranged
hands: 1
range:
  short: 6
  long: 12
melee: true                  # 12"/Melee (dual-purpose)
keywords: ["ASSAULT", "PISTOL"]
cost: null
armoury_tier: null
```

A sophisticated sidearm made of orichalcum or other holy metals, or from Infernal iron taken from the very prisons of Hell to muffle the wails of the damned. It is virtually silent and is excellent for ambushes or for shooting from behind cover.

- **Silent**: Add `+1 DICE` to the roll if the attacker is in contact with a terrain piece that is at least ½" tall and that lies in between it and the target model.

### Sniper Rifle

```yaml
weapon: sniper-rifle
type: ranged
hands: 2
range:
  short: 24
  long: 48
melee: false
keywords: ["+1 DICE", "CRITICAL", "RISKY"]
cost: null
armoury_tier: null
```

A sniper rifle is a high-precision, long-range rifle, widely used in the trenches to pick off high value targets such as officers, sappers and artillery crews. Expensive and rare, they are commonly given to the best marksmen and sharpshooters of the warband.

- **Bull's Eye**: If the Success Roll for a Ranged Attack made with a Sniper Rifle is a **Critical Success** then the Injury Roll for the attack has the `IGNORE ARMOUR` Keyword.

### Submachine Gun

```yaml
weapon: submachine-gun
type: ranged
hands: 2
range:
  short: 8
  long: 16
melee: false
keywords: ["ASSAULT"]
cost: null
armoury_tier: null
```

The submachine gun (or SMG) is a fully automatic firearm, trading lower penetration power and range for a much higher rate of fire. Ideal for short-range engagements, it is much sought-after by warbands despite its scarcity and high cost.

- **Quick Bursts**: A model armed with a Submachine Gun can take **two Shoot ACTIONS** during the same Activation, as long as the Submachine Gun is used to make both attacks. The Shoot ACTIONS can be taken one after the other, or other ACTIONS can be taken between the Shoot ACTIONS.

---

## Melee Weapons

Melee Weapons can be used to perform a **Melee Attack** (→ `rules/02-comprehensive-rules.md` Melee Combat). They cannot make Ranged Attacks unless a numeric range is listed.

### Anti-Tank Hammer

```yaml
weapon: anti-tank-hammer
type: melee
hands: 2
range: melee
keywords: ["+1 INJURY DICE", "CRITICAL", "IGNORE ARMOUR", "RISKY"]
cost: null
armoury_tier: null
```

A polearm with a directional explosive mounted on its head. It is exceedingly good at taking out armoured targets but puts its user in grave danger.

- **Dangerous**: Place 1 `BLOOD MARKER` next to the model using this Weapon if it makes a Melee Attack and the Success Roll is a Success or a Critical Success.

### Bayonet

```yaml
weapon: bayonet
type: melee
hands: 2
range: melee
keywords: ["CUMBERSOME"]
cost: null
armoury_tier: null
```

Bayonets are blades in the form of spikes or daggers that can be fixed to the tip of a firearm and used in melee combat.

> **PDF marker**: `PW` (Prussian / Westfalia source flag).

### Flail/Scourge

```yaml
weapon: flail-scourge
type: melee
hands: 1
range: melee
keywords: ["+1 DICE"]
cost: null
armoury_tier: null
```

The metal whips of the Church are supremely good at both instilling discipline in the ranks of the faithful and tormenting the heretics. Many devils also enjoy using these weapons due to the excruciating pain they inflict. These weapons are extremely difficult to dodge.

- **Unwieldy**: The `+1 DICE` Keyword does **not** apply when this Weapon is used as an **Off-Hand Weapon**.

### Great Hammer/Maul

```yaml
weapon: great-hammer-maul
type: melee
hands: 2
range: melee
keywords: ["+1 INJURY MODIFIER", "HEAVY"]
cost: null
armoury_tier: null
```

These are large, cumbersome weapons, often made from sturdy wood with a metal tip of steel, lead or iron of Tartarus. It takes great strength to fight with it for any length of time. They are especially suited for attacking armoured targets.

### Great Sword/Axe

```yaml
weapon: great-sword-axe
type: melee
hands: 2
range: melee
keywords: ["+1 INJURY DICE", "CRITICAL", "HEAVY"]
cost: null
armoury_tier: null
```

Claymores, Zweihänders and even huge battle axes are used in the trenches when bullets fail to stop quick or well-armoured targets. The strikes from these weapons can easily lop off limbs and heads.

### Misericordia

```yaml
weapon: misericordia
type: melee
hands: 1
range: melee
keywords: []
cost: null
armoury_tier: null
```

The misericordia dagger is designed to put enemies out of their misery by finding chinks in the armour: eye slits, neck joints and every other vulnerable seam.

- **Despatch**: This weapon has the `IGNORE ARMOUR` Keyword if the target is **Down**.

### Polearm

```yaml
weapon: polearm
type: melee
hands: 2
range: melee
keywords: ["BLOCK", "CUMBERSOME"]
cost: null
armoury_tier: null
```

Trench pikes, billhooks, spears and other long polearms are excellent defensive weapons, but are cumbersome and heavy.

### Sword/Axe

```yaml
weapon: sword-axe
type: melee
hands: 1
range: melee
keywords: ["CRITICAL"]
cost: null
armoury_tier: null
```

Because of the martial traditions of many proud nations and due to the advances in armour technology, swords and axes are extremely popular, especially amongst elite units and officers. They are supremely useful for finishing off downed opponents and causing profusely bleeding wounds.

### Trench Club

```yaml
weapon: trench-club
type: melee
hands: 1
range: melee
keywords: []
cost: null
armoury_tier: null
```

Trench Clubs are one of the most common weapons of the Great War, as melee combat is frequent and brutal. Usually made of wood with a metal tip from iron, lead or steel, trench clubs often feature spikes and hobnails. Most designs have some form of cord or leather strap at the end to wrap around the user's wrist.

### Trench Knife

```yaml
weapon: trench-knife
type: melee
hands: 1
range: melee
keywords: ["-1 DICE"]
cost: null
armoury_tier: null
```

Virtually all soldiers carry a trench knife, dagger or other kind of blade for close quarter engagements. It may lack the devastating power of a great maul or other heavier melee weapons, but this humble weapon has taken countless lives during the Great War.

---

## Grenades

Grenades have a Range and can be used to perform a **Ranged Attack** even though they are not specifically a Ranged Weapon (→ `rules/02-comprehensive-rules.md` Ranged Combat / Grenades). They do **not** count towards the number of Ranged Weapons a model can have, and a model is assumed to be carrying enough to be able to use them every Turn.

### Frag Grenades

```yaml
weapon: frag-grenades
type: grenade
hands: 1
range:
  short: 4
  long: 8
melee: false
keywords: ["ASSAULT", "BLAST 2\"", "IGNORE COVER", "IGNORE LONG RANGE", "SHRAPNEL"]
cost: null
armoury_tier: null
```

Fragmentation grenades or hand bombs are a staple of trench warfare. Usually referred to as frag grenades, they can kill the enemy underground or behind cover. They can also force the enemy into the open, providing targets for rifle and machine gun fire.

### Gas Grenades

```yaml
weapon: gas-grenades
type: grenade
hands: 1
range:
  short: 4
  long: 8
melee: false
keywords: ["-1 INJURY DICE", "ASSAULT", "BLAST 3\"", "GAS", "IGNORE ARMOUR", "IGNORE COVER", "IGNORE LONG RANGE"]
cost: null
armoury_tier: null
```

Gas grenades are insidious weapons, attacking the lungs and other internal organs with noxious fumes. Devil alchemists of the Fifth Circle are especially clever in creating these fiendish and hated weapons.

### Incendiary Grenades

```yaml
weapon: incendiary-grenades
type: grenade
hands: 1
range:
  short: 4
  long: 8
melee: false
keywords: ["ASSAULT", "FIRE", "IGNORE COVER", "IGNORE LONG RANGE"]
cost: null
armoury_tier: null
```

Incendiary grenades can set their target alight with sulphur, phosphorous or flammable gas captured from the Lake of Fire in the Seventh Circle of Hell.

- **Liquid Fire**: If the Success Roll for a Ranged Attack made with an Incendiary Grenade is a **Critical Success** then the Injury Roll for the attack has the `IGNORE ARMOUR` Keyword.

### Molotov Cocktail

```yaml
weapon: molotov-cocktail
type: grenade
hands: 1
range:
  short: 3
  long: 6
melee: false
keywords: ["-1 INJURY DICE", "ASSAULT", "FIRE", "IGNORE COVER", "IGNORE LONG RANGE"]
cost: null
armoury_tier: null
```

Developed on the desperate Finnish battle frontier against ice demons, this improvised weapon consists of a glass bottle containing a flammable substance such as gasoline, alcohol or a napalm-like mixture plus a source of ignition.

- **Liquid Fire**: If the Success Roll for a Ranged Attack made with a Molotov Cocktail is a **Critical Success** then the Injury Roll for the attack has the `IGNORE ARMOUR` Keyword.

### Satchel Charge

```yaml
weapon: satchel-charge
type: grenade
hands: 2
range:
  short: 3
  long: 6
melee: false
keywords: ["+1 INJURY DICE", "BLAST 3\"", "CONSUMABLE", "HEAVY", "IGNORE ARMOUR", "IGNORE COVER", "SCATTER"]
cost: null
armoury_tier: null
```

Battlefield explosives designed to break apart enemy fortifications and to crack even the toughest of armour.

- **Heavy Explosive**: **Once during a game**, a model with a Satchel Charge can use it to make a Ranged Attack.

> **PDF marker**: `PW` (Prussian / Westfalia source flag).

---

## Shields

Keywords for Shields only apply to **Injury Rolls** for the model that is using the Shield (ignore them at all other times). The effect of a Shield can be combined with the effect of a suit of Armour unless noted otherwise. A Shield does **not** block Line of Sight to the model that is carrying it.

### Trench Shield

```yaml
battlekit: trench-shield
type: shield
hands: 1
range: none
keywords: ["-1 INJURY MODIFIER"]
cost: null
armoury_tier: null
```

Shields used in trench warfare are made of steel reinforced with orichalcum to allow them to withstand even high-calibre bullets, or from metal mined from Infernal bedrock and shaped in the armouries of Pandemonium, the capital of Hell.

---

## Armour

Keywords for Armour only apply to **Injury Rolls** for the model that is wearing the Armour (ignore them at all other times).

> **PDF p.80 caveat**: Sometimes the INJURY MODIFIER for Armour or a Shield is listed in the Injury Modifiers Table in the Core Rules and is repeated for completeness in the Profile for the Armour or Shield as well. When this is the case, be careful **not to apply the modifier more than once**.

### Standard Armour

```yaml
battlekit: standard-armour
type: armour
range: none
keywords: ["-1 INJURY MODIFIER"]
cost: null
armoury_tier: null
```

With the advancements in metallurgy and technology, both Faithful and Heretic armies are well-equipped with suits of alloy armour that can withstand an impact from a bullet or turn aside the sharpest of blades. Standard armour is usually mass-produced, but highly effective even against high-calibre weapons.

### Reinforced Armour

```yaml
battlekit: reinforced-armour
type: armour
range: none
keywords: ["-2 INJURY MODIFIER"]
cost: null
armoury_tier: null
```

Reinforced armour is a master-crafted suit made individually for the most important and elite troops. Each one is richly decorated and often carries the personal device of the warrior who wears it.

> **Note**: PDF p.68-86 lists only **Standard Armour** and **Reinforced Armour** as common Armour. Faction-specific suits such as **Machine Armour** (per the import guide §3.7 / §H) are defined in `warbands/*.md` (e.g. New Antioch Anchorite Shrine / mechanized units).

---

## Equipment

Unless noted otherwise a model can have any number of pieces of Equipment, but **cannot have the same piece of Equipment more than once**. For example, a model could have an Iron Capirote and a Medi-kit, but could not have two Iron Capirotes or two Medi-kits.

### Armour-Piercing Bullets

```yaml
battlekit: armour-piercing-bullets
type: equipment
range: none
keywords: ["AMMUNITION (ARMOUR-PIERCING)", "CONSUMABLE"]
cost: null
armoury_tier: null
```

Advanced armour technology has forced the armouries of the Great War to forge new types of bullets. Expensive and labour-intensive to produce, these hardened tungsten rounds are more effective against battlefield armour.

### Binoculars

```yaml
battlekit: binoculars
type: equipment
range: none
keywords: []
cost: null
armoury_tier: null
```

It is quite common for officers to carry finely-crafted battlefield binoculars to survey the land ahead, spot hidden enemy troops and observe any sign of movement.

- **Survey the Land**: Enemy models cannot use the `INFILTRATOR` Keyword to deploy within 16" of a model with this Keyword unless they are in their own side's deployment zone.

### Blessed Icon

```yaml
battlekit: blessed-icon
type: equipment
range: none
keywords: ["CONSUMABLE"]
cost: null
armoury_tier: null
```

Small icons of saints, great angels and holy warriors are a common sight amongst the Trench Pilgrims. They are hung on rosaries, belts, or attached to portable shrines carried on the Pilgrims' backs.

- **Talisman**: **Once during a game**, when a Risky Success Roll for a model with a Blessed Icon is a Failure, you can say that the model will use its Talisman. If you do, the model's Activation does not end.

### Combat Helmet

```yaml
battlekit: combat-helmet
type: equipment
range: none
keywords: ["NEGATE SHRAPNEL"]
cost: null
armoury_tier: null
```

The simple combat helmet has proven its value on the battlefield time and again.

### Dum-Dum Bullets

```yaml
battlekit: dum-dum-bullets
type: equipment
range: none
keywords: ["AMMUNITION (CRITICAL)", "CONSUMABLE"]
cost: null
armoury_tier: null
```

These hollow-point bullets are far more likely to cause fatal wounds than standard ammunition.

### Field Shrine

```yaml
battlekit: field-shrine
type: equipment
range: none
keywords: ["DEPLOYABLE"]
cost: null
armoury_tier: null
```

Holy reliquaries, blessed artefacts and sacred crosses are often carried to the battlefield to encourage the troops, while the Heretics bring idols of the Golden Calf, tortured captives or other wicked totems to bear.

A Field Shrine is represented by a terrain piece that is **at least ½" high** and which is mounted on a **40mm base**. It is **Impassable** terrain.

- **Site of Worship**: After you deploy a model that has Field Shrine, you can also deploy their Field Shrine anywhere wholly within their deployment zone. In the **Morale Phase**, each friendly Field Shrine on the battlefield adds **3** to the number of models you have in your Warband that are not Down or Out of Action, up to a maximum bonus of **9 extra models**. Once deployed, the model that had the Field Shrine is **not** considered to be carrying it for the rest of the game.
- **Tear It Down!**: Models can attack a Field Shrine as if it were an enemy model. If it is hit by an attack or is in the blast radius of an attack made with a Weapon that has the `BLAST` Keyword, it is removed from the battlefield and is removed from the Warband Roster (no Injury Roll is required).

### Gas Mask

```yaml
battlekit: gas-mask
type: equipment
range: none
keywords: ["NEGATE GAS"]
cost: null
armoury_tier: null
```

Mustard gas, phosgene, chlorine as well as noxious fumes from the bolgias of Hell plague the battlefield. The gas mask allows soldiers to withstand such attacks.

### Hellbound Soul Contract

```yaml
battlekit: hellbound-soul-contract
type: equipment
range: none
keywords: []
cost: null
armoury_tier: null
```

An infernal contract signed by a Heretic and the demon who will come to collect the damned soul when death is close. The mortal signatory bursts into Infernal flames when seriously wounded.

- **Fiery Exodus**: If a model with a Hellbound Soul Contract is taken **Out of Action**, before removing it from the battlefield add **1 `BLOOD MARKER`** to each enemy model that is within 1" of it. Models that have the `NEGATE FIRE` Keyword are **not** affected by this special rule.

### Holy Relic

```yaml
battlekit: holy-relic
type: equipment
range: none
keywords: ["BLESSED 1"]
cost: null
armoury_tier: null
```

Due to the threat to all Creation, the churches, cathedrals and basilicas have emptied their reliquaries and distributed their relics to the frontline troops to aid them in their battle against the damned.

### Incendiary Ammunition

```yaml
battlekit: incendiary-ammunition
type: equipment
range: none
keywords: ["AMMUNITION (FIRE)", "CONSUMABLE"]
cost: null
armoury_tier: null
```

Developed by Aym, the great duke of Hell, these bullets set any target they hit on fire.

### Infernal Brand

```yaml
battlekit: infernal-brand
type: equipment
range: none
keywords: ["NEGATE FIRE"]
cost: null
armoury_tier: null
```

A Heretic who has made a holy pilgrimage into Hell itself is branded by their patron devil with an ever-burning mark. Mortal fire no longer has the power to harm them.

### Martyrdom Pills

```yaml
battlekit: martyrdom-pills
type: equipment
range: none
keywords: ["CONSUMABLE"]
cost: null
armoury_tier: null
```

Martyrdom pills are a potent mixture of mind-altering drugs and chemicals that inure a soldier against all pain and injury. However, it takes a tremendous toll on the body.

- **Inured to Pain**: When you deploy a model that has Martyrdom Pills you can say that they will consume them. If you do so, until the end of the game the model has the `NEGATE FEAR` Keyword. In addition, add `-1 INJURY DICE` to rolls for attacks that hit the model.

### Medi-kit

```yaml
battlekit: medi-kit
type: equipment
range: none
keywords: []
cost: null
armoury_tier: null
```

Battlefield first aid has brought many soldiers back from the brink of death. Blessed ointments can seal fatal wounds completely, while the black blood of demons used by twisted Heretic medics allows mangled troops to return to the fray.

- **Treat ACTION**: A model with this Keyword can take a **Treat ACTION**. If it does so, take a **Risky Success Roll** for the model. If the roll is a Failure, the model's Activation ends immediately. If it is a Success or a Critical Success, you can do **one** of the following:
  - Remove 1 `BLOOD MARKER` from the model or a friendly model within 1" of the model.
  - Stand up a friendly model that is **Down** and within 1" of the model.

### Mountaineer Kit

```yaml
battlekit: mountaineer-kit
type: equipment
range: none
keywords: []
cost: null
armoury_tier: null
```

This kit includes ropes, carabiners, slings, mountaineering harness and pitons to aid a soldier in overcoming almost any vertical obstacle.

- **Ropes and Pitons**: Add `+1 DICE` to Risky Success Rolls for friendly models with this special rule that are attempting to climb a sheer surface.

### Musical Instrument

```yaml
battlekit: musical-instrument
type: equipment
range: none
keywords: ["HELD"]
cost: null
armoury_tier: null
```

Horns, drums, trumpets, whistles, bagpipes and many other types of instruments are used extensively in the battles of the Great War. They can bolster the hearts of those facing the horrors of Hell, or they can recite terrifying hymns praising the lords of the Inferno!

- **Fanfare**: Add `+1 DICE` to Risky Success Rolls for friendly models that are taking a **Dash ACTION** and are within 4" of one or more models with a Musical Instrument.

### Shovel

```yaml
battlekit: shovel
type: equipment
range: none
keywords: []
cost: null
armoury_tier: null
```

Battlefield shovels allow troops to dig in and fight from cover in virtually any battlefield.

- **Dug In**: A model equipped with a Shovel that starts the game on **Open terrain** has the `COVER` Keyword until it moves away from its starting position. In addition, a model equipped with a Shovel can use it as a **2-Handed Melee Weapon** instead of using any other Melee Weapons it has.

> **Errata 裁决（BK Q2，STRONG + Shovel 单手化）**：拥有 `STRONG` 关键词的模型**仍不能**将 Shovel 当作 1-Handed Melee Weapon——`STRONG` 允许把 2H Weapon 当 1H 使用的优惠**不适用于** Shovel，因为 Shovel 的"2H Melee Weapon"形态是 *Dug In* 特殊规则赋予的替代用法，并非武器本身的标称类型。Shovel 在槽位规则中始终按 Equipment 计。（→ `errata/rules-commentaries.md` BK Q2）

### Tracer Bullets

```yaml
battlekit: tracer-bullets
type: equipment
range: none
keywords: ["AMMUNITION (+1 DICE)", "CONSUMABLE"]
cost: null
armoury_tier: null
```

Tracer bullets allow soldiers to adjust their aim efficiently.

### Troop Flag

```yaml
battlekit: troop-flag
type: equipment
range: none
keywords: ["LEADER", "HELD"]
cost: null
armoury_tier: null
```

Most warbands and units carry banners, flags, standards, pennants or other symbols to rally the troops.

### Unholy Relic

```yaml
battlekit: unholy-relic
type: equipment
range: none
keywords: ["FEAR"]
cost: null
armoury_tier: null
```

An artefact bestowed with unholy power. Examples include nephilim heads, desecrated splinters of the True Cross or mummified body parts of fallen saints and bishops.

### Unholy Trinket

```yaml
battlekit: unholy-trinket
type: equipment
range: none
keywords: ["CONSUMABLE"]
cost: null
armoury_tier: null
```

Many Heretic Troopers carry a talisman or charm that are sold by soothsayers and imps in the Heretic domains. Such a trinket might be a skull, preserved foetus, horn of a goat, and is often covered in Goetic runes.

- **Talisman**: **Once during a game**, when a Risky Success Roll for a model with an Unholy Trinket is a Failure, you can say that the model will use it. If you do, the model's Activation does not end.

> **PDF marker**: `GD` (Great Hunger source flag — present in PDF margin near Unholy Trinket entry).
