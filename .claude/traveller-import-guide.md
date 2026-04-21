# Classic Traveller 导入指南

> 源 PDF：`Rule Books/Traveller/Classic Traveller/Classic Traveller (Facsimile 1981 edition).pdf`
> 版本：1981 年修订版（GDW Little Black Books 1-2-3 合订复刻，161 页）
> 提取文件：同目录下 `Classic Traveller (Facsimile 1981 edition).md`（4997 行，docling + OCR 生成）
> 输出目录：`output/Traveller/rules/`

---

## 1. 导入前须知

- **扫描件 + OCR**：原 PDF 是 1981 年 LBB 照相复刻，pymupdf 直接提取会丢失大部分正文（只剩小部分 errata 行）。**必须**用 `--docling` 模式重跑，docling 自带 OCR 能把 161 页的扫描页转出 ~5000 行干净文本。
- **OCR 偶有残缺**：表格数字、短缩写（如 `DM+1`、`Cr31,200`）可能粘连或缺格；每导入一章都要对照 PDF 原页校对关键数值。
- **不要混其他版本**：Classic Traveller ≠ MegaTraveller ≠ T4 ≠ Mongoose 2e，规则差距很大。看到有疑问的数字直接查 errata（md 4831 行之后）。

## 2. 输出文件规划

| 输出文件 | 对应章节 | md 源行 | 优先级 |
|---|---|---|---|
| `book1-characters.md` | Book 1: Introduction + Characters（创角、职业、技能、退役、年龄） | 148–983 | **P0** |
| `book1-combat.md` | Book 1: Combat（流程、武器表、护甲、白刃） | 984–1624 | P0 |
| `book2-starships.md` | Book 2: Travelling + Starship Economics + Design & Construction + Space Combat | 1626–3006 | P1 |
| `book2-computers-economy.md` | Book 2: Computers + Experience + Drugs + Trade & Commerce | 3007–3257 | P1 |
| `book3-worlds-equipment.md` | Book 3: Worlds（星图生成、UWP）+ Equipment | 3258–3935 | P2 |
| `book3-encounters.md` | Book 3: Encounters + Animal Encounters + Psionics + A Final Word | 3936–4818 | P2 |

共 **6 个文件**（errata 不独立成文）。

### Errata 策略：内联合并，取消独立文件

`Consolidated Traveller Errata`（md 行 4831–4984）修订分两类：

- **`a` 标记**（checkmark）：facsimile 原文已内联修正，导入时正文已是修订版
- **`;` 标记**（marginal）：原书因排版未内联，导入时**直接合并**到相应规则段落（markdown 无排版限制）

**具体合并清单**（导入时执行）：

- `book1-combat.md`：
  - 替换 Combat Procedure 为 errata p.30 新版
  - Weapons Matrix 修正值：Dagger/Combat = -7、Foil/Combat = -6、Carbine/Ablat = -1、Rifle/Cloth = -3、Rifle/Reflec = +2、Rifle/Combat = -5
  - Range Matrix：SMG/Long = -3
  - 补 Ablat 脚注（激光每命中 DM -1）
  - 补 Claws 2D / Cutlass 3D / Body Pistol 2D 伤害
  - 补 Untrained "+3 defending" 修正
  - Morale 25%（非 20%）
  - 补齐武器缺漏描述（Body Pistol/Auto Pistol/Revolver/Carbine/Rifle/Shotgun/SMG 的 silencer/folding-stock 等）
  - 补 Special Considerations 整节：Reloading / Darkness & Night / Cover & Concealment / Zero Gravity / Throwing Blades / Weapon Length / Armor Layering
- `book1-characters.md`：
  - Other Skills 补 Maximum Skills 规则（Int + Edu 上限）
  - Electronics Skill 补 Referee 段
  - Vehicle Skill 改为新分组（Aircraft / Grav / Tracked / Wheeled / Watercraft）
  - Gunnery Skill：page 13 → page 17
  - 例题 Jamison 起始现金：Cr33,200 → **Cr31,200**
- `book2-starships.md`：
  - Ship Design 修正：Scout/Courier MCr 29.43、Subsidized Merchant MCr 100.035、Subsidized Liner MCr 245.97、Yacht MCr 51.057、Mercenary Cruiser MCr 429.804 / 28 个月、Patrol Cruiser 160 吨油 / MCr 229.59 / 16 个月
  - 补 Retrofitting Components（Computers/Turrets 段）
  - 补 Pulse Lasers 规则（DM -1 to hit, 双倍伤害骰）
  - Decompression：`throw Dexterity or less`（非 8+）
  - 补 Expendables 段（Missiles Cr5600 / Sand Cr400）
  - Drive Failure：每**月** +1（非每周）
  - Starship Encounters Table：C/D 级星港无 naval base 栏位
- `book2-computers-economy.md`：
  - Non-Agricultural world 分类：atmos 3- / hydro 3- / pop 6+
  - Trade Speculation 基价修正：Air/Raft Cr600,000、ATV Cr30,000、AFV Cr70,000、Petrochemicals 数量 6D×5
- `book3-worlds-equipment.md`：
  - Hydrographics 公式：`2D - 7 + atmosphere`（非 size）
  - Gas Giant 精炼包含来回航行时间，采样 8 小时
  - Vacc Suit 引用 Book 1 page 41
- `book3-encounters.md`：
  - Animal Wounds：牙齿 2D（非 1D）
  - Atmosphere 8+ DM 修正为 +2
  - Psionic Ranges 增 Far Orbital：Telep 7 / Clair 5 / TK — / Aware 6

**每个文件头部引用块追加**：

```
> Errata：本文件已合并 Don McKinney's Consolidated Traveller Errata 中的修订，
> 原 1981 版错误见源 PDF p.154-158。
```

## 3. 每个对话只做 1-2 个文件

Context 会堆积，OCR 噪声需要逐段人工清理，单对话超过 2 文件质量下降明显。建议顺序：

1. 对话 A：`book1-characters.md`（核心的"人生模拟"创角——Traveller 的灵魂）
2. 对话 B：`book1-combat.md`
3. 对话 C：`book2-starships.md`（注意这个文件跨 4 个章节，可再拆为 2 个对话）
4. 对话 D：`book2-computers-economy.md` + `errata.md`
5. 对话 E：`book3-worlds-equipment.md`
6. 对话 F：`book3-encounters.md`（含 Psionics）

## 4. 格式规范

遵循主 `CLAUDE.md` 第 3 节通用规范，外加：

- **英文导入**：PDF 为英文原版，markdown 保留英文正文；关键术语首次出现附中文注释：`Strength（力量，Str）`。
- **术语表**：章节开头放"Key Terms"小表格列出该章核心缩写：`UPP`、`UWP`、`DM`、`Cr`、`TL`、`Str/Dex/End/Int/Edu/Soc`。
- **骰子**：2d6 记为 `2D`，3d6 记为 `3D`，单 d6 记为 `1D`（原书写法）。修正记作 `DM +2` / `DM -3`。
- **Throw**：Traveller 称"目标值"为 "throw"。保留原表达：`throw 8+ to succeed (DM +1 per level of skill)`。
- **信用币**：`Cr` 前缀表示 Credits，逐字保留 `Cr500`、`Cr31,200`、`MCr100.035` 等写法。
- **职业表格**：Prior Service / Personal Development / Service Skills / Advanced Education 等 6x6 表格用 markdown 表格，右对齐数字列。
- **UPP（Universal Personal Profile）**：角色 6 属性用十六进制两位写法，例：`787C46`。
- **UWP（Universal World Profile）**：星球用 `A788899-B` 形式。
- **章节结构**：每个输出文件开头：
  - `#` 书名 + 章节名
  - `>` 引用块：源 PDF + 版本 + 页码范围
  - `## Index` 章节目录
  - `## Key Terms` 缩写表
  - 正文

## 5. 数值校对重点（Book 1 优先）

每章导入后至少抽查 5 处：

- **Characteristics**：2D 生成 Str/Dex/End/Int/Edu/Soc，每项 2–12
- **Aging table**：34 岁起每 4 年掷 1 次物理属性检定
- **Career Types**：6 种（Navy/Marines/Army/Scouts/Merchants/Other）对应 Enlistment throw
- **Prior Service Table**：6 列 × 6 行，每格含 Enlistment / Survival / Commission / Promotion / Reenlistment 5 个 throw
- **Skill throws**：Personal Development / Service Skills / Advanced Education / Advanced Education (Edu 8+) 各 6 项
- **Combat DMs**：武器 × 护甲矩阵（Dagger / Foil / Cutlass / Body Pistol / Auto Pistol / Revolver / Carbine / Rifle / Auto Rifle / Shotgun / SMG / Laser Carbine / Laser Rifle 等 × Nothing / Jack / Mesh / Cloth / Reflec / Ablat / Combat / Battle）

对每个 throw 目标值、每个 DM、每个 Cr 售价，都要对照 PDF 扫描页二次确认。

## 6. 参考资源

- **Errata**：md 4831-4984 含 Book 1/2/3 已知错误及修正，先看一遍再导入
- **Extracted images**：md 末尾 `## Extracted Images` 表列出 docling 提取出的 9 张图（表格型），需要时对照
- **原页 PDF**：用 `pdf_extract.py --pages N-M` 可重新提某页原始文本做交叉验证
