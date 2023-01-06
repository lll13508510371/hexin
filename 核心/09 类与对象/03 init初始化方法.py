"""
定义一个猫的外形类
"""
# class Shape:
#     def __init__(self):
#         # 初始化函数没有设置参数
#         # 在下方定的形式, 相当于把实例属性写死了
#         self.color = '灰色'  # 颜色属性
#         self.limbs = 4  # 脚数量的属性
#         self.behavior = ['喵喵叫']  # 行为的属性
#
#     def print_info(self):
#         print(f'猫的颜色是: {self.color}')
#         print(f'猫的爪子数量是: {self.limbs}')
#         print(f'猫的行为是: {self.behavior}')
#
# # 如果 __init__ 方法中没有参数, 那么在实例化对象的时候就不能传参数
# cat1 = Shape()
# cat1.print_info()
#
# cat2 = Shape()
# cat2.print_info()

class Shape:
    # --> __init__ 方法中涉不设置参数决定了对象的属性是死还是活
    def __init__(self, color, limbs, behavior):
        self.color = color  # 颜色属性
        self.limbs = limbs  # 脚数量的属性
        self.behavior = behavior  # 行为的属性

    def print_info(self):
        print(f'猫的颜色是: {self.color}')
        print(f'猫的爪子数量是: {self.limbs}')
        print(f'猫的行为是: {self.behavior}')

cat1 = Shape('黄色', 4, ['喵喵叫'])
cat1.print_info()

cat2 = Shape('白色', 3, ['喵喵叫', '呜呜叫'])
cat2.print_info()