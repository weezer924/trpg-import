# Sword World RPG 1.0 导入指南

> 将 Sword World RPG 1.0 Complete Edition 核心规则导入为结构化 markdown，供 AI GM 查阅。

## 源文件

- **主源**：`source/Sword World 1.0/Sword World.txt`（17692 行，英文 fan translation）
- 参考：同目录 PDF（日文原版）仅作校对备查
- 前 799 行为完整 ToC，第 800 行起为正文
- 章节边界以 `CHAPTER N` 行首标记

## 输出结构

```
output/SwordWorld/rules/
  index.md              系统介绍 + 2d6 骰系 + 文件索引
  players-section.md    CH1–CH4, CH6–CH8
  magic.md              CH5 + CH11 + CH17
  gm-section.md         CH9, CH10, CH12, CH14, CH15
  monsters.md           CH13 全怪物
  optional-rules.md     CH16, CH18
```

## 源章节行号索引

| CH | 标题 | 行号 |
|----|------|------|
| 1  | CHARACTERS | 800 |
| 2  | SUCCESS ROLLS | 2174 |
| 3  | COMBAT ROUNDS | 2393 |
| 4  | WEAPON COMBAT | 2594 |
| 5  | MAGIC | 3896 |
| 6  | NON-COMBAT/MAGIC SKILLS | 7343 |
| 7  | GENERAL SKILLS | 7865 |
| 8  | CHARACTER GROWTH | 8068 |
| 9  | NOTES ON SUCCESS ROLLS | 8243 |
| 10 | NOTES ON COMBAT | 8385 |
| 11 | NOTES ON MAGIC | 8512 |
| 12 | VARIOUS CHECKS | 9357 |
| 13 | MONSTERS! | 10137 |
| 14 | TREASURE | 15299 |
| 15 | CALCULATING XP | 16612 |
| 16 | COMBAT OPTIONS | 16666 |
| 17 | MAGIC OPTIONS | 17376 |
| 18 | OTHER OPTIONS | 17474 |

## 分对话计划

每对话只处理下列一批，完成后开新对话继续。

| # | 产出文件 / 追加内容 | txt 行范围 |
|---|--------------------|------------|
| 1 | 新建 `index.md` + 新建 `players-section.md` 含 CH1–CH4 | 800–3895 |
| 2 | 追加 CH6–CH8 到 `players-section.md` | 7343–8242 |
| 3 | 新建 `magic.md` 含 CH5 | 3896–7342 |
| 4 | 追加 CH11 + CH17 到 `magic.md` | 8512–9356, 17376–17473 |
| 5 | 新建 `gm-section.md`（CH9, CH10, CH12, CH14, CH15） | 8243–8511, 9357–10136, 15299–16665 |
| 6 | 新建 `monsters.md` 含 CH13 前半 | 10137–~12700 |
| 7 | 追加 CH13 后半到 `monsters.md` + 新建 `optional-rules.md`（CH16, CH18） | ~12700–15298, 16666–17375, 17474–end |

## 格式规范

- 语言：**保持英文原文**（与 OWB / MorkBorg 一致）
- 文件头：`#` 标题 + `>` 来源块（标注 "Complete Edition fan translation, source: Sword World.txt lines X–Y"）+ `## Index`
- 数值表用 markdown 表，数字列右对齐
- 怪物数据块参考 `output/OSE/rules/monsters.md` 风格（统一字段顺序）
- 法术数据块统一格式：Name / Level / Targets / Range / Duration / Resistance / Effect

## 每章节完成后执行

CLAUDE.md §3.3 检查清单：完整性、数值准确、表格完整、格式一致、无乱码。

特别注意 SW 1.0 独有项：
- 技能（Skill）≠ 职业：玩家可多技能叠加（Fighter + Sorcerer 等），升级独立计算
- Adventurer Level = 各技能等级加总（非最大值）
- 2d6 双6=自动成功（含暴击），双1=自动失败
- Mental Power（精神力）是法术消耗资源

## 不在本次范围

- World Guide（阿雷克拉斯特 / 罗德斯岛 / 十童子）
- Lodoss World Guide
- Western Countries World Guide
- Character Making Course（Dragon Magazine 连载）

后续如导入世界设定，新建 `output/SwordWorld/setting/` 目录。
