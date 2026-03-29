---
name: OSE CRPG 游戏项目
description: 基于 OSE 规则的老派 CRPG 设计 — 规则引擎+编辑器+Mod 支持，忠实还原不做妥协
type: project
---

用户正在规划一个基于 OSE (Old-School Essentials) 的 CRPG 游戏项目。

**产品形态**：规则引擎 + 编辑器 + Mod 支持（类似 Neverwinter Nights 模式）

**核心设计哲学**：硬核忠实还原，规则书怎么写引擎就怎么跑。不为迎合现代玩家而降低难度或提供便利化替代。只保留 OSE 书中明确标注为 Optional Rule 的可选规则。

**开发路线**：Classic 先行 → Advanced 扩展 → Mod 生态。Classic 是完整游戏，Advanced 主要是加数据。

**架构关键决策**：
- 种族和职业从一开始设计为可分离的两个实体（为 Advanced 预留）
- 法术独立于职业，通过法术列表关联
- 所有游戏内容为外部数据文件，引擎不硬编码具体职业/法术/怪物
- Mod 可添加新实体、扩展现有实体

**设计文档位置**：`output/OSE/ose-crpg-design.md`

**Why:** 用户想做老派桌游到电子游戏的忠实翻译，面向 OSR 社区玩家。

**How to apply:** 涉及 OSE 规则讨论或游戏设计时参考此项目背景。不要建议降低难度或现代化改动。
