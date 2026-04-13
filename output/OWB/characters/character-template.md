# Operation WhiteBox — 特战员角色模板

## 创建步骤

1. 投 3d6（按顺序）六项属性：STR、DEX、CON、INT、WIS、CHA
2. 选国籍 Nationality（American / British / Canadian / Free French / Soviet / 等）
3. 选职业 Class（8 个，见下）
4. 选 Profession（职业前的平民/军旅背景）
5. 选军衔 Rank + Alignment（Lawful / Neutral / Chaotic）
6. 购买装备（起始金额按职业/国籍）
7. 在 `state.yaml` 的 `party` 下添加数据
8. 本目录创建 `{id}.md` 记录背景

## 8 职业（Character Classes）

| 职业 | 首要属性 | HD | 说明 |
|------|---------|----|----|
| Combat Engineer | INT | d6 | 爆破、障碍、工事 |
| Commando | STR | d6 | 近战专家、突袭 |
| Field Medic | WIS | d6 | 治疗、稳定伤员 |
| Grease Monkey | INT | d6 | 机械/载具维修与驾驶 |
| Hunter | DEX | d6 | 狙击、追踪、潜行 |
| Maquis | DEX | d6 | 游击队、抵抗运动 |
| Officer | CHA | d6 | 指挥、外交、鼓舞 |
| Scrounger | DEX | d6 | 搜刮、补给、装备替换 |

详情见 `rules/owb-rules.md` § Character Classes。

## state.yaml 特战员模板

```yaml
party:
  operative_id:              # e.g. sgt_miller
    name: SSgt. John Miller
    nationality: American
    profession: Former boxing coach
    class: Commando
    rank: Staff Sergeant
    level: 1
    alignment: Lawful
    attributes:                # score / modifier
      str: { score: 15, mod: +1 }
      int: { score: 10, mod:  0 }
      wis: { score: 11, mod:  0 }
      con: { score: 14, mod: +1 }
      dex: { score: 13, mod: +1 }
      cha: { score: 12, mod:  0 }
    hp:
      current: 7
      max: 7
    aac: 14                    # Ascending AC（10 + 护甲 + DEX mod）
    bhb: 1                     # Base Hit Bonus
    save: 15                   # 单一豁免值
    xp: 0
    class_abilities:
      - Melee specialist (+1 dmg with bayonet/knife)
      - Sneak attack
    languages:                 # F=Fluent / M=Moderate / B=Basic（官方角色纸标记）
      - { name: English, level: F }
      - { name: French,  level: B }
    weapons:                   # 官方字段：Weapon / Dmg / ROF / Range
      - name: M1911A1
        type: Pistol
        damage: 1d6+1
        rof: 1                 # Rate of Fire（shots/round）
        range: "50'"
        ammo: 7/21             # 当前弹匣/备用
      - name: Thompson M1A1
        type: SMG
        damage: 1d6+1
        rof: "1 / auto"        # 半自动 / 全自动扫射
        range: "50'"
        ammo: 30/90
    armor: Olive drab uniform
    gear:
      - K-ration x4
      - Medical pack
      - Wire cutters
      - 2x M1 Frag grenade
```

## 武器 & 弹药

详见 `rules/owb-rules.md` § Gear and Weapons。弹药按武器单独追踪（`inventory` MCP 工具），不可通用。

## 升级

- 击败敌人 + 任务目标 + 情报/装备回收 → XP（详见 `rules/owb-rules.md` § Experience）
- 满 XP 升级 → HP + BHB + 豁免进步，按职业表
