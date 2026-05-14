# rules/07-glory-items: Glory Items

> 源：`Rule Books/Trench Crusade/Trench Crusade - Digital Rulebook v1.0.2.pdf` p.125-143
> 版本：v1.0.2
> 范围：Glory Items 完整表（战役装备）——战团用 ☼ (Glory Points) 兑换。
> 关联章节：`rules/06-campaign-rules.md` §2 Glory Points（获取规则）+ §7 Quartermaster Step（兑换流程）。
> 关键词定义：`rules/03-keywords-glossary.md`。
> 距离 / Short-Long Range 语义：`matches/coordinate-system.md` §3.2。
>
> **v0.1 单场对战不需要 Glory Items**——本文件仅供战役（campaign）模式使用。

## Index

- [About This Chapter](#about-this-chapter)
- [Glory Item Tables (by Faction)](#glory-item-tables-by-faction)
  - [Principality of New Antioch](#principality-of-new-antioch)
  - [Trench Pilgrims](#trench-pilgrims)
  - [Sultanate of the Iron Wall](#sultanate-of-the-iron-wall)
  - [Heretic Legions](#heretic-legions)
  - [Cult of the Black Grail](#cult-of-the-black-grail)
  - [Court of the Seven-Headed Serpent](#court-of-the-seven-headed-serpent)
- [Glory Item Cartulary](#glory-item-cartulary)
  - [Armour of Cobar](#armour-of-cobar)
  - [Armour of the Fly](#armour-of-the-fly)
  - [Battlefield Title](#battlefield-title)
  - [Beelzebub's Embrace](#beelzebubs-embrace)
  - [Bestial Skin Cloak](#bestial-skin-cloak)
  - [Book of Battle Prayers](#book-of-battle-prayers)
  - [Cruel Helmet](#cruel-helmet)
  - [Cup of Filth](#cup-of-filth)
  - [Damascus Armour](#damascus-armour)
  - [Demonic Aura Grenade](#demonic-aura-grenade)
  - [Donkey's Jawbone](#donkeys-jawbone)
  - [Ducal Winged Armour](#ducal-winged-armour)
  - [Executioner's Axe](#executioners-axe)
  - [Field Hospital](#field-hospital)
  - [Great Banner of New Antioch](#great-banner-of-new-antioch)
  - [Holy Grenade](#holy-grenade)
  - [Horn of Joshua](#horn-of-joshua)
  - [Kilij](#kilij)
  - [Knighthood](#knighthood)
  - [Koraktor, the Great Tome of Hell](#koraktor-the-great-tome-of-hell)
  - [Locust Spitter](#locust-spitter)
  - [Lordship of This World](#lordship-of-this-world)
  - [Masterwork Jezzail](#masterwork-jezzail)
  - [Mobile Sultanate Grand Cannon](#mobile-sultanate-grand-cannon)
  - [Piece of Silver](#piece-of-silver)
  - [Restraining Muzzle](#restraining-muzzle)
  - [Resurrection Engine](#resurrection-engine)
  - [Rocket-Propelled Grenade](#rocket-propelled-grenade)
  - [Salvage Golem](#salvage-golem)
  - [Smokescreen](#smokescreen)
  - [Sniper Scope](#sniper-scope)
  - [The Mark of Cain](#the-mark-of-cain)
  - [Tormentor Chain](#tormentor-chain)
  - [Trench Dog](#trench-dog)

---

## About This Chapter

This chapter catalogues all **Glory Items**（晋升装备）defined in the core Digital Rulebook **p.125-143** — Battlekit-like items that can **only** be acquired during a campaign, using ☼ (Glory Points) earned from games and Exploration discoveries. They are listed per-Faction in a Glory Item Table, then described once each in the **Glory Item Cartulary** (PDF p.128-143).

**Acquisition rules** (PDF p.125):

- Purchasable **only** during a campaign.
- Either taken for free from an Exploration discovery, or purchased in the **Quartermaster Step** (→ `rules/06-campaign-rules.md` §7).
- Some discoveries cap the Glory Item cost (e.g. **Trench Merchant** on the Common Exploration Locations Table allows purchase of Glory Items costing **5 ☼ or less**).

**Stipulations** (e.g. `ELITE only`, `Limit: 1`) work exactly as they do in a Faction's Armoury Table (→ `warbands/*.md`).

**Notation in this file**:

- Each Glory Item gets one YAML block (structured for MCP roster validation) followed by lore + special-rule prose.
- `cost_glory` is the standard ☼ price from the Faction's Glory Item Table. When a single item appears in **multiple Faction tables** at the **same** cost, a single value is recorded; if costs differ across Factions, the table-side cost is used (this never happens in v1.0.2).
- `factions` lists every Faction whose table contains this item. A Glory Item can only be taken if the Warband's Faction appears in this list.
- `stipulation` carries the per-Faction selectors (e.g. `ELITE only`, `Brazen Bull only`, `Wretched only, Headgear`).
- `limit` records the per-Warband cap. For Trench Dog and Restraining Muzzle the cap varies by Faction — see the per-Faction table below.
- Numeric Keyword parameters (e.g. `BLAST 3"`, `CLEAVE 2`, `BLESSED 1`) are preserved verbatim in the `keywords` list.

---

## Glory Item Tables (by Faction)

The tables below mirror PDF p.125-127. Each row gives the item name + per-Faction stipulation/limit + cost in ☼. Full rules live in the **Cartulary** below.

### Principality of New Antioch

PDF p.125.

| Glory Item                  | Stipulation                                       | Cost  |
| --------------------------- | ------------------------------------------------- | ----: |
| Battlefield Title           | `ELITE only`, Limit: 1                            |  5 ☼ |
| Book of Battle Prayers      | `ELITE only`, Limit: 1                            |  7 ☼ |
| Ducal Winged Armour         | Battlefield Title or Knighthood only, Limit: 1 ¹ |  8 ☼ |
| Field Hospital              | Limit: 1                                          | 10 ☼ |
| Great Banner of New Antioch | Limit: 1                                          | 12 ☼ |
| Knighthood                  | `ELITE only`, Limit: 1                            |  4 ☼ |
| Resurrection Engine         | Consumable, Limit: 1                              | 11 ☼ |
| Rocket-Propelled Grenade    | Consumable, Limit: 2                              |  2 ☼ |
| Salvage Golem               | Limit: 1                                          |  4 ☼ |
| Smokescreen                 | Consumable, Limit: 1                              |  5 ☼ |
| Sniper Scope                | Limit: 2                                          |  2 ☼ |
| Trench Dog                  | Limit: 1                                          | 1-3 ☼ |

¹ Only a model that **already** has a Battlefield Title or a Knighthood can have Ducal Winged Armour.

### Trench Pilgrims

PDF p.126.

| Glory Item               | Stipulation                | Cost  |
| ------------------------ | -------------------------- | ----: |
| Donkey's Jawbone         | `ELITE only`, Limit: 1     |  4 ☼ |
| Holy Grenade             | Limit: 3                   |  2 ☼ |
| Horn of Joshua           | Limit: 1                   |  9 ☼ |
| Rocket-Propelled Grenade | Consumable, Limit: 1       |  2 ☼ |
| Trench Dog               | Limit: 1                   | 1-3 ☼ |

### Sultanate of the Iron Wall

PDF p.126.

| Glory Item                    | Stipulation                | Cost  |
| ----------------------------- | -------------------------- | ----: |
| Damascus Armour               | `ELITE only`, Limit: 1     |  5 ☼ |
| Field Hospital                | Limit: 1                   | 10 ☼ |
| Kilij                         | `ELITE only`, Limit: 2     |  2 ☼ |
| Knighthood                    | `ELITE only`, Limit: 1     |  4 ☼ |
| Masterwork Jezzail            | `ELITE only`, Limit: 1     |  4 ☼ |
| Rocket-Propelled Grenade      | Consumable, Limit: 2       |  2 ☼ |
| Sniper Scope                  | Limit: 2                   |  2 ☼ |
| Mobile Sultanate Grand Cannon | Brazen Bull only, Limit: 1 | 10 ☼ |
| Trench Dog                    | Limit: 1                   | 1-3 ☼ |

### Heretic Legions

PDF p.126.

| Glory Item               | Stipulation                | Cost  |
| ------------------------ | -------------------------- | ----: |
| Armour of Cobar          | `ELITE only`, Limit: 1     |  8 ☼ |
| Battlefield Title        | `ELITE only`, Limit: 1     |  5 ☼ |
| Demonic Aura Grenade     | Limit: 1                   |  3 ☼ |
| Executioner's Axe        | Limit: 1                   |  6 ☼ |
| Knighthood               | `ELITE only`, Limit: 1     |  4 ☼ |
| Rocket-Propelled Grenade | Consumable, Limit: 1       |  2 ☼ |
| Sniper Scope             | Limit: 2                   |  2 ☼ |
| The Mark of Cain         | `ELITE only`, Limit: 1     |  4 ☼ |
| Tormentor Chain          | Limit: 2                   |  3 ☼ |
| Trench Dog               | Limit: 1 ²                 | 1-3 ☼ |

² This item may not be taken by **Trench Ghost** Warbands.

### Cult of the Black Grail

PDF p.127.

| Glory Item               | Stipulation                | Cost  |
| ------------------------ | -------------------------- | ----: |
| Armour of the Fly        | `ELITE only`, Limit: 1     |  7 ☼ |
| Battlefield Title        | `ELITE only`, Limit: 1     |  5 ☼ |
| Beelzebub's Embrace      | `ELITE only`, Limit: 1     | 12 ☼ |
| Cup of Filth             | Limit: 1                   |  4 ☼ |
| Knighthood               | `ELITE only`, Limit: 1     |  4 ☼ |
| Locust Spitter           | Limit: 1                   |  6 ☼ |
| Rocket-Propelled Grenade | Consumable, Limit: 1       |  2 ☼ |
| Trench Dog               | Limit: 1                   | 1-3 ☼ |

### Court of the Seven-Headed Serpent

PDF p.127.

| Glory Item                       | Stipulation                                       | Cost  |
| -------------------------------- | ------------------------------------------------- | ----: |
| Battlefield Title                | `ELITE only`, Limit: 1                            |  5 ☼ |
| Bestial Skin Cloak               | `ELITE only`, Limit: 1                            |  6 ☼ |
| Cruel Helmet                     | Wretched only, Headgear, Limit: 2                 |  2 ☼ |
| Knighthood                       | `ELITE only`, Limit: 1                            |  4 ☼ |
| Koraktor, the Great Tome of Hell | Sorcerer only, Limit: 1                           |  8 ☼ |
| Lordship of This World           | Praetors & Sorcerers only, Limit: 1               |  9 ☼ |
| Piece of Silver                  | `ELITE only`, Limit: 1                            | 12 ☼ |
| Restraining Muzzle               | Yoke Fiends only, Limit: 3 ³                      |  1 ☼ |
| Rocket-Propelled Grenade         | Consumable, Limit: 1                              |  2 ☼ |
| Trench Dog                       | Limit: 1                                          | 1-3 ☼ |

³ A Warband can have up to 3 Restraining Muzzles purchased with **☼** **in addition to** up to 3 Restraining Muzzles purchased with 👑.

---

## Glory Item Cartulary

PDF p.128-143. This section presents descriptions and rules for every Glory Item above. Profiles work exactly as for Battlekit (→ `rules/05-battlekit.md`).

### Armour of Cobar

```yaml
glory_item: armour-of-cobar
name: Armour of Cobar
category: armour
type: armour
hands: 0
range: none
keywords: ["-3 INJURY MODIFIER"]
cost_glory: 8
cost_ducats: null
factions: [heretic-legions]
stipulation: "ELITE only"
limit: 1
```

A suit of armour fashioned after the mail worn by Cobar the Betrayer, the first Lord of the Sixty-Six. This black iron armour is forged in the death-factories of Hell from the souls of those who betrayed their friends in life. It rewards those who lead their followers and friends to ruin and death.

- **Lead to Death**: Place 1 `BLESSING MARKER` next to a model that has the Armour of Cobar each time a friendly model is taken Out of Action.
- **Weight of Sins**: Add `-1 DICE` to the Risky Success Roll for a model that has the Armour of Cobar that is taking a Dash ACTION. In addition, a model wearing the Armour of Cobar cannot have a Shield.

### Armour of the Fly

```yaml
glory_item: armour-of-the-fly
name: Armour of the Fly
category: armour
type: armour
hands: 0
range: none
keywords: ["-2 INJURY MODIFIER", "FLYING", "NEGATE SHRAPNEL"]
cost_glory: 7
cost_ducats: null
factions: [cult-of-the-black-grail]
stipulation: "ELITE only"
limit: 1
```

This suit of armour, crafted from black metal, embodies the visage of Beelzebub himself. It includes wings that propel its wearer into the skies at astonishing speed, and once it latches onto its opponent, its filth-ridden proboscis will suck the target dry.

- **Insect Wings**: Change the Movement Characteristic of a model that has the Armour of the Fly to `8"/Flying`.
- **Sucked Dry**: After a model that has the Armour of the Fly takes a Fight ACTION, it can immediately make an additional Melee Attack with `+1 DICE` to the roll. However, do not make an Injury Roll if this Melee Attack hits the target; instead place 1 `BLOOD MARKER` next to the target model.

### Battlefield Title

```yaml
glory_item: battlefield-title
name: Battlefield Title
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 5
cost_ducats: null
factions: [new-antioch, heretic-legions, cult-of-the-black-grail, court-of-the-seven-headed-serpent]
stipulation: "ELITE only"
limit: 1
```

Glorious deeds on the battlefield may earn the most determined, ruthless and deadly officers a rank within the Holy Orders of the Church, knighthood of the Teutonic Order, or the title of accuser knight to one of the dukes or princes of Hell. Such a warrior is granted the right to carry the heraldic device of their house upon their wargear, and they enjoy many privileges when it comes to accessing an enhanced allocation of the most precious weapons and armour.

- **Privileged Access**: Pick 1 Weapon or suit of Armour from your Armoury Tables that has the `Limit` special rule. Note on your Warband Roster that the Limit is **increased by 1**. The increase will remain in place even if the model that has the Battlefield Title is removed from your Roster later during the campaign. You are encouraged to come up with a special title for the Weapon or Armour that you have gained access to.

### Beelzebub's Embrace

```yaml
glory_item: beelzebubs-embrace
name: Beelzebub's Embrace
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 12
cost_ducats: null
factions: [cult-of-the-black-grail]
stipulation: "ELITE only"
limit: 1
```

The final metamorphosis of those most favoured by the Prince of Plague is to assume the many-legged form of their warped master.

- **Many-Legged Form**: A model that has been blessed with Beelzebub's Embrace has its arms replaced with fly-like limbs. The model **cannot** have Weapons, Grenades, Shields or Equipment that has the `HELD` Keyword. It can take a Melee Attack with the `CLEAVE 4` Keyword even though it doesn't have any Melee Weapons. If **all 4 Melee Attacks** successfully hit the same target model, and the target is mounted on a 32mm base or smaller, then the target is immediately taken Out of Action when it is hit by the fourth attack. Do not make an Injury Roll for the fourth attack, and any rules or abilities that would change the result do not apply (i.e. the `TOUGH` Keyword would not affect the fourth attack). This Battlekit **cannot be removed or lost** for any reason throughout the campaign.

### Bestial Skin Cloak

```yaml
glory_item: bestial-skin-cloak
name: Bestial Skin Cloak
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 6
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "ELITE only"
limit: 1
```

The proud nobles of the Court hunt the mighty creatures of the Path of the Beast for sport, much as a trophy hunter might slay a lion or a tiger for the sake of glory or vanity. The ferocious and malignant spirit of the fallen beast still lingers in its skin influencing its wearer to become ever more bestial in combat. The cloak bristles and moves on its own, seeping blood that covers its bearer.

- **Spirit of the Beast**: Once per Turn, you can do **one** of the following things for a model that has a Bestial Skin Cloak:
  - Add `+1 DICE` to the roll for a Melee Attack made by the model.
  - Add `+1 INJURY DICE` to the roll for a Melee Attack made by the model.
  - Add `+1 DICE` to the Risky Success Roll when the model takes a Dash ACTION.

A **Hunter of the Left-Hand Path** cannot cast the **Oracle Beast Cloak** Goetic Spell if it has a Bestial Skin Cloak.

### Book of Battle Prayers

```yaml
glory_item: book-of-battle-prayers
name: Book of Battle Prayers
category: equipment
type: equipment
hands: 1
range: none
keywords: ["HELD"]
cost_glory: 7
cost_ducats: null
factions: [new-antioch]
stipulation: "ELITE only"
limit: 1
```

Written by the famous Patriarch of New Antioch, Alexios Cerularius, the remaining 137 copies of this blessed book are entrusted only to Warband leaders of extraordinary ability.

- **Continuous Litany of Prayers**: A model that has the Book of Battle Prayers cannot take a Dash ACTION.
- **Speak a Blessing ACTION**: A model that has the Book of Battle Prayers can take a **Speak a Blessing ACTION**. If they do so, take a Success Roll for the model. If the roll is a Failure nothing happens. If the roll is a Success or Critical Success, you can place 1 `BLESSING MARKER` next to a friendly model that is within **12"** of the model with the Book of Battle Prayers.

### Cruel Helmet

```yaml
glory_item: cruel-helmet
name: Cruel Helmet
category: equipment
type: equipment
hands: 0
range: none
keywords: ["HEAVY", "NEGATE SHRAPNEL"]
cost_glory: 2
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "Wretched only, Headgear"
limit: 2
```

This heavy, cumbersome helmet always includes a gruesome mask. Crafted from the iron of Dis, it retains some of the searing heat of the Inferno, its touch causing skin to blister and peel. Due to its weight, it is almost impossible for its wearer to stand for long periods of time. Praetors and Sorcerers often force these dreadful devices onto their Wretched slaves.

- **Gruesome Weight**: When a model with a Cruel Helmet is deployed for the first time in a game, they are placed **Down**. In addition, if they are the target of an attack on the first Turn before they have been Activated, place 1 extra `BLOOD MARKER` next to them (even if the attack misses or the Injury Roll for it has No Effect).

### Cup of Filth

```yaml
glory_item: cup-of-filth
name: Cup of Filth
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 4
cost_ducats: null
factions: [cult-of-the-black-grail]
stipulation: null
limit: 1
```

Drawn from the river of nauseating corruption vomited by the Lord of the Flies since before time began, this liquid is the source of every illness that Creation has ever known or ever will know.

- **Drink from the Cup**: At the start of the game, **before either side deploys**, you can pick **either 1 ELITE model or up to 4 Thralls** to drink from the cup. For the rest of the game, add `+1 DICE` to the Risky Success Roll for models that drank from the cup when they take a Dash ACTION.

### Damascus Armour

```yaml
glory_item: damascus-armour
name: Damascus Armour
category: armour
type: armour
hands: 0
range: none
keywords: ["-2 INJURY MODIFIER", "IMPERVIOUS"]
cost_glory: 5
cost_ducats: null
factions: [sultanate-of-the-iron-wall]
stipulation: "ELITE only"
limit: 1
```

No armour more splendid exists within the Sultanate than this magnificent chain mail, forged from the very Iron Wall itself by the smiths of New Damascus. They are given as a reward to the greatest warriors for their service on the battlefield by the Sultan's hand alone. Each ring of this armour is inscribed with a verse from the Holy Quran and is thus utterly unbreakable.

- **Inspiring Gift**: A model that has a suit of Damascus Armour is **not sent back home until they suffer their 4th Battle Scar**. In addition, a suit of Damascus Armour cannot be removed from a model during a campaign unless the model wearing it has been killed or been declared Unfit for Duty.

### Demonic Aura Grenade

```yaml
glory_item: demonic-aura-grenade
name: Demonic Aura Grenade
category: grenade
type: grenade
hands: 1
range:
  short: 4
  long: 8
melee: false
keywords: ["ASSAULT", "BLAST 3\"", "IGNORE ARMOUR", "IGNORE COVER", "SCATTER"]
cost_glory: 3
cost_ducats: null
factions: [heretic-legions]
stipulation: null
limit: 1
```

> PDF Range: `8"` (= long range; short range = 4" per the short/long convention from `matches/coordinate-system.md` §3.2).

It is theorised this horrific grenade is based on the same technology as the weapon that destroyed the city of Antioch. Its explosion seems to cause no physical damage, but releases an eerie, bright green light that brings rapid, agonizing death to those caught within its reach. Why the Heretics do not use the grenades in greater numbers remains a mystery.

- **Deadly Light**: **Double** the number of `BLOOD MARKERS` placed next to a model by an Injury Roll for an attack made with a Demonic Aura Grenade. In addition, an Injury Roll is made for **all models that are within 3" of the target point** when the Demonic Aura Grenade explodes, **even if interposing terrain blocks the line of sight**.

### Donkey's Jawbone

```yaml
glory_item: donkeys-jawbone
name: Donkey's Jawbone
category: weapon
type: melee
hands: 1
range: melee
keywords: ["+2 INJURY DICE"]
cost_glory: 4
cost_ducats: null
factions: [trench-pilgrims]
stipulation: "ELITE only"
limit: 1
```

Blessed by YHWH, this bone club grants its wielder the strength of Samson himself.

### Ducal Winged Armour

```yaml
glory_item: ducal-winged-armour
name: Ducal Winged Armour
category: armour
type: armour
hands: 0
range: none
keywords: ["-3 INJURY MODIFIER", "FLYING"]
cost_glory: 8
cost_ducats: null
factions: [new-antioch]
stipulation: "Battlefield Title or Knighthood only"
limit: 1
```

> Only a model that **already** has a Battlefield Title or a Knighthood can have Ducal Winged Armour (PDF p.125 footnote 1).

Based on the prototype battlefield armour worn by Duke Constantine XI himself and his personal guard, known as the Myrmidons, these extremely rare and powerful suits are granted only to the most decorated soldiers. They feature a MKIII Myrmidon diesel engine and wings, painted and decorated to celebrate the deeds of the warrior who has "earned their wings".

- **Myrmidon Wings**: Change the Movement Characteristic of a model that has the Ducal Winged Armour to `10"/Flying`.
- **Steadfast**: When a model that has Ducal Winged Armour suffers a **Down** result on the Injury table, it is treated as a **Minor Hit** result instead.

### Executioner's Axe

```yaml
glory_item: executioners-axe
name: Executioner's Axe
category: weapon
type: melee
hands: 2
range: melee
keywords: ["+2 INJURY DICE", "CLEAVE 2", "CRITICAL"]
cost_glory: 6
cost_ducats: null
factions: [heretic-legions]
stipulation: null
limit: 1
```

This axe is wielded by the executioner demons of Hell whose job is to dismember those who brought division on Earth. As the flesh of the damned reforms over time, this grisly task is repeated again and again through eternity.

### Field Hospital

```yaml
glory_item: field-hospital
name: Field Hospital
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 10
cost_ducats: null
factions: [new-antioch, sultanate-of-the-iron-wall]
stipulation: null
limit: 1
```

Field Hospitals have saved many warriors in the immediate aftermath of a bloody battle. Though simpler than the mighty hospices of New Antioch, Athens or New Damascus, they are still highly sought-after by successful warband leaders.

- **Battlefield Surgery**: A Field Hospital **cannot be allocated to a model**, but is added to your **Arsenal**. If your Warband also includes a **Combat Medic**, a **Jabirean Alchemist**, or a **Sister of Saint Cosmas**, at the end of the **Trauma Step** in the Campaign Phase you can use a Field Hospital to treat 1 model from your Warband that has 1 or more Battle Scars. If you do so, roll 2D6:
  - On a roll of **7+**: remove 1 of the model's Battle Scars.
  - On a roll of **3-6**: nothing happens.
  - On a roll of **2**: the model receives 1 **extra** Battle Scar.

### Great Banner of New Antioch

```yaml
glory_item: great-banner-of-new-antioch
name: Great Banner of New Antioch
category: equipment
type: equipment
hands: 1
range: none
keywords: ["HELD"]
cost_glory: 12
cost_ducats: null
factions: [new-antioch]
stipulation: null
limit: 1
```

A famed standard, army's battle banner, or regimental colour. It may also be the flag of one of the many free companies or forces in the service of the Church. Warband leaders often possess their own battle banner adorned with the awards and ribbons their units have won, carried proudly by a trusted warrior.

- **Rally to the Flag**: If a model with a Great Banner of New Antioch is on the battlefield when you take a Morale Check (**even if they are Down**), you can choose for the Morale Check to be a **Success** or for your Warband to flee.

### Holy Grenade

```yaml
glory_item: holy-grenade
name: Holy Grenade
category: grenade
type: grenade
hands: 1
range:
  short: 4
  long: 8
melee: false
keywords: ["ASSAULT", "BLAST 2\"", "IGNORE COVER", "IGNORE LONG RANGE", "SHRAPNEL"]
cost_glory: 2
cost_ducats: null
factions: [trench-pilgrims]
stipulation: null
limit: 3
```

> PDF Range: `8"` (= long range; short range = 4").

The shells of these grenades are forged from the church bells of the original city of Antioch, and imbued with the Lord's spirit of vengeance against all evil, (such as animals possessed by demons).

- **Spirit of Vengeance**: Add `+1 INJURY DICE` to rolls against models that have the `BLACK GRAIL` or `DEMONIC` Keyword.

### Horn of Joshua

```yaml
glory_item: horn-of-joshua
name: Horn of Joshua
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 9
cost_ducats: null
factions: [trench-pilgrims]
stipulation: null
limit: 1
```

Said to be one of the horns that Joshua used to bring down the walls of Jericho. Its blast still has the power to shake the very foundations of the strongest fortifications.

- **Blow Thy Horn ACTION**: A model with the Horn of Joshua can take a **Blow Thy Horn ACTION**. If they do so, take a Risky Success Roll for the model and add `+1 DICE` to the roll.
  - **Failure**: nothing happens and the model's Activation ends.
  - **Success or Critical Success**: pick 1 terrain piece that is within **12"** of the model with the Horn of Joshua and that measures up to **8" by 8"**. Make an Injury Roll for each model (friend or foe) that is on or in contact with the terrain piece, and then **remove the terrain piece from the game**. Models that were on top of the terrain piece **Fall** directly down to the battlefield, and an additional Injury Roll may have to be made for them if they Fall **3" or more**.
  - Once a model has successfully taken a Blow Thy Horn ACTION, it **cannot be used again in the same game**.

### Kilij

```yaml
glory_item: kilij
name: Kilij
category: weapon
type: melee
hands: 1
range: melee
keywords: ["+1 INJURY MODIFIER", "CRITICAL"]
cost_glory: 2
cost_ducats: null
factions: [sultanate-of-the-iron-wall]
stipulation: "ELITE only"
limit: 2
```

Forged for warriors sworn to the martial ideals of furūsīyah, these curved swords are honed to unsurpassed sharpness. Treated by the Alchemists of the House of Wisdom, they are imbued with the power to cut through even the Infernal Tartarus armour.

### Knighthood

```yaml
glory_item: knighthood
name: Knighthood
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 4
cost_ducats: null
factions: [new-antioch, sultanate-of-the-iron-wall, heretic-legions, cult-of-the-black-grail, court-of-the-seven-headed-serpent]
stipulation: "ELITE only"
limit: 1
```

War is the crucible that bestows honorifics more rapidly than any other endeavour. Those who achieve great fame may be granted ranks such as baron, marquis, bishop or other prestigious titles. Within the taifas of the Iron Sultanate, there are many titles to be had, from chelebi knight to the mighty sheik. Hell too has its own twisted ranks of nobility, where those who commit the vilest deeds are bestowed a rank amongst the Infernal principalities.

- **Famous Deeds**: At the end of each game, your Warband receives **1 ☼** for each model with a Knighthood that is on the battlefield.

### Koraktor, the Great Tome of Hell

```yaml
glory_item: koraktor-the-great-tome-of-hell
name: Koraktor, the Great Tome of Hell
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 8
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "Sorcerer only"
limit: 1
```

Each Sorcerer carries a book copied from the Koraktor, the original tome of Goetic magic, said to have been written by the angel Samael, who is also known as the Venom of God. The reason an angel would have authored such a book is unknown, if the story is even true at all.

- **Goetic Secrets**: You can purchase **a Goetic Power** for a Sorcerer that has Koraktor, the Great Tome of Hell. It can be taken **in addition to the 3 Goetic Powers** the Sorcerer can normally have, and you can ignore any stipulations that would normally apply (such as the Sin the Sorcerer's Warband needs to be dedicated to, or it only being allowed for a model that isn't a Sorcerer). The additional power is purchased in the **Quartermaster Step** and its Cost must be paid normally.

### Locust Spitter

```yaml
glory_item: locust-spitter
name: Locust Spitter
category: weapon
type: ranged
hands: 2
range:
  short: 9
  long: 18
melee: false
keywords: ["-1 INJURY DICE", "IGNORE ARMOUR"]
cost_glory: 6
cost_ducats: null
factions: [cult-of-the-black-grail]
stipulation: null
limit: 1
```

> PDF Range: `18"` (= long range; short range = 9").

A nest of infected Hell-locusts serves as the fuel tank for this horrific gun. The voracious, razor-sharp iron locusts which dwell within can penetrate even the smallest chink in armour. Guided by the hateful will of the Lord of the Flies, they consume flesh and swarm to their next nearby target in mere seconds.

- **Devouring Swarm**: When a target is hit with the Locust Spitter, the mindless hunger of the Lord of Flies compels the swarm to continue devouring. If the Success Roll for a Ranged Attack made with Locust Spitter is a Success or Critical Success, after making the Injury Roll for the target, **subtract the range to the target from 18"**. Then make another Injury Roll for the **closest model (friend or foe) that is within this distance of the target model and has a line of sight to it** (no Success Roll is required).

  After the second target's Injury Roll has been made, the swarm moves on again, but this time the remaining distance it can travel is reduced by the distance between the first and second target, and it must target a new model that has not already been attacked. This carries on until the swarm either runs out of new target models it can reach and has a line of sight to, or the distance it is allowed to move is reduced to **0"**.

  For example, if the range to the first target was 10", then after making an Injury Roll for the first target, the closest model that can see the first target and is within (18-10) = 8" of it would also be hit. If the second target was within 3" of the first, then after making the second Injury Roll, the closest model that has not yet been attacked, and which can see the second target and is within (18-10-3) = 5" of it would be hit, and so on.

  Note that if the original attack was a Critical Success, the Injury Roll modifier **only applies to the first Injury Roll**; it does not apply to any subsequent models that are hit by the swarm. However, the `-1 INJURY DICE` and `IGNORE ARMOUR` Keywords apply to **all** of the Injury Rolls made.

### Lordship of This World

```yaml
glory_item: lordship-of-this-world
name: Lordship of This World
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 9
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "Praetors & Sorcerers only"
limit: 1
```

It is written that the powers of evil wield the greatest influence over the material world. The most formidable servants of the Pit, can torment the very earth itself and bend it to do their bidding.

- **Mark of the Pit**: The model carries a mark such as a living tattoo or a rune painted or carved by the hand of its infernal patron. At the start of each game, **after both sides have deployed**, if a friendly model with the Lordship of This World is on the battlefield you can pick **1 terrain piece** that measures up to **8" by 8"** and does not have any models from your Warband on it. You can move the terrain piece **6"** in any direction, but it must finish wholly upon the battlefield, **more than 1" from any other terrain pieces**, and not on top of any of the models from your Warband. Any enemy models that are on the terrain piece are moved with it. Enemy models that the terrain piece is moved on top of are **removed from the battlefield and then immediately redeployed by your opponent anywhere they desire within their deployment zone**.

### Masterwork Jezzail

```yaml
glory_item: masterwork-jezzail
name: Masterwork Jezzail
category: weapon
type: ranged
hands: 2
range:
  short: 18
  long: 36
melee: false
keywords: ["+1 DICE", "CRITICAL"]
cost_glory: 4
cost_ducats: null
factions: [sultanate-of-the-iron-wall]
stipulation: "ELITE only"
limit: 1
```

> PDF Range: `36"` (= long range; short range = 18").

It takes a year of effort from one of the Sultan's own gunsmiths to craft these magnificent longarms. Its bullets are enhanced to seek out new Unbelievers if they penetrate their first target.

- **Enhanced Bullets**: If the target of an attack made with a Masterwork Jezzail is **within 1" of a friendly model**, you do **not** have to roll a D6 to see if the friendly model is hit by the attack. In addition, if the **Success Roll** for an attack made with a Masterwork Jezzail is **more than 7**, after making the Injury Roll for the target, **subtract 7 from the Success Roll**. Then make an Injury Roll for the closest enemy model that is within this distance in inches of the target model and has a Line of Sight to it (no Success Roll is taken).

  For example, if you roll a 9 for the Success Roll, you could make an Injury Roll for a second enemy model that was within (9-7=) 2" of the target model and in its Line of Sight. Note that if the original attack was a Critical Success, you only add the extra `INJURY DICE` to the first Injury Roll; the extra dice do not apply to any subsequent models that are hit.

### Mobile Sultanate Grand Cannon

```yaml
glory_item: mobile-sultanate-grand-cannon
name: Mobile Sultanate Grand Cannon
category: weapon
type: ranged
hands: 1
range:
  short: 24
  long: 48
melee: false
keywords: ["+2 INJURY DICE", "HEAVY", "IGNORE ARMOUR"]
cost_glory: 10
cost_ducats: null
factions: [sultanate-of-the-iron-wall]
stipulation: "Brazen Bull only"
limit: 1
```

> PDF Range: `48"` (= long range; short range = 24"). PDF lists the weapon as `1-Handed` because the Brazen Bull's massive grip can hold it one-handed.

Mounted on the Great Iron Wall, these are the main artillery that the Sultanate produces in vast numbers. Normally fixed in place, a variant suited for the massive hands of the Brazen Bulls has been designed so the living field artillery of the Padishah can take on truly heavily armoured enemies and vehicles.

- **Brazen Bull Grand Cannon**: A Grand Cannon that is found as a Glory Item **must be carried by a Brazen Bull** and uses the profile above for all rules purposes.
- **Unstoppable Object**: If a model that has been hit by a Mobile Sultanate Grand Cannon is **not** taken Out of Action by the Injury Roll, it is **pushed D6" in a straight line directly away from the attacking model**. The model stops if it pushed into another model, Impassable terrain or a terrain piece it cannot cross without having to Climb.

### Piece of Silver

```yaml
glory_item: piece-of-silver
name: Piece of Silver
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 12
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "ELITE only"
limit: 1
```

Said to be a sliver of one of the thirty pieces of silver that Judas Iscariot accepted in return for betraying the Redeemer, there can be no talisman more potent to the servants of Hell.

- **Luck of the Devil**: At the start of each game, **before deployment**, if you have a model with a Piece of Silver in your Warband, take **3 D6**, set them to **6**, and put them aside. During the game, **unless you are making an Injury Roll or a Bloodbath Roll**, you can replace a D6 that you are about to roll with one of the dice you put aside. It is **not rolled** and is always treated as having rolled a **6** (roll any other dice normally). You can only use **one** of the dice you set aside per roll. If the model with the Piece of Silver is taken Out of Action, any of the dice you set aside that remain are **discarded** and cannot be used.

### Restraining Muzzle

```yaml
glory_item: restraining-muzzle
name: Restraining Muzzle
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 1
cost_ducats: null
factions: [court-of-the-seven-headed-serpent]
stipulation: "Yoke Fiends only"
limit: 3
```

> Stacking note: A Warband can have up to 3 Restraining Muzzles purchased with **☼** in addition to up to 3 Restraining Muzzles purchased with 👑 (PDF p.127 footnote 3).

Court nobles use these cruel, barbed muzzles to bring Yoke Fiends to heel. Each can constrict them with a command word until the pain becomes unbearable.

- **Brought to Heel**: Add `+1 DICE` to rolls made for a Ranged Attack made by a Yoke Fiend that has a Restraining Muzzle. In addition, the **Hateful** ability does not apply to a Yoke Fiend that has a Restraining Muzzle.

### Resurrection Engine

```yaml
glory_item: resurrection-engine
name: Resurrection Engine
category: special
type: special
hands: 0
range: none
keywords: ["CONSUMABLE"]
cost_glory: 11
cost_ducats: null
factions: [new-antioch]
stipulation: "Consumable"
limit: 1
```

This miraculous holy clockwork machine grants the ability to bring the dead back to life thanks to the grace of God and the research of the Holy Science Academies of New Antioch.

- **Holy Machine**: A Resurrection Engine **is not allocated to a model** (just add it to your Arsenal instead). **Once during the campaign**, you can use the Resurrection Engine to change the result rolled on the Trauma Table to a **Full Recovery** result. The Resurrection Engine is **Consumed** when it is used.

### Rocket-Propelled Grenade

```yaml
glory_item: rocket-propelled-grenade
name: Rocket-Propelled Grenade
category: special
type: ranged
hands: 0
range:
  short: 18
  long: 36
melee: false
keywords: ["+1 INJURY DICE", "CONSUMABLE", "IGNORE ARMOUR", "RELOAD"]
cost_glory: 2
cost_ducats: null
factions: [new-antioch, trench-pilgrims, sultanate-of-the-iron-wall, heretic-legions, cult-of-the-black-grail, court-of-the-seven-headed-serpent]
stipulation: "Consumable"
limit_by_faction:
  new-antioch: 2
  trench-pilgrims: 1
  sultanate-of-the-iron-wall: 2
  heretic-legions: 1
  cult-of-the-black-grail: 1
  court-of-the-seven-headed-serpent: 1
```

> PDF Range: `36"` (= long range; short range = 18"). PDF labels the Type as `Special`.

These shoulder-fired weapons launch a rocket with an explosive warhead. They are a recent invention, and thus expensive and difficult to manufacture.

- **Disposable Rocket**: A Rocket-Propelled Grenade can be used **once during a campaign** as a Ranged Weapon. If a model that has been hit by a Rocket-Propelled Grenade is **not** taken Out of Action by the Injury Roll, it is **blown D6" in a straight line directly away from the attacking model**. It stops if it is blown into another model, Impassable terrain or terrain it cannot cross without having to Climb.

### Salvage Golem

```yaml
glory_item: salvage-golem
name: Salvage Golem
category: special
type: special
hands: 0
range: none
keywords: []
cost_glory: 4
cost_ducats: null
factions: [new-antioch]
stipulation: null
limit: 1
```

Golem servitors, created by the rabbis of the Kabbalistic School of Prague to alleviate the constant strain on supplies, are equipped with sophisticated sensors and metal detectors. Slow, difficult to maintain and methodical, they are not well-suited for combat, but prove invaluable during lulls in battle as they uncover hidden caches of loot.

- **Helpful Servitor**: A Salvage Golem **is not allocated to a model** (just add it to your Arsenal instead). At the end of each game, your Warband receives an extra **D6×5 👑** for each Salvage Golem it has in its Arsenal.

### Smokescreen

```yaml
glory_item: smokescreen
name: Smokescreen
category: equipment
type: equipment
hands: 0
range: none
keywords: ["CONSUMABLE"]
cost_glory: 5
cost_ducats: null
factions: [new-antioch]
stipulation: "Consumable"
limit: 1
```

The Engineering Corps of New Antioch are experts in the use of smokescreens to shield their Shock Troops from enemy fire.

- **Swathed in Smoke**: At the start of a game, **after deployment**, if you have a model with a Smokescreen, you can say they will use it. If you do so, **divide the battlefield into 4 equal quarters** and say which one is swathed in smoke. Add `-1 DICE` to Ranged Attacks **if the Line of Sight for the attack crosses any part of the quarter that is swathed in smoke**.

### Sniper Scope

```yaml
glory_item: sniper-scope
name: Sniper Scope
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 2
cost_ducats: null
factions: [new-antioch, sultanate-of-the-iron-wall, heretic-legions]
stipulation: null
limit: 2
```

A Sniper Scope is a type of telescope mounted on a rifle or similar weapon. Some feature night-vision enhancements and superb, adjustable crystal lenses, while those crafted by the foundry-monastery of Saint Sebastian for Sniper Priests have an in-built reliquary instead.

- **Enhanced Accuracy**: When this Glory Item is given to a model, you must choose **1 Ranged Weapon** that the model already has and **which has the word "Rifle" as part of its name**. That Weapon gains the `IGNORE LONG RANGE` Keyword. A Sniper Scope **cannot be reallocated during the Quartermaster Step**.

### The Mark of Cain

```yaml
glory_item: the-mark-of-cain
name: The Mark of Cain
category: equipment
type: equipment
hands: 0
range: none
keywords: []
cost_glory: 4
cost_ducats: null
factions: [heretic-legions]
stipulation: "ELITE only"
limit: 1
```

Cain, the first of murderers, was marked by God, as a ward against those who would kill him. Corrupted copies of this mark are carved into the flesh of those who venture to Hell seeking to learn the art of murder from the greatest killers who reside in the Eternal Fire.

- **Retribution**: If an ACTION taken by a model causes **one or more `BLOOD MARKERS`** to be placed next to a model with the Mark of Cain, then place an **equal number** of `BLOOD MARKERS` next to the model that took the ACTION.

### Tormentor Chain

```yaml
glory_item: tormentor-chain
name: Tormentor Chain
category: weapon
type: ranged
hands: 1
range:
  short: 5
  long: 10
melee: false
keywords: ["ASSAULT", "IGNORE COVER", "IGNORE LONG RANGE", "SHRAPNEL"]
cost_glory: 3
cost_ducats: null
factions: [heretic-legions]
stipulation: null
limit: 2
```

> PDF Range: `10"` (= long range; short range = 5"). PDF labels the Type as `1-Handed`. The `10"` Range plus `ASSAULT`/`IGNORE LONG RANGE` keywords indicate this functions as a ranged-reach weapon — the chain itself extends to grapple at range. PDF Keywords line wraps as `ASSAULT, IGNORE COVER, IGNORE LONG, RANGE, SHRAPNEL` — read as: `ASSAULT`, `IGNORE COVER`, `IGNORE LONG RANGE`, `SHRAPNEL`.

A barbed chain used to bind the damned in Hell and sometimes granted as a weapon to Heretic warriors who have proven the most adept at dragging prisoners to the Gates of Hell alive. Possessing a will of its own, the chain can traverse great distances to snare some poor unfortunate soul in its barbed embrace.

- **Dragged Forwards**: If an attack made with a Tormentor Chain is a Success or Critical Success, **do not make an Injury Roll** for the target. Instead, place **1 `BLOOD MARKER`** next to the target, **and then place a second `BLOOD MARKER`** on the target because the Tormentor Chain has the `SHRAPNEL` Keyword. After placing the `BLOOD MARKERS`, you can move the target model **up to 12" in a straight line**, but you must move it so that it finishes the move as close as possible to the attacking model. This move can be used to make the model **move within 1" of an enemy, make a retreat move, Climb, Jump, or Jump Down**. The model cannot make a Diving Charge.
- **Deadly Embrace**: Enemy models **cannot retreat** if they are within **1"** of a model with a Tormentor Chain.

### Trench Dog

```yaml
glory_item: trench-dog
name: Trench Dog
category: special
type: special
hands: 0
range: none
keywords: ["DEPLOYABLE"]
cost_glory_min: 1
cost_glory_max: 3
cost_ducats: null
factions: [new-antioch, trench-pilgrims, sultanate-of-the-iron-wall, heretic-legions, cult-of-the-black-grail, court-of-the-seven-headed-serpent]
stipulation: "represented by a 25mm-base model; Trench Ghost Warbands may not take this item"
limit: 1   # 1 per Warband (per Faction table). Heretic Legions table says "Limit: 12" — see note.
profile:
  movement: '8"/Infantry'
  ranged: null
  melee: "+0 DICE"
  armour: 0
  base: 25mm
  battlekit: "none"
abilities:
  - "Four Paws"
  - "Pack Loyalty"
  - "Teeth and Claws"
```

> **Heretic Legions table note** (PDF p.126): the printed `Limit` value reads `12` in the v1.0.2 cartulary text, which is widely understood by the community to be a typo for `1` — every other Faction lists `Limit: 1`, the pricing range `1-3 ☼` matches a single dog, and footnote 2 only restricts which Heretic Warbands may take a dog (Trench Ghosts may not). Treat as `Limit: 1` unless errata says otherwise.

A great many animals serve in the trenches alongside the soldiers. Wardogs are by far the most common, but tame ocelots, barbary apes, small bears, and other unusual pets abound, while the forces of Hell keep hellhounds and other Infernal beasts as pets.

**Profile (PDF p.143)**:

| Movement      | Ranged | Melee     | Armour | Base  |
| ------------- | -----: | --------: | -----: | ----: |
| `8"/Infantry` |    `-` | `+0 DICE` |    `0` | 25mm |

A Trench Dog **cannot have any Battlekit**.

**Abilities** (PDF p.143):

- **Four Paws**: Add `+1 DICE` to Risky Success rolls for a Trench Dog when they **Climb, Jump or take a Dash ACTION**.
- **Pack Loyalty**: A Trench Dog has the **same Faction Keyword** as the model that has it. For example, if the owner of a Trench Dog had the `NEW ANTIOCH` Faction Keyword, then the Trench Dog will have the `NEW ANTIOCH` Faction Keyword too.
- **Teeth and Claws**: A Trench Dog can **make a Melee Attack even though it doesn't have a Melee Weapon**.

**Loyal Hound (PDF p.142)**: When you give a Trench Dog to a model, you can give the model **and** the Trench Dog the `FIRETEAM` Keyword at a Cost of **+1 ☼**.

**The Dogs of War (PDF p.142)**: After you deploy a model with a Trench Dog, you can also deploy their Trench Dog. The Trench Dog is treated as if it were a model in the Warband, except that **it is not counted as part of the Warband for the purposes of Morale Checks**. If a Trench Dog is taken Out of Action, **roll for its survival in the same way as you would for a Troops model**. Trench Dogs cannot, of course, be Promoted.

**Special Training (PDF p.142)**: When you give a Trench Dog to a model, you can give the Trench Dog **one** of the following special abilities at a Cost of **+1 ☼**:

- **Guard Dog** (not Black Grail or The Court): These dogs warn their masters of impending danger and fight fiercely for their company. Models cannot use the `INFILTRATOR` Keyword to deploy within **12"** of an enemy Guard Dog.
- **Hellhound** (Fallen Warbands only): This horrifying infernal canine is the size of a small pony, and within its tortured belly rage the flames of Hell itself. It howls in constant agony and rage in combat. All Hellhounds gain the `NEGATE FIRE` Keyword. Attacks made by a Hellhound that is part of a **Black Grail or Knights of Avarice** Warband have the `+1 DICE` and `GAS` Keywords. Attacks made by a Hellhound that is part of any other Warband have the `+1 DICE` and `FIRE` Keywords.
- **Martyrdom Dog** (Trench Pilgrims only): Trench Pilgrims often enthusiastically strap their dogs with explosives so they can partake in a glorious martyrdom operation. A Martyrdom Dog has a **Martyrdom Device** and can trigger it like an Ecclesiastic Prisoner.
- **Mercy Dog** (New Antioch only): Mercy Dogs have and can use a **Medi-kit** (→ `rules/05-battlekit.md#medi-kit`). In addition, when you move a Mercy Dog that starts the move in contact with a friendly model that is **Down** that is more than **1"** from any enemy models, it can **drag the friendly model along with itself**. If it does so, **halve the Mercy Dog's Movement Characteristic**. A Mercy Dog cannot drag a friendly model when it retreats or charges.

> **Cost ladder reminder**: the base Trench Dog costs `1 ☼`; each of `FIRETEAM` and Special Training adds `+1 ☼`, totalling up to `3 ☼`. This matches the PDF table's `1-3 ☼` range.
