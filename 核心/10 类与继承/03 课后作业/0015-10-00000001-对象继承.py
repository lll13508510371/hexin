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
    def __init__(self, name, weapon, equipment, power, blood, anger):
        super().__init__(name, weapon, equipment, power, blood, anger)
        self.magical = 0

    def second_form(self):
        print(f'{self.name} 变身第二形态')
        if self.magical >= 50:
            self.big_data()
        self.anger = 0
        print(f'{self.name}恢复原形')

    def big_data(self):
        print(f'{self.name} 释放了大招!')
        self.magical = 0

    def attack(self):  # !!!!主函数
        print(f'{self.name} 发动了攻击!')
        self.magical += 5
        self.anger += 2

        if self.magical == 100:
            self.big_data()

        elif self.anger == 100:
            self.second_form()


mage1 = Mage('牛逼魔法师', '魔法棒', '扫帚', 0, 100, 78)
for i in range(100):
    mage1.attack()
    print(mage1.magical)
    print(mage1.anger)

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 思路 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
变身第二形态是为了干什么 --> 让最大法力变成50:法力50就可以放大 --> 在second_form()当中判断当变身的时候法力如果
大于50就放大. 当然, 没有50就放不了大,之后怒气恢复0.因为题目中是怒气满100自动第二形态,所以能不能放大也要看运气, 可能
第二形态的时候魔力没有满50.
'''
