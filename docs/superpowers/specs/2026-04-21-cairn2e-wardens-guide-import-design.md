# Cairn 2e Warden's Guide 导入设计

> 日期：2026-04-21
> 源 PDF：`Rule Books/OSR related/Cairn 2e/Cairn_2e_Wardens_Guide.pdf`（192 页）
> 输出目录：`output/Cairn/rules/cairn2e-warden-*.md`
> 许可：CC BY-SA 4.0（Yochai Gal, 2024）

---

## 1. 目标

将 Cairn 2e Warden's Guide（192 页）按功能域拆为 9 个结构化 markdown 文件，供 AI Warden 在跑团时查阅。文件名前缀 `cairn2e-warden-` 与已完成的 Player's Guide 5 文件（`cairn2e-{overview,character-creation,rules,procedures,backgrounds}.md`）共存于 `output/Cairn/rules/`。

不涉及：
- Warden Screen（速查屏）— 内容与 Player's Guide 重复，跳过
- Character Sheets PDF — 角色卡信息已在 `cairn2e-character-creation.md` 覆盖
- Spreads 版 PDF — 双页跨页布局会导致文本穿插，不用

---

## 2. 输出文件清单

| # | 文件 | 源页 | 预估行数 | 内容 |
|---|---|---:|---:|---|
| 1 | `cairn2e-warden-worldbuilding.md` | 4–31, 56–79 | ~800 | Setting Seeds / Factions / Topography / Forest Seeds / Example Forest |
| 2 | `cairn2e-warden-dungeon-seeds.md` | 32–55 | ~600 | Dungeon Seeds / Build a Dungeon / Fractured Temple example |
| 3 | `cairn2e-warden-bestiary.md` | 82–105 | ~700 | 字母序怪物表 + 顶部分类索引 |
| 4 | `cairn2e-warden-monster-creation.md` | 106–133 | ~400 | Creating Monsters + Naming Procedures + Growth（含 Growth Examples） |
| 5 | `cairn2e-warden-spellbooks.md` | 134–141 | ~250 | Spellbook 规则（法术列表仍指向 `cairn1e-spells.md`） |
| 6 | `cairn2e-warden-reliquary.md` | 142–147 | ~250 | Relics/Artifacts 条目 |
| 7 | `cairn2e-warden-advice.md` | 150–153, 190 | ~200 | Creating Backgrounds / Pointcrawls / Bibliography |
| 8 | `cairn2e-warden-faq.md` | 154–177 | ~600 | FAQ（每 Q&A 一个 H3） |
| 9 | `cairn2e-warden-vald-setting.md` | 178–189 | ~350 | Setting of Vald 详述 |

---

## 3. 文件结构模板

### 3.1 通用模板（所有文件）

```markdown
# Cairn 2e — {Section Name} (Warden's Guide)

> Source: Cairn 2e Warden's Guide, p.{start}–{end}. CC BY-SA 4.0.
> {一句话节选内容定位}

## Index
1. [Section 1](#section-1)
2. [Section 2](#section-2)
...

---

## {H2 主节}

*(p.{XX})*

{内容}
```

### 3.2 Bestiary 特殊模板（文件 #3）

`cairn2e-warden-bestiary.md` 在 Index 后新增 **Category Index** 区段：

```markdown
## Category Index
| Category | Monsters |
|---|---|
| Humanoids | [Acolyte](#acolyte), [Bandit](#bandit), [Bugbear](#bugbear), ... |
| Undead | [Banshee](#banshee), [Crypt Guardian](#crypt-guardian), ... |
| Beasts | ... |
| Fey | ... |
| Constructs | ... |
| Magical | ... |
| Other | ... |

## Monsters (A–Z)

### Acolyte
*(p.82)*

> 4 HP, 1 Armor, 8 STR, 11 DEX, 14 WIL, ceremonial dagger (d6)

- Holy servants bound to a particular deity. Typically travel in groups of four or more.
- Carry a holy symbol (Ward once per day).
```

条目 H3 使用怪物原名。stat block 保留原书单行 blockquote 格式（`HP, Armor, STR, DEX, WIL, weapon` 顺序），与 `cairn1e-bestiary.md` 一致。分类索引是输出阶段的增值工作，需人工判断每条归属。

### 3.3 随机表重度文件模板（文件 #1, #2, #4 Naming）

Dungeon Seeds（p.32–41）、Forest Seeds（p.56–67）、Naming Procedures（p.116–123）含大量 d6/d20 生成器表。所有表用 markdown 表格，d 骰子列右对齐：

```markdown
### {Table Name}

| d6 | Result |
|---:|---|
| 1 | ... |
| 2 | ... |
```

Build a Dungeon 的 Fractured Temple 完整 example 按原书房间编号保留（每房间一个 H4 `#### Room N. Name`）。

### 3.4 FAQ 模板（文件 #8）

`cairn2e-warden-faq.md`：每个 Q&A 一个 H3，Index 列全部问题锚点：

```markdown
## Index
1. [Q: 问题原文节选...](#q-...)
2. ...

## FAQ

### Q: {完整问题原文}
*(p.{XX})*

{答案正文}
```

---

## 4. 提取流程

1. **PDF → raw md**：pdf-to-markdown skill 转 `Cairn_2e_Wardens_Guide.pdf`
   - 已确认文本非艺术字型 OCR（p.82–86 预览），pymupdf 基础模式即可，**无需 `--docling`**
   - 产物：`Cairn_2e_Wardens_Guide.md` 在源 PDF 同目录
2. **按页范围切片**：按 §2 表格的源页范围截取到 9 个输出文件
3. **结构化重排**：
   - 章节标题按 §3 模板
   - stat block / 表格按 §3.2 / §3.3 模板
   - 保留 2e 专属术语（*petty*, *bulky*, *Cost*, *Watch*, *Heartseed*, *Gate*, *Roots*, *Heart Tree*）
4. **逐文件校验**：§5 清单

---

## 5. 分对话节奏

每对话处理 1–2 文件，遵循 CLAUDE.md §3.2 "每对话 1–2 章节" 原则。

| 对话 | 文件 | 备注 |
|---|---|---|
| #1 | `-bestiary.md` | 数据密集，单文件 |
| #2 | `-monster-creation.md` + `-spellbooks.md` | 中等规模 |
| #3 | `-reliquary.md` + `-advice.md` | 小型 |
| #4 | `-worldbuilding.md` | 最大文件，单独处理 |
| #5 | `-dungeon-seeds.md` | 生成器表多，单独处理 |
| #6 | `-faq.md` | 问答密集，单独处理 |
| #7 | `-vald-setting.md` | 收尾 |

总计 7 次对话。每次开新对话需带：`.claude/cairn2e-import-guide.md` + 本 spec + 目标文件所在章节的 PDF md 切片。

---

## 6. 校验清单

每文件完成后执行（通用清单 + 2e 专属）：

- [ ] **完整性**：PDF 对应页范围的小节是否全部包含？
- [ ] **数值准确**：抽查 5 个关键数值
  - Bestiary：HP / Armor / STR / DEX / WIL / 武器骰
  - 随机表：表格条目对照原文
  - 价格、距离、持续时间
- [ ] **表格完整**：行数与原文一致？d6 表 6 行，d20 表 20 行
- [ ] **格式一致**：
  - H1 `# Cairn 2e — ...` + blockquote 源信息 + Index
  - stat block 单行 blockquote
  - 术语粗体（*petty* 斜体保留原书语义）
- [ ] **2e ↔ 1e 不混淆**：无 1e 残留术语（Reputation、Misfortunes）
- [ ] **无 OCR 残留**：无断行错误、特殊字符、重复行

**Bestiary 专属校验**：
- [ ] 分类索引覆盖全部怪物
- [ ] 每个锚点有效（H3 名与索引链接匹配）
- [ ] 与 `cairn1e-bestiary.md` 的重复条目核对：Cobblehounds、Frost Elf、Boggart 等 1e/2e 都有的怪物，stat block 差异需忠实反映

---

## 7. 导入指南更新

完成后更新 `.claude/cairn2e-import-guide.md` §2 "Warden's Guide → 输出" 表格，把本 spec 的 9 文件列入并标记状态。

完成后更新 `.claude/CLAUDE.md` §1 状态表：Cairn 行改为 "已完成"。

---

## 8. 风险与兜底

- **风险：pdf-to-markdown 输出质量不达预期**（如表格错位、艺术字丢失）
  - 兜底：切到 `--docling` 模式重跑；或用 `pdf_extract.py` 按页取原始文本逐条补录
- **风险：Bestiary 分类归属有歧义**（如 Boggart 属 Fey 还是 Magical？）
  - 兜底：按 Cairn 2e 叙事倾向判断，有疑义时归 Other；不必追求学术分类
- **风险：FAQ 问题边界不清**（原书可能无明显 Q 标题）
  - 兜底：对话 #6 开始前先用 pdf_extract 看 p.154 起的段落结构，必要时按主题聚类重组为 H3，不强求问句原文
