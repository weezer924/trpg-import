# B10 — Night's Dark Terror: Import Plan

> **Source:** B10 — Night's Dark Terror (Jim Bambra, Graeme Morris, Phil Gallagher, 1986)
> **System:** Old-School Essentials (B/X compatible)
> **Levels:** 2–4
> **PDF:** 74 pages (OCR scan) — extracted to `source/D&D Classic/Modules/B10 - Night's Dark Terror.txt` (10628 lines)

---

## Output Files

| File | Content | Required |
|------|---------|----------|
| `region.md` | Background, history, factions, key locations, travel rules, adventure flow | Yes |
| `sukiskyn.md` | Siege at Sukiskyn — homestead + siege events (Areas S1–S10) | Yes |
| `south-of-the-river.md` | Goblin lairs (W9–W17), other wilderness encounters (W1–W8, W18–W19), Wolfskull reckoning | Yes |
| `ruins-of-xitaqa.md` | Outer ruins + Golthar's Tower (Areas X1–X14) | Yes |
| `journey-to-threshold.md` | Sukiskyn→Rifllian (WE events), Rifllian (Map R), on to Threshold (WE events) | Yes |
| `threshold.md` | Threshold town (Map T), Fogor Isle (Map F), Golthar's plan, optional events | Yes |
| `black-peaks.md` | Towards the Black Peaks — Foamfire Valley (Map V), mountain encounters (VE events) | Yes |
| `lost-valley.md` | Lost Valley of Hutaaka (Map H), inhabitants, Temple of Pflarr (H5–H6) | Yes |
| `encounters.md` | Random encounter tables, monster stat block index, fixed encounters by area | Yes |
| `npcs.md` | NPC index by location | Yes |
| `quests.md` | Quest hooks and adventure flow | Yes |

---

## Import Steps

| Step | Content | PDF Pages | TXT Lines (approx.) | Output File | Status |
|------|---------|-----------|---------------------|-------------|--------|
| 1 | TOC + background + region.md | 2–6 | 1–690 | `region.md` | ✅ Done |
| 2 | Siege at Sukiskyn | 7–12 | 690–1646 | `sukiskyn.md` | ✅ Done |
| 3 | South of the River | 13–23 | 1646–3331 | `south-of-the-river.md` | ✅ Done |
| 4 | Ruins of Xitaqa | 24–27 | 3331–3872 | `ruins-of-xitaqa.md` | ✅ Done |
| 5 | Journey to Threshold | 28–33 | 3872–4783 | `journey-to-threshold.md` | ✅ Done |
| 6 | Threshold | 34–39 | 4783–5679 | `threshold.md` | ✅ Done |
| 7 | Towards the Black Peaks | 40–43 | 5679–6374 | `black-peaks.md` | ✅ Done |
| 8 | Lost Valley of Hutaaka | 44–52 | 6374–7952 | `lost-valley.md` | ✅ Done |
| 9 | New Monsters + Pull-out Sheets | 54–74 | 7952–10628 | (reference for other files) | ✅ Done (inline) |
| 10 | Compile encounters.md | — | — | `encounters.md` | ✅ Done |
| 11 | Compile npcs.md | — | — | `npcs.md` | ✅ Done |
| 12 | Compile quests.md | — | — | `quests.md` | ✅ Done |
| 13 | Cross-file validation | — | — | all files | ⬜ Next conversation |

---

## New Monsters (Module-Unique)

These need full stat blocks + ability descriptions wherever they appear:

| Monster | HD | PDF Page | Notes |
|---------|-----|----------|-------|
| Chevall | 7* | 54 | Shapechanging horse/centaur, silver/magic weapons only |
| Ice Wolf | 3+1** to 5+1** | 54 | Frost breath, immune to cold |
| Kartoeba | 10** | 55 | Unique temple guardian, tentacles + acid |
| Living Statue (Silver) | 1+1* | 55 | Small, silver skin, immune to non-metal |
| Living Statue (Rock/Ooze) | 5** | 55 | Grey ooze interior, merge into stone |
| Living Statue (Jade) | 3+1** | 55 | Magic resistant (save as F10) |
| Living Statue (Steel) | 5** | 55 | Absorbs iron/steel weapons |
| Rock Rattler | 1* | 55 | Poisonous mountain snake |
| Giant Foot-pad Lizard | 2+1 | 56 | Climbing mount |
| Wyrd | 4* | 56 | Undead elf spirit, glowing spheres |
| Piranha (Cold-water) | 1hp | 56 | Frenzy swarm |
| Shroud Spider | 5*** | 56 | Paralysing web/bite, silver/magic only |

---

## Goblin Tribes

| Tribe | Name | Symbol | Weapons | ML | Lair |
|-------|------|--------|---------|-----|------|
| Wolfskull | Kloss-lunk | Wolf's head | Axes, spears | 8 | Petrified Forest (W16) |
| Red-blade | Gnhasska | Bloodied sword | Short swords, slings | 7 | Dymrak Forest (W9) |
| Viper | Jaggadash | Snake | War hammers, daggers | 6 | Dymrak Forest (W10) |
| Yellow-fang | Faz-plak | Ruined tower | Short swords, short bows | 8 | Xitaqa (X1–3) |

---

## Key NPCs (Quick Reference)

| NPC | Role | Class/Level | Location |
|-----|------|-------------|----------|
| Pyotr | Clan head of Sukiskyn | F5 | Sukiskyn |
| Stephan | Pyotr's brother, quest-giver | F5 | Kelven → Xitaqa → party companion |
| Golthar | Iron Ring Master, main villain | M6 | Xitaqa → Threshold → Lost Valley |
| Karllag | Backup villain (if Golthar dies) | M6 | Xitaqa → Threshold |
| Jolenta | Iron Ring Reaver | C4 | Rifllian → Threshold |
| Gactis | Iron Ring Reaver | T4 | Rifllian → trails party |
| Mafka | Iron Ring spy | T5 | Threshold |
| Arthol | Town sergeant | F5 | Threshold |
| Loshad | Chevall, horse protector | HD 7* | Wilderness |
| Kforedz | Hutaakan High Priestess | HD 8* (C8) | Lost Valley |
| Guri-ben-Kaal | Traldan Chief | HD 7 (F7) | Lost Valley |
