# Tales from the Loop — Kid 角色模板

## 创建步骤

1. 选 Type（原型）：Bookworm / Computer Geek / Hick / Jock / Popular Kid / Rocker / Troublemaker / Weirdo
2. 年龄 10–15（决定属性总点数 + Luck 上限）
3. 分配属性（Body / Tech / Heart / Mind，每项 1–5，总点数 = 年龄）
4. 选一项 Iconic Item、Problem、Drive、Pride、Anchor、Relationships
5. 在 `state.yaml` 的 `party` 下添加 Kid 数据
6. 本目录创建 `{id}.md` 记录 Kid 背景、朋友、家庭

## Kid 属性

| 属性 | 用于 |
|------|------|
| **Body** | 跑跳、打架、潜行、攀爬 |
| **Tech** | 理解机器、编程、撬锁、制造 |
| **Heart** | 社交、欺骗、人脉、说服 |
| **Mind** | 找弱点、理解他人、解谜、知识 |

## 12 技能

每技能 0–3 点，总技能点数按 Type 决定（Quickstart 是预分配）。技能参见 `rules/quickstart-rules.md` § 12 项技能详解。

## Luck

- 初始 = 15 − 年龄
- 每场开始回满；不可留
- 用于 Help、Push 后的状态缓解

## state.yaml Kid 模板

```yaml
party:
  kid_id:                    # 英文 id，e.g. olle
    name: Olle Eklund
    type: Computer Geek
    age: 12
    attributes:
      body: 2
      tech: 5
      heart: 3
      mind: 2
    skills:                  # 仅列出 ≥1 的
      program: 3
      comprehend: 2
      investigate: 1
    iconic_item: 自组电脑
    problem: 父母刚离婚
    drive: 证明 Loop 现象是真的
    pride: 我比任何大人都懂电脑
    anchor:
      name: 姐姐 Eva
      relation: 唯一相信我的家人
    relationships:
      - kid_id: simone
        note: 她从不取笑我
    conditions: []           # upset/scared/exhausted/injured/broken
    luck:
      current: 3
      max: 3                 # = 15 - age
    xp: 0
```

## 角色成长

- 每场 Mystery 结束投 XP 条件（见 `rules/quickstart-rules.md`，若未导入则协商）
- 满足条件 → +1 skill point
- 每满 16 岁退役
