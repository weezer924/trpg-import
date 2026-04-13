# Operation WhiteBox (OWB) 导入指南

> WWII: Operation WhiteBox 是基于 Swords & Wizardry WhiteBox（0e/OD&D 分支）的 WWII 二战特种作战 OSR 规则。目标：从英文 PDF 提取全部规则与设定内容，生成结构化 markdown，供 AI DM 在游戏中查阅。

---

## 1. 背景

**系统**：WWII: Operation WhiteBox (OWB)
**作者/出版**：Peter C. Spahn / Small Niche Games (2015)
**底层**：Swords & Wizardry WhiteBox（OD&D 复刻）
**题材**：二战欧洲战区特种作战/抵抗组织/突击队
**与 D&D/OSE 的共同点**：d20 攻击、AC（同时提供下降 AC 与上升 AAC 双标记）、HD、Save（单一豁免值，非 B/X 5 类）、XP 分级表、职业驱动

---

## 2. 源文件

| 文件 | 页数 |
|------|------|
| `/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.pdf` | 186 |

已提取 md（pdf-to-markdown 技能产物，含图片）：
`/Users/jack/Projects/trpg-projects/Rule Books/Operation White Box/wwii operation whitebox.md`

导入时优先读取该 md 原文，遇到表格/排版异常时回 PDF 用 `pdf_extract.py --pages` 核实。

---

## 3. 输出文件

全部放在 `output/OWB/rules/`，以 `owb-` 前缀命名。

### 3.1 `owb-rules.md` — 核心规则

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Introduction | 起步、规则一、骰子 | p.10 |
| Attributes | 6 属性 + 可选规则 + Universal Attribute Bonus + Experience Bonus | p.11-16 |
| Special Forces Operatives | 国籍、职业（Profession）、军衔、阵营、起始装备、武器/护甲限制 | p.17-21 |
| Character Classes | 8 个职业（Charmer, Combat Engineer, Grunt, Maquis, Sniper, Tactician, Wheelman, Uberlaufer）+ Alternate Levels of Play + NPC 职业 + 退休 | p.22-34 |
| Gear and Weapons | 负重、通用装备、近战、远程（Archaic/Small Arms/Machinegun/Heavy）、护甲（含 AAC 规则与转换） | p.35-45 |
| Playing the Game | 特种训练、时间、豁免、奇袭、隐藏、负重、移动、XP、Gut Check、招募、Trial by Fire | p.46-52 |
| Personal Combat | 回合、先攻、攻击骰、近战、远程、Autofire（Burst/Suppressive）、Cover、弹药、爆炸物、移动、士气、伤害与死亡、治疗 | p.53-64 |
| Vehicle Combat | 载具战斗回合、先攻、攻击、移动、VC vs PC、扫射、损毁、修理、20/1、获取载具、载具数据（13 种）、改装、XP、长距离旅行 | p.65-77 |
| Gameplay Example | 完整一场战斗示例（7 回合） | p.78-89 |

### 3.2 `owb-setting.md` — NPC / 装备 / 战役设定 / 附录

| PDF 章节 | 内容 | PDF 页码 |
|---------|------|---------|
| Common NPCs and Animals | 攻击骰表、NPC 读法、平民/德军/党卫军/盖世太保/盟军/抵抗军，动物 10 种 | p.90-100 |
| Covert Special Forces Equipment | 秘密行动装备（间谍装备、伪装、破坏器材等） | p.101-102 |
| The WWII Campaign | 时间段/战区/部队类型/运营建议 | p.103-110 |
| Special Forces in the European Theater | 盟军/抵抗组织/德军特种部队介绍 + Special Forces Actions（Operations / Support Missions 阶段） | p.111-? |
| WWII Timeline | 大事年表 | — |
| Historic WWII Special Forces Actions | 历史行动案例 | — |
| Resistance at the Ponteville Bridge | 完整样本任务（可直接当模组跑） | — |
| Mass Combat | 大规模战斗规则 | — |
| Mini-Setting: Nazi Superscience | 纳粹超科学（机甲、射线枪等）| — |
| Mini-Setting: Nazi Occult | 纳粹神秘学（仪式、怪物、神器） | — |
| Mini-Setting: Galaxy War 1939 — SOE | 太空歌剧变体 | — |
| Afterword + OWB Character Sheet + OGL | 附录 | — |

> 第二批章节的精确页码在导入 S-3/S-4 时现读 md 头部的 TOC 确认（TOC 在 md 中全部列出）。

---

## 4. 格式规范

### 4.1 通用

- GitHub Flavored Markdown
- **英文为主**（PDF 原文为英文），关键术语可附中文注释
- 数值必须精确：AC/AAC、HD、HP、To-Hit、Save、伤害骰、射程、爆炸半径等
- 数字列右对齐（`---:`）
- 每个文件开头：`#` 标题 + `>` 来源引用块 + `## Index`

### 4.2 文件头模板

```markdown
# Operation WhiteBox — [文件主题]

> Source: WWII: Operation WhiteBox (Peter C. Spahn / Small Niche Games, 2015)
> Based on: Swords & Wizardry WhiteBox
> Related files: `owb-rules.md`, `owb-setting.md`

## Index

1. [Section Name](#section-name) — brief description
...

---
```

### 4.3 AC / AAC 双标记

OWB 同时支持下降 AC 与上升 AAC（可选规则）。护甲条目与 NPC 数据块必须同时保留两个值：

```
AC 6 [13]   ← 6 为下降，13 为上升
```

### 4.4 职业格式

```markdown
### Charmer

**Prime Attribute**: Charisma (+5% XP if 13+)
**Hit Dice**: 1d6
**Weapons/Armor**: ...

| Level | XP | HD | To-Hit | Save | [能力] |
|------:|--------:|:--:|:-----:|:--:|:------|
| 1 | 0 | 1d6 | +0 | 15 | ... |
...

**Class Abilities**: ...
```

### 4.5 武器/装备格式

```markdown
| Weapon | Damage | Range | Rate of Fire | Cost | Weight |
|--------|-------:|------:|:------------:|-----:|-------:|
| M1 Garand | 1d6+1 | 240 | 1 | — | 10 |
```

完整字段以 PDF 表格为准，不得省略列。

### 4.6 NPC 数据块

```markdown
### German Soldier

*AC* 8 [11], *HD* 1, *HP* 4, *To-Hit* +1, *Att* 1 × rifle (1d6+1) or 1 × bayonet (1d6)
*Save* 17, *Move* 12, *Morale* 8, *XP* 15

**Equipment**: ...
**Notes**: ...
```

### 4.7 载具数据块

每种载具保留：Crew、Passengers、Cargo、AC/AAC、HP、Move、Max Speed、Weapons（如有）、Special。

---

## 5. 导入流程

### 5.0 原则（继承通用规范）

- 每个对话只处理 1-2 个章节
- 章节完成立即校验
- context 增长就开新对话
- 输出文件追加模式
- 优先读 md 原文，表格异常回 PDF 核实（`pdf_extract.py --pages N-M`）

### 5.1 分对话计划（4 个对话）

| 对话 | 输出 | 提取内容 | PDF 页码 |
|------|------|---------|---------|
| S-1 | `owb-rules.md` | 文件头 + Index + Introduction + Attributes + Special Forces Operatives + Character Classes (8 职业 + 可选规则 + NPC 职业) | p.10-34 |
| S-2 | `owb-rules.md` 追加 | Gear & Weapons + Playing the Game + Personal Combat + Vehicle Combat + Gameplay Example | p.35-89 |
| S-3 | `owb-setting.md` | 文件头 + Index + Common NPCs & Animals + Covert Equipment + The WWII Campaign + Special Forces in ETO（含 Special Forces Actions） | p.90-~130 |
| S-4 | `owb-setting.md` 追加 | WWII Timeline + Historic Actions + Resistance at Ponteville + Mass Combat + 三个 Mini-Settings（Superscience / Occult / Galaxy War）+ Afterword | p.~130-186 |

> 精确页码在对应对话开始时查 md 的 TOC 段（第 62-198 行）与章节标题行确认。

### 5.2 每对话工作流程

```
1. 读本指南（owb-import-guide.md）
2. 读当前输出文件（若已有）
3. 从 md 原文读对应章节
4. 按 §4 格式规范转换为规则 markdown
5. 追加写入输出文件
6. 执行章节检查清单（§5.3）
7. 如果 context 过长 → 结束对话
```

### 5.3 每章节检查清单

- [ ] 小节完整：md 中列出的所有小节都收录
- [ ] 数值准确：抽 5 个关键数值（XP 表、伤害骰、射程、AC/AAC、HD）与 md/PDF 比对
- [ ] 表格完整：所有表格行数与原文一致
- [ ] 双标记：AC 条目同时含下降/上升两个值
- [ ] 格式一致：标题层级、stat block 风格统一
- [ ] 无乱码：无 PDF 提取残留

---

## 6. OWB 特有注意事项

### 6.1 WhiteBox 传承

攻击使用"To-Hit Bonus"（+X），非 THAC0。Save 只有**一个**豁免值（等级决定），不是 B/X 的 5 类。不要把 OSE/BX 的 save 格式套进来。

### 6.2 双 AC 系统

护甲和所有 NPC/载具数据块必须同时提供下降 AC（默认）与上升 AAC（可选规则）。护甲表格里两个值都列出。

### 6.3 Autofire / Suppressive Fire

OWB 独有机制，规则较细。完整保留 Burst Fire / Suppressive Fire / Malfunctions / Saves vs Suppressive Fire 子节，不得省略。

### 6.4 WWII 历史术语

保留原文的军事/历史专有名词（SS, Gestapo, Wehrmacht, Maquis, SOE, OSS, LRDG, SIG, Brandenburgers 等），必要时加中文注释。

### 6.5 Mini-Settings 与核心规则分离

三个 Mini-Settings（Superscience/Occult/Galaxy War）是可选变体，放在 `owb-setting.md` 末尾并明确标注"Optional Setting"，避免与核心 WWII 规则混淆。

### 6.6 版本纯净

- 只使用本 PDF 内容
- 不补充 Swords & Wizardry WhiteBox 核心书或其他 OSR 的规则
- 不从 AI 训练数据补充 OWB 之外的内容

---

## 7. 最终质量验证

1. 8 个职业的 XP 表、HD、To-Hit、Save 逐一核对
2. 所有武器表（近战/小型武器/机枪/重武器）完整，伤害/射程正确
3. 13 种载具的 AC/AAC、HP、Move、武器完整
4. Autofire / Explosives 子规则不得省略
5. 样本任务 Resistance at Ponteville 保留完整 NPC 数据块
6. 两个输出文件交叉一致（NPC 武器引用的数据在 rules 文件里存在）
