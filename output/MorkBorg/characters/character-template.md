# Mörk Borg — Scvm 角色模板

## 创建步骤

按 `rules/morkborg-rules.md` § Create a Player Character：

1. 投 d6 决定起始 Container（包/箱/桶等）
2. 随机武器（d10）、护甲（d4）
3. 投属性：Agility / Presence / Strength / Toughness（3d6 → 查表得 −3 到 +3）
4. 投 HP（按 Toughness）
5. （可选）投 Optional Tables（p.38–42）获 Terrible Trait、Broken Body、Bad Habit 等
6. 起始银币 2d6 × 10 s，水袋，d4 天口粮
7. （可选）选 Optional Class：Esoteric Hermit / Fanged Deserter / Gutterborn Scum / Wretched Royalty
8. 给角色起名（不会救你）
9. 在 `state.yaml` 的 `party` 下添加数据
10. 本目录创建 `{id}.md` 记录背景

## 属性表

| 属性 | 用于 |
|------|------|
| **Agility** | 攻击、躲避、反应、潜行 |
| **Presence** | Powers/Scrolls、社交、Reaction |
| **Strength** | 近战伤害、扛物、背包格数 |
| **Toughness** | HP、抗打击、中毒 |

**检定**：d20 + 属性 ≥ DR 12（基准）→ 成功。

## state.yaml Scvm 模板

```yaml
party:
  scvm_id:                   # e.g. gristle
    name: Gristle the Wretched
    description: 驼背、脸颊有疤、穿着父亲留下的破烂皮甲。
    class: Gutterborn Scum   # or None / Esoteric Hermit / Fanged Deserter / Wretched Royalty
    abilities:
      agility: 1
      presence: -1
      strength: 2
      toughness: 0
    hp:
      current: 6
      max: 6
    omens:
      current: 2
      max: 2                 # 按职业/等级
    silver: 40                # s
    weapons:
      - name: Polearm
        damage: d8            # two-handed
        notes: ""
    armor:
      name: Light (leather, padded)
      tier: 1
      armor_die: d2           # d2/d4/d6
    container: Sturdy sack
    inventory:
      - Waterskin (full)
      - Dried food (3 days)
      - Torch x2
    traits:                  # 可选表随机结果
      terrible: Left-handed
      broken_body: Missing finger
      bad_habit: Talks to dead
    powers:
      uses_per_day: "Presence + d4"   # 当日剩余次数追踪在 state
      uses_remaining: 2
    scrolls:
      unclean: []
      sacred: []
    conditions: []
```

## Miseries 追踪

官方角色纸上有 **1–6 Miseries 格子**（= Calendar of Nechrubel 的 6 verses；6 格全满后下一个 Misery → 世界毁灭）。**Miseries 是战役级倒计时**（整个世界共享，非每 PC 独立）。放在：

```
saves/{active}/referee-notes.md  →  ## Miseries
                                     - [x] 1. The first misery ...
                                     - [ ] 2. ...
```

或 `state.yaml` 顶层：

```yaml
campaign:
  miseries_triggered: 2        # 已触发数（0–7）
  calendar_of_nechrubel: ...   # 触发条件/描述
```

触发规则见 `rules/morkborg-rules.md` § Basilisk's Demand。

---

## 背包

- 总格数 = 8 + Strength
- 超格 → 负重惩罚（Agility 检定惩罚）

## 死亡 & 替补

- 0 HP → 投 d4 查 Broken 表（`rules/morkborg-rules.md` § Violence）
- 死亡 → 新 Scvm 顶替（快餐式，5 分钟内创好）
- 已死角色归档到 `roster/{id}.md`（可选）

## 升级（Getting Better）

见 `rules/morkborg-rules.md` § Getting Better。每场 Mystery/冒险结束投升级，随机增减属性、HP、Omens。**Mörk Borg 的升级是随机的，也可能变差**。
