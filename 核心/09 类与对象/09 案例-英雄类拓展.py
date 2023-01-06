"""
创建一个游戏英雄类，

分别有以下属性
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）, 对被攻击人造成对等的攻击力伤害
  逃跑方法: 如果血量低于50, 被攻击者就自动逃跑

创建两个英雄
    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""


class Hero:
    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self, obj, att):  # 此参数必须得传一个英雄对象进来
        obj.blood -= att
        if obj.blood < 50:  # 如果血量小于50
            print(f'目前被攻击者的血量: {obj.blood}')
            # 就自动逃跑
            self.run(obj)
            return ' '
        return f'{self.name} 发动了攻击, 攻击了 {obj.name}'

    def run(self, who):
        print(f'{who.name} 逃跑了')


hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '弓箭', ['头盔', '靴子'], 100)

for i in range(26):
    print(hero1.attack(hero2, 2))
    if hero2.blood < 50:
        break
    print(f'被攻击者的血量: {hero2.blood}')
