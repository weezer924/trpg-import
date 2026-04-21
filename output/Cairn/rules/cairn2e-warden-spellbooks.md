# Cairn 2e — Spellbooks (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.134–141 ("Warden Tools: Spellbooks"). Text licensed under CC BY-SA 4.0.
> This chapter is the d100 Spellbook catalog, presented twice-over: each entry pairs the **spell description** (what the spell does) with the **spellbook's physical appearance and personality** (how that specific tome manifests in the fiction).
> **Spell list:** Cairn 2e reuses the 100-spell catalog from 1e verbatim — see [`cairn1e-spells.md`](cairn1e-spells.md) for the complete d100 → spell-name mapping and the effect descriptions. This file covers only the rules-layer around Spellbooks.
> **Core Spellbook rules** (casting, Fatigue cost, Scrolls, Relics) live in [`cairn2e-rules.md`](cairn2e-rules.md) §Magic — they are not repeated in the Warden's Guide. The Warden's Guide adds no new cost, price, crumble, or depletion tables; all such mechanics remain in the Player's Guide.

## Index

1. [Overview](#overview)
2. [Reading the d100 Spellbook Table](#reading-the-d100-spellbook-table)
3. [Spellbook Appearance and Personality (2e Addition)](#spellbook-appearance-and-personality-2e-addition)
4. [Warden Usage Notes](#warden-usage-notes)
5. [Cross-References](#cross-references)
6. [The d100 Spellbook Table](#the-d100-spellbook-table)

---

## Overview

*(p.134)*

> **Spell description in regular text, *spellbook appearance and personality in italics.*** *(verbatim editor's note at the top of the d100 table)*

The Warden's Guide devotes eight pages (p.134–141) to a single d100 table titled **Spellbooks**. The table is the same d100 → spell mapping that 1e shipped on p.8 of its core rulebook — the 100 spell names and the primary effect text are unchanged from 1e. What 2e adds is a short **italicized phrase** appended to each entry describing the physical form and personality quirks of *that specific Spellbook*.

There is no separate "how to create / price / destroy a Spellbook" section in this chapter. The Warden's Guide presumes the reader already knows the Spellbook rules from the Player's Guide and simply hands the Warden a ready-to-use table of 100 evocatively-described tomes.

---

## Reading the d100 Spellbook Table

*(p.134–141)*

Each row has three columns:

| Column | Contents |
|---|---|
| **d100** | The roll result (1–100), ordered alphabetically by spell name. |
| **Spellbook** | The spell's name — identical to the 1e list with two naming adjustments (see below). |
| **Description** | The **spell's effect** in regular text, followed by the **book's appearance and personality** in *italics*. |

Each page of the PDF holds roughly 12–13 entries:

| PDF page | Spellbook range |
|---:|---|
| 134 | 1 Adhere → 12 Befuddle |
| 135 | 13 Body Swap → 25 Displace |
| 136 | 26 Earthquake → 38 Hatred |
| 137 | 39 Hear Whispers → 52 Masquerade |
| 138 | 53 Miniaturize → 65 Push/Pull |
| 139 | 66 Raise Dead → 77 Sleep |
| 140 | 78 Slick → 89 Teleport |
| 141 | 90 Thicket → 100 X-Ray Vision |

**1e → 2e revisions.** Comparing the 2e table with the 1e list in `cairn1e-spells.md`:

| Change | 1e entry | 2e entry |
|---|---|---|
| Dropped | #80 **Spectacle** | — |
| Dropped | #83 **Summon Cube** | — |
| Dropped | #90 **Summon Idol** | — |
| Added | — | **Fish Lung** (now #30) |
| Added | — | **Passage** (now #61) |
| Added | — | **Skillful Repair** (now #76) |

Because the list stays alphabetical and exactly 100 entries long, the three additions (F-, P-, S-) each shove later entries down by one d100 slot relative to 1e. Any carryover spell's **effect text is unchanged**, so only the d100 index and alphabetical neighbors differ. When resolving a d100 roll at the Cairn 2e table, use the 2e numbering; when porting a 1e Spellbook fiction into a 2e game, look up the spell by **name**, not by d100 number.

---

## Spellbook Appearance and Personality (2e Addition)

*(p.134, editor's note)*

The italicized sentence(s) on each row are the 2e-specific addition. They describe:

- **Sensory signature** — smell (*"smells of vinegar and thyme"*), sound (*"childish laughter sprouts from its pages"*), temperature (*"becomes warm to the touch if magic is used nearby"*), light (*"faintly glows in complete darkness"*).
- **Behavioral quirks** — *"rights itself when dropped or thrown"* (Sort), *"pages flip wildly while open; can cause paper cuts"* (Haste), *"closed by two powerful straps that spring open at inopportune times"* (Repel).
- **Long-term effects on the owner** — *"long-term possession can cause the reader to mistake the thoughts of others as their own"* (Read Mind), *"the owner is haunted by strange visions of their own ancestors"* (Primal Surge), *"extended use causes the owner to develop unconscious yet noticeable tics"* (Masquerade).
- **Side-effects that create complications** — *"bound in rusty ring-mail and is quite heavy. If held, provides +1 Armor"* (Shield), *"gloves required. Nonflammable"* (Icy Touch), *"relics within 100ft of the spellbook cannot be recharged"* (Magic Dampener).
- **Concealed features** — *"a standard piton can be safely stored in its spine"* (Pit), *"inside the front cover is a small pocket containing a thin pad of paper, listing the name and date of death of all previous owners"* (Wizard Mark).

These descriptions are **not mechanical modifiers** by default. They are fictional hooks the Warden can play up for flavor, danger, or side-reward. A few entries, however, do imply hard rules — these should be honored:

| Spellbook | Implied mechanical effect |
|---|---|
| Shield | *If held, provides +1 Armor* — stack with worn armor subject to the usual 3-Armor cap. |
| Magic Dampener | *Relics within 100ft of the spellbook cannot be recharged* — note when party carries both. |
| Telekinesis | *Summoned to hand via mental command; WIL save or become Deprived afterwards.* |
| Manse | *If left inside the cottage, both the book and the cottage vanish forever.* |
| Teleport | *Can be destroyed to create a portal to another dimension.* |

For full per-spell appearance flavor, refer to the source PDF directly — the 100 italic phrases are not reproduced here (per the 2e-vs-1e content boundary: spell-table content lives in `cairn1e-spells.md`).

---

## Warden Usage Notes

The Warden's Guide supplies no explicit guidance for how to deploy the appearance text, but the preceding Growth chapter (p.124–133) includes a worked example — *"Long-term Exposure or Manipulation of a Spellbook or Relic"* (p.126) — starring *Hazel* and her *Control Plants* Spellbook. Key takeaways:

- A character may repeatedly attempt to **enhance** a Spellbook's power through WIL saves; successful enhancements become permanent abilities (e.g. casting without a WIL save under duress).
- Failure to enhance invites a Warden-determined cost on par with the spell — Fatigue, Spellbook destruction, injury, or death (mirroring the casting-under-duress rule in the Player's Guide).
- Because Spellbooks are **unique items of great power**, any success against meaningful risk is a valid trigger for character Growth.
- The appearance/personality line is the hook for these fictional interactions — smell, sound, behavior, side-effects — and should be surfaced whenever the book is opened, carried across thresholds, or left unattended.

Elsewhere in the Warden's Guide, the "Magic is rare and dangerous" creed (p.154+, FAQ) reinforces that Relics and Spellbooks are **not well understood** in-world; attempts to manipulate their power may lead to **self-destruction**.

---

## Cross-References

| Topic | File |
|---|---|
| d100 spell list and spell effect descriptions | [`cairn1e-spells.md`](cairn1e-spells.md) |
| Core Spellbook rules (casting, Fatigue, Scrolls, Relics) | [`cairn2e-rules.md`](cairn2e-rules.md) §Magic |
| Spellbook-centric Growth example (Hazel / *Control Plants*) | `cairn2e-warden-monster-creation.md` (Growth section, p.126) |
| Relics and artifacts (including items that interact with Spellbooks) | `cairn2e-warden-reliquary.md` (p.142–147) |

---

## The d100 Spellbook Table

*(p.134–141)*

> Complete Warden's Guide d100 Spellbook catalog. **Spell effect** (regular text) matches the 1e spell list verbatim; ***italicized phrase*** is the 2e-specific addition describing the spellbook's physical appearance, personality, or side-effects.

| d100 | Spellbook | Description |
|---:|---|---|
| 1 | Adhere | An object is covered in extremely sticky slime. *Adjacent objects stick to the book with great force.* |
| 2 | Anchor | A strong wire sprouts from your arms, affixing itself to two points within 50ft on each side. *If a rope is pulled through the iron loop on its spine, it becomes as heavy as an elephant.* |
| 3 | Animate Object | An object obeys your commands as best it can. *Moldable like clay. Childish laughter sprouts from its pages.* |
| 4 | Anthropomorphize | An animal either gains human intelligence or human appearance for one day. *Whimpers, purrs and growls depending on its treatment.* |
| 5 | Arcane Eye | You can see through a magical floating eyeball that flies around at your command. *Needs a spritz of water to open.* |
| 6 | Astral Prison | An object is frozen in time and space within an invulnerable crystal shell. *Silent, abstract, faces scream in anguish within.* |
| 7 | Attract | Two objects are strongly magnetically attracted to each other if they come within 10 feet. *Nearby compasses spin uselessly.* |
| 8 | Auditory Illusion | You create illusory sounds that seem to come from a direction of your choice. *Produces random and occasionally inopportune sounds throughout the day.* |
| 9 | Babble | A creature must loudly and clearly repeat everything you think. It is otherwise mute. *When the text is read aloud, the words of others become unintelligible.* |
| 10 | Bait Flower | A plant sprouts from the ground that emanates the smell of decaying flesh. *Attracts flies.* |
| 11 | Beast Form | You and your possessions transform into a mundane animal. *Covered in thick fur, its edges lined with small teeth.* |
| 12 | Befuddle | A creature of your choice is unable to form new short-term memories for the duration of the spell. *Its contents shift and change each time it is opened.* |
| 13 | Body Swap | You switch bodies with a creature you touch. If one body dies, the other dies as well. *The front cover shows an image of the last creature to read it.* |
| 14 | Charm | A creature you can see treats you as a friend. *Warm to the touch, and smells of roses.* |
| 15 | Command | A target obeys a single three-word command that does not cause it harm. *Grows thinner over time, until finally disappearing forever.* |
| 16 | Comprehend | You become fluent in all languages for a short while. *Drips letters, staining whatever it touches.* |
| 17 | Cone of Foam | Dense foam sprays from your hand, coating the target. *Spongy and moist with a soapy residue.* |
| 18 | Control Plants | Nearby plants and trees obey you and gain the ability to move at a slow pace. *Leaves grow along the spine, and it smells faintly of decay.* |
| 19 | Control Weather | You may alter the type of weather at will, but you do not otherwise control it. *Highly resistant to fire and water damage.* |
| 20 | Cure Wounds | Restore 1d4 STR per day to a creature you can touch. *Smells of vinegar and thyme. Turns red after use.* |
| 21 | Deafen | All nearby creatures are deafened. *Nearby instruments occasionally sound off, as if in protest.* |
| 22 | Detect Magic | You can see or hear nearby magical auras. *Becomes warm to the touch if magic is used nearby.* |
| 23 | Disassemble | Any of your body parts may be detached and reattached at will, without causing pain or damage. You can still control them. *Regenerates any torn or defaced pages.* |
| 24 | Disguise | You may alter the appearance of one character at will as long as they remain humanoid. Attempts to duplicate other characters will seem uncanny. *The surface makes a perfect mirror.* |
| 25 | Displace | An object appears to be up to 15ft from its actual position. *Bits of string, clothing, and leaves are sometimes stuffed inside.* |
| 26 | Earthquake | The ground begins shaking violently. Structures may be damaged or collapse. *Sand dribbles from the corners, seemingly without stop.* |
| 27 | Elasticity | Your body can stretch up to 10ft. *Smells of taffy, and is very flexible.* |
| 28 | Elemental Wall | A straight wall of ice or fire 50ft long and 10ft high rises from the ground. *Skin and warmer substances stick to it after use.* |
| 29 | Filch | A visible item teleports to your hands. *An ally's prized possession may occasionally be found tucked between its covers.* |
| 30 | Fish Lung | A target can breathe underwater until they surface again. *Smells strongly of the sea. Attracts wild animals.* |
| 31 | Flare | A bright ball of energy fires a trail of light into the sky, revealing your location to friend or foe. *Faintly glows in complete darkness.* |
| 32 | Fog Cloud | A dense fog spreads out from you. *When submersed in water, the book eventually turns all the liquid to vapor.* |
| 33 | Frenzy | A nearby creature erupts in a frenzy of violence. *Rough, sandpaper cover that destroys any book it touches.* |
| 34 | Gate | A portal to a random plane opens. *A large hole is carved into the center, ending in a void. Items dropped within are never seen again.* |
| 35 | Gravity Shift | You can change the direction of gravity, but only for yourself. *Attaches itself to the largest object nearby.* |
| 36 | Greed | A creature develops the overwhelming urge to possess a visible item of your choice. *The cover changes depending on the owner, subtly hinting at their deepest desires.* |
| 37 | Haste | Your movement speed is tripled. *Pages flip wildly while open. Can cause paper cuts.* |
| 38 | Hatred | A creature develops a deep hatred of another creature or group and wishes to destroy them. *Long term exposure to the book can cause suspicion, paranoia and distrust of others.* |
| 39 | Hear Whispers | You can hear faint sounds clearly. *The reader's voice is amplified for a short period of time afterwards.* |
| 40 | Hover | An object hovers, frictionless, 2ft above the ground. It can hold up to one humanoid. *Floats if dropped.* |
| 41 | Hypnotize | A creature enters a trance and will truthfully answer one yes or no question you ask it. *Eye-catching, swirling spirals don its covers.* |
| 42 | Icy Touch | A thick ice layer spreads across a touched surface, up to 10ft in radius. *Gloves required. Nonflammable.* |
| 43 | Identify Owner | Letters appear over the object you touch, spelling out the name of the object's owners, if there are any. *The book's interior lists the name of its previous owner.* |
| 44 | Illuminate | A floating light moves as you command. *When held in light, the pages become a prism of vibrant rainbows.* |
| 45 | Invisible Tether | Two objects within 10ft of each other cannot be moved more than 10ft apart. *Its pages are not attached by glue or thread, yet stay together nonetheless.* |
| 46 | Knock | A nearby mundane or magical lock unlocks loudly. *Locked. A new owner "produces" the key after their next meal.* |
| 47 | Leap | You jump up to 10ft high, once. *When thrown, it just keeps going.* |
| 48 | Liquid Air | The air around you becomes swimmable. *Floats of its own volition, bouncing off of whatever it touches.* |
| 49 | Magic Dampener | All nearby magical effects have their effectiveness halved. *Relics within 100ft of the spellbook cannot be recharged.* |
| 50 | Manse | A sturdy, furnished cottage appears for hours. You can permit and forbid entry to it at will. *If left inside, both the book and the cottage vanish forever.* |
| 51 | Marble Craze | Your pockets are full of marbles and will refill every 30 seconds. *When jostled, makes a playful rattling sound.* |
| 52 | Masquerade | A character's appearance and voice becomes identical to those of a character you touch. *Extended use causes the owner to develop unconscious yet noticeable tics.* |
| 53 | Miniaturize | A creature you touch is shrunk down to the size of a mouse. *The text is ludicrously, comically large.* |
| 54 | Mirror Image | An illusory duplicate of yourself appears and is under your control. *Over time, the owner begins to question who is the original, and who is the duplicate.* |
| 55 | Mirrorwalk | A mirror becomes a gateway to another mirror that you looked into today. *Will not open unless the owner politely knocks on the cover.* |
| 56 | Multiarm | You temporarily gain an extra arm. *After use, the caster is wracked with phantom limb syndrome for a day.* |
| 57 | Night Sphere | A 50ft-wide sphere of darkness displaying the night sky appears before you. *Displays a prominent constellation on its cover.* |
| 58 | Objectify | You become any inanimate object between the size of a grand piano and an apple. *The owner experiences intense pareidolia for days after use.* |
| 59 | Ooze Form | You become a living jelly. *Slowly drips an acid that eventually eats away anything it touches.* |
| 60 | Pacify | A creature near you has an aversion to violence. *Smells of jasmine and incense. Attracts children.* |
| 61 | Passage | Creates a temporary path through wood, stone or brick. *An object dropped on top of the book inevitably falls through the other side.* |
| 62 | Phobia | A nearby creature becomes terrified of an object of your choice. *Over time, haunting, abstract art begins to fill its pages.* |
| 63 | Pit | A pit 10ft wide and 10ft deep opens in the ground. *A standard piton can be safely stored in its spine.* |
| 64 | Primal Surge | A creature rapidly evolves into a future version of its species. *The owner is haunted by strange visions of their own ancestors.* |
| 65 | Push/Pull | An object of any size is pulled directly towards you or pushed directly away from you with the strength of one man. *Any force against the book is comically amplified.* |
| 66 | Raise Dead | A skeleton rises from the ground to serve you. They are incredibly stupid and can only obey simple orders. *The owner becomes more and more fascinated with bones after each use.* |
| 67 | Raise Spirit | The spirit of a nearby corpse manifests and will answer 1 question. *The answers (but not their questions) are forever inscribed in its pages.* |
| 68 | Read Mind | You can hear the surface thoughts of nearby creatures. *Long-term possession can cause the reader to mistake the thoughts of others as their own.* |
| 69 | Repel | Two objects are strongly magnetically repelled from each other within 10 feet. *Closed by two powerful straps that spring open at inopportune times.* |
| 70 | Scry | You can see through the eyes of a creature you touched earlier today. *The owner's eyes turn milky-white for an hour after use.* |
| 71 | Sculpt Elements | Inanimate material behaves like clay in your hands. *Slowly decays on contact with wood or cloth. Bury in dirt or submerge in water to refresh.* |
| 72 | Sense | Choose one kind of object (key, gold, arrow, jug, etc). You can sense the nearest example. *The book's previous owner is always aware of the book's current location.* |
| 73 | Shield | A creature you touch is protected from mundane attacks for one minute. *Bound in rusty ring-mail and is quite heavy. If held, provides +1 Armor.* |
| 74 | Shroud | A creature you touch is invisible until they move. *Invisible to any but the book's current owner.* |
| 75 | Shuffle | Two creatures you can see instantly switch places. *If stolen but not yet read, it reappears wherever its owner last left it.* |
| 76 | Skillful Repair | You make minor repairs to a nonliving object. *Sewn from the vellum of one hundred books, no two pages are alike.* |
| 77 | Sleep | A creature you can see falls into a light sleep. *Soft as a pillow, but yields only fitful sleep.* |
| 78 | Slick | Every surface in a 30ft radius becomes extremely slippery. *Gloves are required for handling, lest the book is dropped in a most comical fashion.* |
| 79 | Smoke Form | Your body becomes a living smoke that you can control. *Smells of campfire. The pages cannot be burnt, but are very sensitive to moisture.* |
| 80 | Sniff | You can smell even the faintest traces of scents. *Expresses a strong odor detectable only by its owner.* |
| 81 | Snuff | The source of any mundane light you can see is instantly snuffed out. *If left in one place for long periods, nearby light sources eventually dim, then finally go out.* |
| 82 | Sort | Inanimate items sort themselves according to categories you set. *Rights itself when dropped or thrown.* |
| 83 | Spellsaw | A whirling blade flies from your chest, clearing any plant material in its way. It is otherwise harmless. *Wrapped in stained leather, it should be oiled at least once a month.* |
| 84 | Spider Climb | You can climb surfaces like a spider. *New cobwebs must be pushed aside prior to each use. They are hard to remove.* |
| 85 | Swarm | You become a swarm of crows, rats, or piranhas. You can only be harmed by blast attacks. *Easily broken into a dozen distinct parts that slowly move towards one another over time.* |
| 86 | Target Lure | An object you touch becomes the target of any nearby spell. *Attracts all manner of magical creatures, spell leaks, and scrying.* |
| 87 | Telekinesis | You may mentally move 1 item under 60lbs. *The owner can summon the book through mental command alone (WIL save or become deprived afterwards).* |
| 88 | Telepathy | Two creatures can hear each other's thoughts, no matter how far apart. *The holder can hear (but not respond) to the thoughts of whoever last possessed it, and vice versa.* |
| 89 | Teleport | An object or person you can see is transported from one place to another in a 50ft radius. *Can be destroyed to create a portal to another dimension.* |
| 90 | Thicket | A thicket of trees and dense brush up to 50ft wide suddenly sprouts up. *Wrapped in vines that must be destroyed again with each use.* |
| 91 | Time Control | Time in a 50ft bubble slows down or increases by 10% for 30 seconds. *Alternates its appearance as either impossibly old or freshly written.* |
| 92 | True Sight | You see through all nearby illusions. *Cannot be concealed by magic, and sticks out like a sore thumb.* |
| 93 | Upwell | A spring of seawater appears. *Hardened leather bindings caked in salt and living barnacles.* |
| 94 | Vision | You completely control what a creature sees. *An unnerving, lidless eye graces the front cover.* |
| 95 | Visual Illusion | A silent, immobile, room-sized illusion of your choice appears. *Filled with rich, colorful pages very much like a children's bedtime story.* |
| 96 | Ward | A silver circle 50ft across appears on the ground. Choose one species that cannot cross it. *The covers are decorated with bizarre, otherworldly creatures with thousands of eyes.* |
| 97 | Web | Your wrists shoot thick webbing. *The text is alien, yet somehow intelligible, for it is the language of dreams.* |
| 98 | Widget | A primitive version of a drawn tool or item appears before you and disappears after a short time. *Smells of iron and rust, sweat and effort. Faint sounds of harsh labor emanate from deep within its pages.* |
| 99 | Wizard Mark | Your finger can shoot a stream of ulfire-colored paint. This paint is only visible to you and can be seen at any distance, even through solid objects. *Inside the front cover is a small pocket containing a thin pad of paper, listing the name and date of death of all previous owners.* |
| 100 | X-Ray Vision | You can see through walls, dirt, clothing, etc. *Long-term exposure can cause hair loss, blurry vision, and fatigue.* |
