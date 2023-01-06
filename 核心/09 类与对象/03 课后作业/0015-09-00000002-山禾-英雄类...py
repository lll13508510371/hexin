"""
### 作业1

1、创建一个游戏英雄类,
+ 分别有以下属性
  名字（name）,武器（weapon）,装备（equipment）, 攻击力（power）,血量（blood）,怒气（anger）
+ 每个英雄类都有游戏技能,分别为（行为）
  攻击（attack）,放大招（nirvana）

用游戏英雄类创建三个游戏人物,分别是（属性）：
    - '韩信','弓箭', ['头盔', '靴子'], 15, 100, 0
    - '刘备', '剑', ['头盔', '盔甲'], 20, 100, 0
    - '李白','长枪',['盔甲', '马'], 30, 100, 0

每个人都有游戏技能,分别为（行为）：
- 攻击
  调用一次 怒气 `+2` （修改anger值）
- 放大招
  怒气值满时自动放大招
"""

"""自己在下方编写代码实现功能"""


class Legends:
    def __init__(self, name, weapon, equipment, power, blood, anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger

    def attack(self, other_legends, other_legends_blood):
        while True:
            print(f'{self.name}用{self.weapon}攻击了{other_legends.name}')
            other_legends_blood -= self.power
            print(f'{other_legends.name}还剩{other_legends_blood}血量')
            self.anger += 2
            print(f'{self.name}当前怒气值为{self.anger}')
            if self.anger == 6:
                self.nirvana(other_legends, other_legends_blood)
                other_legends_blood -= self.power * 2
                print(f'{other_legends.name}还剩{other_legends_blood}血量')
            if other_legends_blood <= 0:
                print(f'{other_legends.name}被{self.name}杀死了')
                # 我设置攻击Legend3的时候怒气值没有归零,拿攻击Legend2最后的怒气值开始计算的
                self.anger = 0
                break

    def nirvana(self, other_legends, other_legends_blood):
        print(f'{self.name}放了大招')
        self.anger = 0


Legend1 = Legends('韩信', '弓箭', ['头盔', '靴子'], 15, 100, 0)
Legend2 = Legends('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)
Legend3 = Legends('李白', '长枪', ['盔甲', '马'], 30, 100, 0)

Legend1.attack(Legend2, Legend2.blood)
print('--------------------------------------')
Legend1.attack(Legend3, Legend3.blood)
print('--------------------------------------')
Legend2.attack(Legend1, Legend1.blood)
print('--------------------------------------')
Legend2.attack(Legend3, Legend3.blood)
print('--------------------------------------')
Legend3.attack(Legend1, Legend1.blood)
print('--------------------------------------')
Legend3.attack(Legend2, Legend2.blood)
'''
!!! 有些时候写if不能写的太绝对了,拿上面的例子来说,我刚开始想的是血量为0就死了,if设置了other_legends_blood == 0,
但韩信攻击力为15,攻击三次刘备还剩55,发动大招刘备还剩25, 再攻击两次刘备会死, 血量为-5, 得不到0, while循环就不会break
所以知道这个情况设置 other_legends_blood <= 0就可以解决了
'''
