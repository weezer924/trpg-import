# Cairn 2e 导入指南

> Cairn 2nd Edition (Yochai Gal, August 2024, CC BY-SA 4.0)
> 包含 Player's Guide 和 Warden's Guide 两本，外加 Warden Screen + Character Sheets
> 源 PDF：`Rule Books/OSR related/Cairn 2e/`
> 输出目录：`output/Cairn/rules/cairn2e-*.md`（与 1e 文件同级，文件名前缀区分版本）

---

## 1. 源 PDF

| 文件 | 页数 | 用途 |
|---|---:|---|
| `Cairn_2e_Players_Guide.pdf` | 88 | 玩家手册（已转 md） |
| `Cairn_2e_Wardens_Guide.pdf` | — | Warden 手册（待转） |
| `Cairn_2e_Warden_Screen.pdf` | — | 速查屏（待转） |
| `Cairn-2e-Character-Sheet-Portrait/Landscape-Letter-Fillable.pdf` | — | 角色卡（参考用） |

> Spreads 版本（双页跨页布局）不要用于解析 — 只用单页版。

---

## 2. 输出文件结构

文件名约定：`cairn2e-{section}.md`，与 1e (`cairn1e-*.md`) 同级。

### Player's Guide → 输出

| 文件 | 状态 | 来源页 | 内容 |
|---|---|---|---|
| `cairn2e-overview.md` | ✓ 已完成 | p.4–5, 86–87 | Design philosophy, Player principles, Setting (Vald, Wood, Roots) |
| `cairn2e-character-creation.md` | ✓ 已完成 | p.6–17 | Section 1: creation steps, attributes, HP, inventory, traits, bonds, omens, marketplace |
| `cairn2e-rules.md` | ✓ 已完成 | p.62–67 | Section 3: core rules, combat, scars, magic |
| `cairn2e-procedures.md` | ✓ 已完成 | p.70–83 | Section 4: dungeon, wilderness, downtime |
| `cairn2e-backgrounds.md` | ✓ 已完成 | p.18–59 | Section 2: 20 backgrounds × 2 d6 表 |

### Warden's Guide → 输出

| 文件 | 状态 | 来源页 | 内容 |
|---|---|---|---|
| `cairn2e-warden-worldbuilding.md` | ✓ 已完成 | p.4–31, 56–79 | Setting Seeds / Factions / Topography / Forest Seeds / Example Forest |
| `cairn2e-warden-dungeon-seeds.md` | ✓ 已完成 | p.32–55 | Dungeon Seeds / Build a Dungeon / Fractured Temple |
| `cairn2e-warden-bestiary.md` | ✓ 已完成 | p.82–105 | 84 怪物字母序 + 分类索引 |
| `cairn2e-warden-monster-creation.md` | ✓ 已完成 | p.106–133 | Creating Monsters + Naming + Growth（9 示例） |
| `cairn2e-warden-spellbooks.md` | ✓ 已完成 | p.134–141 | d100 Spellbook 表（含 2e 外观/性格 flavor）；法术效果沿用 1e |
| `cairn2e-warden-reliquary.md` | ✓ 已完成 | p.142–147 | 46 个 Relic / Artifact |
| `cairn2e-warden-advice.md` | ✓ 已完成 | p.150–153, 190 | Creating Backgrounds / Pointcrawls / Bibliography |
| `cairn2e-warden-faq.md` | ✓ 已完成 | p.154–177 | FAQ（20 主题簇） |
| `cairn2e-warden-vald-setting.md` | ✓ 已完成 | p.178–189 | Setting of Vald 详述（10 节） |

---

## 3. Backgrounds 分对话计划

20 个背景，每个 ~50 行，全部约 1000–1200 行 — 建议分 2–3 个对话完成。

### 推荐拆分

| 对话 | 背景（按字母序） | 页范围 |
|---|---|---|
| #1 | Aurifex, Barber-Surgeon, Beast Handler, Bonekeeper, Cutpurse, Fieldwarden, Fletchwind | p.20–33 |
| #2 | Foundling, Fungal Forager, Greenwise, Half Witch, Hexenbane, Jongleur, Kettlewright | p.34–47 |
| #3 | Marchguard, Mountebank, Outrider, Prowler, Rill Runner, Scrivener | p.48–59 |

### 每个 Background 模板

```markdown
### {N}. {Name}

*(p.{XX})*

> {flavor description, 1–2 sentences}

**Starting Gear:**
- 3d6 Gold Pieces
- Rations (3 uses)
- {Light source}
- {Weapon}
- {Background-specific items}

**Names:** {comma-separated list of 10}

#### {d6 Question 1, e.g. "What rare tool is essential to your work?"}

| d6 | Result |
|---:|---|
| 1 | {effect description} |
| ... | ... |

#### {d6 Question 2}

| d6 | Result |
|---:|---|
| 1 | {effect description} |
| ... | ... |
```

输出全部追加到单一文件 `cairn2e-backgrounds.md`，每个背景一个 H3 (`### N. Name`)，文件开头有 H1 + Index 锚到所有 20 个背景。

---

## 4. 1e ↔ 2e 主要差异

记录关键变化，便于校对：

| 维度 | 1e | 2e |
|---|---|---|
| 角色创建 | d20 名字 + 背景列表，d20 起始装备表 | 20 个详细 Background（每个含独立装备 + d6 表） |
| Reputation/Misfortunes 表 | 有 | 无（被 Bonds 取代） |
| Bonds 表 | 无 | 有（d20）|
| Omens 表 | 无 | 有（d20，最年轻角色掷）|
| Inventory | 10 槽（4 body + 6 backpack）| 同 10 槽，但说明 "舒适承载 4 件" |
| Petty 物品 | 1e 无此类（仅 bulky） | 2e 引入 petty（不占槽）|
| 法术列表 | 100 法术 + d100 表 | 无（沿用 1e 法术表）|
| 反应/士气/Critical/Scars | 与 2e 几乎一致 | 同 |
| Procedures | 简略带过 | 完整章节（Dungeon/Wilderness/Downtime + Watches/Weather）|
| Setting Vald | 无明示 | 详述（Wood, Roots, Heart Tree, Fae）|

---

## 5. 校验清单

每个文件完成后：

- [ ] 完整性：原 PDF 章节小节是否齐全？
- [ ] 数值准确：抽查 5 个关键数值（gp 价格、d6/d20 表条目、HP/Armor/距离）
- [ ] 表格完整：行数与原文一致？
- [ ] 格式一致：粗体术语、petty/bulky 斜体、列表层级统一
- [ ] 1e ↔ 2e 不混淆：检查没有 1e 残留术语（如 Reputation、Misfortunes）

---

## 6. 注意事项

- **2e Player's Guide 不含法术列表**，复用 1e 的 100 法术 → 在 `cairn2e-rules.md` 末尾加 note 指向 `cairn1e-spells.md`
- **Spreads 版 PDF** 是双页跨页，文本会左右穿插，不要用
- **图表很多被 OCR 成 picture text** — 表格内容仍可读，但格式需重排
- 2e 出现新术语：***petty*** (不占槽)、***panicked*** (条件)、***Make Camp***、***Watch***、***Milestone***、***Cost***、***Heart Tree***、***Heartseed***、***Gate***、***Roots***
