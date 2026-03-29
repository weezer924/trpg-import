# OSE Classic Fantasy 导入指南

> 本文档是 OSE Classic Fantasy Rules Tome 的导入工作指南。目标：从英文 PDF 提取规则，生成结构化 markdown 文件，供 AI DM / Keeper 在游戏中查阅。

---

## 1. 背景

OSE (Old-School Essentials) Classic Fantasy 是 B/X D&D 的忠实复刻，由 Necrotic Gnome 出版。Classic 版采用种族即职业（race-as-class）设计，共 7 个职业，是后续 Advanced 导入的基础。

**已有文件**：`output/OSE/ose-basic-rules.md`（来自 OSE Basic Rules PDF，是不同的书，保留并存）。

**已提取原文**：`output/OSE/ose-classic-rules-tome-raw.txt`（551KB，23523 行，从 PDF 全文提取）。

---

## 2. 源文件

| 文件 | 版本 | 页数 |
|------|------|------|
| `/Users/jack/Projects/Rule Books/OSE/OSE Classic/OSE Classic Fantasy Rules Tome v1.4.pdf` | v1.4 | 297 页 |

已提取 txt：`output/OSE/ose-classic-rules-tome-raw.txt`

导入时优先读取 txt 原文，遇到排版不清或表格混乱时回 PDF 核实。

---

## 3. 输出文件

生成 4 个文件，全部以 `ose-classic-` 前缀命名：

### 3.1 `ose-classic-rules.md` — 核心规则参考

**用途**：AI DM 查阅角色创建、职业特性、装备、冒险/战斗规则、DM 指南。

**包含章节**（按 PDF 顺序）：

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Introduction | 游戏简介、术语 | p.6-11 |
| Player Characters | 属性值、创角流程 | p.14-21 |
| Character Classes | 7 个职业完整描述 | p.24-37 |
| Advancement | 经验值、等级称号、财富 | p.38-40 |
| Equipment | 冒险装备、武器、护甲 | p.42-47 |
| Vehicles and Mounts | 载具、坐骑、船只 | p.48-57 |
| Hired Help | 随从、佣兵、专家 | p.58-65 |
| Strongholds | 建造据点、领地管理 | p.66-69 |
| Magic | 魔法规则概述 + 法术列表索引（法术详述在 spells 文件） | p.70-76 |
| Adventuring | 队伍组织、时间/负重/移动、检定、豁免、地下城/野外/水上冒险、遭遇、追逐 | p.112-135 |
| Combat | 战斗流程、攻击、士气、战斗表 | p.132-137 |
| Running Adventures | DM 指南：裁判角色、设计冒险/地下城/野外/城镇、奖励 XP | p.138-150 |

> 注：Magic 章节中的法术列表索引保留在此文件（Cleric Spell List / Magic-User Spell List），但法术详细描述在 `ose-classic-spells.md`。

### 3.2 `ose-classic-spells.md` — 法术参考

**用途**：AI DM 查阅法术效果进行裁定。

**包含章节**：

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Cleric Spells | 1-5 级，共约 30 个法术 | p.78-87 |
| Magic-User Spells | 1-6 级，共约 72 个法术 | p.90-110 |

### 3.3 `ose-classic-monsters.md` — 怪物参考

**用途**：AI DM 查阅怪物数据、操控敌方回合。

**包含章节**：

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Monsters | 怪物通用规则 + 全部怪物描述（A-Z，约 120+ 种） | p.152-217 |
| Encounter Tables | 地下城/野外遭遇表 | p.218-225 |
| NPC Encounters | 冒险队伍、据点 NPC | p.226-228 |

### 3.4 `ose-classic-treasures.md` — 宝物与魔法物品参考

**用途**：AI DM 查阅宝物分配、魔法物品效果。

**包含章节**：

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Treasures | 宝物放置规则、价值物品、宝物类型表 | p.230-239 |
| Magic Items | 护甲/盾牌、杂项物品、药水、戒指、权杖/法杖/魔杖、卷轴/地图、剑、武器 | p.240-271 |
| Sentient Swords | 智能剑规则 | p.272-277 |

---

## 4. 格式规范

### 4.1 通用格式

- GitHub Flavored Markdown
- **英文为主**（PDF 原文为英文），关键术语可附中文注释
- 数值必须精确：AC、HD、HP、伤害骰、Save、距离、持续时间等不可有误
- 每个文件开头需要：
  - `#` 标题行
  - `>` 引用块说明来源和版本
  - `## Index` 目录

### 4.2 文件头格式

```markdown
# OSE Classic Fantasy — [文件主题]

> Source: Old-School Essentials Classic Fantasy Rules Tome v1.4
> Author: Gavin Norman / Necrotic Gnome
> Related files: `ose-classic-rules.md`, `ose-classic-spells.md`, `ose-classic-monsters.md`, `ose-classic-treasures.md`

## Index

1. [Section Name](#section-name) — brief description
...

---
```

### 4.3 职业格式

```markdown
### Cleric

**Requirements**: None
**Prime Requisite**: WIS
**Hit Dice**: 1d6
**Maximum Level**: 14
**Armour**: Any, including shields
**Weapons**: Blunt weapons only (club, mace, sling, staff, war hammer)
**Languages**: Alignment language, Common

| Level | XP | HD | THAC0 | D | W | P | B | S |
|------:|-------:|:--:|:-----:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0 | 1d6 | 19 | 11 | 12 | 14 | 16 | 15 |
| 2 | 1,500 | 2d6 | 19 | 11 | 12 | 14 | 16 | 15 |
...

**Combat**: Clerics can use all types of armour...
**Turning the Undead**: ...（完整描述 + 驱散表格）
```

### 4.4 法术格式

```markdown
### Cure Light Wounds

**Duration**: Instant
**Range**: Touch

This spell has two usages:
1. **Healing a living subject**: ...
2. **Destroying an undead monster**: ...
```

### 4.5 怪物数据块格式

```markdown
### Basilisk

*AC* 4 [15], *HD* 6+1 (28hp), *Att* 1 × bite (1d10 + petrification), *THAC0* 13 [+6]
*MV* 60' (20'), *SV* D10 W11 P12 B13 S14 (6), *ML* 9, *AL* Neutral, *XP* 950
*TT* F

- **Surprise**: On a 1-3, due to sluggishness.
- **Petrifying gaze**: ...（完整描述）
- **Petrifying touch**: ...
```

> 怪物数据块采用紧凑单行格式（斜体标签 + 逗号分隔），特殊能力用列表。
> AC 同时标注降序和升序：`4 [15]`。
> THAC0 同时标注降序和攻击加值：`13 [+6]`。
> Save 格式：`D W P B S (等效等级)` 分别代表 Death/Wands/Paralysis/Breath/Spells。

### 4.6 魔法物品格式

```markdown
### Bag of Holding

A sack-like item that can hold up to 10,000 coins of weight inside, but always weighs only 600 coins.
```

### 4.7 表格格式

数值表格用 markdown 表格，数字列右对齐（`---:`）。所有表格行数必须与 PDF 一致。

---

## 5. 导入流程

### 5.0 核心原则

- **一次只处理一本书**，不要跨书操作
- **每个对话只提取 1-2 个章节**，context 堆积后质量会下降
- **每个章节提取完成后立即校验**，不要等全部做完再查
- **context 变长后果断开新对话**，带上本指南 + 已完成的输出文件继续
- 输出文件采用**追加模式**：每个对话在已有文件末尾追加新章节内容
- 优先读取已提取的 txt 文件（`ose-classic-rules-tome-raw.txt`），格式化为 markdown
- 遇到 txt 中排版混乱的表格或 stat block，回 PDF 用 `pdf_extract.py --pages` 核实

### 5.1 整体顺序

```
Phase 1：Rules（核心规则）→ 输出 ose-classic-rules.md      （4 个对话）
Phase 2：Spells（法术）→ 输出 ose-classic-spells.md        （3 个对话）
Phase 3：Monsters（怪物）→ 输出 ose-classic-monsters.md    （4 个对话）
Phase 4：Treasures（宝物）→ 输出 ose-classic-treasures.md  （3 个对话）
                                                   合计：14 个对话
```

### 5.2 Phase 1：Rules — 分对话计划

| 对话 | 提取内容 | PDF 页码 | 预估规模 |
|------|---------|---------|---------|
| R-1 | 文件头 + Index + Introduction + Player Characters + Character Classes (7 职业) | p.6-37 | 大 |
| R-2 | Advancement + Equipment + Vehicles & Mounts + Hired Help + Strongholds | p.38-69 | 大 |
| R-3 | Magic（规则概述 + 法术列表索引）+ Adventuring（全部子章节） | p.70-76, 112-135 | 大 |
| R-4 | Combat Tables + Running Adventures（DM 指南） | p.136-150 | 中 |

### 5.3 Phase 2：Spells — 分对话计划

| 对话 | 提取内容 | PDF 页码 | 预估规模 |
|------|---------|---------|---------|
| S-1 | 文件头 + Index + Cleric Spells 全部 (1-5 级) | p.78-87 | 中 |
| S-2 | Magic-User Spells 1-3 级 | p.90-97 | 中 |
| S-3 | Magic-User Spells 4-6 级 | p.98-110 | 中 |

### 5.4 Phase 3：Monsters — 分对话计划

| 对话 | 提取内容 | PDF 页码 | 预估规模 |
|------|---------|---------|---------|
| M-1 | 文件头 + Index + Monster 通用规则 + A-F 怪物 (Acolyte ~ Fish, Giant) | p.152-175 | 大 |
| M-2 | G-M 怪物 (Gargoyle ~ Mummy) | p.176-191 | 大 |
| M-3 | N-Z 怪物 (Neanderthal ~ Zombie) | p.194-217 | 大 |
| M-4 | Encounter Tables (Dungeon + Wilderness) + NPC Encounters | p.218-228 | 中 |

### 5.5 Phase 4：Treasures — 分对话计划

| 对话 | 提取内容 | PDF 页码 | 预估规模 |
|------|---------|---------|---------|
| T-1 | 文件头 + Index + 宝物规则 + Treasure Types 表 + Armour/Shields + Miscellaneous Items | p.230-247 | 大 |
| T-2 | Potions + Rings + Rods, Staves, Wands | p.248-263 | 中 |
| T-3 | Scrolls/Maps + Swords + Weapons + Sentient Swords | p.264-277 | 大 |

### 5.6 每个对话的工作流程

```
1. 读取本指南（ose-import-guide.md）
2. 读取当前输出文件（如已有内容）
3. 从 txt 原文读取对应页码范围的内容
4. 格式化为 markdown（按 §4 格式规范）
5. 追加到输出文件
6. 执行章节检查清单（见 §5.7）
7. 如果 context 变长 → 结束对话，下一轮继续
```

### 5.7 每章节检查清单

每提取一个章节后执行：

- [ ] **完整性**：PDF 目录中列出的小节是否全部包含？
- [ ] **数值准确**：抽查 5 个关键数值（AC、HD、XP、THAC0、法术参数），与 PDF/txt 原文对比
- [ ] **表格完整**：所有表格的行数是否与原文一致？
- [ ] **格式一致**：标题层级、stat block 格式、术语是否统一？
- [ ] **无乱码**：没有 PDF 提取残留的特殊字符或断行错误

---

## 6. OSE 特有注意事项

### 6.1 AC 双标记

OSE 同时使用降序 AC（原版 B/X）和升序 AC（现代可选规则），格式为 `4 [15]`。两个值都必须正确。

### 6.2 THAC0 双标记

THAC0 同时标注降序值和攻击加值，格式为 `13 [+6]`。必须同时保留。

### 6.3 种族即职业

Classic 中 Dwarf、Elf、Halfling 是独立职业，不是种族。不要与 Advanced 的种族/职业分离系统混淆。

### 6.4 豁免类型

OSE 使用 5 类豁免：Death/Poison (D)、Wands (W)、Paralysis/Petrification (P)、Breath Attacks (B)、Spells/Rods/Staves (S)。与 D&D 5e 的 6 属性豁免完全不同。

### 6.5 版本纯净

- 只使用 v1.4 Rules Tome 的内容
- 不要混入 Advanced Fantasy 的内容（额外职业、种族、怪物）
- 不要混入 BECMI、AD&D 或任何其他版本的规则
- 不要从 AI 训练数据中补充 PDF 中没有的内容

---

## 7. 质量验证

### 7.1 最终检查

导入完成后：

1. **职业数据**：7 个职业的 HD、XP 表、THAC0、豁免值逐一核对
2. **法术参数**：随机抽 10 个法术，对比 PDF 的射程/持续时间/效果
3. **武器/护甲表**：全部条目的伤害骰/AC/价格是否正确
4. **怪物数据**：随机抽 10 个怪物，核对 AC、HD、Att、Dmg、THAC0、Save、XP
5. **宝物类型表**：行数和概率值与 PDF 一致

### 7.2 四文件交叉一致性

- 法术列表索引（rules）与法术详述（spells）的法术名和数量一致
- 怪物施法能力引用的法术在 spells 文件中有对应条目
- 职业可用武器/护甲（rules）与装备表一致
- 魔法物品效果（treasures）与规则描述不矛盾
