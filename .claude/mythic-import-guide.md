# Mythic GME 2e 导入指南

> Mythic Game Master Emulator 2nd Edition (Tana Pigeon, Word Mill Games)
> 源 PDF：`Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.pdf`（230 页）
> 输出目录：`output/Mythic/`
> 设计 spec：`docs/superpowers/specs/2026-04-22-mythic-gme-import-design.md`
> 执行计划：`docs/superpowers/plans/2026-04-22-mythic-gme-import.md`

---

## 1. 定位

Mythic 2e 是**跨系统的 solo storytelling engine**——不是游戏系统，而是一套程序 + 随机表，用于 solo 或 GM-less 游戏中模拟 GM。

本次导入的**主要消费者是 AI**（运行 solo session）。输出结构按 AI 运行时需要分层，而非按 PDF 目录。

## 2. 输出结构

| 目录 | 角色 | AI 加载时机 | 特点 |
|---|---|---|---|
| `engine/` | **主入口** | Session 开始即全部加载 | 紧凑程序、决策树、解读心法。无叙述文。 |
| `rules/` | **兜底参考** | 规则歧义时查询 | PDF 线性转录，保留原文解释。 |
| `tables/` | **按需查询** | 每次判定/掷骰 | 纯数据，一表一文件。 |
| `examples/` | **风格校准** | 解读僵化时参考 | 4 个 Big Example，可扩展。 |
| `sheets/` | **模板** | Session 准备时参考 | Adventure Journal / Keyed Scenes 记录表。 |

## 3. 写作规范

### rules/
- 线性转录，按 PDF 章节顺序
- 保留 Crane 的概念讲解、设计理由、边界讨论
- Inline mini-examples（"假设 PC 在 X…"）随正文保留
- **4 个 Big Example 不放在 rules/**，迁到 `examples/`；rules/ 各章到 Big Example 前一页为止

### engine/
- 结构：`## When To Use / ## Procedure / ## Decision Tree / ## Failure modes / ## Cross-refs`
- 祈使句，无叙述连接词（"Now let's discuss", "As we've seen" 等）
- 跨文件引用用相对路径：`→ tables/fate-chart.md`

### tables/
- 每文件顶部 2-3 行 `When: / Input: / Output:` 使用说明
- Markdown 表格，数字列右对齐
- `meaning-elements.md` 内部用 `## <Theme>` 分隔 ~100 个子表

### examples/
- Frontmatter：`source` / `chaos-focus` / `length-turns` / `length-scenes`
- `_index.md` 先被 AI 读到，按 `chaos-focus` 标签匹配

### engine/07-interpretation-principles.md 提炼方法
- 读 4 个 Big Example + 扫 rules/ 里的解读相关段落
- 每条原则 = 祈使句 + 1-2 句说明 + 源引用
- 源引用必须精确：`examples/02-wutwo-labs.md turn 3` 或 `rules/02-fate-questions.md §When To Run With Expectations`
- 目标 ~25 条，上限 30

## 4. 章节 → 文件 → 页码对照

> **页码约定**：下表所有页码均为 **PDF 索引页**（pymupdf/pdf_extract 报告的页号）。
> 对应书印刷页码请减 1（PDF p.8 = 印刷 p.7）。

### rules/
| 文件 | PDF 页 | 备注 |
|---|---|---|
| `00-mythic-journey.md` | p.4 | 前言 |
| `01-mythic-adventures.md` | p.8-17 | Ch1 综述 |
| `02-fate-questions.md` | p.18-31 | Ch2（Henny Big Example p.32-35 不含） |
| `03-random-events.md` | p.36-54 | Ch3（Wutwo Big Example p.55-59 不含） |
| `04-scenes.md` | p.60-115 | Ch4（Guardian Big Example p.116-123 不含） |
| `05-variations.md` | p.124-177 | Ch5 可选规则 |
| `06-rules-summary.md` | p.187-192 | Ch7 官方摘要 |

### tables/ 页码分布
| 文件 | PDF 页 |
|---|---|
| `fate-chart.md` | p.20, 195 |
| `fate-chart-variants.md` | p.148-149, 222-223 |
| `fate-question-answers.md` | p.25, 195 |
| `fate-check-modifiers.md` | p.27, 196 |
| `random-event-focus.md` | p.38-44, 198-199 |
| `meaning-actions.md` | p.48, 200 |
| `meaning-descriptions.md` | p.49, 201 |
| `meaning-elements.md` | p.50, 88-106, 202-216 |
| `scene-adjustment.md` | p.71, 217 |
| `npc-behavior.md` | p.110, 218 |
| `npc-statistics.md` | p.128, 218 |
| `thread-progress-track.md` | p.133, 219-220 |
| `adventure-features.md` | p.161-165, 225-226 |

### examples/ 页码
| 文件 | PDF 页 |
|---|---|
| `01-henny-in-z-land.md` | p.32-35 |
| `02-wutwo-labs.md` | p.55-59 |
| `03-guardian-of-chosen-one.md` | p.116-123 |
| `04-the-big-example.md` | p.178-186 |

### sheets/ 页码
| 文件 | PDF 页 |
|---|---|
| `adventure-journal.md` | p.77-84 叙述 + p.193 模板 |
| `keyed-scenes.md` | p.150-154, 224 |

## 5. 质量校验清单

- [ ] Fate Chart 9×9 矩阵逐格核对（PDF p.20）
- [ ] Meaning Tables 每张表恰好 100 条
- [ ] engine/ 无叙述性连接句（`grep -E "Now let's|As we've seen|Let's discuss"` 应为空）
- [ ] 所有跨文件引用 `→ path/file.md` 指向真实文件
- [ ] Big Examples 的骰点 / Chaos Factor 转换 / scene 边界与 PDF 原文逐回合一致
- [ ] `engine/07-interpretation-principles.md` 每条原则都有源引用

## 6. 分对话工作计划

见 `docs/superpowers/plans/2026-04-22-mythic-gme-import.md` §Task 0-9。

## 7. 中间产物

以下文件位于源 PDF 旁边，**不入库**（已在 gitignore 覆盖）：

- `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.md` — pdf-to-markdown 产出的原始 md
- `Rule Books/Mythic GME/Mythic Game Master Emulator 2nd Edition.txt` — pdf_extract 产出，用于 grep 校验
- `Rule Books/Mythic GME/images/` — 提取的图片（本次导入不用）
