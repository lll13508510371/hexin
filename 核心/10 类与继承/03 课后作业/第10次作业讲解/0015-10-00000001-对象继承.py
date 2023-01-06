"""
作业1
在Hero的基础上，新增了法师英雄，多了下面内容

法师（Mage）
    增加属性：魔法值（magical 默认0，最大100）

    - 攻击：
        调用一次 怒气 `+2`
        调用一次 魔法值 `+5`

    - 放大招
      魔法值满时自动放大招

    - 第二形态
      当怒气值满时 自动切换第二形态（魔法值最大值修改为50）
"""

class Hero:
    def __init__(self, name, weapon, equipment, power, blood, anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger

    def attack(self):
        print(f'{self.name} 发动了攻击!')
        self.anger += 2

        if self.anger == 100:  # 怒气值满
            self.big_data()

    def big_data(self):
        print(f'{self.name} 释放了大招!')
        self.anger = 0


class Mage(Hero):
    def __init__(self, name, weapon, equipment, power, blood, anger, magical):
        super().__init__(name, weapon, equipment, power, blood, anger)
        self.magical = magical
        # 魔法值最大值
        self.max_magical = 100

    # 重写法师的攻击方法逻辑
    def attack(self):
        print(f'{self.name} 发动了攻击!')
        self.anger += 2
        self.magical += 5

        if self.magical == self.max_magical:  # 魔法值满了
            self.big_data()
            self.magical = 0  # 释放大招后, 魔法值归0

        if self.anger == 100:
            self.second()

    # 魔法值满了, 自动放大招
    def big_data(self):
        print(f'{self.name} 释放了大招!')

    def second(self):
        print(f'{self.name} 切换了第二形态!')
        self.max_magical = 50

hero1 = Mage('貂蝉', '扇子', ['衣服','鞋子'], 100, 100, 94, 90)
hero1.attack()
print(hero1.anger)
print(hero1.magical)
hero1.attack()
print(hero1.anger)
print(hero1.magical)
hero1.attack()
print(hero1.anger)
print(hero1.magical)