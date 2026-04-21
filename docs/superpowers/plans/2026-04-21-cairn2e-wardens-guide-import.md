# Cairn 2e Warden's Guide Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract the full 192-page Cairn 2e Warden's Guide into 9 structured markdown files under `output/Cairn/rules/cairn2e-warden-*.md`, faithful to source data (stat blocks, random tables, setting details) and usable by AI Wardens at the table.

**Architecture:** PDF-to-markdown pipeline — first convert the source PDF once to a raw markdown dump with `pdf-to-markdown` skill (pymupdf mode), then slice the raw md by page ranges into 9 output files, re-structuring each according to templates defined in the design spec. Validation cross-references numerical data with `pdf_extract.py` raw text.

**Tech Stack:** `pdf-to-markdown` Skill (pymupdf4llm backend), `pdf_extract.py` (pymupdf for grep/validation), Markdown (GitHub Flavored).

**Spec:** `docs/superpowers/specs/2026-04-21-cairn2e-wardens-guide-import-design.md`

---

## File Structure

### Created

- `output/Cairn/rules/cairn2e-warden-bestiary.md` — Monster catalog with A–Z body and category index
- `output/Cairn/rules/cairn2e-warden-monster-creation.md` — Creating Monsters + Naming + Growth
- `output/Cairn/rules/cairn2e-warden-spellbooks.md` — Spellbook rules (points to `cairn1e-spells.md` for spell list)
- `output/Cairn/rules/cairn2e-warden-reliquary.md` — Relics / artifacts
- `output/Cairn/rules/cairn2e-warden-advice.md` — Creating Backgrounds + Pointcrawls + Bibliography
- `output/Cairn/rules/cairn2e-warden-worldbuilding.md` — Setting Seeds + Factions + Topography + Forest Seeds
- `output/Cairn/rules/cairn2e-warden-dungeon-seeds.md` — Dungeon Seeds + Build a Dungeon + Fractured Temple
- `output/Cairn/rules/cairn2e-warden-faq.md` — FAQ
- `output/Cairn/rules/cairn2e-warden-vald-setting.md` — Setting of Vald

### Modified

- `.claude/cairn2e-import-guide.md` — add 9 files to §2 "Warden's Guide → 输出" table
- `.claude/CLAUDE.md` — update §1 status table: Cairn row → "已完成"

### Intermediate (not committed)

- `Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.md` — raw pymupdf dump (source of truth for slicing)
- `Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.txt` — pdf_extract output (for numeric cross-reference)

---

## Task 0: Convert Warden's Guide PDF to raw markdown

**Files:**
- Create (intermediate, not committed): `Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.md`

- [ ] **Step 1: Run pdf-to-markdown in pymupdf basic mode**

The source PDF is non-art-font text (verified by inspecting p.82–86 with `pdf_extract.py --pages 82-86` — stats and bullets are clean text, no stylized fonts). Basic pymupdf is sufficient; `--docling` is not needed.

Invoke the `pdf-to-markdown` Skill with the source path:
```
input:  /Users/jack/Projects/trpg-projects/Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf
output: alongside source (default): Cairn_2e_Wardens_Guide.md
mode:   default (pymupdf4llm, no --docling)
```

- [ ] **Step 2: Verify the raw md covers all 192 pages**

Run:
```bash
grep -c "^# " "/Users/jack/Projects/trpg-projects/Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.md"
wc -l "/Users/jack/Projects/trpg-projects/Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.md"
```
Expected: non-trivial line count (thousands). Spot-check that "Bestiary" appears (from p.82) and "Setting of Vald" appears (from p.178) and "Bibliography" appears (from p.190):
```bash
grep -n "Bestiary\|Setting of Vald\|Bibliography" "/Users/jack/Projects/trpg-projects/Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.md" | head
```
Expected: at least one hit per term.

- [ ] **Step 3: Fallback if pymupdf output is poor**

If Step 2 shows missing sections (e.g., Bestiary absent) or heavy garbled text, re-run with `--docling`. The product is still `Cairn_2e_Wardens_Guide.md` (overwrite).

- [ ] **Step 4: No commit**

These intermediate files live beside the source PDF and are gitignored (check `git status` — they should not appear as untracked).

---

## Task 1: `cairn2e-warden-bestiary.md` (p.82–105)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-bestiary.md`

- [ ] **Step 1: Extract pages 82–105 from raw md**

Read the raw md section covering `Page 82` to `Page 105`. Identify each monster's name (H2/H3-like in raw output), stat line, and bullet abilities.

Cross-reference with raw text for numeric accuracy:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 82-105
# output: Cairn_2e_Wardens_Guide.txt
```

- [ ] **Step 2: Draft file with header + Index + Category Index + Monsters (A–Z)**

Template:

```markdown
# Cairn 2e — Bestiary (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.82–105. Text licensed under CC-BY-SA 4.0.
> Full monster catalog from Part 2: Warden Tools.

## Index

1. [Category Index](#category-index)
2. [Monsters (A–Z)](#monsters-a-z)

---

## Category Index

| Category | Monsters |
|---|---|
| Humanoids | [Acolyte](#acolyte), [Bandit](#bandit), [Bugbear](#bugbear), ... |
| Undead | [Banshee](#banshee), [Crypt Guardian](#crypt-guardian), [Skeleton](#skeleton), ... |
| Beasts | ... |
| Fey | [Boggart](#boggart), [Dryad](#dryad), ... |
| Constructs | [Bone Construct](#bone-construct), [Cobblehounds](#cobblehounds), ... |
| Magical | [Aranea](#aranea), [Basilisk](#basilisk), [Eye of Terror](#eye-of-terror), ... |
| Other | [remaining uncategorizable entries] |

---

## Monsters (A–Z)

### Acolyte

*(p.82)*

> 4 HP, 1 Armor, 8 STR, 11 DEX, 14 WIL, ceremonial dagger (d6)

- Holy servants bound to a particular deity. Typically travel in groups of four or more.
- Carry a holy symbol (Ward once per day).

### Aranea

*(p.82)*

> 6 HP, 13 STR, 12 DEX, 15 WIL, bite (d8)

- Enormous spiders with greenish-black skin and large brains. Can shapeshift into human form at will.
- Conduct their magical research in dark, web-filled caverns. Carry the Charm and Command spellbooks at all times.
- Fire damage against Aranea is enhanced.

[... one H3 per monster, alphabetical order ...]
```

Each monster: H3 with exact original name. `*(p.NN)*` page marker line. Blockquote single-line stat block (HP, Armor if present, STR, DEX, WIL, weapon). Bullet list of abilities. Preserve **Critical Damage:**, **Gaze:**, **Wail:** etc. as bolded inline labels.

- [ ] **Step 3: Fill Category Index**

After drafting all monster entries, assign each to one category based on Cairn 2e flavor text. Rules of thumb:
- **Humanoids** — sapient mortal races (Acolyte, Bandit, Bugbear, Centaur if intelligent, Goblin, etc.)
- **Undead** — explicit undead or spirits (Banshee, Crypt Guardian, Skeleton, etc.)
- **Beasts** — non-magical animals (Cave Locust, Blink Dog, etc.)
- **Fey** — Wood/Fae associated (Boggart, Dryad, Frost Elf, etc.)
- **Constructs** — non-living animated (Bone Construct, Cobblehounds, etc.)
- **Magical** — explicitly magical non-undead-non-fey (Aranea, Basilisk, Eye of Terror, etc.)
- **Other** — anything ambiguous

When in doubt, prefer the narrative role over biology. List each monster exactly once.

- [ ] **Step 4: Validate**

Spot-check 5 stat blocks by picking 5 entries at random and diffing with `Cairn_2e_Wardens_Guide.txt` (produced by pdf_extract). Confirm:
- HP / Armor / STR / DEX / WIL numbers match
- Weapon die match
- No bullet dropped

Confirm all H3 anchor links in Category Index are valid (markdown auto-anchors lowercase, replaces spaces with hyphens, strips punctuation):
```bash
grep -oE "^### .+" output/Cairn/rules/cairn2e-warden-bestiary.md | wc -l
grep -oE "\[.+?\]\(#.+?\)" output/Cairn/rules/cairn2e-warden-bestiary.md | sort -u | wc -l
```

Compare with `cairn1e-bestiary.md` for overlapping monsters (Cobblehounds, Frost Elf, Boggart, Wood Troll, Hooded Men, Root Goblin). Any stat difference between 1e and 2e is expected — do NOT copy from 1e.

- [ ] **Step 5: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-bestiary.md
git commit -m "Cairn 2e: add Warden's Guide bestiary (p.82-105)"
```

---

## Task 2: `cairn2e-warden-monster-creation.md` (p.106–133)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-monster-creation.md`

- [ ] **Step 1: Extract pages 106–133 from raw md**

Three sub-sections:
- Creating Monsters (p.106–115)
- Naming Procedures (p.116–123)
- Growth + Growth Examples (p.124–133)

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 106-133
```

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — Monster Creation (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.106–133. Text licensed under CC-BY-SA 4.0.
> Procedures for creating monsters, naming them, and tracking their growth.

## Index

1. [Creating Monsters](#creating-monsters)
2. [Naming Procedures](#naming-procedures)
3. [Growth](#growth)
4. [Growth Examples](#growth-examples)

---

## Creating Monsters

*(p.106–115)*

[prose + any templates]

## Naming Procedures

*(p.116–123)*

[d-table-based name generators — one H3 per table, each with markdown table]

### {Table Name}

| d6 | Result |
|---:|---|
| 1 | ... |
| ... | ... |

## Growth

*(p.124–125)*

[Growth mechanics prose]

## Growth Examples

*(p.126–133)*

[Worked examples, one H3 per example]
```

- [ ] **Step 3: Validate**

- All random tables have correct row counts (d6 = 6 rows, d8 = 8 rows, d20 = 20 rows)
- Numeric entries match pdf_extract txt
- 2e terminology (`Milestone`, `Growth`, no 1e-isms like `Misfortune`)

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-monster-creation.md
git commit -m "Cairn 2e: add Warden's Guide monster creation (p.106-133)"
```

---

## Task 3: `cairn2e-warden-spellbooks.md` (p.134–141)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-spellbooks.md`

- [ ] **Step 1: Extract pages 134–141 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 134-141
```

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — Spellbooks (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.134–141. Text licensed under CC-BY-SA 4.0.
> Rules for Spellbooks: how they are written, used, and modified.
> **Spell list:** Cairn 2e does not ship with its own 100-spell list; use `cairn1e-spells.md` for the 100-spell catalog from 1e, which 2e explicitly continues.

## Index

[generated from H2s below]

---

## {H2s per the PDF's section breaks}

*(p.NN)*

[prose + any tables]
```

Include any sub-tables (e.g., scroll/tome creation costs) as markdown tables. Preserve 2e-specific terminology: *Cost*, *bulky*, *petty*.

- [ ] **Step 3: Validate**

- All Cost / price / slot counts match pdf_extract txt
- Reference to `cairn1e-spells.md` present in the header blockquote or a note

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-spellbooks.md
git commit -m "Cairn 2e: add Warden's Guide spellbooks (p.134-141)"
```

---

## Task 4: `cairn2e-warden-reliquary.md` (p.142–147)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-reliquary.md`

- [ ] **Step 1: Extract pages 142–147 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 142-147
```

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — Reliquary (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.142–147. Text licensed under CC-BY-SA 4.0.
> Relics and artifacts — magical items with history, cost, and charges.

## Index

1. [Overview](#overview)
2. [Relics](#relics)

---

## Overview

*(p.142)*

[Introductory prose about how Relics work in 2e — charges, depletion, recharging.]

## Relics

*(p.142–147)*

### {Relic Name}

*(p.NN)*

> {slot cost, charges, notable properties as a single-line block}

- {effect / activation}
- {flavor / history}
```

Each relic gets an H3. Preserve original effect text exactly — relics are narrative-heavy and paraphrasing loses nuance.

- [ ] **Step 3: Validate**

- All charge counts / save DCs / numerical effects match pdf_extract
- Slot usage (bulky? petty?) preserved
- No relic dropped

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-reliquary.md
git commit -m "Cairn 2e: add Warden's Guide reliquary (p.142-147)"
```

---

## Task 5: `cairn2e-warden-advice.md` (p.150–153, 190)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-advice.md`

- [ ] **Step 1: Extract pages 150–153 and 190 from raw md**

Three sections:
- Creating Backgrounds (p.150–151)
- Pointcrawls (p.152–153)
- Bibliography (p.190)

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 150-153
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 190-190
```

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — Warden Advice (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.150–153, 190. Text licensed under CC-BY-SA 4.0.
> Guidance for creating new Backgrounds, running Pointcrawls, and further reading.

## Index

1. [Creating Backgrounds](#creating-backgrounds)
2. [Pointcrawls](#pointcrawls)
3. [Bibliography](#bibliography)

---

## Creating Backgrounds

*(p.150–151)*

[prose walking through the template used for the 20 canonical backgrounds: starting gear, d6 tables, names — mirroring the structure seen in `cairn2e-backgrounds.md`]

## Pointcrawls

*(p.152–153)*

[prose + any example diagrams described in text form]

## Bibliography

*(p.190)*

[list of cited works — keep as markdown list]
```

- [ ] **Step 3: Validate**

- Bibliography entries verbatim (titles, authors, years)
- No merging of nearby content (FAQ starts on p.154 and belongs to Task 7, not here)

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-advice.md
git commit -m "Cairn 2e: add Warden's Guide advice sections (p.150-153, 190)"
```

---

## Task 6: `cairn2e-warden-worldbuilding.md` (p.4–31, 56–79)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-worldbuilding.md`

This is the largest file. The source page range is split: p.4–31 covers Setting Seeds / Factions / Topography, and p.56–79 covers Forest Seeds / Example Forest. Pages 32–55 are Task 7 (dungeon-seeds).

- [ ] **Step 1: Extract pages 4–31 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 4-31
```

Sub-sections:
- Setting Seeds (p.6–7)
- Factions (p.8–13)
- Topography (p.14–31)

- [ ] **Step 2: Extract pages 56–79 from raw md**

```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 56-79
```

Sub-sections:
- Forest Seeds (p.56–67)
- Example Forest (p.68–79)

- [ ] **Step 3: Draft file**

```markdown
# Cairn 2e — Worldbuilding (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, Part 1: p.4–31 and p.56–79. Text licensed under CC-BY-SA 4.0.
> Setting generators, faction templates, topographical features, and forest building tools.

## Index

1. [Part 1 Introduction](#part-1-introduction)
2. [Setting Seeds](#setting-seeds)
3. [Factions](#factions)
4. [Topography](#topography)
5. [Forest Seeds](#forest-seeds)
6. [Example Forest](#example-forest)

---

## Part 1 Introduction

*(p.4–5)*

[intro prose]

## Setting Seeds

*(p.6–7)*

### {Seed Table Name}

| d20 | Result |
|---:|---|
| 1 | ... |

## Factions

*(p.8–13)*

### {Faction Template}

[Structure for defining a faction: name, goals, methods, resources, etc.]

## Topography

*(p.14–31)*

### {Feature Type}

[Each topographical feature — hill, river, swamp etc. — as its own H3 with any d6/d20 tables]

## Forest Seeds

*(p.56–67)*

### {Seed}

[d-table generators for forest features]

## Example Forest

*(p.68–79)*

### {Region / Locale}

[Worked example applying the Forest Seeds to build out a specific forest]
```

All d6/d20 tables as markdown tables, d-die column right-aligned.

- [ ] **Step 4: Validate**

- All tables: row counts match (d6=6, d8=8, d20=20)
- Faction templates: all fields (goals/methods/resources) retained for each faction
- Topography features: all feature types from source included
- Forest example: all locales named in the source retained

Spot-check 5 d20 entries and 5 faction descriptions against pdf_extract txt.

- [ ] **Step 5: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-worldbuilding.md
git commit -m "Cairn 2e: add Warden's Guide worldbuilding (p.4-31, 56-79)"
```

---

## Task 7: `cairn2e-warden-dungeon-seeds.md` (p.32–55)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-dungeon-seeds.md`

- [ ] **Step 1: Extract pages 32–55 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 32-55
```

Sub-sections:
- Dungeon Seeds (p.32–41)
- Build a Dungeon (p.42–49)
- The Fractured Temple (example) (p.50–55)

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — Dungeon Seeds (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.32–55. Text licensed under CC-BY-SA 4.0.
> Generators, procedures, and a full worked example (Fractured Temple) for dungeon creation.

## Index

1. [Dungeon Seeds](#dungeon-seeds)
2. [Build a Dungeon](#build-a-dungeon)
3. [The Fractured Temple](#the-fractured-temple)

---

## Dungeon Seeds

*(p.32–41)*

### {Seed Table 1: e.g. Dungeon Theme}

| d20 | Result |
|---:|---|
| 1 | ... |

[one H3 per seed table]

## Build a Dungeon

*(p.42–49)*

[step-by-step procedure for constructing a dungeon]

## The Fractured Temple

*(p.50–55)*

[Fully worked example applying Build a Dungeon to create a sample dungeon]

### Room 1. {Name}

[Room description]

### Room 2. {Name}

[... etc, one H3 per room, numbered per source]
```

- [ ] **Step 3: Validate**

- All d-tables: row counts match
- Fractured Temple: all rooms from source present, numbered correctly
- Any map described in text preserved verbatim (Cairn uses node-based maps, often listed as connections)

Spot-check 5 table entries + all room numbers.

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-dungeon-seeds.md
git commit -m "Cairn 2e: add Warden's Guide dungeon seeds (p.32-55)"
```

---

## Task 8: `cairn2e-warden-faq.md` (p.154–177)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-faq.md`

- [ ] **Step 1: Extract pages 154–177 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 154-177
```

- [ ] **Step 2: Identify Q/A boundaries**

Inspect the raw md first. The source may format questions as bold prose or headers. If clear Q markers exist, use them. If not, cluster content by topic and synthesize H3 titles that capture the topic of each cluster (`### On {topic}: {question phrase}`).

- [ ] **Step 3: Draft file**

```markdown
# Cairn 2e — Frequently Asked Questions (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.154–177. Text licensed under CC-BY-SA 4.0.
> Q&A covering rules clarifications, setting questions, and tone/style guidance.

## Index

1. [Q: {first question, abbreviated}](#q-first-question-abbreviated)
2. [Q: {second}...](#q-second)
...

---

## FAQ

### Q: {First question verbatim if present, else synthesized topic}

*(p.NN)*

{Answer body — preserve all prose, lists, examples.}

### Q: {Second question}

*(p.NN)*

{Answer body.}

[... one H3 per question ...]
```

- [ ] **Step 4: Validate**

- All questions from source present (count H3s; compare rough count to eyeballed source)
- No answer truncated
- Page markers `*(p.NN)*` present at each H3 for traceability
- Index anchors valid

- [ ] **Step 5: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-faq.md
git commit -m "Cairn 2e: add Warden's Guide FAQ (p.154-177)"
```

---

## Task 9: `cairn2e-warden-vald-setting.md` (p.178–189)

**Files:**
- Create: `output/Cairn/rules/cairn2e-warden-vald-setting.md`

- [ ] **Step 1: Extract pages 178–189 from raw md**

Cross-reference:
```bash
python3 pdf_extract.py "Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf" --pages 178-189
```

- [ ] **Step 2: Draft file**

```markdown
# Cairn 2e — The Setting of Vald (Warden's Guide)

> Source: *Cairn* (2nd Edition) Warden's Guide, p.178–189. Text licensed under CC-BY-SA 4.0.
> Expanded canonical setting of Vald: history, geography, inhabitants, and the Heart Tree. Complements the shorter overview in `cairn2e-overview.md`.

## Index

[generated from H2s]

---

## {H2 section per the PDF's actual structure — e.g. History, The Wood, The Roots, Heart Tree, Fae, Timeline}

*(p.NN)*

[prose]
```

Preserve all 2e setting terminology exactly: *Vald*, *Wood*, *Roots*, *Heart Tree*, *Heartseed*, *Gate*, *Fae*, *Marchguard*.

- [ ] **Step 3: Validate**

- All place names, NPC names, timeline dates retained verbatim
- Consistency check: any Vald facts mentioned in `cairn2e-overview.md` must NOT contradict; if this file adds new details, that's expected

- [ ] **Step 4: Commit**

```bash
git add output/Cairn/rules/cairn2e-warden-vald-setting.md
git commit -m "Cairn 2e: add Warden's Guide Vald setting (p.178-189)"
```

---

## Task 10: Update guides and status tables

**Files:**
- Modify: `.claude/cairn2e-import-guide.md`
- Modify: `.claude/CLAUDE.md`

- [ ] **Step 1: Update `cairn2e-import-guide.md` §2**

Locate the section after the Player's Guide output table that says `### Warden's Guide → 输出（未开始）` and `待 Warden's Guide PDF 转换后规划。`. Replace with:

```markdown
### Warden's Guide → 输出

| 文件 | 状态 | 来源页 | 内容 |
|---|---|---|---|
| `cairn2e-warden-worldbuilding.md` | ✓ 已完成 | p.4–31, 56–79 | Setting Seeds / Factions / Topography / Forest Seeds / Example Forest |
| `cairn2e-warden-dungeon-seeds.md` | ✓ 已完成 | p.32–55 | Dungeon Seeds / Build a Dungeon / Fractured Temple |
| `cairn2e-warden-bestiary.md` | ✓ 已完成 | p.82–105 | 字母序怪物表 + 分类索引 |
| `cairn2e-warden-monster-creation.md` | ✓ 已完成 | p.106–133 | Creating Monsters + Naming + Growth |
| `cairn2e-warden-spellbooks.md` | ✓ 已完成 | p.134–141 | Spellbook 规则（法术列表沿用 1e） |
| `cairn2e-warden-reliquary.md` | ✓ 已完成 | p.142–147 | Relics / 圣物 |
| `cairn2e-warden-advice.md` | ✓ 已完成 | p.150–153, 190 | Creating Backgrounds / Pointcrawls / Bibliography |
| `cairn2e-warden-faq.md` | ✓ 已完成 | p.154–177 | FAQ |
| `cairn2e-warden-vald-setting.md` | ✓ 已完成 | p.178–189 | Setting of Vald 详述 |
```

- [ ] **Step 2: Update `CLAUDE.md` §1 status table**

Find the Cairn row:
```
| Cairn (1e & 2e)          | Cairn      | 1e 已完成；2e Player's Guide 已完成（缺 Warden's Guide）| ...
```
Change the status column to: `已完成`

- [ ] **Step 3: Verify**

```bash
grep "Cairn" .claude/CLAUDE.md | head -3
grep -c "cairn2e-warden-" .claude/cairn2e-import-guide.md
```
Expected: Cairn status is `已完成`. Count of `cairn2e-warden-` in the guide is 9.

- [ ] **Step 4: Commit**

```bash
git add .claude/CLAUDE.md .claude/cairn2e-import-guide.md
git commit -m "Cairn 2e: mark Warden's Guide import complete in status tables"
```

---

## Rollback

If any task produces a file that fails validation, the simplest rollback is:
```bash
git reset HEAD~1  # undo the last commit, keep files
git checkout -- output/Cairn/rules/cairn2e-warden-<file>.md  # revert file
```
Then redo the task. Do NOT rebase or force-push — these commits are small and independent.

---

## Success Criteria

- 9 output files under `output/Cairn/rules/cairn2e-warden-*.md`, all committed
- Each file passes the §6 checklist in the design spec
- `CLAUDE.md` status table shows Cairn as `已完成`
- `cairn2e-import-guide.md` has a complete Warden's Guide output table
- Bestiary category index covers every monster exactly once
- No 1e terminology (Reputation, Misfortunes) leaks into 2e files
