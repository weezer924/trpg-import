---
name: 模组导入必读指南
description: 导入战役模组 PDF 时必须先读对应系统的 campaign-import-guide，按其结构输出多文件
type: feedback
---

导入任何战役模组 PDF 时，必须先读取对应系统的 campaign-import-guide 并严格按其规范执行。

**Why:** 用户第一次要求导入模组时，我错误地提议输出为单个 markdown 文件，而正确做法是按 guide 输出到 `output/{System}/campaign/world/{module-name}/` 目录下的多文件结构（region/quests/npcs/encounters/shops/locations）。

**How to apply:** 每次用户提到"导入模组"或指向模组 PDF 时，第一步就是读对应的 campaign-import-guide（如 `.claude/dnd-campaign-import-guide.md`），然后按规范执行。
