"""
创建一个游戏英雄类，

分别有以下属性
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）, 对被攻击人造成对等的攻击力伤害

创建两个英雄
    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""
class Hero:
    def __init__(self, name, weapon, equipment, blood):
        # 将后续传进来的参数绑定到实例属性上
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    # 将你要攻击的对象传进来, 然后print输出你攻击了谁
    # 传入攻击力, 根据攻击力减少被攻击者的血量
    def attack(self, obj, att):  # 此参数必须得传一个英雄对象进来
        obj.blood -= att

        return f'{self.name} 发动了攻击, 攻击了 {obj.name}'


hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '弓箭', ['头盔', '靴子'], 100)

# hero1 攻击 hero2
print('被攻击之前的血量: ', hero2.blood)
print(hero1.attack(hero2, 3))
print('被攻击之后的血量: ', hero2.blood)
print('-0---------------------------------')
# hero2 攻击 hero1
print('被攻击之前的血量: ', hero1.blood)
print(hero2.attack(hero1, 3))
print('被攻击之后的血量: ', hero1.blood)
