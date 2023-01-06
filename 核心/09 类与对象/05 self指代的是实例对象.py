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

    def attack(self):  # --> 攻击方法
        return f'{self.name} 发动了攻击'

    # self指代的就是后续咱们实例化的一个一个的对象
    # 在实例方法中, 默认都会用self作为第一个参数
    # 在类中函数的第一个参数是 self , 就是实例方法, 默认会绑定到一个一个的对象上
    # self 的参数名字可以改, 但是不推荐你改, 约定俗成
    # self的作用:
    #   1.可以在类的内部中调用实例属性
    #   2.可以在类的内部中调用方法 --> 仅限于在class类中
    def get_info(self):
        result = self.attack()
        return result
    # def get_info(self):
    #     return self

hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
attr = hero1.get_info()
print(attr)
print(id(attr))
print(id(hero1))


hero2 = Hero('刘备', '弓箭', ['头盔', '靴子'], 100)
attr2 = hero2.get_info()
print(attr2)
print(id(attr2))
print(id(hero2))
'''
id() 函数返回对象的唯一标识符，标识符是一个整数。
     返回对象的内存地址
'''