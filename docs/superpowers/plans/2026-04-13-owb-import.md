# Operation WhiteBox (OWB) 核心规则导入实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 从 `wwii operation whitebox.pdf`（186 页英文）提取完整核心规则与战役设定，输出 2 个结构化 markdown 文件到 `output/OWB/rules/`，供 AI DM 查阅使用。

**Architecture:** 参考 OSE 规则书的分文件架构，拆为 `owb-rules.md`（规则）+ `owb-setting.md`（NPC/装备/WWII 战役设定/Mini-Settings）。使用已转换的 md 原文作为提取源，按 4 个独立对话（S-1..S-4）分批写入，每对话 1-2 章节，追加模式；完成后更新项目主 CLAUDE.md 状态表并提交。

**Tech Stack:** Markdown / pdf-to-markdown 技能（已生成源 md）/ `pdf_extract.py`（表格核实）/ git。

---

## 源文件

- PDF: `/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.pdf`（186 页）
- 已提取 md（图文）: `/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.md`
- 导入指南: `/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/owb-import-guide.md`

## 输出文件结构

```
output/OWB/
└── rules/
    ├── owb-rules.md      # 规则 (Intro → Gameplay Example), PDF p.10-89
    └── owb-setting.md    # NPC + 设定 + Mini-Settings, PDF p.90-186
```

---

## Task 1: 创建输出目录与占位

**Files:**
- Create: `output/OWB/rules/.gitkeep`

- [ ] **Step 1: 确认目录不存在**

Run: `ls output/OWB/rules/ 2>&1`
Expected: `No such file or directory`

- [ ] **Step 2: 创建目录与 .gitkeep 占位**

```bash
mkdir -p output/OWB/rules
touch output/OWB/rules/.gitkeep
```

- [ ] **Step 3: 提交**

```bash
git add output/OWB/rules/.gitkeep .claude/owb-import-guide.md docs/superpowers/plans/2026-04-13-owb-import.md
git commit -m "scaffold OWB import: guide, plan, output dir"
```

---

## Task 2: 会话 S-1 — `owb-rules.md` 上半（Intro + Attributes + Operatives + Classes）

**Files:**
- Create: `output/OWB/rules/owb-rules.md`
- Read: `/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.md`（页 10-34 对应内容）

> **对话开启指令**：另开新对话，带入 `.claude/CLAUDE.md`、`.claude/owb-import-guide.md`、本计划 Task 2 节选。

- [ ] **Step 1: 读取源 md 中 Introduction + Attributes 段**

Run: `grep -n "^## " "/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.md" | head -40`
使用 Read 精确读取 Introduction (p.10) 到 Experience Bonus 结束（Attributes 章节末）。

- [ ] **Step 2: 写入 `owb-rules.md` 文件头 + Index + Introduction + Attributes**

按导入指南 §4.2 文件头模板：
```markdown
# Operation WhiteBox — Core Rules

> Source: WWII: Operation WhiteBox (Peter C. Spahn / Small Niche Games, 2015)
> Based on: Swords & Wizardry WhiteBox
> Related files: `owb-setting.md`
> PDF pages covered in this file: p.10-89

## Index

1. [Introduction](#introduction) — starting the game, dice
2. [Attributes](#attributes) — 6 attributes, universal attribute bonus, XP bonus
3. [Special Forces Operatives](#special-forces-operatives) — nationality, profession, rank, alignment
4. [Character Classes](#character-classes) — 8 classes + NPC classes + alternate levels
5. [Gear and Weapons](#gear-and-weapons)
6. [Playing the Game](#playing-the-game)
7. [Personal Combat](#personal-combat)
8. [Vehicle Combat](#vehicle-combat)
9. [Gameplay Example](#gameplay-example)

---

## Introduction
...
## Attributes
...
```

所有数值、表格、可选规则（*OPTIONAL RULE: ... 开头的子节）完整保留。

- [ ] **Step 3: 追加 Special Forces Operatives**

读源 md 中 Operatives 章节（国籍表、职业表 Table 4、军衔、阵营、起始装备、武器/护甲限制、A NOTE ON GENDER ROLES），追加到 owb-rules.md。保持原文小节顺序。

- [ ] **Step 4: 追加 Character Classes**

8 个职业（Charmer, Combat Engineer, Grunt, Maquis, Sniper, Tactician, Wheelman, Uberlaufer）各自含：
- 开篇描述
- 要求 / Prime Attribute / HD / 武器护甲
- XP/HD/To-Hit/Save 等级表（完整 10 级或至最高等级）
- Class Abilities 全部条目

外加 *OPTIONAL RULE: ADVANCED STARTING LEVELS / ALTERNATE LEVELS OF PLAY (Traditional/Heroic/Inglorious) / CLASSES FOR NPCs / CHARACTER RETIREMENT。

- [ ] **Step 5: 执行章节检查清单**

按 `owb-import-guide.md` §5.3 六项逐一勾选；特别抽查：
- Charmer / Sniper / Tactician 三职业的 L1、L5、L10 XP 值
- 两张属性加值表（Universal / Advanced）行数一致
- 职业表格 10 行完整

- [ ] **Step 6: Commit**

```bash
git add output/OWB/rules/owb-rules.md
git commit -m "import OWB rules: Intro, Attributes, Operatives, Classes (p.10-34)"
```

---

## Task 3: 会话 S-2 — `owb-rules.md` 下半（Gear → Gameplay Example）

**Files:**
- Modify: `output/OWB/rules/owb-rules.md`（追加）

> **对话开启指令**：另开新对话，带入 CLAUDE.md、导入指南、已完成的 `owb-rules.md`、本计划 Task 3。

- [ ] **Step 1: 读取 Gear and Weapons 段**

Read 源 md 的 Gear/Weapons 全部子节（Equipment Weight, Standard Gear, Melee Weapons, Missile/Ranged Weapons 四子类, Armor 含 AAC 规则与转换）。

- [ ] **Step 2: 追加 Gear and Weapons 到 owb-rules.md**

全部武器表保留完整列（Damage / Range / RoF / Cost / Weight 等）。护甲表同时含 AC 和 AAC 两列。AAC 可选规则单独小节说明。

- [ ] **Step 3: 追加 Playing the Game**

全部子节：Special Forces Training / Time / Saving Throws / Surprise / Hidden Things / Carrying / Movement / XP / *Gut Check / Recruiting Help / *Trial by Fire。

- [ ] **Step 4: 追加 Personal Combat**

完整保留 Autofire 组（Burst Fire / Suppressive Fire 及所有子条：Reloads / Malfunctions / Movement / vs Suppressive Fire / Saves）。完整保留 Explosives 组（Impact 含 Mortars / Timed / Static / Default Damage / Saves）。Damage and Death 含 *Nonlethal / *Unconsciousness and Death 可选。Healing 含 Natural / First Aid。

- [ ] **Step 5: 追加 Vehicle Combat**

13 种载具数据块逐一：Motorcycle / Car / Truck (Small) / Truck (Large) / Armored Car / APC / Tank Destroyer / Tank (Light/Medium/Heavy) / Boat (Patrol) / Aircraft (Small/Large)。每种给完整统计（Crew, Passengers, Cargo, AC [AAC], HP, Move, Max Speed, Weapons, Special）。含 Modifications / XP for Vehicle Combat / Long-Distance Travel。

- [ ] **Step 6: 追加 Gameplay Example**

7 回合示例完整转为 markdown（可用 blockquote 或标准段落），保留所有骰值、DM 裁决与对白说明。

- [ ] **Step 7: 执行章节检查清单 + 抽查**

- 武器表行数与 md 一致
- Suppressive Fire 子节全部六条存在
- 13 种载具逐一存在
- AC/AAC 双标记在护甲表和载具数据块全部存在

- [ ] **Step 8: Commit**

```bash
git add output/OWB/rules/owb-rules.md
git commit -m "import OWB rules: Gear, Play, Personal/Vehicle Combat, Example (p.35-89)"
```

---

## Task 4: 会话 S-3 — `owb-setting.md` 上半（NPCs + Covert Gear + Campaign + ETO）

**Files:**
- Create: `output/OWB/rules/owb-setting.md`

> **对话开启指令**：另开新对话，带入 CLAUDE.md、导入指南、本计划 Task 4。

- [ ] **Step 1: 定位源 md 中对应章节起止**

Run: `grep -n "^## " "/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.md"`
定位 `COMMON NPCS AND ANIMALS` 起始行、`SPECIAL FORCES IN THE EUROPEAN THEATER` 末尾（Special Forces Actions 结束处）。

- [ ] **Step 2: 写入 owb-setting.md 文件头 + Index**

```markdown
# Operation WhiteBox — NPCs, Gear, and WWII Setting

> Source: WWII: Operation WhiteBox (Peter C. Spahn / Small Niche Games, 2015)
> Related files: `owb-rules.md`
> PDF pages covered in this file: p.90-186

## Index

1. [Common NPCs and Animals](#common-npcs-and-animals)
2. [Covert Special Forces Equipment](#covert-special-forces-equipment)
3. [The WWII Campaign](#the-wwii-campaign)
4. [Special Forces in the European Theater](#special-forces-in-the-european-theater)
5. [WWII Timeline](#wwii-timeline)
6. [Historic WWII Special Forces Actions](#historic-wwii-special-forces-actions)
7. [Resistance at the Ponteville Bridge](#resistance-at-the-ponteville-bridge)
8. [Mass Combat](#mass-combat)
9. [Mini-Setting: Nazi Superscience](#mini-setting-nazi-superscience)
10. [Mini-Setting: Nazi Occult](#mini-setting-nazi-occult)
11. [Mini-Setting: Galaxy War 1939](#mini-setting-galaxy-war-1939)
12. [Afterword](#afterword)

---
```

- [ ] **Step 3: 追加 Common NPCs and Animals**

包含 NPC/Animal to-hit 表、读法说明、9 种 NPC（Civilians, German Soldier, German Officer, SS Soldier, SS Officer, Gestapo Agent, Allied Soldier, Allied Officer, Resistance Fighter）+ 10 种动物（Bat, Bear, Cat Big, Dog, Eagle, Herd Animal, Horse, Rat, Snake Venomous, Wolf）。每条使用指南 §4.6 数据块格式，含 AC 双标记。保留 SS/Gestapo/Wehrmacht 说明 sidebar。

- [ ] **Step 4: 追加 Covert Special Forces Equipment**

全部条目（间谍装备、伪装、破坏器材等），含价格/重量/效果。

- [ ] **Step 5: 追加 The WWII Campaign**

全部子节：Who Is at War / Time Period / *Blitzkrieg / Theater / Unit Type / Game Type / Tips for Running（所有子条目含 *Holocaust / *Fritzis 等 sidebars）。

- [ ] **Step 6: 追加 Special Forces in the European Theater**

三组（Allied / Resistance / German Special Forces）全部条目 + Special Forces Actions（Operations / Support Missions / Stages of Support Mission 各阶段）。

- [ ] **Step 7: 章节检查清单**

抽查 9 个 NPC 数据块、10 个动物数据块数量一致；AC [AAC] 双标记全部到位；Support Mission 阶段齐全（Objective / Briefing / Planning / Insertion / ...）。

- [ ] **Step 8: Commit**

```bash
git add output/OWB/rules/owb-setting.md
git commit -m "import OWB setting: NPCs, Covert Gear, WWII Campaign, ETO (p.90-~130)"
```

---

## Task 5: 会话 S-4 — `owb-setting.md` 下半（Timeline → Mini-Settings → Afterword）

**Files:**
- Modify: `output/OWB/rules/owb-setting.md`（追加）

> **对话开启指令**：另开新对话，带入 CLAUDE.md、导入指南、已完成的 `owb-setting.md`、本计划 Task 5。

- [ ] **Step 1: 追加 WWII Timeline**

按源 md 原文完整年表，保留日期精度。

- [ ] **Step 2: 追加 Historic WWII Special Forces Actions**

每则历史行动的描述完整保留。

- [ ] **Step 3: 追加 Resistance at the Ponteville Bridge**

完整样本任务：背景、地点描述、NPC 数据块（用 §4.6 格式）、事件流程、奖励。可直接作为模组跑。

- [ ] **Step 4: 追加 Mass Combat**

完整规则（单位代表、规模、骰法、结算）不得省略。

- [ ] **Step 5: 追加 Mini-Setting: Nazi Superscience**

章首以 blockquote 标注"Optional Setting"。完整保留新装备/怪物/规则。

- [ ] **Step 6: 追加 Mini-Setting: Nazi Occult**

同上；保留怪物数据块、仪式、神器、新法术（如有）。

- [ ] **Step 7: 追加 Mini-Setting: Galaxy War 1939 — SOE**

同上；保留太空变体载具、异星怪物等。

- [ ] **Step 8: 追加 Afterword（OGL / 角色卡只放一句说明 + PDF 页码引用，不导入图像）**

```markdown
## Afterword

...（作者感言原文）

> **OWB Character Sheet** 见 PDF p.181-182（图像形式，未导入）。
> **OGL** 见 PDF p.183-186（法律文本，未导入；使用者自行参阅）。
```

- [ ] **Step 9: 最终质量验证（导入指南 §7）**

- 8 职业 XP/HD/To-Hit/Save 全对
- 武器/护甲表完整
- 13 种载具完整
- Autofire/Explosives 子规则完整
- Ponteville NPC 数据块完整
- 两文件交叉一致（NPC 武器引用在 rules 里存在）

- [ ] **Step 10: 更新主 CLAUDE.md 状态表 + 指南索引**

将 `.claude/CLAUDE.md` 系统状态表中 OWB 行标为"已完成"（如尚无行则新增）：

```
| Operation WhiteBox | OWB | 已完成 | `Operation White Box/` | `output/OWB/` |
```

在 §4 系统导入指南表新增：

```
| OWB 规则书 | `.claude/owb-import-guide.md` | WWII OSR 二战特战 → 2 个输出文件 |
```

- [ ] **Step 11: Commit**

```bash
git add output/OWB/rules/owb-setting.md .claude/CLAUDE.md
git commit -m "finalise OWB import: Timeline, Ponteville, Mini-Settings, Afterword"
```

---

## 自审记录

- **Spec 覆盖**：源 PDF 的 TOC 全部落到两个输出文件之一 ✅
- **无占位**：每个 Step 都明确了要读的章节和要写的格式 ✅
- **类型一致**：AC [AAC] 双标记、数据块格式、To-Hit 加值命名在所有 Task 中统一 ✅
- **风险点**：
  1. Mini-Settings 页码需要在 S-4 开始时现查 md TOC（指南已提醒）
  2. Gameplay Example（p.78-89，12 页）可能较长，如 S-2 context 紧张可拆分到 S-2b
  3. 载具与 NPC 数据块需要两遍 AC 值（下降/上升），容易漏，已在检查清单中强调
