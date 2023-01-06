"""
需求：
    警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作
"""


class Dog:
    def work(self):
        pass


class ArmyDog(Dog):
    def work(self):
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('追查毒品...')


class Person:
    def work_with_dog(self, dog):  # 传入一个狗的对象
        dog.work()


ad = ArmyDog()  # 追击犬
bb = DrugDog()  # 缉毒犬

# 根据传入对象的不同, 执行不同的结果
wanzi = Person()
wanzi.work_with_dog(ad)
wanzi.work_with_dog(bb)
