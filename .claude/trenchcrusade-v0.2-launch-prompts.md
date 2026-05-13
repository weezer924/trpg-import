# Trench Crusade v0.2 新对话启动 prompts

> 用法：v0.2 Phase A-E 每个 phase 开一个**新对话**（避免 context 累积），从本文件复制对应 prompt 粘贴。
> 每个 prompt 是 self-contained 的——读不到本对话，所以包含完整必读路径。
> 配套规划文档：[[trenchcrusade-v0.2-engineering-plan]]

---

## Phase A 启动 prompt — sibling 项目脚手架

```
# Trench Crusade v0.2 Phase A — 建 sibling 项目脚手架

## 任务
建 `/Users/jack/Projects/trpg-projects/TrenchCrusade/` sibling 项目，让 v0.1 已完成的规则文档可被 AI 通过 symlink + .mcp.json 访问。预计 0.5 工作日。

## 必读（按顺序）

1. **v0.2 工程化计划**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-v0.2-engineering-plan.md` **§Phase A**（详细步骤 / 目录骨架 / 完成判定）
2. **v0.1 导入指南 §7**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-import-guide.md`（sibling 项目设计原则，特别是 TC 与 TTRPG sibling 的差异——AI 是 Opponent 不是 Warden）
3. **Mothership sibling 项目（唯一 Python MCP 模板）**：
   - `/Users/jack/Projects/trpg-projects/Mothership/.claude/CLAUDE.md`
   - `/Users/jack/Projects/trpg-projects/Mothership/.mcp.json`
   - `/Users/jack/Projects/trpg-projects/Mothership/README.md`
   - `/Users/jack/Projects/trpg-projects/Mothership/tools/mcp-server/`（只看目录结构 + pyproject.toml；不抄 Mothership 业务代码）
4. **v0.1 主入口**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/rules/00-overview.md`（理解 AI 角色 + 文件地图）

## 具体步骤
完全按 v0.2 plan §A.2 执行。注意：
- `matches/` **不能**整体 symlink——内部 markdown 是 symlink，`test-match/` 是本地子目录
- sibling `.claude/CLAUDE.md` 必须明确 AI = Opponent + Battle Narrator，不是 GM
- `tools/mcp-server/` 和 `.mcp.json` 本 Phase 只建占位（Phase B 才填实际内容）

## 完成判定（v0.2 plan §A.3）
- [ ] `ls /Users/jack/Projects/trpg-projects/TrenchCrusade/rules/` 显示 9 个 v0.1 文件
- [ ] `.claude/CLAUDE.md` 给清晰 AI 角色定位 + 入口 → rules/00-overview.md
- [ ] `matches/test-match/match-state.yaml` 可写（非 symlink）
- [ ] git init + first commit
- [ ] **`.claude/trenchcrusade-import-guide.md` §7 状态行更新为"已建"**

## 报告
完成后输出：
1. sibling 根目录绝对路径
2. 目录树（`tree -L 2 -d` 或 `find . -maxdepth 2 -type d`）
3. 所有 symlinks 的目标对照表
4. `.claude/CLAUDE.md` 行数 + 大节目录
5. 第一次 git commit hash
6. 启动 Phase B 前的注意事项
```

---

## Phase B 启动 prompt — Python MCP server v0

```
# Trench Crusade v0.2 Phase B — Python MCP server v0

## 任务
实现 coordinate-system §8 的 6 接口 + 6 骰子工具 + 7 yaml CRUD + roster 校验，集成到 sibling 项目。预计 1.5-2 工作日。

## 前提
Phase A 已完成——sibling 项目 `/Users/jack/Projects/trpg-projects/TrenchCrusade/` 已建，含 symlinks + 占位 `.mcp.json`。如未完成，先执行 Phase A。

## 必读（按顺序）

1. **v0.2 工程化计划**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-v0.2-engineering-plan.md` **§Phase B**（接口表 / 骰子表 / yaml CRUD 表 / roster 校验 10 条）
2. **数字化契约**（最关键，规定所有算法）：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/coordinate-system.md`
   - §3.1 距离算法 + §3.3 6 个测试用例
   - §6.2 LOS 算法 + §6.3 4 个测试用例
   - §7 地形 schema
   - §8 6 接口签名
3. **战场状态 schema**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/match-template.yaml`（MCP CRUD 操作的对象）
4. **roster 校验规范**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/roster-template.md` §6（10 条 self-check）
5. **骰子规则源**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/rules/02-comprehensive-rules.md` §Success Rolls / §Injury Rolls / §Bloodbath Rolls / §Falling
6. **Mothership MCP 实现参考**：`/Users/jack/Projects/trpg-projects/Mothership/tools/mcp-server/` 的 pyproject.toml + 任一 tool 模块结构（不抄业务，看技术栈）

## 实施顺序（建议）
1. `pyproject.toml`（uv + fastmcp + pyyaml + pytest）
2. `src/coord.py` 6 接口 → 用 §3.3 6 测试用例 + §6.3 4 测试用例做 pytest
3. `src/dice.py` 6 骰子 → 单元测试看分布合理
4. `src/match.py` yaml CRUD → 用 match-template.yaml 做 round-trip 测试
5. `src/roster.py` 校验器 → 用 roster-template.md §7 两个示例做正例 + 至少 3 个错误 case 做反例
6. `src/server.py` 注册所有工具到 MCP
7. 更新 sibling `.mcp.json` cwd + command
8. `pytest` 全绿后整体 commit

## 关键约束
- **数值绝对精确**：距离保留 1 位小数（§3.1），骰子 success 阈值是 7+（§1.4），injury 阈值 1-/2-6/7-8/9+（§10）
- **`valid_charge_paths` v0 可 stub**（仅校验 distance + LOS，complex pathing 留 v0.5）
- **schema 与 yaml template 同步**：server 启动时校验
- 骰子返回 `{rolls, picked, total, result}` 完整结构（让 AI 能解释）

## 完成判定（v0.2 plan §B.7）
- [ ] 6 coord + 6 骰子 + 7 yaml CRUD + 1 roster 校验全部实现
- [ ] pytest 全绿（含 §3.3 6 距离 + §6.3 4 LOS 用例）
- [ ] sibling `.mcp.json` 注册成功，Claude Code `/mcp` 显示 trenchcrusade server
- [ ] 能从 Claude Code 调用任意工具且返回合理结果

## 报告
完成后输出：
1. sibling MCP server 代码行数（按模块）
2. pytest 报告（通过数 / 总数 + 任何 skipped）
3. 6 距离 + 4 LOS 用例的实测数值表（vs §3.3 / §6.3 预期）
4. MCP 工具注册清单（tool name + 简介）
5. 已知 limitation（如 `valid_charge_paths` 是 stub）
6. 启动 Phase C 前的注意事项
```

---

## Phase C 启动 prompt — AI master prompt

```
# Trench Crusade v0.2 Phase C — AI master prompt

## 任务
写 AI 对手的 system prompt，让 Claude 能在 sibling 项目中按规则出招、调 MCP 不心算、套描述模板。预计 1 工作日。

## 前提
Phase A + B 已完成——sibling + MCP server 跑通。如未完成，先做 Phase A/B。

## 必读（按顺序）

1. **v0.2 工程化计划**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-v0.2-engineering-plan.md` **§Phase C**（大纲 8 节）
2. **AI 角色规范**：
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/rules/00-overview.md`（§AI 对手运行流程 7-step）
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/narrative/tone-guide.md`（语气 + 禁区）
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/narrative/world-primer.md`（意象调色板）
3. **描述模板**：
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/narrative/injury-flavor.md`（6 结果 × 8 武器类别矩阵）
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/narrative/event-triggers.md`（7 事件钩子）
4. **规则源**：
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/rules/02-comprehensive-rules.md`（详细规则）
   - `/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/errata/rules-commentaries.md`（裁决）
5. **MCP 工具清单**：调 sibling MCP server `/mcp` 或读 `tools/mcp-server/src/server.py` 看注册的工具名 + 签名

## 输出
- **方案 a（推荐）**：独立文件 `tools/ai-opponent-prompt.md`（sibling 项目内）
- 或方案 b：扩展 sibling `.claude/CLAUDE.md`

推荐 a——prompt 会迭代多次，独立文件方便 diff。

## 内容（v0.2 plan §C.2 大纲，目标 300-500 行）
1. 角色定位（Opponent + Battle Narrator，不是 GM）
2. 必读清单（rules/00-overview / tone-guide / world-primer / 自己 warband）
3. **激活回合 7-step 决策树**（参考 rules/00-overview §7）
4. 拒绝违规请求的护栏
5. 边界条件（问玩家 vs 自决）
6. 描述长度规范（引 tone-guide）
7. 错误恢复（MCP 失败 / schema 错位）
8. **自检 prompt 段**：每个激活前自问"我准备心算了吗？应该调 MCP"

## 关键约束
- **反复强调调 MCP 不心算**（这是 coord §1 的硬规）
- **拒绝**：玩家提议非规则行动 → 引规则文档；推翻骰子结果 → 拒绝；战场外剧情 → 拒绝
- AI **始终**是 Opponent + Battle Narrator（narrative/tone-guide.md ❌ 禁区）

## 测试
用 Phase D 的 match-cli（如已有）或直接在 sibling 项目用 Claude Code 触发一个 sample turn：
- 加载 `roster-template.md` §7 的 NA 示例 roster
- 加载 Scenario I battlefield
- 让 AI 做一次激活，观察输出是否含：
  - 选了哪个模型 + 为什么
  - MCP 调用 log（distance / los / validate_move）
  - 骰子结果
  - 描述 1-3 段（按 tone-guide 风格）

## 完成判定（v0.2 plan §C.4）
- [ ] Prompt 300-500 行
- [ ] sample turn 跑通，AI 输出含 MCP 调用 log + 描述
- [ ] AI **5 次激活内 0 次心算**（log 全是 MCP 调用）

## 报告
完成后输出：
1. prompt 文件路径 + 行数
2. 8 大节是否齐全（每节行数）
3. sample turn 文本日志（含 AI 输出 + MCP 调用）
4. 自检 prompt 段的具体措辞
5. 启动 Phase D 前的注意事项
```

---

## Phase D 启动 prompt — match-cli

```
# Trench Crusade v0.2 Phase D — match-cli CLI 文本 UI

## 任务
最小命令行工具让玩家能完整跑一局：看状态 / 移棋子 / 触发 AI 回合 / 投骰。预计 1 工作日。

## 前提
Phase A + B 已完成（MCP server 跑通，CLI 是 thin wrapper 调它）。Phase C 推荐已完成（CLI 触发 AI turn 才有意义）。

## 必读（按顺序）

1. **v0.2 工程化计划**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-v0.2-engineering-plan.md` **§Phase D**（命令集 / ASCII grid / 架构）
2. **战场 schema**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/match-template.yaml`
3. **地形分类**（ASCII 渲染需要）：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/coordinate-system.md` §7.3
4. **Phase B 实现的 MCP server**：sibling `tools/mcp-server/src/server.py`（看可调工具清单）
5. **roster 示例**（开始一局用）：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/roster-template.md` §7

## 8 个命令（v0.2 plan §D.1）

| 命令 | 用途 |
|---|---|
| `match-cli new <scenario> --red-roster X.yaml --blue-roster Y.yaml` | 新建战场 |
| `match-cli show [--grid]` | 显示状态（ASCII grid 或 yaml） |
| `match-cli move <model_id> <pos>` | 玩家移棋 |
| `match-cli activate <model_id> <action> [target]` | 触发 ACTION（含投骰） |
| `match-cli ai-turn` | 触发 AI 激活所有未激活模型 |
| `match-cli end-turn` | 结束回合 + Morale Phase |
| `match-cli history` | 显示事件日志 |
| `match-cli quit` | 保存退出 |

## ASCII grid 渲染
36×36 战场，5 类地形字符（v0.2 plan §D.2）+ 双方模型 ID 缩写。横向 1:1、纵向压缩。

## 架构
所有命令通过 sibling MCP server 调用——CLI 只做 dispatcher + 输入解析 + 输出渲染。

## 完成判定（v0.2 plan §D.4）
- [ ] 8 命令实现
- [ ] ASCII grid 渲染 5 类地形 + 双方棋子
- [ ] `match-cli ai-turn` 触发 Phase C prompt 跑通

## 报告
完成后输出：
1. CLI 工具路径（sibling 内）+ 代码行数
2. 8 命令的实测输出示例（每个 1 行）
3. ASCII grid sample（36×36 截图，文本）
4. 启动 Phase E 前的注意事项
```

---

## Phase E 启动 prompt — 试玩 + 文档回填

```
# Trench Crusade v0.2 Phase E — 试玩 Claim No Man's Land + 文档回填

## 任务
完整跑一局 Scenario I "Claim No Man's Land"（New Antioch vs Heretic Legions），记录所有 friction，回填到对应文档。预计 1-2 工作日。

## 前提
Phase A-D 全部完成——sibling + MCP server + AI prompt + match-cli 跑通。

## 必读

1. **v0.2 工程化计划**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/.claude/trenchcrusade-v0.2-engineering-plan.md` **§Phase E**（试玩流程 / friction 分类 / 完成判定）
2. **Scenario I 规则**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/rules/08-scenarios.md` §2（Claim No Man's Land）
3. **两个示例 roster**：`/Users/jack/Projects/trpg-projects/dnd-rules-import/output/TrenchCrusade/matches/roster-template.md` §7
4. **AI prompt**：sibling `tools/ai-opponent-prompt.md`（Phase C 产出）

## 试玩流程

1. `match-cli new claim-no-mans-land --red-roster roster-a.yaml --blue-roster roster-b.yaml`
2. 部署（玩家 + AI 各部）
3. **跑 4 回合**（Scenario I 长度）或胜利
4. 玩家操作红方（NA "Duke's Forlorn Hope"），AI 操作蓝方（HL "Sevenfold Maw"）
5. 全程记录 friction

## Friction 记录格式

每条 friction 记成：
```
- type: rules-gap | schema | ai-prompt | narrative | mcp-bug | unit-data
- description: ...
- occurred-at: turn N, model X, action Y
- proposed-fix: 改哪个文件、改什么
- severity: critical (阻塞游戏) | major (规则错) | minor (体验问题)
```

## Friction 回填目标（v0.2 plan §E.2）

| 类型 | 回填目标 |
|---|---|
| rules-gap | `rules/02-comprehensive-rules.md` 增补 |
| schema | `matches/coordinate-system.md` §7 + `match-template.yaml` |
| ai-prompt | sibling `tools/ai-opponent-prompt.md` |
| narrative | `narrative/injury-flavor.md` / `event-triggers.md` |
| mcp-bug | sibling `tools/mcp-server/src/*` + 加测试 |
| unit-data | `warbands/*` 或 `rules/05-battlekit.md` |

## 完成判定

- [ ] 一局完整跑完（4 回合或胜利）
- [ ] 至少 5 条 friction 回填对应文档
- [ ] **第二局测试基本无新 friction**（v0.2 finalized）
- [ ] 更新 `.claude/CLAUDE.md` 状态行从 "v0.1 完成（v0.2 工程化中）" → "已完成（v0.2 含 sibling + MCP）"

## 报告
完成后输出：
1. 第一局完整日志（回合 1-4，每回合关键决策 + 骰子结果 + 描述节选）
2. Friction 列表（按 severity 排序）+ 回填 commit 列表
3. 第二局摘要日志 + 新 friction 计数（目标 ≤ 1）
4. v0.2 finalize 状态
5. v0.3 候选 backlog（如玩家体验问题 / web UI 需求 / 多 scenario 需求）
```

---

## 使用建议

- **顺序执行 Phase A → B → C → D → E**，每个 Phase 开新对话
- 每个 prompt 顶部都带"前提"——确保前置 Phase 已完成
- Phase B 是关键 phase（最长），如果对话 context 不够，可拆成 B.1 coord 接口 + B.2 骰子+yaml+roster 两个对话
- Phase E 是验收 phase，friction 多时不要硬撑——记录就好，下个对话回填
- 每个 Phase 完成后**更新 v0.2-engineering-plan.md** 标注实际产出 + 偏差
