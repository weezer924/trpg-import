# OSE 战役模组 PDF 导入指南

> 本指南用于将 Classic D&D B 系列模组 PDF（英文，30-80 页）转换为结构化 markdown 文件，使用 OSE 规则体系，供 AI DM 在游戏中查阅使用。

---

## 1. 背景

B 系列模组（B1-B12）是为 D&D Basic/Expert (B/X) 编写的经典冒险。OSE 是 B/X 的忠实复刻，规则完全兼容，因此这些模组可以直接用 OSE 运行。

**规则对齐**：所有怪物数据、术语、格式均使用 OSE 体系（参见 `output/OSE/` 下的规则文件）。

**已有参考**：`output/OSE/campaign/the-hole-in-the-oak/` 是已完成的 OSE 模组导入范例，新模组应遵循相同格式。

---

## 2. 待导入模组

| 模组 | 全名 | 页数 | 等级 | PDF 路径 | 已提取 txt |
|------|------|------|------|---------|-----------|
| B2 | The Keep on the Borderlands | 35 | 1-3 | `source/D&D Classic/Modules/B2 - The Keep on the Borderlands.pdf` | `.txt` (170 KB) |
| B4 | The Lost City | 34 | 1-3 | `source/D&D Classic/Modules/B4 - The Lost City.pdf` | `.txt` (151 KB) |
| B10 | Night's Dark Terror | 74 | 2-4 | `source/D&D Classic/Modules/B10 - Night's Dark Terror.pdf` | `.txt` (340 KB) |

**注意**：这些 PDF 是 OCR 扫描版。已用 `pdf_extract.py` 提取为 txt 文件。导入时优先读取 txt 原文，遇到排版混乱或数值存疑时回 PDF 用 `pdf_extract.py --pages` 核实。

---

## 3. 输出结构

每个模组输出到 `output/OSE/campaign/{module-name}/` 目录下：

| 文件 | 用途 | 必须 |
|------|------|------|
| `region.md` | 区域总览：冒险背景、历史、派系、地点索引、旅行规则、主线流程 | 是 |
| `encounters.md` | 遭遇表：随机遭遇表 + 怪物数据块索引表 + 各地点固定遭遇索引 | 是 |
| `npcs.md` | NPC 索引：按地点分组，含种族/身份、位置、态度、关键信息 | 是 |
| `{location-name}.md` | 地点详情：每个可探索地点一个文件，含逐区域描述 | 是 |
| `shops.md` | 商店与交易：商店列表、魔法物品索引、财宝汇总（如模组有商店/城镇） | 视情况 |
| `quests.md` | 任务钩子汇总（如模组有明确任务结构） | 视情况 |

> B 系列模组结构比 5e 模组简洁得多。许多 B 系列模组没有明确的任务系统或商店，这些文件可以省略或合并到 region.md 中。

---

## 4. 文件格式规范

### 4.1 通用规范

- GitHub Flavored Markdown
- **英文为主**（PDF 原文为英文），关键术语可附中文注释
- 数值必须精确：AC、HD、HP、THAC0、伤害骰、Save、距离、持续时间等不可有误
- 交叉引用格式：`See filename.md` 或 `See filename.md Area X1`
- 每个文件开头需要：`#` 标题行 + `>` 引用块说明来源和版本 + `## Index` 目录
- 每个大章节开头标注 PDF 页码：`*(PDF p.X–Y)*`

### 4.2 文件头格式

```markdown
# Module Name — File Subject

> **System:** Old-School Essentials (B/X compatible)
> **Source:** Module Code — Full Name (Author, Year)
> **Levels:** X–Y

## Index

- [Section Name](#section-name) — brief description
...

---
```

### 4.3 怪物数据块格式（OSE 标准）

内联紧凑格式，与 the-hole-in-the-oak 一致：

```markdown
**Monster Name** ×N: AC X [Y], HD Z (Whp), Att 1 × weapon (damage), THAC0 X [+Y], MV X' (Y'), SV DX WX PX BX SX (class/level), ML X, AL X, XP X.
```

格式要点：
- **AC 双标记**：降序 [升序]，如 `6 [13]`
- **THAC0 双标记**：降序 [攻击加值]，如 `17 [+2]`
- **Save 格式**：`D W P B S (等效类型/等级)`，如 `D12 W13 P14 B15 S16 (F1)`
- **HD 格式**：骰子 + 修正，如 `3+1`；括号内写平均/实际 HP
- **MV 格式**：`X' (Y')`，分别为每回合和每轮移动速度

### 4.4 怪物数据处理原则

1. **OSE 标准怪物**（在 `ose-classic-monsters.md` 或 `ose-advanced-monsters.md` 中有的）：写完整内联数据块，但不需要写特殊能力的详细描述，注明 `See ose-classic-monsters.md`
2. **与 OSE 标准有差异的怪物**：写完整数据块 + 标注差异
3. **模组独有怪物**（OSE 书中没有的）：写完整数据块 + 完整特殊能力描述
4. **B/X 原版数据转 OSE**：B/X 和 OSE 数据完全一致，无需转换。只需确保格式符合 OSE 标准（双标记 AC/THAC0）

### 4.5 `encounters.md` 格式

参照 `the-hole-in-the-oak/encounters.md`：

```markdown
## Random Encounter Tables

（随机遭遇表，保留原文骰子和频率）

---

## Monster Stat Block Index

| Monster | AC | HD | HP | Att | THAC0 | MV | SV | ML | AL | XP | Area |
|---------|----|----|-----|-----|-------|----|----|----|----|-----|------|

---

## Fixed Encounters by Area

### Location Name
| Area | Monsters | Notes |
|------|----------|-------|
```

### 4.6 `region.md` 格式

```markdown
## Adventure Background
（冒险背景：谁、在哪、发生了什么）

---

## History
（历史背景，如有）

---

## Factions
（势力/派系，如有）

---

## Key Locations

| Location | Direction/Distance | Level | Overview |
|----------|-------------------|-------|----------|

---

## Travel Rules
（旅行规则、野外遭遇检定频率等，如模组涉及野外探索）

---

## Adventure Flow
（主线流程概览）

---

## Dungeon Areas Index
- Location (N areas) → See `filename.md`
```

### 4.7 地点文件格式

参照 `the-hole-in-the-oak/entrance-roots.md`：

```markdown
# Module — Location Name (Areas X–Y)

> **Source / System / Levels**

## General Features
- **Walls:** ...
- **Light:** ...
- **Doors:** ...

---

## X. Area Name

*(PDF p.X)*

Description of the area (terrain, atmosphere, sensory details).

- **Monsters:** Monster Name ×N: AC X [Y], HD Z (Whp), ...
- **Treasure:** Item (value/effect)
- **Traps/Checks:** Description, save/check required
- **Interactions:** NPCs, special items

---

## Y. Next Area...
```

### 4.8 `npcs.md` 格式

参照 `the-hole-in-the-oak/npcs.md`：

```markdown
### NPC Name
- **Species/Identity:** Race, gender, role
- **Location:** Area X (Location Name)
- **Attitude:** 2-3 descriptive words
- **Key Info:** Role in adventure, special abilities, relationships, treasure
- **Stats:** See `filename.md` Area X
```

---

## 5. OCR 扫描 PDF 注意事项

这些 B 系列模组 PDF 都是 OCR 扫描版，常见问题：

| 常见错误 | 处理方式 |
|----------|---------|
| 数字混淆（1/l/I, 0/O, 5/S） | 根据上下文和 B/X 规则常识修正。HD 通常 1-10，AC 通常 9 到 -2 |
| 表格列错位 | 根据列头和数据类型重新对齐 |
| 特殊符号丢失（—、×、'） | 补回正确符号 |
| 页眉/页脚混入正文 | 删除 |
| Stat block 断行 | 合并为完整数据块 |
| 地图标注混入文本 | 删除，仅保留文字内容 |

**原则**：如果 OCR 结果含义模糊且无法从上下文推断，标注 `[OCR unclear: "xxx"]` 供后续人工校对。

---

## 6. B/X → OSE 术语对照

B 系列模组使用原版 B/X 术语，导入时转为 OSE 标准格式：

| B/X 原版 | OSE 格式 | 说明 |
|----------|---------|------|
| AC 5 | AC 5 [14] | 补充升序 AC：AAC = 19 - DAC |
| THAC0 未标注 | 根据 HD 查表补充 | B/X 早期模组可能不写 THAC0，需要从 HD 推算 |
| Save: F2 | D12 W13 P14 B15 S16 (F2) | 展开为五项豁免值，查 OSE 豁免表 |
| Move 120' (40') | MV 120' (40') | 格式统一 |
| Morale 8 | ML 8 | 缩写统一 |
| No. Appearing | 不导入 | 遭遇人数由模组文本决定 |
| Treasure Type D | TT D | 仅在怪物巢穴宝物时需要 |

**THAC0 快查表（按 HD）**：

| HD | THAC0 | Attack Bonus |
|---:|------:|:------------|
| Up to 1 | 19 | [+0] |
| 1+ to 2 | 18 | [+1] |
| 2+ to 3 | 17 | [+2] |
| 3+ to 4 | 16 | [+3] |
| 4+ to 5 | 15 | [+4] |
| 5+ to 6 | 14 | [+5] |
| 6+ to 7 | 13 | [+6] |
| 7+ to 8 | 12 | [+7] |
| 8+ to 9 | 11 | [+8] |

---

## 7. 导入流程

### 7.1 第一步：读取目录，生成导入计划

1. 读取已提取的 txt 文件前 100-200 行（目录、引言）
2. 如 txt 中目录不清晰，用 `pdf_extract.py --info` 查看 PDF 内嵌目录
3. 列出所有章节和地点
4. 确定输出文件列表（哪些地点需要独立文件）
5. 生成 `{module-name}-import-plan.md`，放在模组输出目录下

### 7.2 第二步：逐章提取

每个对话的工作流：

```
1. 读取本指南（ose-campaign-import-guide.md）
2. 读取当前模组的 import-plan
3. 读取已完成的输出文件（了解当前进度）
4. 从 txt 文件读取对应页码范围的内容（按 PAGE 分隔符定位）
5. 格式化为 markdown（按 §4 格式规范）；遇到 txt 中排版混乱处，回 PDF 用 `pdf_extract.py --pages X-Y --stdout` 核实
6. 写入对应输出文件
7. 执行章节检查清单（§7.5）
8. 继续下一章节（不要停下来问用户）
9. 如果 context 变长 → 完成当前地点后结束，更新 import-plan 进度
```

### 7.3 建议的处理顺序

```
对话 1：目录 + 导入计划 + region.md（背景、地点、派系、流程）
对话 2-N：逐个地点文件（按模组章节顺序）
倒数第 2 个对话：encounters.md + npcs.md（+ shops.md / quests.md 如需要）
最后一个对话：交叉校验 + 修正
```

> 汇总文件（encounters / npcs）放在后面做：它们需要引用所有地点数据，在地点文件完成后编写更准确。

### 7.4 导入计划的进度跟踪格式

在 `{module-name}-import-plan.md` 中用状态标记每个步骤：

```markdown
| Step | Content | PDF Pages | Output File | Status |
|------|---------|-----------|-------------|--------|
| 1 | TOC + region.md | 1-8 | region.md | ✅ Done |
| 2 | The Keep | 9-16 | the-keep.md | ✅ Done |
| 3 | Caves of Chaos | 17-28 | caves-of-chaos.md | 🔄 In Progress |
| 4 | Wilderness | 29-32 | wilderness.md | ⬜ Not Started |
| 5 | encounters + npcs | — | encounters.md, npcs.md | ⬜ Not Started |
```

### 7.5 每章节检查清单

每提取一个章节/地点后，检查：

- [ ] **完整性**：PDF 中该章节的所有区域（area numbers）是否全部包含？
- [ ] **数值准确**：抽查 3-5 个怪物数据块（AC/HD/THAC0/Damage/Save），与 PDF 对比
- [ ] **AC/THAC0 双标记**：所有怪物都有降序和升序双标记？
- [ ] **表格完整**：所有表格的行数是否与原文一致？
- [ ] **格式一致**：标题层级、区域编号、stat block 格式是否统一？
- [ ] **OCR 修正**：明显的 OCR 错误是否已修正？存疑处是否已标注？

---

## 8. 各模组特别注意事项

### 8.1 B2 — The Keep on the Borderlands (35 pages)

- **结构**：城堡（The Keep）+ 混沌洞穴（Caves of Chaos）+ 野外
- **地点文件建议**：
  - `the-keep.md` — 城堡区域描述（有商店、NPC）
  - `caves-of-chaos.md` — 洞穴群（A-K 共 11 个洞穴，是模组核心）
  - `wilderness.md` — 野外遭遇和地点（如有足够内容，否则合并到 region.md）
- **shops.md**：城堡有商人和交易，需要此文件
- **特点**：经典沙盒地城，无固定主线。多个怪物部落有互动关系

### 8.2 B4 — The Lost City (34 pages)

- **结构**：金字塔上层（Tier 1-5）+ 地下城市（Lower Catacombs）+ 失落城市（Lost City，仅有大纲）
- **地点文件建议**：
  - `upper-pyramid.md` — 金字塔上层（Tier 1-5，详细描述的区域）
  - `lower-catacombs.md` — 地下墓穴
  - `lost-city.md` — 地下城市大纲（模组只提供了框架，由 DM 自行扩展）
- **特点**：有三个对立派系（Brotherhood of Gorm / Magi of Usamigaras / Warrior Maidens of Madarua），派系关系是模组核心

### 8.3 B10 — Night's Dark Terror (74 pages)

- **结构**：线性冒险，分多个章节逐步推进，从 Sukiskyn 围城 → 南方探索 → Xitaqa 废墟 → Threshold 城镇 → 黑山 → Hutaaka 失落山谷
- **地点文件建议**：
  - `sukiskyn.md` — 围城战和庄园
  - `south-of-the-river.md` — 南方野外和哥布林巢穴
  - `ruins-of-xitaqa.md` — Xitaqa 废墟和 Golthar 塔
  - `journey-to-threshold.md` — 旅途事件和 Rifllian
  - `threshold.md` — Threshold 城镇
  - `black-peaks.md` — 黑山山谷
  - `lost-valley.md` — Hutaaka 失落山谷和 Pflarr 神殿
- **shops.md**：Threshold 和 Rifllian 有商人
- **quests.md**：有明确的主线任务链
- **特点**：最长最复杂的模组（74 页），有大量 NPC、多个地点、野外探索。需要多个对话完成。有独有怪物（Chevall, Ice Wolf, Kartoeba 等）需要完整数据块

---

## 9. 跨文件一致性

导入完成后，确保以下一致性：

- [ ] `region.md` 地点索引中的所有地点都有对应的 `.md` 文件
- [ ] `encounters.md` Monster Stat Block Index 包含所有地点文件中出现的怪物
- [ ] `npcs.md` 中的区域编号与地点文件中的编号一致
- [ ] NPC 名字在所有文件中拼写一致
- [ ] 怪物数据在 encounters.md 汇总表和地点文件内联数据中一致
- [ ] 如有 `shops.md`，财宝/物品与地点文件中描述一致

---

## 10. 版本纯净

- 只使用 PDF 原文内容，不要从 AI 训练数据中补充
- 不要混入 BECMI（Companion/Master/Immortals）、AD&D、或 5e 的内容
- 怪物数据以 PDF 原文为准，格式转为 OSE 标准
- 如果 PDF 中的怪物数据与 OSE 标准怪物有出入（极少见，因为 B/X = OSE），以 PDF 模组原文为准并标注差异
