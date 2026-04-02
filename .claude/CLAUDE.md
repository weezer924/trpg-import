# TRPG 规则 PDF 导入项目

> 本项目从各类 TRPG（桌面角色扮演游戏）的 PDF 规则书中提取内容，生成结构化 markdown 文件，供 AI DM / Keeper 在游戏中查阅使用。

---

## 1. 支持的游戏系统

| 系统 | 简称 | 状态 | 源 PDF 目录 | 输出目录 |
|------|------|------|------------|---------|
| D&D 5e (2014) | Dnd5e | 已完成 | `D&D 5e/Core/` | `output/Dnd5e/` |
| D&D 5e 模组 | — | 部分完成 | `D&D 5e/Modules/` | `output/Dnd5e/campaign/` |
| D&D 5.5e (2024) | — | 待导入 | `D&D 5.5e/Core/` | `output/Dnd5e2024/` |
| D&D 3.5e | — | 待导入 | `D&D 3.5e/` | `output/Dnd35e/` |
| AD&D 1e | ADnD1e | 导入中 | `AD&D 1st edition/` | `output/ADnD1e/` |
| AD&D 2e | ADnD2e | 待导入 | `AD&D 2nd edition/` | `output/ADnD2e/` |
| D&D Classic (Mentzer/RC) | DnDClassic | 部分完成 | `D&D Classic/` | `output/DnDClassic/` |
| Old-School Essentials | OSE | 已完成 | `OSE/` | `output/OSE/` |
| Call of Cthulhu 7e | CoC | 待导入 | `Call of Cthulhu/` | `output/CoC/` |
| Cairn (1e & 2e) | Cairn | 待导入 | `Cairn/` | `output/Cairn/` |
| OSR 相关 | — | 参考 | `OSR related/` | — |
| 其他系统 | — | 按需添加 | `{System}/` | `output/{System}/` |

**战役模组/战役设定**导入到各系统输出目录下的 `campaign/` 子目录，详见各系统的战役导入指南。

---

## 2. 项目结构

```
/Users/jack/Projects/trpg-projects/Rule Books/   # 源 PDF 文件（所有系统）
  ├── D&D 5e/
  │   ├── Core/                    # PHB, MM, DMG 中译
  │   ├── Modules/                 # 战役模组（中译为主）
  │   └── Supplements/             # 补充规则
  ├── D&D 5.5e/
  │   └── Core/                    # 2024 修订版核心书
  ├── D&D 3.5e/                    # 3.5e 补充书
  ├── AD&D 1st edition/            # AD&D 1e 核心书 + 模组（T1-4, GDQ1-7, Dragonlance 等）
  ├── AD&D 2nd edition/            # AD&D 2e 核心书 + PHBR/DMGR 系列 + Dragonlance + FR
  ├── D&D Classic/                 # Mentzer BECMI 全套 + Rules Cyclopedia + 模组
  │   └── Modules/                 # B/X 系列模组
  ├── OSE/                         # Old-School Essentials (B/X 复刻)
  ├── Call of Cthulhu/             # 克苏鲁的呼唤 7e
  ├── Cairn/                       # Cairn 1e & 2e
  │   ├── Cairn 1st/
  │   └── Cairn 2e/
  ├── OSR related/                 # OSR 相关参考资料
  └── Todos/                       # 待整理

output/                            # 输出目录，按系统分子目录
  ├── Dnd5e/                       # D&D 5e
  │   ├── rules/                   # 规则书输出（PHB, MM, DMG, Spells）
  │   └── campaign/                # 战役模组输出
  │       └── thessalhydra/        # Thessalhydra 自作模组
  ├── ADnD1e/                      # AD&D 1e
  │   └── campaign/                # 战役模组输出
  │       ├── ravenloft/           # I6 Ravenloft（完成）
  │       └── temple-of-elemental-evil/  # T1-4（计划中）
  ├── DnDClassic/                  # D&D Classic (Mentzer/RC)
  │   └── campaign/
  ├── OSE/                         # Old-School Essentials
  │   ├── rules/                   # 规则书输出（Classic + Advanced）
  │   ├── campaign/                # 战役模组输出（含 B/X 经典模组，按 OSE 格式导入）
  │   │   ├── keep-on-the-borderlands/   # B2
  │   │   ├── nights-dark-terror/        # B10
  │   │   ├── the-hole-in-the-oak/       # OSE 原创
  │   │   └── the-lost-city/             # B4
  │   └── supplements/             # 补充（necromancer）
  └── ...
pdf_extract.py                     # PDF 文本提取工具（pymupdf）
```

---

## 3. 通用导入规范

以下规范适用于所有系统的规则导入。各系统的专属指南会补充或覆盖这些规范。

### 3.1 格式规范

- GitHub Flavored Markdown
- 中文为主（如源 PDF 是中文），专有名词保留中英对照：`中文名（English Name）`
- 英文 PDF 按原文导入，关键术语可附中文注释
- 数值必须精确：AC、HP、伤害骰、DC、距离、持续时间等不可有误
- 数值表格用 markdown 表格，数字列右对齐
- 每个文件开头需要 `#` 标题行 + `>` 引用块说明来源版本 + `## Index` 目录

### 3.2 导入流程核心原则

- **一次只处理一本书**，不要跨书操作
- **每个对话只提取 1-2 个章节**，context 堆积后质量会下降
- **每个章节提取完成后立即校验**，不要等全部做完再查
- **context 变长后果断开新对话**，带上相应系统的导入指南 + 已完成的输出文件继续
- 输出文件采用**追加模式**：每个对话在已有文件末尾追加新章节内容
- 优先使用 `pdf_extract.py` 提取 PDF 文本，再格式化为 markdown

### 3.3 每章节检查清单

每提取一个章节后执行：

- [ ] **完整性**：目录中列出的小节是否全部包含？
- [ ] **数值准确**：抽查 5 个关键数值，与 PDF 原文对比
- [ ] **表格完整**：所有表格的行数是否与原文一致？
- [ ] **格式一致**：标题层级、标记符号、术语格式是否统一？
- [ ] **无乱码**：没有 PDF 提取残留的特殊字符或断行错误

### 3.4 质量验证

- 数值必须逐条对照 PDF，不可凭记忆补充
- 不同版本内容不可混入（如 D&D 不能混 2014 和 2024，CoC 不能混 6 版和 7 版）
- 同一系统的多个输出文件之间不能有矛盾

---

## 4. 各系统专属导入指南

每个游戏系统有独立的详细导入指南，包含：输出文件列表、章节优先级、格式模板、分对话计划、版本注意事项等。

| 系统             | 指南文件                                  | 说明                                               |
| ---------------- | ----------------------------------------- | -------------------------------------------------- |
| D&D 5e 规则书    | `.claude/dnd5e-rules-import-guide.md`     | 三本核心书 → 5 个输出文件                          |
| D&D 战役模组     | `.claude/dnd-campaign-import-guide.md`    | 模组 PDF → output/Dnd5e/campaign/ 多文件结构       |
| OSE 规则书       | `.claude/ose-import-guide.md`             | OSE Classic/Advanced 规则书导入                    |
| OSE 战役模组     | `.claude/ose-campaign-import-guide.md`    | B 系列模组 → output/OSE/campaign/ 多文件结构       |
| AD&D 1e 战役模组 | `.claude/adnd1e-campaign-import-guide.md` | T1-4 等模组 → output/ADnD1e/campaign/ 多文件结构   |
| CoC              | `.claude/coc-import-guide.md`             | 待创建                                             |

**导入新系统时**：先创建该系统的专属导入指南（参考 dnd5e 指南的结构），再按指南逐步执行。

---

## 5. 工具

### 5.1 pdf_extract.py

基于 pymupdf 的 PDF 文本提取工具。导入时优先使用此工具提取原文，再格式化为 markdown。

### 5.2 convert_pdfs.py

批量转换辅助脚本。

---

## 6. 注意事项

1. **不要混版本**：每个系统严格使用指定版本的 PDF，不要从 AI 训练数据中补充其他版本内容
2. **不要省略**：规则描述、数据块、法术/技能效果必须完整，不能缩写
3. **保留原文术语**：PDF 中的术语格式保持原样
4. **页码标注**：在每个大章节开头标注 PDF 页码范围，便于后续校对
5. **导入模组时**：先读对应系统的战役导入指南，按其规范执行
