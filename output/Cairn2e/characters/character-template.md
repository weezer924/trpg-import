# Cairn 2e Character Template

> Cairn 2e 角色创建步骤 + `state.yaml` 角色字段 schema。
> 规则出处：`rules/cairn2e-character-creation.md`、`rules/cairn2e-backgrounds.md`、`rules/cairn2e-rules.md`。

## 创建步骤（Warden 引导）

按顺序掷：

1. **Background（d20）**
   - 表：`rules/cairn2e-character-creation.md` § Backgrounds Table
   - 详情：`rules/cairn2e-backgrounds.md`（20 个职业每个 2 页：起始物品 + 专属 d6/d10 小表 × 2-3 张）
   - 玩家从背景自带的物品表中掷出自己的起始装备、技能或专长
2. **Attributes（STR / DEX / WIL）**
   - 各掷 **3d6**（共 3 次，按顺序记 STR → DEX → WIL）
   - 玩家可 **交换其中两个**（仅一次）
3. **Hit Protection（HP）**
   - 掷 **1d6**；这是全部起始 HP（不是每级，Cairn 没级别）
4. **Traits（外观与性格）**—— 各掷 d10
   - Physique / Skin / Hair / Face / Speech / Clothing / Virtue / Vice（共 8 项）
   - 表在 `rules/cairn2e-character-creation.md` § Character Traits Tables
5. **Bonds（d20）**
   - 表在 `rules/cairn2e-character-creation.md` § Bonds Table
   - 记到人物卡 Bonds 栏
6. **Age（2d20+10）**；**最小年龄**的玩家掷 **Omen（d20）**
   - Omen 念给全桌听，Warden 将其织入世界
7. **Petty Items** — Warden 酌情给几件不占格的小物件（火石、信纸、骨针等）
8. **Armor & Weapons**
   - 多数背景自带基础武器/护甲；不够的用起始金币（背景决定数量，一般 3d6 gp）去 Marketplace 补
   - 护甲规则：Light=1 / Medium=2 / Heavy=3（只有 Bulky 铠能叠到 Armor 3；见 rules §Armor）

---

## `state.yaml` 角色字段 schema

```yaml
party:
  {pc_id}:                    # slug，如 vania / old-torvald
    name: "Vania of the Fen"
    pronouns: she/her
    background: "Bog Witch"   # 见 backgrounds.md
    age: 31

    # 核心属性（current / max）
    str: {current: 11, max: 11}
    dex: {current: 13, max: 13}
    wil: {current: 14, max: 14}
    hp:  {current: 4,  max: 4}

    deprived: false            # true 时无法恢复 HP / 属性，每 24h 失 1 Fatigue
    armor: 1                   # 0-3；来自装备的护甲加总
    gold: 8

    # 外观性格（建卡时掷出）
    traits:
      physique: "wiry"
      skin: "weathered"
      hair: "braided grey"
      face: "sharp"
      speech: "whispered"
      clothing: "patchwork robes"
      virtue: "patient"
      vice: "superstitious"

    # 社交
    bonds:
      - "I owe a debt to the hag who raised me."
    omens: []                  # 只有最年轻 PC 有 1 条

    # 物品：10 格背包 + petty + 具名小物
    inventory:                 # 10 格，每格 string 或 null
      - "shortsword (d6)"
      - "shield (+1 armor)"
      - "lantern"
      - "oil flask"
      - "rations ×3"           # 可把堆叠数写进名字
      - "rope, 50ft"
      - null
      - null
      - null
      - null
    petty_items:               # 不占格
      - "flint & steel"
      - "silver locket"
    fatigue: 0                 # 独立计数；每级 Fatigue 占 inventory 末尾 1 格

    # Warden 提醒用
    notes: "从家乡躲瘟疫逃出。"
    conditions: []             # 临时状态：prone, blinded 等
    scars: []                  # Scars 表结果（rules § Scars Table）
    spellbooks: []             # 具名 Spellbook（占 1 格，见 cairn2e-warden-spellbooks.md）
    relics: []                 # 具名 Relic（通常 1 格，见 cairn2e-warden-reliquary.md）
```

### 关键机制提醒

- **HP = 0 → Critical Damage**：掷 STR Save；失败死亡；成功读 **Scars 表**（`rules/cairn2e-rules.md` § Scars Table）
- **属性伤害归零**：STR=0 死、DEX=0 瘫、WIL=0 疯
- **Save = d20 ≤ 当前属性**（注意用 **current**，不是 max）
- **Fatigue**：每级 Fatigue 占一格 inventory 直到背包塞满；塞满后再来 Fatigue → 角色 **Deprived**
- **Deprived**：不回 HP / 属性；每 24h 再 −1 Fatigue（此时 Fatigue 反而是负数概念：指实际减去的属性值，见 rules § Deprivation）
- **Scroll**：单次施法卷轴；Spellbook 可反复但 **每次施法 1 Fatigue**
- **Relic charges**：每日/每 session 刷新，按该遗物条目

### Inventory 槽位规则速查

| 项目 | 占格 |
|------|------|
| 普通武器 / 护甲片 / 工具 | 1 格 |
| Bulky 物（两手武器、重甲、大桶） | 2 格 |
| Petty Items（小饰品、信件、钥匙） | 0 格 |
| Spellbook | 1 格（Bulky=2） |
| Relic | 通常 1 格，某些 Bulky |
| Fatigue | 每级 1 格（从末尾算起） |

---

## 新建 PC 流程（Warden checklist）

- [ ] 问玩家：先掷还是先选 Background？
- [ ] 确定 Background → 查 `cairn2e-backgrounds.md` 对应页，执行该背景的小表掷骰
- [ ] 掷 3d6×3（STR/DEX/WIL），确认是否交换两项
- [ ] 掷 1d6（HP）
- [ ] 掷 8×d10（Traits）
- [ ] 掷 d20（Bonds）
- [ ] 掷 2d20+10（Age）；party 里最年轻者加掷 d20 Omen
- [ ] 收拢 Petty Items（Warden 酌情）
- [ ] 填 Marketplace 补齐装备（若有剩余 gp）
- [ ] 把以上写进 `saves/{active}/state.yaml` 的 `party.{pc_id}` 节点
- [ ] 在 `adventure-log.md` 记一笔"{name} 加入冒险"
