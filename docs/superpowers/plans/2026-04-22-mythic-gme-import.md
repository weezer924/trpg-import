# Mythic GME 2e Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Import the 230-page Mythic GME 2nd Edition PDF as an AI-facing solo storytelling engine at `output/Mythic/`, producing 37 markdown artifacts across 5 subdirectories plus a project import guide.

**Architecture:** One-time PDF→raw-md conversion, then slice-and-restructure into five layered tiers. `rules/` carries linear PDF-fidelity text; `engine/` holds refined AI runtime procedures; `tables/` hosts pure-data lookup tables; `examples/` stores the four Big Examples as calibration material; `sheets/` provides record templates. English original throughout (no translation).

**Tech Stack:** `pdf-to-markdown` Skill (pymupdf4llm backend, `--docling` fallback), `pdf_extract.py` (pymupdf for grep/validation), Markdown (GitHub Flavored), YAML frontmatter.

**Spec:** `docs/superpowers/specs/2026-04-22-mythic-gme-import-design.md`

---

## File Structure

### Created — Output

```
output/Mythic/
  rules/
    00-mythic-journey.md            # PDF p.4
    01-mythic-adventures.md         # PDF p.8-17
    02-fate-questions.md            # PDF p.18-31 (Big Example excluded)
    03-random-events.md             # PDF p.36-54 (Big Example excluded)
    04-scenes.md                    # PDF p.60-115 (Big Example excluded)
    05-variations.md                # PDF p.124-177
    06-rules-summary.md             # PDF p.187-192
  engine/
    00-core-loop.md
    01-fate-questions.md
    02-random-events.md
    03-scenes.md
    04-threads-and-characters.md
    05-chaos-factor.md
    06-npc-behavior.md
    07-interpretation-principles.md
    08-variations.md
    09-session-protocol.md
  tables/
    fate-chart.md
    fate-chart-variants.md
    fate-question-answers.md
    fate-check-modifiers.md
    random-event-focus.md
    meaning-actions.md
    meaning-descriptions.md
    meaning-elements.md
    scene-adjustment.md
    npc-behavior.md
    npc-statistics.md
    thread-progress-track.md
    adventure-features.md
  examples/
    _index.md
    01-henny-in-z-land.md           # PDF p.32-35
    02-wutwo-labs.md                # PDF p.55-59
    03-guardian-of-chosen-one.md    # PDF p.116-123
    04-the-big-example.md           # PDF p.178-186
  sheets/
    adventure-journal.md            # PDF p.193 + sections embedded in p.77-84
    keyed-scenes.md                 # PDF p.154, 224
```

### Created — Documentation

- `.claude/mythic-import-guide.md` — per-system import guide (directory layout, conventions, page maps, validation checklist)

### Modified

- `.claude/CLAUDE.md` — §1 status table add Mythic row; §4 guides table add Mythic row

### Intermediate (not committed; lives beside source PDF, gitignored via existing `Rule Books/**/*.md` patterns)

- `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.md` — raw pymupdf dump
- `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.txt` — pdf_extract output for numeric cross-reference

---

## Task 0: Scaffold — convert PDF, create directories, write import guide, update CLAUDE.md

**Files:**
- Create (intermediate, not committed): `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.md`
- Create: `.claude/mythic-import-guide.md`
- Create (empty directories): `output/Mythic/{rules,engine,tables,examples,sheets}/`
- Modify: `.claude/CLAUDE.md` (two table rows)

- [ ] **Step 1: Create output directory skeleton**

```bash
mkdir -p output/Mythic/{rules,engine,tables,examples,sheets}
```

Expected: `ls output/Mythic/` shows all 5 directories.

- [ ] **Step 2: Run pdf-to-markdown on source PDF (pymupdf fast mode)**

Invoke the `pdf-to-markdown` Skill:
```
input:  /Users/jack/Projects/trpg-projects/Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf
output: alongside source: Mythic Game Master Emulator 2nd Edition.md (+ images/)
mode:   default (pymupdf4llm)
```

Mythic 2e is text-heavy with some section banners in stylized fonts, but the body uses standard serif — pymupdf should handle it fine. Do not preemptively use `--docling`.

- [ ] **Step 3: Verify raw md covers all 230 pages**

```bash
RAW="/Users/jack/Projects/trpg-projects/Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.md"
wc -l "$RAW"
grep -c "^# \|^## " "$RAW"
grep -nE "Fate Chart|Chaos Factor|Meaning Table|Adventure Journal|Keyed Scenes" "$RAW" | head
```

Expected: several thousand lines; at least one hit per search term above.

- [ ] **Step 4: Fallback if raw md is garbled**

If Step 3 shows missing sections (Fate Chart absent, or massive text gaps), re-run pdf-to-markdown with `--docling`. The product is still the same `.md` file (overwrite).

- [ ] **Step 5: Also generate pdf_extract txt for grep validation**

```bash
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf"
```

Expected: creates `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.txt`.

- [ ] **Step 6: Write `.claude/mythic-import-guide.md`**

Template:

````markdown
# Mythic GME 2e 导入指南

> Mythic Game Master Emulator 2nd Edition (Tana Pigeon, Word Mill Games)
> 源 PDF：`Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf`（230 页）
> 输出目录：`output/Mythic/`
> 设计 spec：`docs/superpowers/specs/2026-04-22-mythic-gme-import-design.md`

---

## 1. 定位

Mythic 2e 是**跨系统的 solo storytelling engine**——不是游戏系统，而是一套程序 + 随机表，用于 solo 或 GM-less 游戏中模拟 GM。

本次导入的**主要消费者是 AI**（运行 solo session）。输出结构按 AI 运行时需要分层，而非按 PDF 目录。

## 2. 输出结构

| 目录 | 角色 | AI 加载时机 | 特点 |
|---|---|---|---|
| `engine/` | **主入口** | Session 开始即全部加载 | 紧凑程序、决策树、解读心法。无叙述文。 |
| `rules/` | **兜底参考** | 规则歧义时查询 | PDF 线性转录，保留原文解释。 |
| `tables/` | **按需查询** | 每次判定/掷骰 | 纯数据，一表一文件。 |
| `examples/` | **风格校准** | 解读僵化时参考 | 4 个 Big Example，可扩展。 |
| `sheets/` | **模板** | Session 准备时参考 | Adventure Journal / Keyed Scenes 记录表。 |

## 3. 写作规范

### rules/
- 线性转录，按 PDF 章节顺序
- 保留 Crane 的概念讲解、设计理由、边界讨论
- Inline mini-examples（"假设 PC 在 X…"）随正文保留
- **4 个 Big Example 不放在 rules/**，迁到 `examples/`；rules/ 各章到 Big Example 前一页为止

### engine/
- 结构：`## When To Use / ## Procedure / ## Decision Tree / ## Failure modes / ## Cross-refs`
- 祈使句，无叙述连接词（"Now let's discuss", "As we've seen" 等）
- 跨文件引用用相对路径：`→ tables/fate-chart.md`

### tables/
- 每文件顶部 2-3 行 `When: / Input: / Output:` 使用说明
- Markdown 表格，数字列右对齐
- `meaning-elements.md` 内部用 `## <Theme>` 分隔 ~100 个子表

### examples/
- Frontmatter：`source` / `chaos-focus` / `length-turns` / `length-scenes`
- `_index.md` 先被 AI 读到，按 `chaos-focus` 标签匹配

### engine/07-interpretation-principles.md 提炼方法
- 读 4 个 Big Example + 扫 rules/ 里的解读相关段落
- 每条原则 = 祈使句 + 1-2 句说明 + 源引用
- 源引用必须精确：`examples/02-wutwo-labs.md turn 3` 或 `rules/02-fate-questions.md §When To Run With Expectations`
- 目标 ~25 条，上限 30

## 4. 章节 → 文件 → 页码对照

### rules/
| 文件 | PDF 页 | 备注 |
|---|---|---|
| `00-mythic-journey.md` | p.4 | 前言 |
| `01-mythic-adventures.md` | p.8-17 | Ch1 综述 |
| `02-fate-questions.md` | p.18-31 | Ch2（Henny Big Example p.32-35 不含） |
| `03-random-events.md` | p.36-54 | Ch3（Wutwo Big Example p.55-59 不含） |
| `04-scenes.md` | p.60-115 | Ch4（Guardian Big Example p.116-123 不含） |
| `05-variations.md` | p.124-177 | Ch5 可选规则 |
| `06-rules-summary.md` | p.187-192 | Ch7 官方摘要 |

### tables/ 页码分布
| 文件 | PDF 页 |
|---|---|
| `fate-chart.md` | p.20, 195 |
| `fate-chart-variants.md` | p.148-149, 222-223 |
| `fate-question-answers.md` | p.25, 195 |
| `fate-check-modifiers.md` | p.27, 196 |
| `random-event-focus.md` | p.38-44, 198-199 |
| `meaning-actions.md` | p.48, 200 |
| `meaning-descriptions.md` | p.49, 201 |
| `meaning-elements.md` | p.50, 88-106, 202-216 |
| `scene-adjustment.md` | p.71, 217 |
| `npc-behavior.md` | p.110, 218 |
| `npc-statistics.md` | p.128, 218 |
| `thread-progress-track.md` | p.133, 219-220 |
| `adventure-features.md` | p.161-165, 225-226 |

### examples/ 页码
| 文件 | PDF 页 |
|---|---|
| `01-henny-in-z-land.md` | p.32-35 |
| `02-wutwo-labs.md` | p.55-59 |
| `03-guardian-of-chosen-one.md` | p.116-123 |
| `04-the-big-example.md` | p.178-186 |

### sheets/ 页码
| 文件 | PDF 页 |
|---|---|
| `adventure-journal.md` | p.77-84 叙述 + p.193 模板 |
| `keyed-scenes.md` | p.150-154, 224 |

## 5. 质量校验清单

- [ ] Fate Chart 9×9 矩阵逐格核对（PDF p.20）
- [ ] Meaning Tables 每张表恰好 100 条
- [ ] engine/ 无叙述性连接句（`grep -E "Now let's|As we've seen|Let's discuss"` 应为空）
- [ ] 所有跨文件引用 `→ path/file.md` 指向真实文件
- [ ] Big Examples 的骰点 / Chaos Factor 转换 / scene 边界与 PDF 原文逐回合一致
- [ ] `engine/07-interpretation-principles.md` 每条原则都有源引用

## 6. 分对话工作计划

见 `docs/superpowers/plans/2026-04-22-mythic-gme-import.md` §Task 1-8。
````

- [ ] **Step 7: Update `.claude/CLAUDE.md` — add Mythic to status table (§1)**

Insert a new row into the "支持的游戏系统" table after the existing rows. Use Edit to add after the `Shadowdark` row:

Find: `| 其他系统                 | —          | 按需添加 | \`{System}/\`               | \`output/{System}/\`         |`

Insert immediately before it:
```
| Mythic GME 2e            | Mythic     | 导入中   | `Mythic GME/`             | `output/Mythic/`           |
```

- [ ] **Step 8: Update `.claude/CLAUDE.md` — add Mythic to guides table (§4)**

Find the guides table. Insert a new row after `| Cairn 2e         | ... |`:
```
| Mythic GME 2e    | `.claude/mythic-import-guide.md`          | Solo storytelling engine → 5 目录 37 文件（AI-facing）   |
```

- [ ] **Step 9: Commit**

```bash
git add .claude/mythic-import-guide.md .claude/CLAUDE.md
# intermediate raw md/txt next to PDF are gitignored
git commit -m "mythic: scaffold import guide + CLAUDE.md status rows"
```

Verify `git status` shows a clean tree except for `.claude/worktrees/` (already untracked).

---

## Task 1: `rules/` Ch1 + Ch2 — Mythic Adventures + Fate Questions

**Files:**
- Create: `output/Mythic/rules/00-mythic-journey.md`
- Create: `output/Mythic/rules/01-mythic-adventures.md`
- Create: `output/Mythic/rules/02-fate-questions.md`

- [ ] **Step 1: Slice raw md for p.4 (Mythic Journey preface)**

Read the raw md section that maps to PDF p.4 ("A Mythic Journey" preface by Tana Pigeon). Copy its prose into `00-mythic-journey.md`.

- [ ] **Step 2: Write `00-mythic-journey.md`**

Template:
```markdown
# A Mythic Journey

> Source: *Mythic Game Master Emulator 2nd Edition*, p.4 (preface by Tana Pigeon).

## Index

This file contains the author's preface only. No mechanical content.

---

[preface prose transcribed from raw md]
```

- [ ] **Step 3: Slice raw md for p.8-17 (Ch1 Mythic Adventures)**

Read raw md for p.8-17. Sub-sections per the PDF TOC:
- Mythic, Your Role-Playing Partner (p.8)
- Fate Questions (p.10)
- Chaos Factor (p.10)
- Random Events (p.12)
- Scenes (p.12)
- Lists (p.13)
- Meaning (p.13)
- Expectations & Interpretations (p.14)
- Your Chosen RPG (p.16)

- [ ] **Step 4: Write `01-mythic-adventures.md`**

Template:
```markdown
# Mythic Adventures

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch1, p.8-17.
> High-level overview of Mythic's five pillars: Fate Questions, Chaos Factor, Random Events, Scenes, Lists, Meaning.

## Index

1. [Mythic, Your Role-Playing Partner](#mythic-your-role-playing-partner)
2. [Fate Questions (Overview)](#fate-questions-overview)
3. [Chaos Factor (Overview)](#chaos-factor-overview)
4. [Random Events (Overview)](#random-events-overview)
5. [Scenes (Overview)](#scenes-overview)
6. [Lists (Overview)](#lists-overview)
7. [Meaning (Overview)](#meaning-overview)
8. [Expectations & Interpretations](#expectations--interpretations)
9. [Your Chosen RPG](#your-chosen-rpg)

---

## Mythic, Your Role-Playing Partner

*(p.8)*

[transcribed paragraphs, preserving Crane's voice and all inline mini-examples]

## Fate Questions (Overview)

*(p.10)*

[transcribed]

... [one ## per sub-section, in PDF order]
```

All inline mini-examples (blast shields, occult investigator, etc.) stay in the flow.

- [ ] **Step 5: Slice raw md for p.18-31 (Ch2 Fate Questions, Big Example EXCLUDED)**

Read raw md from "Fate Questions" chapter opener to immediately before "The Big Fate Question Example: Henny In Z Land" (which starts p.32). Sub-sections:
- When To Ask A Fate Question (p.18)
- The Fate Chart (p.19)
- Fate Chart [the table itself] (p.20)
- Example Odds (p.21)
- To Answer Your Question (p.24)
- Fate Question Answers (p.25)
- The Fate Check (p.26)
- Fate Check Modifiers (p.27)
- Fate Check Answers (p.27)
- When To Run With Expectations And When To Question Them (p.28)
- Using Fate Questions To Replace RPG Rules (p.29)
- Fate Questions As RPG Rules (p.31)

- [ ] **Step 6: Write `02-fate-questions.md`**

Template:
```markdown
# Fate Questions

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch2, p.18-31.
> The Big Fate Question Example (Henny In Z Land, p.32-35) is in `examples/01-henny-in-z-land.md`.

## Index

1. [When To Ask A Fate Question](#when-to-ask-a-fate-question)
2. [The Fate Chart](#the-fate-chart)
3. [Example Odds](#example-odds)
4. [To Answer Your Question](#to-answer-your-question)
5. [Fate Question Answers](#fate-question-answers)
6. [The Fate Check](#the-fate-check)
7. [Fate Check Modifiers](#fate-check-modifiers)
8. [Fate Check Answers](#fate-check-answers)
9. [When To Run With Expectations And When To Question Them](#when-to-run-with-expectations-and-when-to-question-them)
10. [Using Fate Questions To Replace RPG Rules](#using-fate-questions-to-replace-rpg-rules)
11. [Fate Questions As RPG Rules](#fate-questions-as-rpg-rules)

---

[transcribed sections, with the Fate Chart itself rendered as a proper 9×9 markdown table with right-aligned percentage columns]
```

The Fate Chart on p.20 is THE critical table. Extract with care — 9 Odds rows × 9 Chaos Factor columns = 81 cells. Cross-reference every cell against `.txt` via:
```bash
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 20 --stdout
```

- [ ] **Step 7: Validate**

```bash
# Each file has a top H1 and Index
for f in output/Mythic/rules/0{0..2}-*.md; do
  head -3 "$f" | grep -q "^# " || echo "MISSING H1: $f"
done

# No residual "The Big Fate Question Example" content in rules/
grep -l "Henny\|Big Fate Question Example" output/Mythic/rules/0*-*.md && echo "LEAK: Big Example should not be in rules/"

# Spot-check 5 numeric cells in the Fate Chart against raw text
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 20 --stdout | grep -E "50/50|Likely|Nearly"
```

Expected: no stderr output from the first check; no stdout from the second (no Henny leak); Fate Chart numeric cells match.

- [ ] **Step 8: Commit**

```bash
git add output/Mythic/rules/00-mythic-journey.md output/Mythic/rules/01-mythic-adventures.md output/Mythic/rules/02-fate-questions.md
git commit -m "mythic: add rules Ch1-2 (Mythic Adventures + Fate Questions)"
```

---

## Task 2: `rules/` Ch3 + Ch4 — Random Events + Scenes

**Files:**
- Create: `output/Mythic/rules/03-random-events.md`
- Create: `output/Mythic/rules/04-scenes.md`

- [ ] **Step 1: Slice raw md for p.36-54 (Ch3 Random Events, Wutwo Big Example EXCLUDED)**

Sub-sections (per TOC):
- Generating Random Events (p.37)
- Context (p.37)
- Event Focus (p.37)
- Random Event Focus Table (p.38)
- Choosing The Event Focus (p.44)
- Lists As Random Tables (p.45)
- Adventure Lists (p.46)
- Event Meaning (p.47)
- Meaning Tables: Actions (p.48)
- Meaning Tables: Descriptions (p.49)
- Meaning Tables: Elements (p.50)
- Interpreting The Event (p.52)

Stop at p.54 (Wutwo Big Example starts p.55).

- [ ] **Step 2: Write `03-random-events.md`**

Template:
```markdown
# Random Events

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch3, p.36-54.
> Meaning Tables themselves are transcribed in `../tables/meaning-{actions,descriptions,elements}.md`.
> The Big Random Event Example (Wutwo Labs, p.55-59) is in `examples/02-wutwo-labs.md`.

## Index
[11 sub-sections listed above]

---

[transcribed prose; for the Meaning Tables sections, include the introductory rules text but reference tables/ for the full entries — do NOT duplicate the 100-entry lists here]
```

- [ ] **Step 3: Slice raw md for p.60-115 (Ch4 Scenes, Guardian Big Example EXCLUDED)**

Sub-sections (per TOC):
- Making A Big Scene (p.60)
- Preparing Lists (p.61)
- Threads & Characters Lists (p.61)
- Scene Structure (p.64)
- The First Scene (p.64)
- Expected Scenes (p.68)
- Altered Scenes (p.68)
- Scene Adjustment Table (p.71)
- Interrupt Scenes (p.73)
- Playing Out The Scene (p.74)
- Adventure Journal (p.77)
- Discovering Meaning (p.85)
- Meaning Tables: Elements (p.88) — the ~100 sub-tables
- Generating NPC Behavior (p.107)
- NPC Behavior Table (p.110)
- End Of Scene Bookkeeping (p.112)

Stop at p.115 (Guardian Big Example starts p.116).

Note: the Meaning Tables: Elements section (p.88-106) contains ~100 themed sub-tables. In `rules/04-scenes.md`, include only the introductory/rules text and a short "See `tables/meaning-elements.md` for all ~100 themed sub-tables." pointer. The tables themselves go in tables/ (Task 6).

- [ ] **Step 4: Write `04-scenes.md`**

Template similar to 03-random-events.md. The file is the longest in rules/ (~55 pages of prose). Allow this — it's one coherent chapter.

- [ ] **Step 5: Validate**

```bash
# Big Examples should not leak
grep -l "Wutwo\|Weird Times At Wutwo\|Guardian Of The Chosen One" output/Mythic/rules/0{3,4}-*.md && echo "LEAK"

# Page range headers present
grep -E "\(p\.38\)|\(p\.47\)|\(p\.85\)|\(p\.107\)" output/Mythic/rules/03-random-events.md output/Mythic/rules/04-scenes.md
```

Expected: first check silent; second shows hits for each page marker.

- [ ] **Step 6: Commit**

```bash
git add output/Mythic/rules/03-random-events.md output/Mythic/rules/04-scenes.md
git commit -m "mythic: add rules Ch3-4 (Random Events + Scenes)"
```

---

## Task 3: `rules/` Ch5 + Rules Summary

**Files:**
- Create: `output/Mythic/rules/05-variations.md`
- Create: `output/Mythic/rules/06-rules-summary.md`

- [ ] **Step 1: Slice raw md for p.124-177 (Ch5 Variations)**

Sub-sections (per TOC):
- Getting Prepared For A Solo Adventure (p.124)
- Determining NPC Statistics (p.128)
- NPC Statistics Table (p.128)
- Getting The Most Out Of Sourcebooks (p.129)
- The Thread Progress Track (p.133)
- Discovery Fate Question (p.137)
- Thread Discovery Check (p.138)
- Diversifying Threads (p.141)
- Resolving Character vs. Player Knowledge (p.142)
- Player Vs. PC Knowledge (p.145)
- Conclusive Adventure Conclusions (p.146)
- Mid-Chaos Fate Chart (p.148)
- Mid-Chaos Fate Check Modifiers (p.148)
- Low-Chaos Fate Chart (p.149)
- Low-Chaos Fate Check Modifiers (p.149)
- No-Chaos Fate Chart (p.149)
- What Is "A Session" In Solo Play? (p.149)
- Control Your Adventures With Keyed Scenes (p.150)
- Keyed Scenes Record Sheet (p.154)
- Using Mythic With Prepared Adventures (p.157)
- Adventure Features List (p.161)
- Prepared Adventure Event Focus Table (p.165)
- Handling Complicated Campaigns (p.167)
- Peril Points (p.171)
- Using The Adventure Crafter With Mythic (p.172)
- Where To Get More Support (p.176)

- [ ] **Step 2: Write `05-variations.md`**

Template:
```markdown
# Variations

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch5, p.124-177.
> Optional/advanced rules. Each Variation can be mixed and matched with the core system.
> Where tables (Mid-Chaos Fate Chart, NPC Statistics, Adventure Features, etc.) are referenced, see `../tables/` for the pure-data version.

## Index
[all 26 sub-sections above]

---

[transcribed]
```

- [ ] **Step 3: Slice raw md for p.187-192 (Ch7 Rules Summary)**

This is Crane's own terse end-of-book recap. Transcribe verbatim.

- [ ] **Step 4: Write `06-rules-summary.md`**

Template:
```markdown
# Rules Summary

> Source: *Mythic Game Master Emulator 2nd Edition*, Ch7 "Rules Summary", p.187-192.
> This is the author's own end-of-book recap. It complements `engine/` (which is procedurally oriented) by providing a terse memory-anchor reading.

## Index

[auto-structured headings matching PDF]

---

[transcribed]
```

- [ ] **Step 5: Validate**

```bash
# Ch5 should reference all 9 variation names
for term in "Keyed Scenes" "Peril Points" "Thread Progress" "Mid-Chaos" "Adventure Features"; do
  grep -q "$term" output/Mythic/rules/05-variations.md || echo "MISSING: $term in 05-variations.md"
done
```

Expected: silent (all present).

- [ ] **Step 6: Commit**

```bash
git add output/Mythic/rules/05-variations.md output/Mythic/rules/06-rules-summary.md
git commit -m "mythic: add rules Ch5 (Variations) + Ch7 (Rules Summary)"
```

---

## Task 4: `tables/` — Fate + Event + NPC + Scene (10 tables)

**Files:**
- Create: `output/Mythic/tables/fate-chart.md`
- Create: `output/Mythic/tables/fate-chart-variants.md`
- Create: `output/Mythic/tables/fate-question-answers.md`
- Create: `output/Mythic/tables/fate-check-modifiers.md`
- Create: `output/Mythic/tables/random-event-focus.md`
- Create: `output/Mythic/tables/scene-adjustment.md`
- Create: `output/Mythic/tables/npc-behavior.md`
- Create: `output/Mythic/tables/npc-statistics.md`
- Create: `output/Mythic/tables/thread-progress-track.md`
- Create: `output/Mythic/tables/adventure-features.md`

- [ ] **Step 1: Write `fate-chart.md` (the critical 9×9 matrix)**

Primary source: PDF p.20. Secondary (should be identical): p.195 (Collected Tables).

Template:
```markdown
# Fate Chart

> When: answering a Fate Question (Odds + Chaos Factor → percentile).
> Input: chosen Odds (Impossible … Certain), current Chaos Factor (1-9).
> Output: percentile target for 1d100 Yes roll.
> Source: PDF p.20 / 195.

|                     |  CF 1 |  CF 2 |  CF 3 |  CF 4 |  CF 5 |  CF 6 |  CF 7 |  CF 8 |  CF 9 |
|---------------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| Certain             |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Nearly Certain      |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Very Likely         |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Likely              |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| 50/50               |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Unlikely            |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Very Unlikely       |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Nearly Impossible   |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
| Impossible          |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |   ... |
```

Fill each cell by reading the raw md for p.20 AND cross-checking against p.195 AND against `pdf_extract.py --pages 20 --stdout`. All three sources must agree for each cell.

- [ ] **Step 2: Write `fate-chart-variants.md` (Mid/Low/No-Chaos variants)**

Sources: p.148-149, 222-223. Three variant Fate Charts + two modifier variants.

Template:
```markdown
# Fate Chart Variants

> When: running a Mid-Chaos / Low-Chaos / No-Chaos adventure (see `rules/05-variations.md`).
> Input: variant choice + Odds + Chaos Factor.
> Output: percentile target.
> Source: PDF p.148-149, 222-223.

## Mid-Chaos Fate Chart

[9×9 table, right-aligned]

## Mid-Chaos Fate Check Modifiers

[table of +/- modifiers]

## Low-Chaos Fate Chart

[9×9 table]

## Low-Chaos Fate Check Modifiers

[table]

## No-Chaos Fate Chart

[9×9 table — note: p.149 No-Chaos is simpler, fewer columns]
```

- [ ] **Step 3: Write remaining 8 tables following the same pattern**

Each file starts with 3-line `When/Input/Output/Source:` header. Each table is transcribed as a markdown table with right-aligned numeric columns.

- `fate-question-answers.md` — p.25, 195: percentile → Yes/No/Exceptional + Random Event trigger rule (matching digits)
- `fate-check-modifiers.md` — p.27, 196: list of +/- modifiers for Fate Check variant
- `random-event-focus.md` — p.38-44, 198-199: 10-category Event Focus table + the Prepared Adventure variant on p.226
- `scene-adjustment.md` — p.71, 217: Scene Adjustment outcomes
- `npc-behavior.md` — p.110, 218: NPC Behavior table with behavior words
- `npc-statistics.md` — p.128, 218: quick NPC stat generation
- `thread-progress-track.md` — p.133, 219-220: Thread Progress Check + Discovery Check tables
- `adventure-features.md` — p.161-165, 225-226: Prepared Adventure Feature list + its Event Focus variant

- [ ] **Step 4: Validate — Fate Chart spot-check**

Pick 10 random cells from `fate-chart.md` and verify each against p.20 extraction:
```bash
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 20 --stdout > /tmp/p20.txt
# Manually spot-check: e.g., "Likely" row × "CF 5" column value in table matches raw text
```

- [ ] **Step 5: Validate — header conformance**

```bash
for f in output/Mythic/tables/*.md; do
  head -5 "$f" | grep -q "^> When:" || echo "MISSING When: header in $f"
  head -5 "$f" | grep -q "^> Source:" || echo "MISSING Source: header in $f"
done
```

Expected: silent.

- [ ] **Step 6: Commit**

```bash
git add output/Mythic/tables/fate-chart.md output/Mythic/tables/fate-chart-variants.md output/Mythic/tables/fate-question-answers.md output/Mythic/tables/fate-check-modifiers.md output/Mythic/tables/random-event-focus.md output/Mythic/tables/scene-adjustment.md output/Mythic/tables/npc-behavior.md output/Mythic/tables/npc-statistics.md output/Mythic/tables/thread-progress-track.md output/Mythic/tables/adventure-features.md
git commit -m "mythic: add tables — Fate, Event, NPC, Scene (10 tables)"
```

---

## Task 5: `tables/` — Meaning Actions + Descriptions

**Files:**
- Create: `output/Mythic/tables/meaning-actions.md`
- Create: `output/Mythic/tables/meaning-descriptions.md`

- [ ] **Step 1: Extract p.48 (Actions) and p.49 (Descriptions) from raw md**

Primary source pages. Verify against p.200, 201 (Collected Tables duplicate). If any discrepancy, prefer the primary source (Ch3) and flag the difference.

- [ ] **Step 2: Write `meaning-actions.md`**

Each Meaning Table has **two columns of 100 entries each** (Action 1 and Action 2). Roll d100 on each column, combine for a compound result.

Template:
```markdown
# Meaning Tables — Actions

> When: interpreting a Random Event or generating random narrative content.
> Input: two d100 rolls.
> Output: a compound action seed (Action 1 + Action 2).
> Source: PDF p.48 (primary); duplicated at p.200.

## How To Read

Roll d100 twice. The first roll selects from Action 1; the second from Action 2. Treat the pair as a single compound seed — force synthesis rather than interpreting them independently. See `../engine/07-interpretation-principles.md` for guidance.

---

## Action 1 / Action 2

|   # | Action 1      | Action 2      |
|----:|---------------|---------------|
|   1 | ...           | ...           |
|   2 | ...           | ...           |
|  ...|               |               |
| 100 | ...           | ...           |
```

Transcribe all 100 pairs from raw md. Preserve exact wording (Mythic's word choices are deliberate — "Hasten", "Oppose", "Debase", etc.).

- [ ] **Step 3: Write `meaning-descriptions.md`**

Same structure, source p.49 + p.201.

- [ ] **Step 4: Validate — exact 100 rows per file**

```bash
for f in output/Mythic/tables/meaning-actions.md output/Mythic/tables/meaning-descriptions.md; do
  # Count data rows (skip header and separator)
  rows=$(grep -cE "^\| *[0-9]+ *\|" "$f")
  echo "$f: $rows rows"
  [ "$rows" -eq 100 ] || echo "FAIL: expected 100, got $rows"
done
```

Expected: both files report `100 rows`, no FAIL lines.

- [ ] **Step 5: Validate — primary vs Collected Tables agreement**

```bash
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 48,49,200,201 --stdout > /tmp/meaning-check.txt
# Spot-check 5 entries: entry #1, #25, #50, #75, #100 in each table
```

- [ ] **Step 6: Commit**

```bash
git add output/Mythic/tables/meaning-actions.md output/Mythic/tables/meaning-descriptions.md
git commit -m "mythic: add tables — Meaning Actions + Descriptions (2×100 entries each)"
```

---

## Task 6: `tables/` — Meaning Elements (the ~100 sub-tables)

**Files:**
- Create: `output/Mythic/tables/meaning-elements.md`

This is the largest single file in the import. Split into Task 6a + Task 6b if context-pressured.

- [ ] **Step 1: Enumerate all sub-tables**

Extract p.50 (introductory mechanics) + p.88-106 (bulk themed tables) + p.202-216 (Collected duplicate) from raw md. Build a list of all `## <Theme>` headings. Mythic 2e has ~100 themed Meaning Tables such as: Adventure Tone, Alien Species, Ambush, Animals, Armies, Artifacts, Characters, Characters Appearance, Characters Background, Characters Descriptors, Characters Identity, Characters Motivation, Characters Personality Traits, Characters Skills, Characters Traits Flaws, Characters Visuals, Cities, Colors, Combat, Conspiracies, Creatures, Crews, Cults, Curses, Deities, Disasters, Domiciles, Dungeons, Elements, Events, Factions, Forests, Gadgets, Gifts, Health, Heists, Hierarchies, Horror, Investigations, Legal, Locations, Magic, Magic Items, Mass Combat, Military, Missions, Monsters, Mysteries, Mystical, Names Common, Names Fantasy, NPC Goals, NPC Identity Scifi, NPC Personality, Objects Mundane, Occupations, Oddities, Organizations, Parties Celebrations, Passages, Physical Event, Places, Plot Twists, Plots, Politics, Powers Abilities, Professions, Quests, Relationships, Religions, Rulerships, Rumors, Scavenging, Scenery, Scifi, Smells, Societies, Sounds, Spaceships, Spells, Starships, Stores Shops, Strongholds, Structures, Tasks, Tavern Names, Technology Advanced, Technology Simple, Terrain Aquatic, Terrain Cold, Terrain Desert, Terrain Forest, Terrain Mountain, Terrain Swamp, Terrain Urban, Tombs, Traps, Treasure, Vehicles, Village, Visions Dreams, Weapons, Weather, Wilderness, Wounds.

(Exact list may differ slightly — use what the raw md yields as ground truth, not this pre-guess.)

- [ ] **Step 2: Decide on ordering**

**Decision**: use PDF order (same as printed book). Rationale: matches reader expectations; easier to validate against source; alphabetical ordering can be added later as an index if useful.

Override only if the raw md reveals the PDF itself is alphabetical — in which case keep PDF order regardless, since the two coincide.

- [ ] **Step 3: Write file header + index**

Template:
```markdown
# Meaning Tables — Elements

> When: generating random narrative content matching a specific theme (weather, a city, a dungeon, etc.).
> Input: a chosen theme + two d100 rolls.
> Output: a compound element (word 1 + word 2) for interpretation.
> Source: PDF p.50 (rules), p.88-106 (themed tables), p.202-216 (Collected duplicate).

## How To Read

Each sub-table below is a themed pair of d100 columns. Use the table matching your current narrative need. Combine the two rolls as a compound seed, following `../engine/07-interpretation-principles.md`.

---

## Index

- [Adventure Tone](#adventure-tone)
- [Alien Species](#alien-species)
[... one link per sub-table, in PDF order ...]

---

## Adventure Tone

*(p.88)*

|   # | Column 1       | Column 2       |
|----:|----------------|----------------|
|   1 | ...            | ...            |
[...100 rows]

---

## Alien Species

*(p.88)*

[...100 rows]

[... one ## per sub-table, each with ## heading + `*(p.NN)*` marker + 100-row table ...]
```

- [ ] **Step 4: Transcribe all sub-tables**

Work through raw md systematically. For each theme: write `## Theme Name`, `*(p.NN)*`, the table. Each table must have exactly 100 rows.

If context pressure grows, commit partial progress and continue in a follow-up session.

- [ ] **Step 5: Validate — every sub-table has exactly 100 rows**

```bash
python3 - <<'EOF'
import re
with open('output/Mythic/tables/meaning-elements.md') as f:
    content = f.read()
sections = re.split(r'^## ', content, flags=re.MULTILINE)[2:]  # skip preamble and Index
for s in sections:
    name = s.splitlines()[0].strip()
    rows = len(re.findall(r'^\| *\d+ *\|', s, flags=re.MULTILINE))
    if rows != 100:
        print(f"FAIL {name}: {rows} rows")
    else:
        print(f"OK   {name}: 100 rows")
EOF
```

Expected: all `OK` lines; no `FAIL`.

- [ ] **Step 6: Validate — index anchors match sub-tables**

```bash
# count ## sub-table headings (excluding top-level preamble and Index)
heads=$(grep -cE "^## [A-Z]" output/Mythic/tables/meaning-elements.md)
# count index entries
idx=$(grep -cE "^- \[.*?\]\(#" output/Mythic/tables/meaning-elements.md)
echo "Sub-tables: $heads / Index entries: $idx"
[ "$heads" -eq "$((idx + 2))" ] || echo "MAYBE OK: How To Read + Index count as ## — verify manually"
```

Confirm the numbers line up, accounting for the two non-sub-table `##` sections ("How To Read" and "Index").

- [ ] **Step 7: Commit**

```bash
git add output/Mythic/tables/meaning-elements.md
git commit -m "mythic: add tables — Meaning Elements (~100 themed sub-tables)"
```

If work was split across sessions, commit each partial chunk with a chunk identifier in the message, e.g.:
```bash
git commit -m "mythic: add tables — Meaning Elements (chunk 1/2, themes A–M)"
```

---

## Task 7: `examples/` (4 Big Examples + index) + `sheets/` (2 templates)

**Files:**
- Create: `output/Mythic/examples/_index.md`
- Create: `output/Mythic/examples/01-henny-in-z-land.md`
- Create: `output/Mythic/examples/02-wutwo-labs.md`
- Create: `output/Mythic/examples/03-guardian-of-chosen-one.md`
- Create: `output/Mythic/examples/04-the-big-example.md`
- Create: `output/Mythic/sheets/adventure-journal.md`
- Create: `output/Mythic/sheets/keyed-scenes.md`

- [ ] **Step 1: Write `01-henny-in-z-land.md` (p.32-35)**

Template:
```markdown
---
source: pdf
chaos-focus: [fate-questions, interpretation]
length-turns: <count-from-source>
length-scenes: <count-from-source>
---

# The Big Fate Question Example: Henny In Z Land

> Source: *Mythic Game Master Emulator 2nd Edition*, p.32-35.
> Demonstrates the full Fate Question loop: Odds selection → Fate Chart → roll → interpret → narrate → iterate.

## Setup

[PC name, situation, starting Chaos Factor — transcribed from p.32]

## Play

### Turn 1 — [what PC is doing]

**Question:** [exact phrasing from PDF]
**Odds:** [the Odds the Player chose]
**Chaos Factor:** [current CF]
**Roll:** [d100 roll]
**Result:** [Yes / No / Exceptional Yes / Exceptional No]
**Interpretation:** [narrative continuation]

### Turn 2 — ...

[one subsection per turn]

## Outcome

[how the scene resolves, chaos factor transitions]
```

Transcribe all turns exactly as written. Preserve every roll, Odds, CF value — these are the ground truth for engine/interpretation-principles extraction later.

- [ ] **Step 2: Write `02-wutwo-labs.md` (p.55-59)**

Same template. This example focuses on Random Events — turns here show Event Focus rolls and Meaning Table interpretations.

Frontmatter:
```yaml
source: pdf
chaos-focus: [random-events, meaning-tables, event-focus]
```

- [ ] **Step 3: Write `03-guardian-of-chosen-one.md` (p.116-123)**

Same template. This example focuses on Scenes — First Scene, Expected/Altered/Interrupt transitions, Scene Adjustment Table usage.

Frontmatter:
```yaml
source: pdf
chaos-focus: [scenes, scene-adjustment, interrupt-scenes, threads]
```

- [ ] **Step 4: Write `04-the-big-example.md` (p.178-186)**

Full end-to-end session. Longest example. Same template but may span multiple scenes with scene-level headings:

```markdown
## Scene 1: [name]

### Setup
### Turn 1
### Turn 2
...
### End Of Scene (CF transition, journal update)

## Scene 2: [name]
...
```

Frontmatter:
```yaml
source: pdf
chaos-focus: [full-loop, scenes, fate-questions, random-events, threads, chaos-factor]
```

- [ ] **Step 5: Write `examples/_index.md`**

Template:
```markdown
# Examples Index

> AI loads this file first, then selectively loads matching example files based on `chaos-focus` tags.

## Examples

### 01-henny-in-z-land.md
- **Source**: PDF p.32-35
- **Focus**: fate-questions, interpretation
- **Scope**: [N] turns, 1 scene
- **Why read**: to calibrate how Odds are chosen in context and how an unexpected answer is accepted and narrated.

### 02-wutwo-labs.md
- **Source**: PDF p.55-59
- **Focus**: random-events, meaning-tables, event-focus
- **Scope**: [N] turns, [M] events
- **Why read**: to see Meaning Table rolls interpreted as compound story beats rather than independent words.

### 03-guardian-of-chosen-one.md
- **Source**: PDF p.116-123
- **Focus**: scenes, scene-adjustment, interrupt-scenes, threads
- **Scope**: [N] scenes
- **Why read**: to see when a scene gets Altered vs Interrupted, and how Threads/Characters lists evolve.

### 04-the-big-example.md
- **Source**: PDF p.178-186
- **Focus**: full-loop, scenes, fate-questions, random-events, threads, chaos-factor
- **Scope**: [N] scenes across one full adventure
- **Why read**: to see how Chaos Factor shifts across a session and how multiple mechanisms interact in play.

## Adding Examples

New examples go here as `05+-{short-name}.md` with frontmatter. Add a section above. Preferred sources: user solo-play logs demonstrating non-obvious Mythic decisions.
```

Fill `[N]` placeholders with actual counts from each file.

- [ ] **Step 6: Write `sheets/adventure-journal.md`**

The Adventure Journal rules are described p.77-84 (in Ch4) with a reproducible template at p.193 (Collected Sheets).

Template:
```markdown
# Adventure Journal — Template

> Source: *Mythic Game Master Emulator 2nd Edition*, p.77-84 (rules) + p.193 (template).
> Fill out during play. `../engine/09-session-protocol.md` prescribes when to write each section.

## Header

- **Adventure Name**:
- **Chosen RPG System**:
- **Starting Chaos Factor**: 5 (default)
- **Date Started**:

## Threads List

An open list of plot threads the PC is pursuing. Each thread: a short verb-object phrase ("escape the lab", "find sister"). Add new threads during play via random events or in-fiction decisions; resolve or remove as they conclude.

1. [thread]
2. [thread]
...

## Characters List

NPCs and relevant non-PC entities. Short tags: name + role + allegiance.

1. [name] — [role], [allegiance/relationship]
...

## Scene Log

Per scene: setup, turns taken, events triggered, resolution, end-of-scene CF.

### Scene 1 — [name]
- **Setup**: (Expected / Altered / Interrupt)
- **Events**: [random events that fired]
- **Resolution**: [one-sentence outcome]
- **End CF**: [number]

### Scene 2 — ...

## End-Of-Session Bookkeeping

- **Final CF**:
- **New threads added**:
- **Threads resolved**:
- **Cliffhanger / resume point**:
```

- [ ] **Step 7: Write `sheets/keyed-scenes.md`**

Source: p.150-154 (rules) + p.224 (template).

Template:
```markdown
# Keyed Scenes Record Sheet

> Source: *Mythic Game Master Emulator 2nd Edition*, p.150-154 (rules) + p.224 (template).
> Keyed Scenes let the Player pre-plan future scenes that MUST happen at specified Chaos Factor or Thread states. See `../rules/05-variations.md` §Keyed Scenes.

## Keyed Scenes

Up to 5 pre-keyed future scenes. Each scene has a trigger condition and a brief setup.

### Keyed Scene 1
- **Trigger**: (e.g., "CF reaches 7" / "Thread 'escape lab' progresses twice")
- **Setup**: [one-paragraph setup]
- **Status**: (pending / fired / expired)

### Keyed Scene 2
...

### Keyed Scene 5
...
```

- [ ] **Step 8: Validate — example frontmatter present**

```bash
for f in output/Mythic/examples/01-*.md output/Mythic/examples/02-*.md output/Mythic/examples/03-*.md output/Mythic/examples/04-*.md; do
  head -1 "$f" | grep -q "^---$" || echo "MISSING frontmatter: $f"
done
```

Expected: silent.

- [ ] **Step 9: Validate — dice roll fidelity spot-check**

Pick 3 random turns from each example file. Compare the recorded `**Roll:**` / `**Chaos Factor:**` / `**Odds:**` values to the PDF raw text:
```bash
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 32-35,55-59,116-123,178-186 --stdout > /tmp/examples-check.txt
# Manual spot-check
```

Discrepancy = bug. Fix before commit.

- [ ] **Step 10: Commit**

```bash
git add output/Mythic/examples/ output/Mythic/sheets/
git commit -m "mythic: add examples (4 Big Examples + index) + sheets (2 templates)"
```

---

## Task 8: `engine/` — 10 refined procedure files

This is the highest-judgment task. It synthesizes everything from Tasks 1-7 into the AI runtime. Do Tasks 1-7 first; this Task depends on their content.

**Files:**
- Create: `output/Mythic/engine/00-core-loop.md`
- Create: `output/Mythic/engine/01-fate-questions.md`
- Create: `output/Mythic/engine/02-random-events.md`
- Create: `output/Mythic/engine/03-scenes.md`
- Create: `output/Mythic/engine/04-threads-and-characters.md`
- Create: `output/Mythic/engine/05-chaos-factor.md`
- Create: `output/Mythic/engine/06-npc-behavior.md`
- Create: `output/Mythic/engine/07-interpretation-principles.md`
- Create: `output/Mythic/engine/08-variations.md`
- Create: `output/Mythic/engine/09-session-protocol.md`

- [ ] **Step 1: Read all `rules/` and `examples/` content**

Before writing a single engine file, load into context:
- `output/Mythic/rules/*.md` (all 7)
- `output/Mythic/examples/*.md` (all 5)
- Relevant `output/Mythic/tables/*.md` for cross-ref paths

Do not paraphrase from memory. Write engine files against the loaded source.

- [ ] **Step 2: Write `00-core-loop.md`**

The top-level cycle. Mythic has no single canonical "game loop" statement; synthesize from Ch4 Scene Structure + Ch5 session guidance.

Template:
```markdown
# Core Loop

> The end-to-end cycle for running a Mythic solo session. Load first at session start.

## When To Use
- At start of every Mythic session (`→ engine/09-session-protocol.md` for initial setup).
- As the outer loop governing when to invoke other engine/ files.

## Procedure
1. **Scene Setup**. Decide Expected Scene; roll Scene Adjustment if applicable (`→ engine/03-scenes.md`).
2. **Play the scene**:
   a. Improvise narrative based on Expectations.
   b. At any narrative tension point, invoke `→ engine/01-fate-questions.md`.
   c. On matching-digit Fate roll, invoke `→ engine/02-random-events.md`.
   d. For NPC actions/reactions, invoke `→ engine/06-npc-behavior.md`.
3. **End of Scene**. Update Chaos Factor (`→ engine/05-chaos-factor.md`). Update Threads / Characters (`→ engine/04-threads-and-characters.md`). Record in Adventure Journal (`→ sheets/adventure-journal.md`).
4. **Loop to Step 1** for next scene, OR conclude session per `→ engine/09-session-protocol.md`.

## Decision Tree
- Scene starts → Expected? Altered? Interrupt? (see `engine/03-scenes.md`)
- Mid-scene, uncertainty arises → Fate Question? (see `engine/01-fate-questions.md`)
- Matching digits on Fate roll → Random Event (see `engine/02-random-events.md`)

## Failure modes
- Skipping Chaos Factor updates → story momentum feels flat.
- Over-asking Fate Questions for things Player can just decide → undermines Expectations-driven play (see `engine/07-interpretation-principles.md` P-01).
- Not using Adventure Journal → lose Thread continuity across sessions.

## Cross-refs
→ engine/01-fate-questions.md
→ engine/02-random-events.md
→ engine/03-scenes.md
→ engine/04-threads-and-characters.md
→ engine/05-chaos-factor.md
→ engine/06-npc-behavior.md
→ engine/09-session-protocol.md
```

- [ ] **Step 3: Write `01-fate-questions.md` through `06-npc-behavior.md`**

Each follows the same shell: `## When To Use / ## Procedure / ## Decision Tree / ## Failure modes / ## Cross-refs`. Keep each file under 200 lines.

Per-file content notes:

- `01-fate-questions.md` — draws from rules/02-fate-questions.md. Procedure = the 6-step flow on p.18-27. Decision tree = how to pick Odds given Context.
- `02-random-events.md` — draws from rules/03-random-events.md. Procedure = Event Focus → Meaning → Interpretation. Decision tree = how to handle Event Focus categories (Remote / NPC / New NPC / Move Toward / Move Away / Close Thread / PC Negative / PC Positive / Ambiguous / Current Context — confirm exact list from source).
- `03-scenes.md` — draws from rules/04-scenes.md. Procedure = First Scene setup → iterate Expected/Altered/Interrupt. Decision tree = when to alter vs interrupt (Scene Adjustment Table conditions).
- `04-threads-and-characters.md` — draws from rules/04-scenes.md §Threads & Characters Lists + rules/05-variations.md §Thread Progress Track. Procedure = maintenance (add/remove/resolve).
- `05-chaos-factor.md` — synthesis from multiple rules/ chapters. Procedure = CF as a narrative throttle; increase on failure/loss of control, decrease on success.
- `06-npc-behavior.md` — draws from rules/04-scenes.md §Generating NPC Behavior.

- [ ] **Step 4: Write `07-interpretation-principles.md` (the highest-leverage file)**

Method per `.claude/mythic-import-guide.md` §3:
1. Read all 4 example files in `output/Mythic/examples/`.
2. Scan rules/ sections explicitly about interpretation: rules/01-mythic-adventures.md §Expectations & Interpretations, rules/02-fate-questions.md §When To Run With Expectations, rules/03-random-events.md §Interpreting The Event, rules/04-scenes.md §Discovering Meaning, §Playing Out The Scene.
3. Extract patterns. Each pattern becomes an imperative principle with source citation.

Template:
```markdown
# Interpretation Principles

> Distilled heuristics for turning Mythic's mechanical outputs into coherent narrative. Load alongside engine/ at session start. Reference when interpretation feels stale.

## How To Use
Principles are numbered P-01, P-02, ... Use them as a checklist when a roll result feels ambiguous or forced. Each cites its source; audit-friendly.

---

## P-01 Accept, don't re-roll
When a Fate answer contradicts expectation, accept it as truth and retroactively find the cause. Never re-roll for a "better" answer.
> Source: rules/02-fate-questions.md §When To Run With Expectations; examples/01-henny-in-z-land.md turn [N]

## P-02 [next principle]
[one-sentence imperative] [1-2 sentence rationale]
> Source: [path § or example turn]

[... ~25 principles ...]
```

Write exactly the principles you can cite. Do NOT invent principles without a source. Target 20-28 principles; hard cap 30.

- [ ] **Step 5: Write `08-variations.md`**

Compact summary of each Variation rule from rules/05-variations.md. For each: 1-paragraph summary + when to enable + cross-ref to rules/ for detail.

Resolution of spec §9 open question: include ALL variations. Each gets ~5-15 lines. The summary helps AI pick; full detail lives in rules/.

Variations to cover (from rules/05-variations.md):
- Getting Prepared For A Solo Adventure
- Determining NPC Statistics
- Getting The Most Out Of Sourcebooks
- Thread Progress Track
- Discovery Fate Question
- Thread Discovery Check
- Diversifying Threads
- Resolving Character vs Player Knowledge
- Conclusive Adventure Conclusions
- Mid-Chaos / Low-Chaos / No-Chaos Fate Charts
- Session definition in solo play
- Keyed Scenes
- Using Mythic With Prepared Adventures
- Handling Complicated Campaigns
- Peril Points
- Using The Adventure Crafter With Mythic

- [ ] **Step 6: Write `09-session-protocol.md`**

This file is NEW content (does not exist in the PDF). It's AI-runtime meta-instructions.

Template:
```markdown
# Session Protocol

> AI-runtime instructions for starting, running, and ending a Mythic solo session. Not derived from the PDF; invented for the AI layer.

## At Session Start

1. Load into context:
   - All `engine/*.md` files
   - `sheets/adventure-journal.md` template
   - On-demand `tables/*.md` files as needed per roll
2. If resuming: load the save's `state.yaml` (Threads, Characters, CF, last scene) + `adventure-journal.md` for that save.
3. If new session: ask Player for:
   - Chosen RPG system (D&D, CoC, OSE, etc. — may be "none")
   - PC basics
   - Adventure seed (one sentence)
4. Initialize: CF = 5 (or per variant), empty Threads, empty Characters.
5. Begin with First Scene per `engine/03-scenes.md`.

## During Session

- After each roll: announce the roll, the Odds, the CF, the result tier.
- After each Random Event: narrate the Event Focus category, the Meaning roll, the interpretation.
- Update state.yaml after each scene (Threads delta, Characters delta, CF).

## At Session End

1. Prompt Player to confirm session end point.
2. Update Adventure Journal:
   - End-of-session CF
   - New/resolved Threads
   - Cliffhanger or resume point
3. Save state.yaml.
4. Offer: start next session now, or conclude.

## State Fields

The save's `state.yaml` should carry at minimum:
```yaml
system: <RPG system name or "mythic-only">
chaos-factor: <1-9>
variant: default | mid-chaos | low-chaos | no-chaos
threads:
  - id: t1
    description: <short>
    status: active | resolved | abandoned
characters:
  - id: c1
    name: <name>
    role: <role>
    relationship: <allied | hostile | neutral>
journal-path: saves/<name>/adventure-journal.md
current-scene: <number>
last-scene-outcome: <one-sentence>
```
```

- [ ] **Step 7: Validate — no narrative connectors in engine/**

```bash
grep -rnE "Now let's|As we've seen|Let's discuss|In this section|We'll|Moving on" output/Mythic/engine/
```

Expected: no output. Any hit is a bug; rewrite the offending line in imperative form.

- [ ] **Step 8: Validate — every engine file has the 5-section structure**

```bash
for f in output/Mythic/engine/*.md; do
  for sec in "## When To Use" "## Procedure" "## Cross-refs"; do
    grep -q "^$sec" "$f" || echo "$f missing $sec"
  done
done
```

`09-session-protocol.md` is exempt from this check (it has its own structure). Adjust the loop:

```bash
for f in output/Mythic/engine/0{0..8}-*.md; do
  for sec in "## When To Use" "## Procedure" "## Cross-refs"; do
    grep -q "^$sec" "$f" || echo "$f missing $sec"
  done
done
```

- [ ] **Step 9: Validate — all cross-refs resolve**

```bash
python3 - <<'EOF'
import os, re, glob
errors = 0
for f in glob.glob('output/Mythic/engine/*.md'):
    with open(f) as fh:
        content = fh.read()
    for m in re.finditer(r'→ ((engine|rules|tables|examples|sheets)/[-a-z0-9_]+\.md)', content):
        target = 'output/Mythic/' + m.group(1)
        if not os.path.exists(target):
            print(f'{f}: unresolved → {m.group(1)}')
            errors += 1
print(f'{errors} unresolved cross-refs')
EOF
```

Expected: `0 unresolved cross-refs`.

- [ ] **Step 10: Validate — every principle in 07 cites a source**

```bash
python3 - <<'EOF'
import re
with open('output/Mythic/engine/07-interpretation-principles.md') as f:
    content = f.read()
# Each principle starts with "## P-NN" and should end before the next "## P-" or EOF
principles = re.split(r'^## P-\d+', content, flags=re.MULTILINE)[1:]
uncited = 0
for i, p in enumerate(principles, 1):
    if '> Source:' not in p:
        print(f'P-{i:02d}: no Source citation')
        uncited += 1
print(f'{uncited} uncited principles out of {len(principles)}')
EOF
```

Expected: `0 uncited principles`.

- [ ] **Step 11: Commit**

```bash
git add output/Mythic/engine/
git commit -m "mythic: add engine layer — 10 refined procedure files (AI runtime)"
```

---

## Task 9: Cross-cutting validation + CLAUDE.md status update

**Files:**
- Modify: `.claude/CLAUDE.md` (§1 status: Mythic 导入中 → 已完成)

- [ ] **Step 1: Run full spec §6 validation checklist**

```bash
cd /Users/jack/Projects/trpg-projects/dnd-rules-import

# Check 1: Fate Chart 9×9 — manual comparison
python3 pdf_extract.py "Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf" --pages 20 --stdout > /tmp/fc_p20.txt
cat output/Mythic/tables/fate-chart.md
# Manual diff each of 81 cells

# Check 2: Meaning Tables 100-entry completeness
python3 - <<'EOF'
import re, glob
for f in glob.glob('output/Mythic/tables/meaning-*.md'):
    with open(f) as fh:
        content = fh.read()
    if 'meaning-elements' in f:
        # each ## sub-table should have 100 rows
        sections = re.split(r'^## ', content, flags=re.MULTILINE)[1:]
        for s in sections:
            name = s.splitlines()[0].strip()
            if name in ('How To Read', 'Index'):
                continue
            rows = len(re.findall(r'^\| *\d+ *\|', s, flags=re.MULTILINE))
            if rows != 100:
                print(f'FAIL {f} § {name}: {rows}')
    else:
        rows = len(re.findall(r'^\| *\d+ *\|', content, flags=re.MULTILINE))
        if rows != 100:
            print(f'FAIL {f}: {rows}')
print('meaning-tables check done')
EOF

# Check 3: Engine prose check
grep -rnE "Now let's|As we've seen|Let's discuss|In this section|We'll|Moving on" output/Mythic/engine/ && echo "PROSE LEAK" || echo "prose check clean"

# Check 4: Cross-ref resolution (reuse Task 8 Step 9 script) — expand to all of output/Mythic/
python3 - <<'EOF'
import os, re, glob
errors = 0
for f in glob.glob('output/Mythic/**/*.md', recursive=True):
    with open(f) as fh:
        content = fh.read()
    for m in re.finditer(r'→ ((engine|rules|tables|examples|sheets)/[-a-z0-9_]+\.md)', content):
        target = 'output/Mythic/' + m.group(1)
        if not os.path.exists(target):
            print(f'{f}: unresolved → {m.group(1)}')
            errors += 1
    # also check ../ relative refs
    for m in re.finditer(r'`\.\./((engine|rules|tables|examples|sheets)/[-a-z0-9_]+\.md)`', content):
        target = 'output/Mythic/' + m.group(1)
        if not os.path.exists(target):
            print(f'{f}: unresolved ../{m.group(1)}')
            errors += 1
print(f'{errors} unresolved cross-refs')
EOF

# Check 5: Big Examples fidelity — manual spot-check on random turns
# Check 6: Principle citations (reuse Task 8 Step 10)
```

- [ ] **Step 2: Fix any failures**

For each validation failure, make the focused fix. Commit per-fix:

```bash
git add <fixed files>
git commit -m "mythic: fix <specific issue>"
```

- [ ] **Step 3: Update `.claude/CLAUDE.md` Mythic status**

Find: `| Mythic GME 2e            | Mythic     | 导入中   |`
Replace with: `| Mythic GME 2e            | Mythic     | 已完成   |`

- [ ] **Step 4: Final commit**

```bash
git add .claude/CLAUDE.md
git commit -m "mythic: mark import complete in CLAUDE.md status table"
```

- [ ] **Step 5: Verify final repo state**

```bash
git status
git log --oneline | head -15
tree output/Mythic/ -L 2
wc -l output/Mythic/**/*.md
```

Expected: clean working tree; all 37 files present; reasonable line counts (rules/ files 100-1500 lines each, engine/ files 50-200 lines each, meaning-elements.md several thousand lines).

---

## Open Questions Resolved During Planning

- **spec §9 `engine/08-variations.md` scope** → resolved at Task 8 Step 5: include ALL variations with compact summaries pointing to rules/ for detail.
- **spec §9 `meaning-elements.md` ordering** → resolved at Task 6 Step 2: PDF order.
- **spec §9 `examples/` machine-readable turn index** → deferred (frontmatter tags via `chaos-focus` suffice for now; revisit if AI usage warrants).

## Dependencies Between Tasks

```
Task 0 (scaffold)
  ↓
Task 1 ←┐
Task 2 ←┤  (rules/, parallel-safe after Task 0)
Task 3 ←┘
  ↓
Task 4 ←┐
Task 5 ←┤  (tables/, parallel-safe after Task 0)
Task 6 ←┘
  ↓
Task 7 (examples + sheets — depends on Task 0 only, parallel-safe)
  ↓
Task 8 (engine — REQUIRES Tasks 1-7 done)
  ↓
Task 9 (final validation)
```

Tasks 1-7 can run in any order or in parallel. Task 8 must wait. Task 9 must be last.
