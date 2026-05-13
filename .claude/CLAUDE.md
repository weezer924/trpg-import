# TRPG 规则 PDF 导入项目

> 本项目从各类 TRPG（桌面角色扮演游戏）的 PDF 规则书中提取内容，生成结构化 markdown 文件，供 AI DM / Keeper 在游戏中查阅使用。

---

## 0. 新对话从这里开始

1. 确认要导入的系统 → 查第 1 节状态表
2. 读该系统的专属导入指南（第 4 节表格）
3. 按指南执行；每对话只处理 1-2 章节，完成后立即校验
4. 输出追加到 `output/{System}/` 对应文件

---

## 1. 支持的游戏系统

| 系统                     | 简称       | 状态     | 源 PDF 目录               | 输出目录                   |
| ------------------------ | ---------- | -------- | ------------------------- | -------------------------- |
| D&D 5e (2014)            | Dnd5e      | 已完成   | `D&D 5e/Core/`            | `output/Dnd5e/`            |
| D&D 5e 模组              | —          | 部分完成 | `D&D 5e/Modules/`         | `output/Dnd5e/campaign/`   |
| D&D 5.5e (2024)          | —          | 待导入   | `D&D 5.5e/Core/`          | `output/Dnd5e2024/`        |
| D&D 3.5e                 | —          | 待导入   | `D&D 3.5e/`               | `output/Dnd35e/`           |
| AD&D 1e                  | ADnD1e     | 导入中   | `AD&D 1st edition/`       | `output/ADnD1e/`           |
| AD&D 2e                  | ADnD2e     | 待导入   | `AD&D 2nd edition/`       | `output/ADnD2e/`           |
| D&D Classic (Mentzer/RC) | DnDClassic | 部分完成 | `D&D Classic/`            | `output/DnDClassic/`       |
| Old-School Essentials    | OSE        | 已完成   | `OSE/`                    | `output/OSE/`              |
| Call of Cthulhu 7e       | CoC        | 待导入   | `Call of Cthulhu/`        | `output/CoC/`              |
| Cairn (1e & 2e)          | Cairn      | 已完成   | `OSR related/Cairn 1st/`、`OSR related/Cairn 2e/` | `output/Cairn/rules/`      |
| Mörk Borg (Bare Bones)   | MorkBorg   | 已完成   | `Mork Borg/`              | `output/MorkBorg/`         |
| Operation WhiteBox       | OWB        | 已完成   | `Operation White Box/`    | `output/OWB/`              |
| Tales from the Loop      | TFTL       | 部分完成 | `Tales from the Loop/`    | `output/TalesFromTheLoop/` |
| Sword World 1.0          | SW         | 已完成   | `source/Sword World 1.0/` | `output/SwordWorld/`       |
| Classic Traveller (1981) | Traveller  | 已完成   | `Traveller/Classic Traveller/` | `output/Traveller/`   |
| Shadowdark               | Shadowdark | 部分完成 | `Shadowdark/`             | `output/Shadowdark/`       |
| Mythic GME 2e            | Mythic     | 已完成   | `Mythic GME/`             | `output/Mythic/`           |
| Mausritter               | Mausritter | 已完成   | `OSR related/Mausritter/` | `output/Mausritter/`       |
| Lodoss War (Companion I) | Lodoss     | 已完成   | `Record of Lodoss War RPG/` | `output/Lodoss/`         |
| Mothership 1e            | Mothership | 已完成（除模组）| `OSR related/Mothership/` | `output/Mothership/`       |
| **Trench Crusade 1.0.2** ⚔️战棋 | TrenchCrusade | 待导入 | `Trench Crusade/` | `output/TrenchCrusade/` |
| OSR 相关                 | —          | 参考     | `OSR related/`            | —                          |
| 其他系统                 | —          | 按需添加 | `{System}/`               | `output/{System}/`         |

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
  ├── OSR related/                 # OSR 相关参考资料（Cairn 1e/2e 在此）
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
  │   └── campaign/                # B/X 经典模组（按 OSE 格式导入）
  │       ├── keep-on-the-borderlands/   # B2
  │       ├── nights-dark-terror/        # B10
  │       └── the-lost-city/             # B4
  ├── OSE/                         # Old-School Essentials
  │   ├── rules/                   # 规则书输出（Classic + Advanced）
  │   ├── campaign/                # OSE 原创模组
  │   │   └── the-hole-in-the-oak/
  │   └── supplements/             # 补充（necromancer）
  ├── OWB/                         # Operation WhiteBox (WWII OSR)
  │   └── rules/
  ├── MorkBorg/                    # Mörk Borg
  │   └── rules/
  ├── Cairn/                       # Cairn 1e + 2e（文件名前缀区分）
  │   └── rules/                   # cairn1e-{rules,spells,bestiary}.md
  │                                # cairn2e-{overview,character-creation,rules,procedures,backgrounds}.md
  ├── TalesFromTheLoop/            # Tales from the Loop
  │   ├── rules/
  │   ├── campaign/
  │   └── characters/
  ├── Mothership/                  # Mothership 1e (Sci-Fi Horror)
  │   ├── rules/                   # PSG（玩家手册） + WOM（监守手册）切分
  │   ├── supplements/             # 拆船员工具箱 / 黑客 / 仿生人扩展 / 术语表 / 飞船 d100
  │   ├── campaign/                # 6 个中译模组（Bug Hunt / Ypsilon 14 等）
  │   └── characters/
  ├── TrenchCrusade/               # Trench Crusade（战棋，AI 当对手玩家）
  │   ├── rules/                   # 核心规则拆分
  │   ├── warbands/                # 战团（每 faction 一文件）
  │   ├── errata/                  # 官方 FAQ/裁决
  │   ├── narrative/               # 叙事调色板（tone-guide + injury-flavor + event-triggers）
  │   ├── matches/                 # 战场状态 yaml + 坐标系契约（替代 TTRPG saves/）
  │   └── lore/                    # 可选 lore（简略时间线）
  └── ...
pdf_extract.py                     # PDF 文本提取工具（pymupdf，备用/grep 用）
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
- 优先使用 pdf-to-markdown skill 转换 PDF，再在 `output/{System}/` 下整理为结构化 markdown

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

| 系统             | 指南文件                                  | 说明                                             |
| ---------------- | ----------------------------------------- | ------------------------------------------------ |
| D&D 5e 规则书    | `.claude/dnd5e-rules-import-guide.md`     | 三本核心书 → 5 个输出文件                        |
| D&D 战役模组     | `.claude/dnd-campaign-import-guide.md`    | 模组 PDF → output/Dnd5e/campaign/ 多文件结构     |
| OSE 规则书       | `.claude/ose-import-guide.md`             | OSE Classic/Advanced 规则书导入                  |
| OSE 战役模组     | `.claude/ose-campaign-import-guide.md`    | B 系列模组 → output/OSE/campaign/ 多文件结构     |
| AD&D 1e 战役模组 | `.claude/adnd1e-campaign-import-guide.md` | T1-4 等模组 → output/ADnD1e/campaign/ 多文件结构 |
| OWB 规则书       | `.claude/owb-import-guide.md`             | WWII 特战 OSR → 2 个输出文件                     |
| Sword World 1.0  | `.claude/swordworld-import-guide.md`      | 日式 2d6 OSR → 6 个输出文件（源为 txt）          |
| Classic Traveller | `.claude/traveller-import-guide.md`      | LBB 1-2-3 合订（扫描件，需 docling OCR）→ 6 个输出文件（errata 内联合并）|
| Cairn 2e         | `.claude/cairn2e-import-guide.md`         | Player's Guide → 5 文件（已完成）+ Warden's Guide 待办 |
| Mythic GME 2e    | `.claude/mythic-import-guide.md`          | Solo storytelling engine → 5 目录 37 文件（AI-facing） |
| Lodoss War (Companion I) | `.claude/lodoss-import-guide.md`  | 1989 Group SNE 独立 TRPG（英译版）→ rules/ 9 + lore/ 4 + collections/ 5 + campaign/ 4 已完成 |
| Mothership 1e    | `.claude/mothership-import-guide.md`      | Sci-Fi horror（中译 v1.3）→ rules/ 15 + supplements/ 5 + campaign/ 6 + characters/ |
| **Trench Crusade ⚔️** | `.claude/trenchcrusade-import-guide.md` | **战棋**（非 TTRPG，AI 当对手玩家）→ v0.1 MVP: rules/ 7 + warbands/ 2 派 + errata + narrative/ 4 + matches/（坐标系契约） |
| CoC              | `.claude/coc-import-guide.md`             | 待创建                                           |

**导入新系统时**：先创建该系统的专属导入指南（参考 dnd5e 指南的结构），再按指南逐步执行。

---

## 5. 工具

### 5.1 pdf-to-markdown skill

**首选**，任何 PDF 转 markdown 都先用它。基于 pymupdf4llm，输出结构化 markdown（含图片、表格、缓存）。见 `.claude/skills/pdf-to-markdown/`。

- 艺术字型密集的 PDF（Mörk Borg 等 OSR 美术重度书）必须加 `--docling`，否则 pymupdf 会静默丢失艺术字文本。

### 5.2 pdf_extract.py

备用。基于 pymupdf 的原始文本提取，用于 grep 搜索或校对 markdown 输出。

```bash
python3 pdf_extract.py "Rule Books/<系统>/<书>.pdf" --pages 10-30
python3 pdf_extract.py some.pdf --info   # 查总页数+目录
```

---

## 6. 注意事项

1. **不要混版本**：每个系统严格使用指定版本的 PDF，不要从 AI 训练数据中补充其他版本内容
2. **不要省略**：规则描述、数据块、法术/技能效果必须完整，不能缩写
3. **保留原文术语**：PDF 中的术语格式保持原样
4. **页码标注**：在每个大章节开头标注 PDF 页码范围，便于后续校对
5. **导入模组时**：先读对应系统的战役导入指南，按其规范执行

---

## 7. AI 查阅项目（sibling 目录）

每个系统在 `/Users/jack/Projects/trpg-projects/{SystemName}/` 下有独立项目目录，供 AI DM / Keeper 运行游戏：

- `rules/` → symlink 到 `dnd-rules-import/output/{System}/rules/`（结构化规则）
- `campaign/` → symlink 到 `.../output/{System}/campaign/`（模组）
- `characters/` → symlink 到 `.../output/{System}/characters/`（PC/pregens）
- `rule books/` → symlink 到 `Rule Books/{系统}/md files/`（PDF→md 原文，对照用）
- `tools/mcp-server/` — 骰子/状态/存档 MCP 服务
- `.mcp.json` 的 `cwd` 必须指向本项目目录（不是旧的 `/Users/jack/Projects/OSE`）

已建：OSE、WW2 OBW、Tales from the loop、Mork Borg、SwordWorld、DnDClassic、Shadowdark、Traveller、Cairn2e、**Mothership**。新增系统时复制 Mork Borg 模板即可。

**Mothership 注意**：是首个用 **Python MCP** 的 sibling（其他系统用 Node/TS）。`tools/mcp-server/` 用 `uv` 管理依赖，`.mcp.json` 的 `command` 是 `uv` 而非 `node`。结构对 AI 透明，但维护时记得 `uv sync` 而非 `npm install`。详见 `tools/mcp-server/README.md`。

**Cairn2e 注意**：rules/ 里每个 md 是指向 `output/Cairn/rules/cairn2e-*.md` 的 symlink（还附带 `cairn1e-spells.md`，因 2e Spellbooks 沿用 1e 法术表）。characters/ 和 campaign/ 目前在 `output/Cairn2e/` 下，是独立于 `output/Cairn/` 的 2e 专用子树。

**Trench Crusade 注意**：⚔️**唯一战棋系统**，sibling 项目暂缓（v0.2+ 规则稳定后再建）。与 TTRPG sibling 关键差异：
- AI 角色是 **Opponent**（对手玩家），不是 GM/Warden/Keeper
- 用 `matches/{name}/match-state.yaml`（战场状态）替代 `saves/{name}/{role}-notes.md`
- 不需要 `characters/`，改用 `warbands/`（战团列表）+ `matches/roster-template.md`（战团构建模板）
- 计划增加 `web-ui/` 子目录（HTML 战场 UI，玩家拖动棋子）
- MCP 主要工具：距离查询 / LOS 查询 / 移动合法性 / 战团构建校验 / 骰子（Python MCP，参考 Mothership）
- 详见 `.claude/trenchcrusade-import-guide.md` §4（坐标系契约）和 §7（sibling 项目设计）

### 7.1 角色模板约定

每系统在 `output/{System}/characters/character-template.md` 写创建步骤 + state.yaml schema。
建模板前查 `Rule Books/{系统}/Character Sheets.pdf`（若有）——纯表单图用 `Read` 工具多模态预览字段，
pdf-to-markdown 对这类 PDF 只能提标签文字。

### 7.2 saves/ 结构与命名

```
saves/{name}/
  state.yaml           # party/npcs/inventory/campaign 等
  {role}-notes.md      # referee-notes / gm-notes / keeper-notes（按系统角色术语）
  {theme}-log.md       # quest-log / mystery-log / mission-log / misery-log
saves/.active          # 当前活跃存档名
```

角色术语按系统官方定义（D&D=DM, OSE/OWB/MB=Referee, TFTL=GM, CoC=Keeper, Cairn=Warden, Mothership=Warden 监守）。
