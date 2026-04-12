# Mörk Borg Bare Bones Edition Import Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Import the 76-page Mörk Borg Core Rulebook (Bare Bones Edition) into structured English markdown files under `output/MorkBorg/rules/`, faithful to the PDF, suitable for an AI GM to consult at the table.

**Architecture:** Three output files split by query-use: `morkborg-rules.md` (character creation + core rules + optional rules + 6 optional classes), `morkborg-bestiary.md` (12 creatures + 4 outcasts), `morkborg-setting.md` (Dying World lore + Calendar of Nechrubel + reference tables + Dungeon Generator + Rules Reference Sheet). Source material is already converted at `Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).md` via pdf-to-markdown; body text is clean but many tables (names, occult treasures, traps, corpse plundering, optional class feature tables) are mangled and must be rebuilt from the PDF directly.

**Tech Stack:** Markdown (GFM), `pdf_extract.py --pages` for per-page raw text verification, pdf-to-markdown skill output as primary source.

---

## Sources

- **PDF:** `/Users/jack/Projects/trpg-projects/Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf` (76 pages)
- **Converted markdown:** `/Users/jack/Projects/trpg-projects/Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).md` (2032 lines; tables often broken — see Known Extraction Issues below)
- **Raw text:** `/Users/jack/Projects/trpg-projects/Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).txt` (pdf_extract.py output)

## Known Extraction Issues

The following sections appear mangled in the pdf-to-markdown output (numbers present, row content missing or split) and **must be rebuilt by re-extracting the single PDF page** with `pdf_extract.py --pages N`:

| Section | PDF page |
|---|---|
| Name table | p.2 |
| Occult treasures (d10) | p.3 |
| Traps and devilry / Weather (d12) / Corpse plundering (d66) | p.4-5 |
| Optional class feature tables (tags, backgrounds) for classes 1–6 | p.46, 48, 50, 52, 54, 56 |
| Even More Reasons (d100 scenario sparks) | p.68-70 |
| Dungeon Generator sub-tables (d10/d12 tables p.71-74) | p.71-74 |

If a single-page re-extract is still mangled, fall back to `pdf_extract.py --pages N-M` with a wider range, or read the PDF visually via the `Read` tool.

## File Structure

```
output/MorkBorg/rules/
├── morkborg-rules.md       # char creation, core rules, optional rules, 6 classes
├── morkborg-bestiary.md    # 12 creatures + 4 outcasts
└── morkborg-setting.md     # Dying World, Calendar, reference tables, Dungeon Generator, Rules Reference
```

## Format conventions

All three files share this header template (fill in subtitle per file):

```markdown
# Mörk Borg — <subtitle>

> Source: Mörk Borg Core Rulebook (Bare Bones Edition), Free League / Stockholm Kartell.
> Bare Bones is the official text-only digest of Mörk Borg. Flavour tables and stat blocks are faithful to the full book.
> Related files: `morkborg-rules.md`, `morkborg-bestiary.md`, `morkborg-setting.md`.

## Index

1. [Section](#section) — one-line description
...

---
```

**Creature stat block format** (from pdf_extract on p.58-62 — keep inline, single paragraph):

```markdown
### <Name>, <type>

**HP** <n> · **Morale** <n> · **<Armor>** -d<n> · **<Weapon>** d<n>
**Special:** <one-line trait>

<Flavour paragraph, one or two sentences.>

*Bounty:* Captured <n>s · Dead <n>s · <extra parts if present>
```

**Reference table format** (d-dice header, right-aligned die column):

```markdown
### Occult treasures (d10)

| d10 | Result |
|----:|--------|
| 1 | <exact row text from PDF> |
| ... | ... |
```

**Optional class format** — one `###` heading per class; first paragraph = flavour; then `**Begins with** 3d6×10s and d4 Omens. **hp:** Toughness + d8`; then sub-heading for each flavour table (*Was born in*, *Tags*, etc.) as its own table.

**Psalms / Calendar** — preserve verse numbering (`5:1`, `5:2`, ...) as plain bullet-style lines under a `### Psalm V` heading.

## Validation checklist (per task)

After each task, run through this before committing:

- [ ] All sub-sections from the PDF TOC (see `pdf_extract.py --info`) for the task range are present
- [ ] Spot-check 5 numerical values vs PDF (HP, damage die, Morale, dr, bounty prices)
- [ ] Every table from the PDF range is present, row count matches PDF
- [ ] No `<br>` artifacts, no stray `1 2 3 4 5 666` bullet lists, no duplicate "MÖRK BORG BARE BONES EDITION" headers/footers
- [ ] Non-ASCII characters (Ö, ü, é, ‘, ’) survived correctly

---

## Task 1: Scaffold three output files with headers + empty Index

**Files:**
- Create: `output/MorkBorg/rules/morkborg-rules.md`
- Create: `output/MorkBorg/rules/morkborg-bestiary.md`
- Create: `output/MorkBorg/rules/morkborg-setting.md`

- [ ] **Step 1: Create `morkborg-rules.md` with header and Index placeholder**

```markdown
# Mörk Borg — Rules

> Source: Mörk Borg Core Rulebook (Bare Bones Edition), Free League / Stockholm Kartell.
> Bare Bones is the official text-only digest of Mörk Borg. Flavour tables and stat blocks are faithful to the full book.
> Related files: `morkborg-rules.md`, `morkborg-bestiary.md`, `morkborg-setting.md`.

## Index

1. [Create a Player Character](#create-a-player-character)
2. [Abilities & Tests](#abilities--tests)
3. [Hit Points](#hit-points)
4. [Violence (Combat)](#violence-combat)
5. [Rest](#rest)
6. [Reaction](#reaction)
7. [Morale](#morale)
8. [Getting Better](#getting-better)
9. [Powers (Scrolls)](#powers-scrolls)
10. [The Basilisk's Demand](#the-basilisks-demand)
11. [Optional Rules: Omens](#optional-rules-omens)
12. [Optional Tables: Terrible Traits, Broken Bodies, Bad Habits, Troubling Tales](#optional-tables)
13. [Arcane Catastrophes](#arcane-catastrophes)
14. [Optional Classes](#optional-classes)

---
```

- [ ] **Step 2: Create `morkborg-bestiary.md` with header and Index placeholder**

```markdown
# Mörk Borg — Bestiary

> Source: Mörk Borg Core Rulebook (Bare Bones Edition), Free League / Stockholm Kartell.
> Bare Bones is the official text-only digest of Mörk Borg. Flavour tables and stat blocks are faithful to the full book.
> Related files: `morkborg-rules.md`, `morkborg-bestiary.md`, `morkborg-setting.md`.

## Index

1. [Creatures](#creatures) — 12 iconic foes
2. [Outcasts](#outcasts) — 4 hostile NPC types

---
```

- [ ] **Step 3: Create `morkborg-setting.md` with header and Index placeholder**

```markdown
# Mörk Borg — Setting & Tools

> Source: Mörk Borg Core Rulebook (Bare Bones Edition), Free League / Stockholm Kartell.
> Bare Bones is the official text-only digest of Mörk Borg. Flavour tables and stat blocks are faithful to the full book.
> Related files: `morkborg-rules.md`, `morkborg-bestiary.md`, `morkborg-setting.md`.

## Index

1. [The Dying World](#the-dying-world) — Psalms and regions
2. [The Calendar of Nechrubel](#the-calendar-of-nechrubel)
3. [Reference Tables](#reference-tables) — Names, Occult Treasures, Traps, Weather, Corpse Plundering
4. [Even More Reasons to Risk One's Life](#even-more-reasons-to-risk-ones-life) — d100 scenario sparks
5. [Dungeon Generator](#dungeon-generator)
6. [Rules Reference Sheet](#rules-reference-sheet)

---
```

- [ ] **Step 4: Verify all three files exist**

Run: `ls -la /Users/jack/Projects/trpg-projects/dnd-rules-import/output/MorkBorg/rules/`
Expected: three `.md` files listed.

- [ ] **Step 5: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-rules.md output/MorkBorg/rules/morkborg-bestiary.md output/MorkBorg/rules/morkborg-setting.md
git commit -m "scaffold Mörk Borg Bare Bones output files"
```

---

## Task 2: Import core rules into `morkborg-rules.md` (PDF p.20–36)

**Files:**
- Modify (append after `---`): `output/MorkBorg/rules/morkborg-rules.md`

**Source ranges:**
- Primary: `Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).md` lines covering pages 20–36.
- Re-extract for mangled ability/equipment tables: `python3 pdf_extract.py "Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 20-36`

**Sections to include, in order:**

1. `## Create a Player Character` (steps 1–5, optional-rules note)
2. `### Starting Equipment` (d6 container, d20 packs × 6 groups = 120 items if tables present, weapon/armor tables)
3. `### Weapons` (small d4, medium d6, heavy 2-handed d10 — exact names/dmg from p.22-23)
4. `### Armor` (4 tiers with Agility penalties from p.23)
5. `### Equipment` (misc gear list p.24-26)
6. `### Abilities` (Strength, Agility, Presence, Toughness — roll 3d6, convert table 3→-3 … 18→+3 from p.27)
7. `### Tests` (dr system, dr12 default, dr4–dr20 range, description from p.28)
8. `### Carrying Capacity` (p.28)
9. `### Hit Points` (Toughness + d8 default, class overrides noted p.29)
10. `## Violence` (Initiative Agility test, attack = roll vs defender, damage vs armor, Crits on 20 / Fumbles on 1, death at 0 hp test Toughness dr12, Broken body table reference — p.30)
11. `## Rest` (short/long rest rules p.31)
12. `## Reaction` (2d6 table from p.32)
13. `## Morale` (2d6 vs Morale rating p.32)
14. `## Getting Better` (GM decides, More HP / debris table / Ability changes mechanics p.33)
15. `## Powers (Scrolls)` (Presence + d4 uses/day, dr12 test, unclean + sacred scroll lists of 7 each from p.34-35)
16. `## The Basilisk's Demand` (the one-time-per-session mechanic from p.36)

- [ ] **Step 1: Extract pages 20–36 raw to verify tables**

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 20-36
```
Expected: txt written. Open it to read the weapon/armor/ability tables with correct row pairing.

- [ ] **Step 2: Draft sections 1–9 (character creation → Hit Points) into a scratch buffer**

Read the primary .md for body prose; for each table, copy row-by-row from the raw txt, formatted as a GFM table with right-aligned die column.

- [ ] **Step 3: Draft sections 10–16 (Violence → Basilisk's Demand)**

Body prose is clean in the pdf-to-markdown output; paste and fix only the `MÖRK BORG BARE BONES EDITION` / page-number artefacts. Normalise headings to `##` for top-level, `###` for sub.

- [ ] **Step 4: Append all drafted sections to `morkborg-rules.md`**

Use `Edit` (old_string = `---\n` at end of header, new_string = `---\n\n<drafted sections>\n`) or `Write` (only if file still only contains the header — then paste header + sections).

- [ ] **Step 5: Run validation checklist**

Spot-check vs PDF via `Read` tool on the PDF (pages 20, 27, 30, 34):
  - Weapons table: confirm "small weapon d4", "medium d6", "heavy/two-handed d10" damage
  - Abilities conversion table: confirm roll 3=-3, 4-5=-2, 6-8=-1, 9-12=0, 13-15=+1, 16-17=+2, 18=+3
  - Violence: confirm death test is `Toughness dr12`
  - Powers: confirm `Presence + d4` daily uses, `dr12` scroll test

- [ ] **Step 6: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-rules.md
git commit -m "import Mörk Borg core rules (PC creation through Basilisk's Demand)"
```

---

## Task 3: Import optional rules + 6 optional classes into `morkborg-rules.md` (PDF p.37–57)

**Files:**
- Modify (append): `output/MorkBorg/rules/morkborg-rules.md`

**Sections to include, in order:**

1. `## Optional Rules: Omens` (p.37 — d2 Omens baseline, 5 uses: max damage / reroll / -d6 damage taken / neutralise Crit or Fumble / lower dr by 4)
2. `## Optional Tables` — four d20 tables:
   - `### Terrible Traits (d20, roll twice)` (p.38 — 20 rows)
   - `### Broken Bodies (d20)` (p.39 — 20 rows)
   - `### Bad Habits (d20)` (p.40 — 20 rows)
   - `### Troubling Tales (d20)` (p.41-42 — 20 rows; verify row count on this table, it spans 2 pages)
3. `## Arcane Catastrophes (d20)` (p.43-45 — 20 rows; verify)
4. `## Optional Classes` intro paragraph (p.46)
5. Six class sections, each as `### N. <Class Name>`:
   - `### 1. Fanged Deserter` (p.46-47)
   - `### 2. Gutterborn Scum` (p.48-49)
   - `### 3. Esoteric Hermit` (p.50-51)
   - `### 4. Wretched Royalty` (p.52-53)
   - `### 5. Heretical Priest` (p.54-55)
   - `### 6. Occult Herbmaster` (p.56-57)

Each class must include:
- Flavour paragraph
- `**Begins with** <Ns><starting silver> and <Omens>. **hp:** Toughness + d<n>`
- Background / origin tables (re-extract from PDF — the pdf-to-markdown output has them as `1 2 3 4 5 666` fragments)
- Class feature tables (special abilities, tags, decoctions, etc.)

- [ ] **Step 1: Re-extract pages 37–57 raw for table content**

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 37-57
```

- [ ] **Step 2: Draft Omens and the four d20 optional tables**

Use the primary .md where tables came out correctly (Terrible Traits, Bad Habits look OK), use raw txt for Broken Bodies and Troubling Tales if the .md has them as inline bullets. Each table as a 2-column GFM table: `| d20 | Result |`.

- [ ] **Step 3: Draft Arcane Catastrophes (d20)**

Verify the table is 20 rows matching PDF p.43-45. If the .md has it mangled, rebuild from raw txt with die values 1–20.

- [ ] **Step 4: Draft the 6 optional classes**

For each class, assemble: flavour intro → Begins with / HP → all background + feature tables as their own sub-tables. Cross-check starting silver and HP formula against the PDF directly (spot-check via `Read` tool on the PDF page).

- [ ] **Step 5: Append all drafted sections to `morkborg-rules.md`**

- [ ] **Step 6: Run validation checklist**

Specifically verify:
- Four d20 optional tables each have exactly 20 rows
- Arcane Catastrophes has 20 rows
- Each of 6 classes has `Begins with` line and at least one origin/tag table
- Heretical Priest HP = `Toughness + d8`, Occult Herbmaster HP = `Toughness + d6` (these were visible in sample)

- [ ] **Step 7: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-rules.md
git commit -m "import Mörk Borg optional rules and 6 optional classes"
```

---

## Task 4: Import bestiary into `morkborg-bestiary.md` (PDF p.58–67)

**Files:**
- Modify (append): `output/MorkBorg/rules/morkborg-bestiary.md`

**Sections to include, in order:**

1. `## Creatures` intro sentence (if any on p.58) + 12 creature blocks:
   - Seth, Goblin (p.58)
   - Bent, Scum (p.58)
   - Zukuma, berserker (p.59)
   - Wrat, Wraith (p.59)
   - Belze, blood-drenched skeleton (p.60)
   - Lich, undead (weak) necromancer (p.60)
   - Troll (p.60)
   - Zombie (p.61)
   - Undead doll (p.61)
   - Grotesque (p.62)
   - Wickhead knife-wielder (p.62)
   - Wyvern (p.62)
2. `## Outcasts` intro (p.63) + 4 outcast blocks:
   - 1. Earthbound (p.64)
   - 2. Wild Wickhead (p.65)
   - 3. Pale one (p.66)
   - 4. Prowler (p.67)

**Stat block template** (reuse from Format conventions above):

```markdown
### Seth, Goblin

**HP** 6 · **Morale** 7 · **Ropy skin** -d2 · **Knife/shortbow** d4
**Special:** Quick, attacks and defence are dr14.

All goblins carry a curse. Once like you, they are now trapped in the prison of their crazed goblin flesh. …

*Bounty:* Head 7s · Captured 150s · Dead 20s
```

- [ ] **Step 1: Read pages 58–67 from the primary .md and re-extract as raw for safety**

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 58-67
```

- [ ] **Step 2: Draft all 12 Creatures in the stat block template**

Carry over every field: HP, Morale, armor (if any), weapon(s) with dmg die, Special, flavour paragraph, bounty line.

- [ ] **Step 3: Draft all 4 Outcasts**

Outcasts typically have a weapon-choice d-table — include as a sub-table under the stat block.

- [ ] **Step 4: Append to `morkborg-bestiary.md`**

- [ ] **Step 5: Run validation checklist**

Spot-check vs PDF:
- Seth (Goblin): HP 6, Morale 7, Ropy skin -d2, attacks dr14
- Wrat (Wraith): HP 15, Morale –, touch drains STR/PRE/AGI by 1
- Troll stat block present (not just name)
- Each of 4 Outcasts has a weapon sub-table

- [ ] **Step 6: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-bestiary.md
git commit -m "import Mörk Borg bestiary (creatures and outcasts)"
```

---

## Task 5: Import Dying World + Calendar into `morkborg-setting.md` (PDF p.9–19)

**Files:**
- Modify (append): `output/MorkBorg/rules/morkborg-setting.md`

**Sections to include, in order:**

1. `## The Dying World` intro (p.9)
2. `### What Was Written Must Be Known` — Psalms I–VII (p.10-11, 16-19 — the scattered verses 1:1 through 7:7). Verses must be in numerical order, grouped by Psalm.
3. `### Regions` with sub-regions:
   - `#### Tveland` (Galgenbeck, Sarkash, Graven-Tosk, Palace of the Shadow King — p.12-13)
   - `#### Grift` (p.14)
   - `#### Kergüs / Alliáns` (p.15)
   - `#### The Western Kingdom` (Lake Onda, Schleswig, Valley of the Unfortunate Undead — p.15-16)
4. `## The Calendar of Nechrubel` (p.17) — the Miseries mechanic: how to roll, consequences, list of Miseries. Verify list length against PDF.

- [ ] **Step 1: Draft Psalms**

Read the primary .md sections headed `PSALM I` through `PSALM VII`. Normalise to `### Psalm V` headings. Verses listed one per line: `- **5:1** The lake and brook shall blacken…`.

- [ ] **Step 2: Draft regions**

Straight prose copy from .md, remove page-number/artefact lines.

- [ ] **Step 3: Draft Calendar of Nechrubel**

Re-extract p.17 raw if the Miseries list is mangled:

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 17-19
```

- [ ] **Step 4: Append to `morkborg-setting.md`**

- [ ] **Step 5: Run validation checklist**

- All 7 Psalms present, verses in numeric order (1:1 → 7:7)
- All 4 regions with their sub-locations
- Calendar of Nechrubel: Miseries list row-count matches PDF

- [ ] **Step 6: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-setting.md
git commit -m "import Mörk Borg Dying World and Calendar of Nechrubel"
```

---

## Task 6: Rebuild mangled reference tables in `morkborg-setting.md` (PDF p.2–5)

**Files:**
- Modify (append): `output/MorkBorg/rules/morkborg-setting.md`

**Why separate task:** these tables are the most badly mangled by pdf extraction (see Known Extraction Issues). Rebuild them from the PDF page directly using the `Read` tool on the PDF, or — preferred — `pdf_extract.py --pages 2-5` and manual row pairing.

**Sections:**

1. `## Reference Tables` intro (one sentence — "Drop-in random tables for flavour and gameplay.")
2. `### Name Table (d6 × d8)` — 48 names (p.2). Present as a single `d6 | d8 | Name` 3-column table, OR two columns showing the d6 group and an 8-row inner list — match PDF layout.
3. `### Occult Treasures (d10)` (p.3). 10 rows, each row is a short artefact description.
4. `### Traps and Devilry (d12)` (p.4). 12 rows.
5. `### Weather (d12)` (p.4). 12 rows.
6. `### Corpse Plundering (d66)` (p.4-5). The "d66" format is roll two d6 — first as tens digit, second as ones digit, giving values 11–16, 21–26, 31–36, 41–46, 51–56, 61–66. 36 rows total. Present as `| d66 | Result |` with values `11 … 66`.

- [ ] **Step 1: Re-extract pages 2–5 raw**

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 2-5
```

- [ ] **Step 2: If raw txt is still ambiguous, view the PDF pages directly**

Use the `Read` tool with `file_path="/Users/jack/Projects/trpg-projects/Rule Books/Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf", pages="2-5"` — this reads the PDF visually.

- [ ] **Step 3: Build the Name table (48 rows)**

Format:
```markdown
### Name Table (d6 × d8)

| d6 | d8 | Name |
|---:|---:|------|
| 1 | 1 | Aerg-Tval |
| 1 | 2 | Agn |
| ... | ... | ... |
| 6 | 8 | Wemut |
```

- [ ] **Step 4: Build Occult Treasures (d10), Traps and Devilry (d12), Weather (d12)**

Each as `| dN | Result |` table. Row counts must match PDF exactly.

- [ ] **Step 5: Build Corpse Plundering (d66) — 36 rows**

```markdown
### Corpse Plundering (d66)

| d66 | Result |
|----:|--------|
| 11 | … |
| 12 | … |
| ... | ... |
| 66 | … |
```

- [ ] **Step 6: Append the Reference Tables section to `morkborg-setting.md`**

- [ ] **Step 7: Run validation checklist**

- Name table: 48 rows (6 × 8)
- Occult Treasures: 10 rows, all non-empty
- Traps and Devilry: 12 rows
- Weather: 12 rows
- Corpse Plundering: 36 rows with values 11–16, 21–26, 31–36, 41–46, 51–56, 61–66

- [ ] **Step 8: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-setting.md
git commit -m "import Mörk Borg reference tables (names, treasures, traps, weather, corpse plundering)"
```

---

## Task 7: Import Even More Reasons, Dungeon Generator, Rules Reference Sheet (PDF p.68–76)

**Files:**
- Modify (append): `output/MorkBorg/rules/morkborg-setting.md`

**Sections:**

1. `## Even More Reasons to Risk One's Life` (p.68-70):
   - `### Where do you wander? (d12)` — 12 rows
   - `### Who (or what) contacts you? (d20)` — 20 rows (p.68 has 1-12 visible, p.69 top has 13-20; verify)
   - `### The job (d100)` — 50 entries in 2-row groups (1-2, 3-4, ... 99-00). Present as `| d100 | Mission |` with ranges. Verify row count.
2. `## Dungeon Generator` (p.71-74):
   - Intro ("draw a map, ~10 rooms")
   - `### What is it called? (d12 × d12)` — roll twice, first = prefix, second = suffix
   - `### Status (d6)` — Still active / Inactive because (d4)
   - `### Imminent Danger (d10)`
   - `### Who or what dwells here now? (d12)`
   - `### Distinctive feature (d12)`
   - Any further tables on p.73-74 (verify by reading PDF)
3. `## Rules Reference Sheet` (p.76) — one-page recap of all core rules

- [ ] **Step 1: Re-extract pages 68–76 raw**

```bash
cd "/Users/jack/Projects/trpg-projects/Rule Books"
python3 /Users/jack/Projects/trpg-projects/dnd-rules-import/pdf_extract.py "Mork Borg/Mork Borg Core Rulebook (Bare Bones Edition).pdf" --pages 68-76
```

- [ ] **Step 2: Build Even More Reasons tables**

For the d100 missions table, preserve exact ranges from PDF. If the pdf-to-markdown fragments it (it did in the sample — entries appear as `1-2 y awaits`, `3-4 Thirteen priests…`), stitch together by matching each range to its line in the raw txt; if still ambiguous, read the PDF page directly via `Read` tool with `pages="68-70"`.

- [ ] **Step 3: Build Dungeon Generator**

All sub-tables as individual GFM tables. For the "What is it called? (d12 × d12)" two-column table, present each column as its own table (first roll chooses prefix, second chooses suffix).

- [ ] **Step 4: Build Rules Reference Sheet**

Compact summary from p.76 — usually a one-page cheatsheet. Preserve as a single section with bullet/sub-heading structure mirroring the PDF.

- [ ] **Step 5: Append to `morkborg-setting.md`**

- [ ] **Step 6: Run validation checklist**

- Even More Reasons "The job" has 50 entries covering 1-2 through 99-00
- Dungeon Generator "What is it called?" prefix and suffix each 12 rows
- Rules Reference Sheet present, covers at minimum: Tests/dr, Violence order, Rest, Getting Better

- [ ] **Step 7: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/morkborg-setting.md
git commit -m "import Mörk Borg Dungeon Generator, Even More Reasons, Rules Reference Sheet"
```

---

## Task 8: Cross-file consistency pass + final checklist

**Files:**
- Modify: all three `output/MorkBorg/rules/*.md` as needed

- [ ] **Step 1: Read all three files end-to-end**

Use `Read` on each; look for:
- `MÖRK BORG BARE BONES EDITION` header/footer artefacts that slipped through
- Stray `<br>` tags from the table extraction
- Broken numeric ranges (e.g. `d20` table with only 19 rows)
- Inconsistent heading levels (e.g. a `####` where a `###` is expected)

- [ ] **Step 2: Update each file's `## Index` section**

Replace the placeholder anchors with the actual section titles that were written. GFM anchor format: lowercase, spaces→dashes, strip punctuation. Example: `## Violence (Combat)` → `#violence-combat`.

- [ ] **Step 3: Verify cross-references**

- `morkborg-rules.md` Powers section references the Arcane Catastrophes table → add inline link `see [Arcane Catastrophes](#arcane-catastrophes)`.
- `morkborg-rules.md` Violence section references Broken Bodies → link into the Optional Tables section.
- `morkborg-setting.md` Dungeon Generator "Inactive because … A Misery was fulfilled" references the Miseries list in Calendar of Nechrubel → link.

- [ ] **Step 4: Final spot check vs PDF**

Random 10 checks — 4 numeric (HP/dr/dmg), 3 table row counts, 3 text passages — read the PDF page directly and diff against the output.

- [ ] **Step 5: Verify no binary/encoding issues**

```bash
grep -P '[^\x00-\x7F]' /Users/jack/Projects/trpg-projects/dnd-rules-import/output/MorkBorg/rules/*.md | head -20
```
Expected: only legitimate non-ASCII (Ö, ü, é, curly quotes). No `�`, `\ufffd`, or stray control chars.

- [ ] **Step 6: Commit**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add output/MorkBorg/rules/
git commit -m "finalise Mörk Borg Bare Bones import: cross-refs, index, consistency pass"
```

- [ ] **Step 7: Update project CLAUDE.md status line**

In `/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/CLAUDE.md`, change the Mörk Borg row (or add one if absent) in the supported-systems table to:
```
| Mörk Borg (Bare Bones) | MorkBorg | 已完成 | `Mork Borg/` | `output/MorkBorg/` |
```

- [ ] **Step 8: Commit CLAUDE.md**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import
git add .claude/CLAUDE.md
git commit -m "mark Mörk Borg Bare Bones as imported in project status"
```

---

## Self-review notes

- Spec coverage — every PDF TOC entry has a home: DYING WORLD/Calendar → Task 5; Reference tables → Task 6; THE GAME core → Task 2; Optional Rules/Classes → Task 3; CREATURES/OUTCASTS → Task 4; Even More Reasons/Dungeon Generator/Rules Reference → Task 7.
- Placeholders — none. Each task specifies exact PDF page ranges, exact table row counts, exact validation criteria.
- Consistency — file names, stat-block format, and cross-references reused identically across Tasks 1, 4, 8.
- Source-of-truth — pdf-to-markdown output is primary; `pdf_extract.py --pages` is the verification/rebuild tool; `Read` on the PDF itself is the final fallback for mangled tables.
