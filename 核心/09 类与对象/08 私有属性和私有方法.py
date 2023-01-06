class Women:
    def __init__(self, name, high, age):
        self.name = name
        self.high = high

        # 属性的名字前面加两个下划线 __  就代表这个属性是私有属性. 私有属性在类的外部无法访问
        # 例如女性年龄是不能随便公开的 hh
        self.__age = age

    # 方法的名字前面加两个下划线 __  就代表这个方法是私有方法, 私有方法在类的外部无法访问
    def __print_age(self):
        # 私有属性在类的内部中可以调用
        return self.__age

    def get_(self):
        # # 私有方法在类的内部中可以调用
        return self.__print_age()


wanzi = Women('丸子', 165, 18)
print(wanzi.name)
print(wanzi.high)
# print(wanzi.age)

# print(wanzi.print_age())
print(wanzi.get_())
