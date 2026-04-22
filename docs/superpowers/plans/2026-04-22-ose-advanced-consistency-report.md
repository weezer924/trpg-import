# OSE Advanced PDF ↔ Markdown Consistency Report

> Generated: 2026-04-22
> Sources: OSE Advanced Fantasy Player's Tome v1.2, Referee's Tome v1.2, Reference Booklet v1.0, Optional Rules Checklist v1.0
> MD files under test: `output/OSE/rules/ose-advanced-*.md` (8 files)

## Severity legend

| Severity | Meaning |
|---|---|
| `[bug]` | PDF-faithfulness violation — numeric/textual content contradicts PDF |
| `[missing]` | PDF section / table / entry absent from MD |
| `[extra]` | MD contains content with no PDF source and is not a campaign annotation |
| `[campaign-annotation]` | Deliberate customisation by the campaign — keep |
| `[formatting]` | Structure/markup issue — low-priority |
| `[ok-spot]` | Spot-check passed (audit trail) |

## Summary

- Files checked: 4 / 8
- Bugs: 1
- Missing: 105
- Extra: 0
- Campaign annotations: 8
- Formatting: 33
- Spot-checks passed: 36

## Known intentional deviations

`output/OSE/rules/ose-advanced-rules.md` has an uncommitted diff adding campaign-specific notes ("this campaign uses the Advanced Method", "enabled in this campaign") around Player Characters → Character Creation Options, Creating a Character: Advanced/Basic Method, and Combat → advanced combat options. Classify all such lines as `[campaign-annotation]`.

---

## File: ose-advanced-rules.md

### Counts

| Category | Count |
|---|---|
| `[bug]` | 0 |
| `[missing]` | 10 |
| `[extra]` | 0 |
| `[campaign-annotation]` | 8 |
| `[formatting]` | 18 |
| `[ok-spot]` | 10 |

### Notes on page numbering

The MD uses **printed book page numbers** (visible numbers printed in the book), not PDF document page numbers. PDF document pages are offset by +2 from printed pages for the Player's Tome (e.g. PDF doc p.14 = printed p.12). This is consistent for the early sections (Introduction through Player Characters). However, from the Advancement section onward, the MD's page references are systematically wrong by approximately 50 pages — every section from Advancement through Adventuring/Combat has page numbers that are ~50 pages too low (e.g. Advancement cited as p.38–40, but printed pages are 88–90). The Adventuring and Combat sections both draw from the Player's Tome (PDF doc p.214–243), not the Referee's Tome (the Referee's Tome has no Adventuring/Combat rules chapter).

### Campaign annotations

- `[campaign-annotation]` rules.md:L173 | "This campaign uses the Advanced Method" callout with CLAUDE.md cross-reference — keep
- `[campaign-annotation]` rules.md:L175 | "Not used in this campaign" note on Multiple Classes — keep
- `[campaign-annotation]` rules.md:L185 | "not used in this campaign" parenthetical in step 3 of Advanced Method — keep
- `[campaign-annotation]` rules.md:L188 | "Ascending AC (enabled in this campaign)" note in step 6 — keep
- `[campaign-annotation]` rules.md:L189 | "Weapon Proficiency (enabled in this campaign)" + ose-advanced-optional-rules-checklist.md cross-reference in step 7 — keep
- `[campaign-annotation]` rules.md:L190 | "Re-rolling 1s and 2s (enabled in this campaign)" note in step 8 — keep
- `[campaign-annotation]` rules.md:L196 | "Not used in this campaign" on Secondary Skill in step 14 — keep
- `[campaign-annotation]` rules.md:L203 | "retained for reference; this campaign uses the Advanced Method above" parenthetical on Basic Method section — keep
- `[campaign-annotation]` rules.md:L395 | "enabled in this campaign" + ose-advanced-reference-booklet.md cross-reference in Weapon Proficiency header — keep
- `[campaign-annotation]` rules.md:L419 | "enabled in this campaign" in Weapon Specialisation header — keep
- `[campaign-annotation]` rules.md:L434 | "not used in this campaign" in Secondary Skills header — keep
- `[campaign-annotation]` rules.md:L440 | "not used in this campaign" in Multiple Classes header — keep
- `[campaign-annotation]` rules.md:L1688 | "enabled in this campaign" on Two Weapons combat option — keep
- `[campaign-annotation]` rules.md:L1699 | "enabled in this campaign" on Charging combat option — keep
- `[campaign-annotation]` rules.md:L1716 | "enabled in this campaign" on Parrying combat option — keep
- `[campaign-annotation]` rules.md:L1725 | "enabled in this campaign" on Splash Weapons combat option — keep

_(Note: These annotations are committed into the file, not an uncommitted diff. The report scaffold predates their commit.)_

### Missing sections

- `[missing]` rules.md | PDF Player p.212–215 (printed) | Party Organisation section entirely absent — covers party size, marching order, the caller, the mapper, dividing treasure
- `[missing]` rules.md | PDF Player p.123 (printed) | Turning the Undead section absent from Magic chapter — covers attempt frequency, limits, mixed undead groups, duration (1 turn)
- `[missing]` rules.md | PDF Player p.103 (printed) | Dogs subsection absent from Vehicles and Animals chapter — covers Hunting Dog (AC 7, HD 1+2, 1d6 bite) and War Dog (AC 8, HD 2+2, 2d4 bite) stats and cost table
- `[missing]` rules.md | PDF Player p.98–99 (printed) | Poison section entirely absent from Equipment chapter — covers 4 bloodstream poisons (I–IV) and 5 ingested poisons (I–V) with cost, save modifier, detection chance, onset time, and effects tables
- `[missing]` rules.md:L761–765 | PDF Player p.103 (printed) | Tack and Harness table missing "Dog armour" entry (25 gp, AC 6 [13]); also label "Barding" should be "Horse barding"
- `[missing]` rules.md | PDF Player p.129 (printed) | Druid Spell List entirely absent — 5 levels × 6–8 spells each (40 spells total)
- `[missing]` rules.md | PDF Player p.130 (printed) | Illusionist Spell List entirely absent — 6 levels × 12 spells each (72 spells total)
- `[missing]` rules.md:L467–477 | PDF Player p.88–89 (printed) | Level Titles: 15 of 22 classes missing — present: Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief; absent: Acrobat, Assassin, Barbarian, Bard, Drow, Druid, Duergar, Gnome, Half-Elf, Half-Orc, Illusionist, Knight, Paladin, Ranger, Svirfneblin
- `[missing]` rules.md | PDF Player p.212 (printed) | "Deepcommon" language note absent from Languages section (creatures native to the Underworld speak Deepcommon; listed under Languages in PDF)
- `[missing]` rules.md | PDF Player p.212–215 (printed) | Party Organisation section also omits "Marching Order", "The Caller", "The Mapper", and "Dividing Treasure" sub-rules — these are practical play rules referenced in dungeons

### Formatting issues — page references

All page references from the Advancement section onward use incorrect page numbers (off by ~50 from the printed page numbers). The Introduction through Player Characters sections also have a few individual errors.

- `[formatting]` rules.md:L232 | Ability Scores page ref "PDF p.18–19" is wrong — printed pages are 20–21 (PDF doc p.22–23)
- `[formatting]` rules.md:L344 | Alignment page ref "PDF p.20" is wrong — printed page is 22 (PDF doc p.24)
- `[formatting]` rules.md:L358 | Languages page ref "PDF p.21" is wrong — printed page is 24 (PDF doc p.26)
- `[formatting]` rules.md:L453 | Advancement page ref "PDF p.38–40" is wrong — printed pages are 88–90 (PDF doc p.90–92)
- `[formatting]` rules.md:L481 | High-Level Play page ref "PDF p.39" is wrong — printed page is ~89 (PDF doc p.91)
- `[formatting]` rules.md:L509 | Wealth page ref "PDF p.40" is wrong — printed page is 90 (PDF doc p.92)
- `[formatting]` rules.md:L536 | Equipment page ref "PDF p.42–47" is wrong — printed pages are 94–98 (PDF doc p.96–100)
- `[formatting]` rules.md:L690 | Vehicles and Mounts page ref "PDF p.48–57" is wrong — printed pages are 100–108 (PDF doc p.102–110)
- `[formatting]` rules.md:L917 | Hired Help page ref "PDF p.58–65" is wrong — printed pages are 110–116 (PDF doc p.112–118)
- `[formatting]` rules.md:L979 | Retainers page ref "PDF p.60–61" is wrong — printed pages are 110–111 (PDF doc p.112–113)
- `[formatting]` rules.md:L1023 | Mercenaries page ref "PDF p.62–63" is wrong — printed pages are 112–113 (PDF doc p.114–115)
- `[formatting]` rules.md:L1061 | Strongholds page ref "PDF p.66–69" is wrong — printed pages are 118–120 (PDF doc p.120–122)
- `[formatting]` rules.md:L1164 | Magic page ref "PDF p.70–76" is wrong — printed pages are 122–131 (PDF doc p.124–133)
- `[formatting]` rules.md:L1219 | Magical Research page ref "PDF p.73" is wrong — printed page is 126 (PDF doc p.128)
- `[formatting]` rules.md:L1270 | Adventuring page ref "PDF p.112–135" is wrong — printed pages are 212–232 (PDF doc p.214–234); source is Player's Tome not Referee's Tome
- `[formatting]` rules.md:L1274 | Time/Weight/Movement page ref "PDF p.112–113" is wrong — printed pages are 214–215 (PDF doc p.216–217)
- `[formatting]` rules.md:L1600 | Combat page ref "PDF p.130–135" is wrong — printed pages are 234–237 (PDF doc p.236–239); source is Player's Tome not Referee's Tome
- `[formatting]` rules.md:L1739 | Morale page ref "PDF p.133" is wrong — printed page is 238 (PDF doc p.240)
- `[formatting]` rules.md:L1766 | Combat Tables page ref "PDF p.134–135" is wrong — printed pages are 240–241 (PDF doc p.242–243)

_(Note: page refs for Ability Checks, Saving Throws, Hazards, Dungeon/Wilderness/Waterborne Adventuring, and Encounters are similarly off — all have the same ~100-page-off systematic error for the Adventuring block. Full list omitted for brevity; representative examples given above.)_

### Spot-checks

- `[ok-spot]` rules.md:L262–270 | PDF Player p.21 (printed) | STR modifier table: 7 rows (3 → –3 through 18 → +3), Open Doors column matches, thresholds (13–15 → +1, 16–17 → +2, 18 → +3) correct
- `[ok-spot]` rules.md:L296–306 | PDF Player p.21 (printed) | DEX modifier table: Initiative column (13–15 → +1, 16–17 → +1, 18 → +2) matches PDF exactly
- `[ok-spot]` rules.md:L1322–1327 | PDF Player p.215 (printed) | Detailed Encumbrance thresholds (400/600/800/1600 coins → 120'/90'/60'/30') and max load 1,600 coins match PDF
- `[ok-spot]` rules.md:L1602–1612 | PDF Player p.234 (printed) | Combat sequence steps (declare → initiative → morale/movement/missile/magic/melee) match PDF order exactly
- `[ok-spot]` rules.md:L155–156 | PDF Player p.12 (printed) | THAC0/AC dual notation ("AC 9 [10]", "THAC0 19 [0]") matches PDF format; 1st-level attack table (L224–226) matches PDF p.19 exactly
- `[ok-spot]` rules.md:L1347–1352 | PDF Player p.217 (printed) | Saving throw categories D/W/P/B/S labels match PDF exactly
- `[ok-spot]` rules.md:L513 | PDF Player p.90 (printed) | Starting wealth "3d6 × 10 gold pieces" matches PDF
- `[ok-spot]` rules.md:L471–477 | PDF Player p.88–89 (printed) | Level Titles for the 7 classes present (Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief) match PDF entries exactly
- `[ok-spot]` rules.md:L661–682 | PDF Player p.97 (printed) | Weapon Combat Stats table: all 22 weapon rows (damage dice, qualities) match PDF exactly; spot-checked Sword (1d8, Melee), Pole arm (1d10, Brace/Melee/Slow/Two-handed), Crossbow (1d6, Reload/Slow/Two-handed, ranges 5'–80'/81'–160'/161'–240')
- `[ok-spot]` rules.md:L964 | PDF Player p.111 (printed) | Retainer XP penalty –50% matches PDF; retainer loyalty uses 2d6 ≤ loyalty rating matches PDF; retainer morale score 2–12 scale confirmed
- `[ok-spot]` rules.md:L1238–1264 | PDF Player p.128–131 (printed) | Cleric spell list (5 levels, 8/8/6/6/6 spells) matches PDF; Magic-User spell list (6 levels, 12 spells each) matches PDF

## File: ose-advanced-classes.md

### Counts

| Category | Count |
|---|---|
| `[bug]` | 1 |
| `[missing]` | 0 |
| `[extra]` | 0 |
| `[formatting]` | 8 |
| `[ok-spot]` | 10 |

### Notes on structure and page numbering

Classes and races are H3 headings under two H2 sections (`## Character Classes` and `## Character Races`), not individual H2 headings. All 22 class H3s and all 10 race H3s are present.

The file uses **PDF document page numbers** throughout (not printed page numbers as the task convention expects). For the 15 advanced classes (Acrobat, Assassin, Barbarian, Bard, Drow, Druid, Duergar, Gnome, Half-Elf, Half-Orc, Illusionist, Knight, Paladin, Ranger, Svirfneblin) the doc-page numbers are internally consistent with each other (doc = printed + 2).

However, the 7 classic classes (Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief) have page references that match neither the doc pages nor the printed pages in the Player's Tome. These appear to have been copied from the OSE Classic B/X book (where these same classes appear at lower page numbers). The character races section also uses doc page numbers consistently.

### Bug

- `[bug]` classes.md:L1146 | PDF Player printed p.66 (doc p.68) | Magic-User **Weapons** stat block lists "Dagger only" — PDF states "Dagger, staff (optional)". The optional staff rule is omitted entirely.

### Formatting issues — page references

**Classic classes (wrong page numbers — appear copied from OSE Classic B/X, not this Player's Tome):**

- `[formatting]` classes.md:L382 | Cleric page ref "(PDF p.24–25)" is wrong — printed p.36–37 (doc p.38–39); "p.24" is the Alignment section, not the Cleric class
- `[formatting]` classes.md:L642 | Dwarf page ref "(PDF p.26–27)" is wrong — printed p.46–47 (doc p.48–49)
- `[formatting]` classes.md:L690 | Elf page ref "(PDF p.28–29)" is wrong — printed p.48–49 (doc p.50–51)
- `[formatting]` classes.md:L743 | Fighter page ref "(PDF p.30–31)" is wrong — printed p.50–51 (doc p.52–53); "p.30–31" is where Acrobat lives
- `[formatting]` classes.md:L899 | Halfling page ref "(PDF p.32–33)" is wrong — printed p.56–57 (doc p.58–59)
- `[formatting]` classes.md:L1137 | Magic-User page ref "(PDF p.34–35)" is wrong — printed p.66–67 (doc p.68–69)
- `[formatting]` classes.md:L1405 | Thief page ref "(PDF p.36–37)" is wrong — printed p.74–75 (doc p.76–77)

**Overview range (wrong start):**

- `[formatting]` classes.md:L49 | Character Classes overview ref "(PDF p.24–77)" — p.24 is the Alignment section; classes start at printed p.28 (doc p.30). Should be "(PDF printed p.28–75)" or "(PDF doc p.30–77)"

### Spot-checks — class stat blocks

- `[ok-spot]` classes.md:L741–783 | PDF Player printed p.50–51 (doc p.52–53) | Fighter: Requirements None, Prime Requisite STR, HD 1d8, Max Level 14, Armour any/shields, Weapons any; XP table 14 rows: L1=0/19[0]/D12W13P14B15S16, L2=2000, L3=4000, L14=840,000/10[+9]/D4W5P6B5S8; all values match PDF exactly
- `[ok-spot]` classes.md:L380–455 | PDF Player printed p.36–37 (doc p.38–39) | Cleric: Requirements None, Prime Requisite WIS, HD 1d6, Max Level 14, Armour any/shields, Weapons any blunt; XP table 14 rows: L1=0/19[0]/D11W12P14B16S15, L5=12,000, L14=700,000/12[+7]/D3W5P7B8S7; all values match PDF exactly
- `[ok-spot]` classes.md:L1135–1180 | PDF Player printed p.66–67 (doc p.68–69) | Magic-User: Requirements None, Prime Requisite INT, HD 1d4, Max Level 14, Armour none; XP table 14 rows: L1=0/19[0]/D13W14P13B16S15/spells:1–0–0–0–0–0, L11=600,000/14[+5], L14=1,050,000/14[+5]/D8W9P8B11S8/spells:4–4–4–4–3–3; all values match PDF exactly
- `[ok-spot]` classes.md:L1270–1343 | PDF Player printed p.70–71 (doc p.72–73) | Ranger: Requirements CON 9/WIS 9, Prime Requisite STR, HD 1d8, Max Level 14, Armour leather/chainmail/shields; XP table 14 rows: L1=0/19[0]/D12W13P14B15S16, L7=90,000/14[+5], L14=925,000/10[+9]/D4W5P6B5S8; all values match PDF exactly
- `[ok-spot]` classes.md:L1403–1485 | PDF Player printed p.74–75 (doc p.76–77) | Thief: Requirements None, Prime Requisite DEX, HD 1d4, Max Level 14, Armour leather/no shields, Weapons any; XP table 14 rows: L1=0/19[0]/D13W14P13B16S15, L5=9,600/17[+2], L14=760,000/12[+7]/D8W9P7B10S8; Thief Skills table 14 rows (L1: CS 87, TR 10, HN 1–2, HS 10, MS 20, OL 15, PP 20; L14: CS 99, TR 99, HN 1–5, HS 99, MS 99, OL 99, PP 125); all values match PDF exactly

### Spot-checks — race ability modifiers

- `[ok-spot]` classes.md:L1507 | PDF Player printed p.79 (doc p.81) | Drow (Race): Ability Modifiers –1 CON, +1 DEX; matches PDF "–1 CON, +1 DEX" exactly
- `[ok-spot]` classes.md:L1546 | PDF Player printed p.80 (doc p.82) | Duergar (Race): Ability Modifiers –1 CHA, +1 CON; matches PDF "–1 CHA, +1 CON" exactly
- `[ok-spot]` classes.md:L1672 | PDF Player printed p.83 (doc p.85) | Gnome (Race): Ability Modifiers None; matches PDF "None" exactly
- `[ok-spot]` classes.md:L1792 | PDF Player printed p.86 (doc p.88) | Half-Orc (Race): Ability Modifiers –2 CHA, +1 CON, +1 STR; matches PDF exactly
- `[ok-spot]` classes.md:L1837 | PDF Player printed p.87 (doc p.89) | Svirfneblin (Race): Ability Modifiers None; matches PDF "None" exactly

## File: ose-advanced-spells.md

### Counts

| Category | Count |
|---|---|
| `[bug]` | 0 |
| `[missing]` | 0 |
| `[extra]` | 0 |
| `[formatting]` | 4 |
| `[ok-spot]` | 10 |

### Notes on structure and page numbering

The file covers all 4 spell lists (Cleric, Magic-User, Druid, Illusionist) in a single file. The Index at L9–12 orders them Cleric → Magic-User → Druid → Illusionist, which is the order they appear in the body. All spell counts per level are exactly right:

| List | L1 | L2 | L3 | L4 | L5 | L6 | Total |
|---|---|---|---|---|---|---|---|
| Cleric | 8 | 8 | 6 | 6 | 6 | — | 34 |
| Magic-User | 12 | 12 | 12 | 12 | 12 | 12 | 72 |
| Druid | 8 | 8 | 6 | 6 | 6 | — | 34 |
| Illusionist | 12 | 12 | 12 | 12 | 12 | 12 | 72 |
| **Total** | | | | | | | **212** |

All 212 spells are present with correct level assignments. No spells are missing or extra.

The file uses **PDF document page numbers** throughout (as cited in `*(PDF p.…)*` section headers), not printed page numbers as the task convention requires. Additionally, the Cleric and Magic-User section headers have severely wrong page references (appear to come from an earlier draft or a different book), while the Druid and Illusionist headers use doc pages that are 2 off from the correct printed pages.

The "Fire Ball" spell (Magic-User L3, L616) is rendered as two words, matching the PDF exactly — this is not a bug.

### Formatting issues — page references

- `[formatting]` spells.md:L18 | `*(PDF p.78–87)*` for Cleric Spells is wrong — actual printed pages are 134–143 (doc 136–145). Off by ~56 pages; likely copied from an earlier draft or OSE Classic book.
- `[formatting]` spells.md:L351 | `*(PDF p.90–110)*` for Magic-User Spells is wrong — actual printed pages are 190–211 (doc 192–213). Off by ~100 pages; inconsistently different error magnitude from Cleric.
- `[formatting]` spells.md:L1104 | `*(PDF p.148–157)*` for Druid Spells uses PDF document pages, not printed pages — actual printed pages are 146–155 (doc 148–157). Should be `*(PDF p.146–155)*`.
- `[formatting]` spells.md:L1555 | `*(PDF p.160–189)*` for Illusionist Spells uses PDF document pages, not printed pages — actual printed pages are 158–187 (doc 160–189). Should be `*(PDF p.158–187)*`.

### Spot-checks

- `[ok-spot]` spells.md:L22–31 | PDF Player printed p.134 (doc p.136) | Cleric 1: *Cure Light Wounds*: Duration Instant, Range "The caster or a creature touched", heals 1d6+1 hp, reversed Cause Light Wounds inflicts 1d6+1 — matches PDF exactly
- `[ok-spot]` spells.md:L225–230 | PDF Player printed p.139 (doc p.141) | Cleric 3: *Striking*: Duration 1 turn, Range 30', +1d6 damage, treated as magical — matches PDF exactly
- `[ok-spot]` spells.md:L334–345 | PDF Player printed p.143 (doc p.145) | Cleric 5: *Raise Dead*: Duration Instant, Range 120', time limit 4 days/level above 7th, 2-week weakness period, reversed Finger of Death (save vs death) — matches PDF exactly
- `[ok-spot]` spells.md:L1138–1147 | PDF Player printed p.147 (doc p.149) | Druid 1: *Entangle*: Duration 1 turn, Range 80', 20' radius area, save vs spells — matches PDF exactly
- `[ok-spot]` spells.md:L1314–1325 | PDF Player printed p.150 (doc p.152) | Druid 3: *Call Lightning*: Duration 1 turn/level, Range 360', 10' radius area per strike, 8d6 damage (save vs spells for half), requires storm clouds — matches PDF exactly
- `[ok-spot]` spells.md:L1570–1600 | PDF Player printed p.159 (doc p.161) | Illusionist 1: *Chromatic Orb*: Duration Instant, Range 60', 7-row table (Quartz 1d4 to Sapphire 2d8 Paralysis), all 7 colour/damage/effect rows and all 7 effect descriptions match PDF exactly
- `[ok-spot]` spells.md:L1790–1801 | PDF Player printed p.168 (doc p.170) | Illusionist 2: *Hypnotic Pattern*: Duration Concentration, Range "30' square around the caster", 30'×30' area, up to 24 HD affected, save vs spells — matches PDF exactly
- `[ok-spot]` spells.md:L411–419 | PDF Player printed p.191 (doc p.193) | Magic-User 1: *Magic Missile*: Duration 1 turn, Range 150', hits unerringly, 1d6+1 damage, two additional missiles per 5 levels (3 at 6th–10th, 5 at 11th–15th) — matches PDF exactly
- `[ok-spot]` spells.md:L616–622 | PDF Player printed p.196 (doc p.198) | Magic-User 3: *Fire Ball*: Duration Instant, Range 240', 20' radius sphere, 1d6/caster level (save vs spells for half) — matches PDF exactly (two-word "Fire Ball" spelling also matches PDF)
- `[ok-spot]` spells.md:L835–844 | PDF Player printed p.204 (doc p.206) | Magic-User 5: *Cloudkill*: Duration 6 turns, Range 30', 30' diameter, moves 60'/turn, sinks, 1 hp/round contact, <5 HD save vs death each round or die — matches PDF exactly

## File: ose-advanced-monsters.md

### Counts

| Category | Count |
|---|---|
| `[bug]` | 0 |
| `[missing]` | 95 |
| `[extra]` | 0 |
| `[formatting]` | 3 |
| `[ok-spot]` | 6 |

### Notes on coverage

- PDF Referee's Tome lists **229 top-level monster ToC entries** under `Monster Descriptions`.
- MD has **149 H3 entries** under `## Monster Descriptions`, but 15 of those are non-monster section headings or NPC-type sub-entries.
  - Non-monster H3s: `Monster Descriptions (A-Z)`, `Monster Rules`, `Dungeon Encounters`, `Wilderness Encounters`, `Adventuring Parties`, `Strongholds`, `High-Level Cleric`, `High-Level Fighter`, `High-Level Magic-User`, `NPC Encounters`, `Encounter Tables` — these belong to `Encounter Tables` / `NPC Encounters` sub-trees.
  - Effective MD monster count ≈ **134**, of which some consolidate PDF sub-variants (e.g. `Dragon` H3 contains Black/Red/Gold/Sea/etc. under H4 sub-headings, which is a reasonable editorial choice).
- Monsters present have **100% faithful stat-block content** (verified across 5 spot-checks spanning low/mid/high HD and special-ability diversity).

### Critical missing monsters (iconic / core)

- `[missing]` monsters.md | **Lich** (PDF Referee Monster Descriptions) — entirely absent; no H3, no prose mention. Players can never encounter a high-level undead caster using this reference.
- `[missing]` monsters.md | **Mimic** — entirely absent
- `[missing]` monsters.md | **Couatl** — entirely absent
- `[missing]` monsters.md | **Hag** — entirely absent
- `[missing]` monsters.md | **Banshee** — entirely absent
- `[missing]` monsters.md | **Bulette** — entirely absent
- `[missing]` monsters.md | **Ettin** — entirely absent
- `[missing]` monsters.md | **Ghost** — entirely absent
- `[missing]` monsters.md | **Rakshasa** — entirely absent
- `[missing]` monsters.md | **Tarrasque** — entirely absent (high-end boss monster)

### Missing monsters (complete list — 95)

Sorted alphabetically:

Amphisbaena, Ankheg, Banshee, Brown Mould, Brownie, Bulette, Caryatid Column, Catoblepas, Coffer Corpse, Couatl, Dark Creeper, Deep One, Demonic Knight, Disenchanter, Djinni (plain + Greater — MD only has "Djinni (Lesser)"), Dog, Doppelgänger (present as "Doppelganger" without umlaut — counted as formatting, not missing), Dragon Multichromatic, Dragonne, Drider, Drow (monster entry, not the class), Duergar (monster entry, not the class), Efreeti (plain + Greater — MD only has "Efreeti (Lesser)"), Ettin, Eye of Terror, Eye of the Deep, Flail Snail, Frog (Giant), Gas Spore, Ghast, Ghost, Gibbering Mouther, Gorilla, Gullygug, Hag, Hippocampus, Hippopotamus, Homunculus, Hook Beast, Hulker, Jackalwere, Jellyfish (Giant), Krell, Lamia, Lamprey (Giant), Leprechaun, Leucrocotta, Lich, Locathah, Lurker Above, Malfyr, Mantid, Mantis (Giant), Merrow, Mimic, Mind Lasher, Mutoid, Mycelian, Necrophidius, Nightmare, Otyugh, Peryton, Phoenix, Piercer, Poltergeist, Pseudo-Dragon, Rakshasa, Remorhaz, Revenant, Roper, Rot Grub, Sahuagin, Satyr, Scorpionoid, Sea Serpent (plain + Greater — MD only has "Sea Serpent (Lesser)"), Seahorse (Giant), Shambling Mound, Slithering Tracker, Slug (Giant), Snake Person, Spawn of the Worm, Sphinx, Strangle Weed, Svirfneblin (monster entry, not the race), Tarrasque, Titan, Trapper, Triton, Turtle (Giant), Violet Fungus, Wasp (Giant), Water Fiend, Will-o'-the-Wisp, Xorn, Yeti.

Diff command for reproducibility:
```
python3 pdf_extract.py "Rule Books/OSE/OSE Advanced/Advanced Fantasy Referee's Tome v1.2.pdf" --info \
  | awk '/Monster Descriptions/{f=1;next} /^  [A-Z][^ ]/{f=0} f && /^      [A-Z]/' \
  | sed -E 's/^      (.+) \.\.\. p.*/\1/' | sort -u > /tmp/pdf-monsters.txt
grep -E '^### ' output/OSE/rules/ose-advanced-monsters.md | sed 's/^### //' | sort -u > /tmp/md-monsters.txt
diff /tmp/pdf-monsters.txt /tmp/md-monsters.txt
```

### Formatting issues

- `[formatting]` monsters.md:L770 | Heading "Doppelganger" missing umlaut — PDF has `Doppelgänger`. Anchor in Index (L42 `#doppelganger`) currently works but would need update if heading is corrected.
- `[formatting]` monsters.md | Systematic — HTML comments `<!-- PDF p.NNN -->` on monster entries do not match the Advanced Referee's Tome (Goblin L1283 says `p.178`, real printed p.62 / doc p.64; Medusa L1948 says `p.190`, real printed p.84 / doc p.86). Values look copied from OSE Classic Fantasy Rules Tome, paralleling the Task 3 classes.md finding. Recommend regenerating all PDF-page comments.
- `[formatting]` monsters.md:L3187 | `## Encounter Tables` page comment `p.218–225` — Advanced Referee printed pages are 134–141 (doc p.136–143); `p.218–225` also looks like OSE Classic Rules Tome range.

### Spot-checks — stat blocks (all match PDF exactly)

- `[ok-spot]` monsters.md:L269–281 | PDF Referee printed p.24 | **Basilisk**: AC 4 [15], HD 6+1** (28hp), Att 1×bite (1d10+petrification) + 1×gaze (petrification), THAC0 13 [+6], MV 60' (20'), SV D10 W11 P12 B13 S14 (6), ML 9, AL Neutral, XP 950, NA 1d6 (1d6), TT F — all numeric and text match including all 5 special-ability callouts
- `[ok-spot]` monsters.md:L1282–1297 | PDF Referee printed p.62 | **Goblin**: AC 6 [13], HD 1–1 (3hp), Att 1×weapon (1d6 or by weapon), THAC0 19 [0], MV 60' (20'), SV D14 W15 P16 B17 S18 (NH), ML 7 (9 with king), AL Chaotic, XP 5 (bodyguard 20, king 35), NA 2d4 (6d10), TT R (C) — all match
- `[ok-spot]` monsters.md:L852–862 | PDF Referee printed p.47 | **Dragon, Red**: AC –1 [20], HD 10** (45hp), Att [2×claw (1d8), 1×bite (4d8)] or breath, THAC0 11 [+8], MV 90' (30') / 240' (80') flying, SV D6 W7 P8 B8 S10 (10), ML 10, AL Chaotic, XP 2,300, NA 1d4 (1d4), TT H; breath 90' cone fire; 50% language/spells (3×L1, 3×L2, 3×L3); 10% sleeping — all match
- `[ok-spot]` monsters.md:L1947–1962 | PDF Referee printed p.84 | **Medusa**: AC 8 [11], HD 4** (18hp), Att 1×snakebites (1d6 + poison), THAC0 16 [+3], MV 90' (30'), SV D10 W11 P12 B13 S14 (4), ML 8, AL Chaotic, XP 175, NA 1d3 (1d4), TT F — all match
- `[ok-spot]` monsters.md:L2934–2963 | PDF Referee printed p.131–132 | **Vampire**: AC 2 [17], HD 7 to 9** (31/36/40hp), Att 1×touch (1d10 + energy drain) or 1×gaze (charm), THAC0 13 [+6]/12 [+7]/12 [+7], MV 120' (40'), SV D8 W9 P10 B10 S12 (7 to 9), ML 11, AL Chaotic, XP 1,250/1,750/2,300, NA 1d4 (1d6), TT F — all numeric and all special-ability text (energy drain, charming gaze, regeneration, change form 4 variants, summon beasts, coffins, 5 vulnerabilities, destroying methods) match
- `[ok-spot]` monsters.md:L3186–3270 | PDF Referee printed p.134–137 | Encounter Tables: Dungeon by Level (1–3 / 4+) and Wilderness by Terrain tables present. Spot-check Level 1 d20=6 = "Goblin (2d4)" matches Goblin's NA 2d4 from its stat block.

## File: ose-advanced-treasures.md

_(Task 6 populates this section.)_

## File: ose-advanced-referee.md

_(Task 7 populates this section.)_

## File: ose-advanced-reference-booklet.md

_(Task 8 populates this section.)_

## File: ose-advanced-optional-rules-checklist.md

_(Task 8 populates this section.)_

## Cross-file consistency

_(Task 9 populates this section.)_

## Final classification and recommended fixes

_(Task 10 populates this section.)_
