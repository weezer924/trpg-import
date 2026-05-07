# Record of Lodoss War RPG (Companion I) 导入指南

> 源书：`Rule Books/Record of Lodoss War RPG/Record of Lodoss War Companion I.pdf`
> 版本：1989 年 Group SNE 出版的 Companion I 規則書（英文同人翻译版，149 页）
> 输出：`output/Lodoss/`
> 系统简称：Lodoss

## 0. 系统背景

- 罗德岛战记（Record of Lodoss War / ロードス島戦記）原以 Replay I/II 形式连载于 Comptiq 杂志（1986–1988，使用 Classic D&D 规则）
- **Companion I（1989）是 Group SNE 为 Lodoss 题材开发的独立系统**，与早期 D&D Replay 不同
- 后续作品：Replay III（1988–1989）已使用 Companion 規則
- 本系统是 Sword World RPG 的设计前身，Forceria 设定亦最早成型于本书
- 本仓库已有 Sword World 1.0 输出（独立系统，不要混同）

## 1. 输出文件结构

```
output/Lodoss/
├── rules/                           # 8 章核心规则
│   ├── 00-overview.md               # Rule Section intro + Dice Explanation + 阅读指引
│   ├── 01-character-creation.md     # Ch.1 PC 创建（种族 / 职业 / 属性 / 技能 / 流程）
│   ├── 02-character-growth.md       # Ch.2 角色成长（经验值、升级、属性增长）
│   ├── 03-combat.md                 # Ch.3 战斗系统
│   ├── 04-magic.md                  # Ch.4 魔法（5 大法术系统 + 全法术列表）
│   ├── 05-action-resolution.md      # Ch.5 行动判定（六大技能检定）
│   ├── 06-monsters.md               # Ch.6 怪物（数据读法 + 样本怪物）
│   ├── 07-items.md                  # Ch.7 基础装备
│   └── 08-gm-advice.md              # Ch.8 GM 建议
├── lore/                            # 世界观（如导入）
│   ├── mythology.md                 # 罗德岛神话
│   ├── history.md                   # 罗德岛历史
│   ├── geography.md                 # 罗德岛地理
│   └── encyclopedia.md              # 编年史百科
├── collections/                     # NPC / 法术 / 怪物 / 装备 / 建筑数据集（如导入）
│   ├── characters.md                # 主要 NPC（Parn、Deedlit、Slayn、Ghim、Etoh、Woodchuck 等）
│   ├── spells.md                    # 法术补充
│   ├── monsters.md                  # 怪物补充
│   ├── items.md                     # 装备补充（含著名魔法物品）
│   └── buildings.md                 # 建筑数据
└── campaign/                        # 4 个收录冒险（PDF p.99–127）
    ├── 01-strange-love-potion.md    # Episode 1（已完成，p.99–105）
    ├── 02-wizards-move.md           # Episode 2（已完成，p.106–112）
    ├── 03-dark-elf-statue.md        # Episode 3（已完成，p.113–121）
    └── 04-invitation-from-past.md   # Episode 4（已完成，p.122–127）
```

## 2. 章节优先级

**P0 — 核心规则（先做）**

| 文件                       | 源 MD 行号    | 源 PDF 页码 | 估计篇幅 |
| -------------------------- | ------------- | ----------- | -------- |
| `00-overview.md`           | 296–360       | 22–23       | 小       |
| `01-character-creation.md` | 362–728       | 24–30       | 中       |
| `02-character-growth.md`   | 730–794       | 31–33       | 小       |
| `03-combat.md`             | 796–948       | 34–37       | 中       |
| `04-magic.md`              | 950–1856      | 38–48       | **大**   |
| `05-action-resolution.md`  | 1858–1965     | 49–51       | 小       |
| `06-monsters.md`           | 1966–2316     | 52–61       | 中       |
| `07-items.md`              | 2318–2456     | 62–64       | 中       |
| `08-gm-advice.md`          | 2458 起       | 65          | 小       |

**P1 — 世界观（按需）**：lore/ 下 4 文件，对应 PDF p.13–21 + p.93–97
**P2 — 数据集合（按需）**：collections/ 下 5 文件，对应 PDF p.66–92
**P3 — 冒险模组（按需）**：campaign/ 下 4 文件，对应 PDF p.99–127

## 3. 格式约定

- 英文为主（源 PDF 是英文同人翻译）
- 关键术语 / 专有名词附中文注释：`Warrior（战士）`、`Pharis（法利斯）`
- 罗德岛专有人名 / 神名第一次出现保留英文 + 中文：`Parn（帕恩）`、`Deedlit（蒂德利特）`
- 数值表格用 markdown 表格，数字列右对齐
- 每个文件开头：`#` 标题 + `>` 引用块标注来源（PDF 页码范围）+ `## Index`

### 文件头模板

```markdown
# Chapter N: Title

> 来源：Record of Lodoss War Companion I（1989, Group SNE）PDF p.XX–YY
> 译本：英文同人翻译版

## Index

- [小节 1](#小节-1)
- [小节 2](#小节-2)
```

## 4. 关键术语对照（保持全书一致）

### 种族 Races
- Human（人类）、Elf（精灵）、Half-Elf（半精灵）、Dwarf（矮人）

### 职业 Classes
- Warrior W（战士）、Priest P（神官）、Scout T（斥候）、Knight K（骑士）
- Shaman H（精灵使）、Sorcerer S（魔术师）、Wizard Z（贤者）

### 属性 Stats（7 项）
- Strength ST（力量）、Endurance EN（耐力）、Agility AG（敏捷）
- Intelligence IN（智力）、Luck LU（幸运）、Physical Beauty PB（外貌）
- Concentration CN（精神力）

### 技能 Skills（6 项）
- Fighting Skill FS（战斗技能）、Defense Skill DE（防御技能）
- Thief Skill TS（盗贼技能）、Magic Skill MS（魔法技能）
- Resistance RE（抗性）、Concentration CN（专注）

### 数值 Stats
- LP（Life Points 生命点）、MP（Mental Points 精神点）
- DB（Damage Bonus 伤害加值）

### 神明 Gods（神官信仰对象）
- Pharis（法利斯，至高神）、Marfa（玛法，地母神）
- Myrii（玛利，战神）、Rahda（拉达，知识神）、Cha Za（夏扎，财神）

### 法术系统 Magic Systems
- Shaman Magic（精灵魔法）、Sorcerer Magic（魔术）、Common Magic（共通魔法）
- Priest Magic（神官魔法）、Demon Scream（魔神咏唱）

## 5. 处理 PDF 转换产物的注意事项

源 MD（pymupdf4llm 输出）有以下伪影需清理：

1. **页码裸行**：单独的 `8`、`24` 等数字行 → 删除
2. **End of picture text 标记**：`<br>**----- End of picture text -----**<br>` → 删除
3. **章节扉页装饰文字**：很多章节有占整页的章节图说明，提取时混入正文 → 整理或删除
4. **段落内换行**：原文换行符在 md 里被保留为段落断开 → 合并为完整段落
5. **表格裂行**：复杂表格可能被切成多块 → 检查并重组
6. **中文标记意外混入**：偶有 `①②③` 等数字符号，保留即可

## 6. 校验清单（每个文件完成后）

- [ ] 文件头有 `#` 标题、`>` 来源说明、`## Index`
- [ ] 数值（LP/MP 表、技能修正表、伤害骰、伤害加值表）逐条对照 PDF
- [ ] 表格行数与 PDF 一致
- [ ] 法术 / 装备名称英中对照统一
- [ ] 没有页码裸行、End of picture text 等伪影
- [ ] 与其他章节交叉引用正确（如「详见 Chapter 5」）

## 7. 已知特殊章节

- **Chapter 4: Magic** 篇幅最大（~900 行），包含五大法术系统和全法术列表，建议单独一个对话处理
- **Character Creation** 含 LP/MP 表、Skill Modifier 表等多个数值表，需特别仔细
- **Demon Scream** 是本系统独有的「魔神咏唱」机制，与一般法术规则差异大，注意保留特别说明
