# Mothership 1e 导入指南

> **系统**：Mothership Sci-Fi Horror RPG（Tuesday Knight Games, 2023, v1.x）
> **源 PDF**：`Rule Books/OSR related/Mothership/`（中英双版核心 + 6 模组中译 + 系统扩展）
> **输出目录**：`output/Mothership/`
> **系统简称**：Mothership
> **语言**：中文为主，章节标题保留中英双语

---

## 0. 系统背景

- Mothership 是 d100 / d10 骰池系统，sci-fi horror（《异形》《游星》《2001》风格）
- 核心机制：4 属性（力量/速度/智力/战斗）+ 3 豁免（理智/恐惧/身体），属性 2d10+25，豁免 2d10+10
- **压力（Stress）+ 惊恐检定（Panic Check）** 是系统签名机制
- 4 职类：陆战队员 Marine / 仿生人 Android / 科学家 Scientist / 技工 Teamster
- 中文译者发布版本：玩家手册 ZH v1.3.3 / 监守手册 ZH v1.3.1（与 md files 同步）

## 1. 输出文件结构

```
output/Mothership/
├── rules/                          # 核心规则（15 文件）
│   ├── psg-overview.md             # 简介 + 索引 + 速查 + 游戏范例 + 安全指引
│   ├── psg-character-creation.md   # 9 步角色创建 + 4 职类
│   ├── psg-skills.md               # 技能详细（受训/专家/大师 + 训练 + 军事训练）
│   ├── psg-equipment.md            # 信用/武器/护甲/行装/饰品/贴章/装备/宠物/负载
│   ├── psg-checks-and-stress.md    # 骰子/检定/豁免/压力/惊恐/状态
│   ├── psg-combat.md               # 暴力遭遇/回合/伤害/损伤/死亡/范围
│   ├── psg-survival.md             # 大气/出血/缺氧/辐射/医疗
│   ├── psg-port-and-crew.md        # 星港/上岸休假/雇员
│   ├── wom-overview.md             # WOM 简介 + 索引 + 恐怖/主题 d100
│   ├── wom-prep.md                 # 准备首回 10 步
│   ├── wom-scenario-design.md      # TOMBS 五幕 + 求生/解题/谜题/拯救/绘图
│   ├── wom-running-game.md         # 主持首回 + 6 步流程 + 房规 + 社交/暴力
│   ├── wom-investigations-and-ships.md  # 调查 + 飞船与太空
│   ├── wom-campaign-design.md      # 战役风格/框架/派系/经济/继续/结束
│   └── wom-worldbuilding-tables.md # 行星/派系/定居点 d100 表
├── supplements/
│   ├── glossary.md                 # 中英对照术语表（已有 md，整理）
│   ├── crowded-stars.md            # d100 飞船遭遇表（已有 md，整理）
│   ├── shipbreakers-toolkit.md     # 飞船扩展（源：英文 PDF v1.2）
│   ├── hack-manual.md              # 黑客系统扩展（源：中文 PDF v1.0）
│   └── android-background.md       # 仿生人背景与惊恐表（源：中文 PDF）
├── campaign/                       # 6 个中译模组（按需另开 parallel agents）
│   ├── another-bug-hunt/           # Another Bug Hunt MRPG-M4 (ZH v1.3)
│   ├── ypsilon-14/                 # Haunting of Ypsilon 14 宇普西龙14号疑云
│   ├── moonbase-blues/             # Moonbase Blues 彗星蓝调
│   ├── piece-by-piece/             # Piece by Piece 化整为零
│   ├── the-long-haul/              # The Long Haul 漫漫长路
│   └── warped-beyond-recognition/  # Warped Beyond Recognition 面目全非
└── characters/
    └── character-template.md       # 角色卡模板 + state.yaml schema
```

## 2. 章节优先级

### P0 — 核心规则 PSG（先做）

源文件：`Rule Books/OSR related/Mothership/md files/Player Survival Book.md`（1222 行，已是 v1.3 中文）

| 文件 | 源 md 行号 | 内容 |
|---|---|---|
| `psg-overview.md` | L352-401 + L990-1035 + L1164-1222 | 安全指引/如何进行游戏/速查/游戏范例 |
| `psg-character-creation.md` | L1-83 | 9 步流程 + 4 职类调整 |
| `psg-skills.md` | L543-708 | 技能列表 + 训练 + 军事训练 |
| `psg-equipment.md` | L84-351 | 信用/武器/护甲/行装/饰品/贴章/装备/宠物/负载 |
| `psg-checks-and-stress.md` | L403-541 | 骰子/属性检定/豁免/优劣势/压力/惊恐/状态 |
| `psg-combat.md` | L710-879 | 暴力遭遇/回合/突袭/动作/攻击/伤害/损伤/死亡/范围 |
| `psg-survival.md` | L881-988 | 大气/出血/低温/疲惫/食物/氧气/辐射/温度/医疗 |
| `psg-port-and-crew.md` | L1036-1162 | 星港/上岸休假/雇员 |

### P0 — 核心规则 WOM（先做）

源文件：`Rule Books/OSR related/Mothership/md files/Warden's Operation Manual.md`（2036 行，已是 v1.3 中文）

| 文件 | 源 md 行号 | 内容 |
|---|---|---|
| `wom-overview.md` | L1-75 | 简介 + 信息 + 恐怖 d100 + 主题 d100 |
| `wom-prep.md` | L76-173 | 准备首回 10 步（GET ORGANIZED → FINAL DETAILS） |
| `wom-scenario-design.md` | L174-602 | TOMBS 五幕 + 求生/解题/谜题/拯救/绘图/总结 |
| `wom-running-game.md` | L603-1180 | 主持首回 + 教学 + 安全/礼仪 + 6 步流程 + 房规 + 社交/暴力 |
| `wom-investigations-and-ships.md` | L1181-1281 | 主持调查 + 飞船与太空 |
| `wom-campaign-design.md` | L1282-1860 | 战役风格/框架/起始星域/派系/公司/经济/继续/结束 |
| `wom-worldbuilding-tables.md` | L1861-2010 | 行星/派系/定居点 d100 表 |

### P1 — 扩展（按需）

| 文件 | 源 | 备注 |
|---|---|---|
| `supplements/glossary.md` | `supplyment/Mothership Glossary (ZH).md` | 已是 md，直接整理（243 行） |
| `supplements/crowded-stars.md` | `supplyment/Crowded Stars 拥挤群星 (ZH).md` | 已是 md，直接整理（104 行） |
| `supplements/shipbreakers-toolkit.md` | `core books/Shipbreaker's Toolkit v1.2.pdf` | 英文，需 pdf-to-markdown 提取 |
| `supplements/hack-manual.md` | `supplyment/Hack Manual (ZH v1.0).pdf` | 中文，需 pdf-to-markdown 提取 |
| `supplements/android-background.md` | `supplyment/Android Background and Panic Table (ZH).pdf` | 中文，需 pdf-to-markdown 提取 |

### P2 — 角色卡（按需）

| 文件 | 源 | 备注 |
|---|---|---|
| `characters/character-template.md` | `supplyment/Character Sheet v5.11 (ZH, landscape).pdf` | 表单图，用 Read 多模态预览字段；附 state.yaml schema |

### P3 — 模组（按需，parallel worktree agents）

| 模组 | 源 PDF | 输出目录 |
|---|---|---|
| Another Bug Hunt | `modules/Another Bug Hunt MRPG-M4 (ZH v1.3).pdf` | `campaign/another-bug-hunt/` |
| Ypsilon 14 宇普西龙14号疑云 | `modules/Haunting of Ypsilon 14 宇普西龙14号疑云 (ZH).pdf` | `campaign/ypsilon-14/` |
| Moonbase Blues 彗星蓝调 | `modules/Moonbase Blues 彗星蓝调 (ZH).pdf` | `campaign/moonbase-blues/` |
| Piece by Piece 化整为零 | `modules/Piece by Piece 化整为零 (ZH).pdf` | `campaign/piece-by-piece/` |
| The Long Haul 漫漫长路 | `modules/The Long Haul 漫漫长路 (ZH).pdf` | `campaign/the-long-haul/` |
| Warped Beyond Recognition | `modules/Warped Beyond Recognition 面目全非 (ZH).pdf` + `Maps/` + `NPC Portraits/` | `campaign/warped-beyond-recognition/` |

模组导入需另写一份 `mothership-campaign-import-guide.md`（参考 `dnd-campaign-import-guide.md` 与 `ose-campaign-import-guide.md`）。

## 3. 写作规范

### 通用

- **中文为主**，段落以中文 PDF v1.3 译文为准
- 章节标题保留中英双语（中文在前，英文大写在后）：
  ```
  ## 角色创建流程 HOW TO MAKE YOUR CHARACTER
  ### 步骤 1，投属性 STEP 1. ROLL STATS
  ```
- 关键术语首次出现给中英对照（参考 `supplements/glossary.md`）：
  - `优势 [+]`、`劣势 [−]`、`AP（护甲值）`、`AAP（反护甲）`、`DMG（伤害）`
- 数值精确：属性 2d10+25 / 豁免 2d10+10 / 生命值 1d10+10 / 起始信用点 2d10×10
- 数值表格用 markdown 表格，数字列右对齐
- 每个文件开头：`#` 标题 + `>` 引用块（来源 + md 行号 + PDF 页码）+ `## Index`

### 文件头模板

```markdown
# psg-character-creation: 角色创建

> 源：`Rule Books/OSR related/Mothership/md files/Player Survival Book.md` L1-83
> 对照 PDF：`Rule Books/OSR related/Mothership/core books/Player Survival Guide (ZH v1.3.3).pdf` p.4-7
> 版本：玩家生存指南 v1.3.3（中译）

## Index

- [步骤 1：投属性](#步骤-1投属性-step-1-roll-stats)
- [步骤 2：投豁免](#步骤-2投豁免-step-2-roll-saves)
- ...

---
```

### 表格规范

- **d100 表**统一格式：表头 `D100 | 列1 | 列2 | ...`，区间用 `00-04` 形式（不要 `0-4`）
- 武器表：`武器名 | 价格 | 范围 | 伤害 | 弹药 | 特殊`
- 护甲表：`护甲名 | 价格 | AP | 氧气 | 速度 | 特殊`
- 行装表：`# | 内容` 一栏放完整描述

### 优劣势标记

源 md 用 `[优]` / `[劣]`，沿用此格式（不要改成 GFM 的别的写法）。

## 4. 分对话计划

每对话 1-2 文件，完成后立即校验：

| 阶段 | 文件 | 备注 |
|---|---|---|
| 框架 | 指南 + 目录 + glossary + crowded-stars + 状态表 | ✅ 完成 |
| Pass 1 | psg-overview, psg-character-creation | ✅ 完成 |
| Pass 2 | psg-skills, psg-equipment | ✅ 完成 |
| Pass 3 | psg-checks-and-stress, psg-combat | ✅ 完成 |
| Pass 4 | psg-survival, psg-port-and-crew | ✅ 完成 |
| Pass 5 | wom-overview, wom-prep | ✅ 完成 |
| Pass 6 | wom-scenario-design | ✅ 完成（569 行） |
| Pass 7 | wom-running-game | ✅ 完成（669 行） |
| Pass 8 | wom-investigations-and-ships, wom-worldbuilding-tables | ✅ 完成（121 + 203 行） |
| Pass 9 | wom-campaign-design | ✅ 完成（691 行） |
| Pass 10 | shipbreakers-toolkit | ✅ 完成（~1620 行；docling + Read PDF 多模态全 44 页校对，13 大节：Overview/Quick Ref Card/Ship Basics/Ships ×10（含 Raider+Troopship）/Class-0 Vessels ×7/Upgrades & Weapons/Space Travel/Detection & Range（含 Scanning Examples）/Ship Combat（含 After Battle Report）/Maintenance/Who Pays/Ship Manifest/Glossary） |
| Pass 11 | hack-manual, android-background | ✅ 完成（pdf-to-markdown + Read PDF 多模态校对） |
| Pass 12 | character-template | ✅ 完成（参照 v5.11 横版角色卡 + state.yaml schema） |
| Pass 13+ | 模组（parallel worktree agents） | ⏳ 待办 — 用模组导入指南 |

**rules/ 全部 15 个文件已完成（共 4618 行）**。supplements/ 已完成 5 个（全部完成）：
- ✅ `glossary.md`、`crowded-stars.md`（已有 md 整理）
- ✅ `android-background.md`（仿生人公司名生成器 + 起源表 + 仿生人专用惊恐表）
- ✅ `hack-manual.md`（网络 / 节点 / 安保等级 / 反应表 / 装备 / 一次性软件 / 诺亚四号范例网络）
- ✅ `shipbreakers-toolkit.md`（英文 v1.2 → 1093 行：8 舰种 + 升级武器表 + 飞船战斗 + Megadamage 表 + Maintenance d100 + Bankruptcy 表）

**Pass 10 校对要点**：
- d100 Maintenance Issues 表源 PDF 为 3 列布局（00-33 / 34-66 / 67-99），导入时合并为单列升序，已确保 100 行完整（00-22 Minor 23 行 + 23-99 Major 77 行）。
- Valuable Salvage 表 d10=00 出现两次（疑印刷错），第 06 行原书空白 — 如实保留并加注。
- **舰种属性数值嵌在装饰性圆圈图形中，docling OCR 全部漏掉** — 已用 `Read` PDF 多模态逐页（p.10-27, p.42-43）校对所有 10 艘舰种的完整 stat。
- **源书内部矛盾**：Executive Transport 详情卡（p.12）J2C-I vs Spec Sheet（p.43）J2C-II — 以详情卡为准。
- Particle Beam 价格"3cr"疑印刷错（应 3mcr）— 已加注。
- Contraband 表 d10=01「People」子表 07-08「Drugs」与父项不符 — 如实保留印刷文字。
- 易遗漏的非主要载具：Raider（J1C-I 袭掠者）、Troopship（J3C-V 运兵舰）、7 类 Class-0 飞船详情卡（Boarding Skiff / Coffin Lander / Dropship / Escape Pod / Fighter / Utility Pod / HDP）— 均需 Read PDF 多模态确认 stats。

**本次校对要点（Pass 11）**：
- 仿生人起源表 07 行（"未知外星科技"特性列）和 08 行（整行）在原 PDF 中即为留白 — Docling 把空白渲染成 CID 乱码，需用 `Read` PDF 多模态确认。导入时如实保留并加注。
- Hack Manual 的 ASCII 网络拓扑图（"诺亚四号"范例）pymupdf / Docling 都难以还原，已转为两张 markdown 表（乘组网络 / 指挥网络）+ 布局思路文字说明。

## 5. 校验检查清单（每文件）

- [ ] 完整性：源 md 对应行号区间是否全部覆盖？
- [ ] 数值准确：抽查 5 个数值（属性调整、伤害骰、护甲 AP、信用点等）与源 PDF 对照
- [ ] 表格完整：所有表格行数 = 源原文行数（特别是 d100 表 100 行）
- [ ] 标题双语：中文在前，英文大写在后
- [ ] 优劣势记号：`[优]` / `[劣]` 沿用，不改写
- [ ] 术语一致：与 `supplements/glossary.md` 对照
- [ ] 无乱码：md 提取残留的 `\xa0`、断行错误、HTML 实体等已清理
- [ ] cross-ref 路径：跨文件引用用相对路径（`→ psg-checks-and-stress.md#惊恐检定`）

## 6. sibling 项目

核心规则全部导完后再建 `/Users/jack/Projects/trpg-projects/Mothership/`，复制 Mörk Borg 模板（参考根 CLAUDE.md §7）：
- `rules/` → symlink 到 `dnd-rules-import/output/Mothership/rules/`
- `supplements/` → symlink 到 `.../output/Mothership/supplements/`
- `campaign/` → symlink 到 `.../output/Mothership/campaign/`
- `characters/` → symlink 到 `.../output/Mothership/characters/`
- `tools/mcp-server/` 用骰子/状态/存档 MCP

存档结构（按 CLAUDE.md §7.2）：
```
saves/{name}/
  state.yaml
  warden-notes.md   # Mothership 角色术语 = Warden（监守）
  mission-log.md
saves/.active
```
