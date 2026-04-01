# AD&D 1st Edition 战役模组 PDF 导入指南

> 本指南用于将 AD&D 1st Edition 战役模组 PDF（英文）转换为结构化 markdown 文件，供 AI DM 在游戏中查阅使用。
> **双系统兼容**：所有 stat block 同时标注 AD&D 1e 原版数据和 OSE 兼容标记，使输出文件可直接用于 AD&D 1e 或 OSE 游戏。

---

## 1. 背景

AD&D 1st Edition (1977-1989) 是 Gary Gygax 设计的高级版 D&D。其模组使用独特的数据格式，与 B/X (OSE) 和后来的 AD&D 2e 均有区别。

**AD&D 1e 与 OSE (B/X) 的关键区别：**

| 数据 | AD&D 1e | OSE (B/X) | 转换方式 |
|------|---------|-----------|---------|
| AC | 降序，可为负数 | 降序 [升序] 双标记 | 补充升序：AAC = 19 - DAC |
| 攻击 | Attack Matrix（无 THAC0） | THAC0 [攻击加值] 双标记 | 按 HD 查 OSE THAC0 表补充 |
| 移动 | 英寸（"）：`MV 12"` | 英尺（'）：`MV 120' (40')` | ×10 转英尺，括号内为遭遇速度（÷3） |
| 豁免 | 5 类，按 AD&D 表 | 5 类，按 B/X 表 | 保留 AD&D 原值，格式转为 OSE 标记 |
| NPC 属性 | 通常有完整六项属性值 | 通常不标注 | 保留 AD&D 原始属性值 |
| 法术体系 | MU / Illusionist / Cleric / Druid 各自独立 | MU / Cleric 两系 | 保留 AD&D 原始法术列表 |
| 特殊能力 | SA / SD / MR | 文字描述 | 保留 AD&D 格式（SA/SD/MR） |

**转换原则**：AD&D 1e 原始数据为主，OSE 标记为辅。数值以 PDF 原文为准，不用 OSE 标准值覆盖。DM 用 OSE 跑时可自行决定是否微调豁免等差异项。

**OSE THAC0 快查表（按 HD）**：

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
| 9+ to 10 | 10 | [+9] |
| 10+ to 11 | 9 | [+10] |
| 11+ to 12 | 8 | [+11] |
| 12+ to 13 | 7 | [+12] |
| 13+ to 15 | 6 | [+13] |
| 15+ to 17 | 5 | [+14] |
| 17+ to 19 | 4 | [+15] |
| 19+ to 21 | 3 | [+16] |
| 21+ | 2 | [+17] |

---

## 2. 输出结构

每个模组输出到 `output/ADnD1e/campaign/{module-name}/` 目录下：

| 文件 | 用途 | 必须 |
|------|------|------|
| `import-plan.md` | 导入计划和进度跟踪 | 是 |
| `region.md` | 区域总览：冒险背景、历史、派系、地点索引、旅行规则、主线流程 | 是 |
| `encounters.md` | 遭遇汇总：随机遭遇表 + 怪物数据块索引 + 固定遭遇索引 | 是 |
| `npcs.md` | NPC 索引：按地点分组 | 是 |
| `{location-name}.md` | 地点详情：逐区域描述 | 是 |
| `appendices.md` | 附录：独有怪物、魔法物品、神祇等 | 视情况 |

---

## 3. 文件格式规范

### 3.1 通用规范

- GitHub Flavored Markdown
- **英文为主**（PDF 原文为英文）
- 数值必须精确：AC、HP、damage dice、距离、持续时间等不可有误
- 交叉引用格式：`See filename.md` 或 `See filename.md Area X`
- 每个文件开头：`#` 标题行 + `>` 引用块说明来源版本 + `## Index` 目录
- 每个大章节开头标注 PDF 页码：`*(PDF p.X–Y)*`

### 3.2 文件头格式

```markdown
# Module Code — Section Name

> **System:** AD&D 1st Edition (OSE compatible)
> **Source:** Module Code — Full Name (Author, Year)
> **Levels:** X–Y

## Index

- [Section Name](#section-name) — brief description
...

---
```

### 3.3 NPC Stat Block 格式

AD&D 1e NPC 数据量大（属性、装备、法术），用多行结构，同时标注 OSE 兼容数据：

```markdown
### NPC Name

- **Race/Class/Level:** Human Fighter 5
- **AC:** 2 [17] (plate mail + shield)
- **HP:** 35
- **#AT:** 1, **D:** longsword (1-8+2)
- **THAC0:** 16 [+3]
- **MV:** 90' (30')
- **SV:** D10 W11 P12 B13 S14 (F5)
- **AL:** LG
- **S** 16 **I** 12 **W** 13 **D** 10 **C** 15 **Ch** 14
- **Equipment:** plate mail, shield +1, longsword +1, 45 gp
- **Spells (if caster):** spell list by level
- **Notes:** role in adventure, personality, hidden info for DM
```

对于次要 NPC（无属性值的）简化为：

```markdown
- **NPC Name:** Race, role, AL. Brief description. Equipment of note.
```

### 3.4 Monster Stat Block 格式（内联紧凑，OSE 兼容）

```markdown
**Monster Name** ×N: AC X [Y], HD Z (Whp), Att X × weapon (damage), THAC0 X [+Y], MV X' (Y'), SV DX WX PX BX SX (class/level), ML X, AL XX; XP X. SA special, SD special, MR X%.
```

示例：
```markdown
**Bugbear** ×4: AC 5 [14], HD 3+1 (15hp), Att 1 × morningstar (2-8), THAC0 16 [+3], MV 90' (30'), SV D12 W13 P14 B15 S16 (F3), ML 9, AL CE; XP 135. SA surprise on 1-3, SD none.
```

格式要点：
- **AC**：降序 [升序] 双标记，可为负数：`AC -2 [21]`
- **HD**：如 `3+1`，括号内写实际 HP
- **THAC0**：按 HD 查 §1 快查表，附攻击加值：`THAC0 16 [+3]`
- **MV**：英尺（'），括号内遭遇速度：`MV 120' (40')`。飞行/游泳另标：`MV 120' (40') / Fly 180' (60')`
- **SV**：五项豁免值 + 等效类型/等级。使用 AD&D 1e PDF 原始豁免值，格式标记为 OSE 风格
- **ML**：士气值（AD&D 1e 模组通常不标 ML，需从上下文或怪物描述推断，无法确定时标注 `ML —`）
- **SA/SD**：特殊攻击/防御（如有），放在 XP 之后
- **MR**：魔法抗性%（如有）
- **XP**：使用 PDF 原文的经验值

### 3.5 AD&D 1e 独特数据注意

| 数据 | 说明 |
|------|------|
| 负数 AC | 完全正常，高等级战士/怪物常见 AC -1 到 -5 |
| 武器速度因子 | 模组中偶尔提及，如有则保留 |
| Psionic Ability | 部分怪物有灵能数据，如有则保留 |
| % Lair | 遭遇表可能包含，如有则保留 |
| Treasure Type | 字母代码（A-Z），保留原文 |
| Magic Resistance | 百分比，某些强力怪物特有 |
| 多次攻击 | 同一回合多次攻击很常见（claw/claw/bite） |
| 施法 NPC | 常有完整法术列表，必须完整保留 |

---

## 4. 导入流程

### 4.1 准备

1. 用 `pdf_extract.py` 提取全文为 `.txt`
2. 读取目录页，确定章节结构
3. 生成 `import-plan.md`

### 4.2 逐章提取

每个对话的工作流：

```
1. 读取本指南（adnd1e-campaign-import-guide.md）
2. 读取当前模组的 import-plan（了解进度）
3. 读取已完成的输出文件（如有，确保一致性）
4. 用 pdf_extract.py 提取对应页码的 PDF 文本
5. 从 txt 文件读取对应内容（PAGE 分隔符定位）
6. 格式化为 markdown（按 §3 格式规范）
7. 写入对应输出文件
8. 执行章节检查清单（§4.3）
9. 更新 import-plan 进度
```

### 4.3 每章节检查清单

- [ ] **完整性**：PDF 中该章节的所有区域编号是否全部包含？
- [ ] **数值准确**：抽查 3-5 个 NPC/怪物数据（AC/HP/Damage/AL），与 PDF 对比
- [ ] **装备完整**：NPC 的装备和法术列表是否完整？
- [ ] **表格完整**：所有表格行数与原文一致？
- [ ] **格式一致**：标题层级、区域编号、stat block 格式统一？
- [ ] **OCR 修正**：明显错误已修正？存疑处标注 `[OCR unclear]`？

---

## 5. OCR 注意事项

AD&D 1e 模组 PDF 多为扫描版，常见问题：

| 常见错误 | 处理方式 |
|----------|---------|
| 数字混淆（1/l/I, 0/O） | 根据上下文和 AD&D 规则修正 |
| 负号丢失（AC -2 → AC 2） | AC ≤ 0 在高等级冒险中正常，注意检查 |
| 引号/特殊符号 | 统一为标准 ASCII 或 Unicode |
| 多栏排版错乱 | 根据上下文重组 |
| 法术名拼写错误 | 以 PHB 为准修正 |

---

## 6. 版本纯净与 OSE 兼容原则

- **数值以 PDF 原文为准**——AC、HP、伤害、豁免等数值不可用 OSE 标准值覆盖
- OSE 兼容标记（升序 AC、THAC0、英尺移动、五项豁免格式）是**附加标注**，不替代原始数据
- 不要混入 AD&D 2e、D&D 5e 或其他版本数据
- 保留 AD&D 1e 独有数据（SA/SD/MR/六项属性/法术列表）——这些在 OSE 中没有对应项，但对 DM 仍有参考价值
- AD&D 1e 独有怪物特殊能力必须完整描述，不能只写 `See ose-classic-monsters.md`（因为 OSE 怪物书中可能没有该怪物）
