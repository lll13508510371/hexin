'''
定义一个猫的外形类
'''


class Cat_shape:
    def __init__(self, color, limbs, behavior):
        self.color = color
        self.limbs = limbs
        self.behavior = behavior

    def print_info(self):
        print(f'猫的颜色: {self.color}')
        print(f'猫的脚数量: {self.limbs}')
        print(f'猫的行为: {self.behavior}')

    def info(self):
        return self

# 如果__init__方法中没有参数,那么在实例化对象的时候就不能传参数
cat1 = Cat_shape('黄色', 5, ['喵喵叫'])
print(cat1)
cat1.print_info()

cat2 = Cat_shape('灰色', 4, ['喵喵叫', '呜呜叫'])
print(cat2)
cat2.print_info()

a = cat1.info()
print(a)
print(id(a))
print(id(cat1))