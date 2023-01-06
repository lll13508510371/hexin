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
    # 类的名字下面定义的属性叫做类属性

    hand = 2  # 每个英雄有两只手
    head = 1  # 每个英雄有一个头
    class_name = '人类'

    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self, obj, att):
        obj.blood -= att

        return f'{self.name} 发动了攻击, 攻击了 {obj.name}'

    # 定义一个类方法
    @classmethod  # 标记此方法是类方法
    def boast(cls):  # cls代表当前类的类属性 --> 应该是代表当前类
        # 类方法可以调用类属性
        return cls.class_name + '会吹牛'

    @staticmethod  # 标记此方法是静态方法
    def info_():  # 静态方法没有参数
        return '人类生活在地球'


hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '弓箭', ['头盔', '靴子'], 100)

"""调用类属性的方式"""
# # 通过实例化对象调用类属性
print(f'{hero1.name} 的手有: {hero1.hand} 只')
print(f'{hero1.name} 的头有: {hero1.head} 个')
# 通过类对象调用类属性, 类对象值得就是类名
print(Hero.head)
print(Hero.hand)

"""修改类属性"""
# 仅针对一个对象做修改, 不会影响其他对象
hero1.hand = 6  # 修改手的类属性为6
print(f'{hero1.name} 的手有: {hero1.hand} 只')
print(f'{hero2.name} 的手有: {hero2.hand} 只')

# 如果针对类对象修改类属性, 那么所有对象都会被修改
Hero.head = 3  # 修改头的类属性为3
print(f'{hero1.name} 的头有: {hero1.head} 个')
print(f'{hero2.name} 的头有: {hero2.head} 个')

"""调用类方法"""
print(hero1.boast())  # # 通过实例对象调用类方法
print(Hero.boast())  # # 通过类对象调用类方法

"""调用静态方法"""
print(hero1.info_())  # # 通过实例对象调用静态方法
print(Hero.info_())  # # 通过类对象调用静态方法
