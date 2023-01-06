
class Legends:
    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self):
        return f'{self.name}发起了攻击'

    def get_info(self):
        return self


legends1 = Legends('黄忠', '弓箭', ['头盔', '靴子'], 100)
print(legends1.name)
print(legends1.attack())
legends2 = Legends('刘备', '剑', ['头盔', '盔甲'], 100)
print(legends2.name)
print(legends2.attack())
arr = legends1.get_info()
print(id(legends2))
print(id(legends1))
print(id(arr))

# self 未实例化的对象
