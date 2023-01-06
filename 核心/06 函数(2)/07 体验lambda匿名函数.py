# 通过函数返回数字100
def return_num():
    return 100


result = return_num()
print(result)

# 匿名函数定义简单函数逻辑
# lambda 参数: 返回值
# !函数名()  --> 调用函数
fn1 = lambda: 100
print(fn1)
print(fn1())

"""
鸭子类型: 如果一只鸡吃东西像鸭子, 游泳像鸭子, 那么我们就可以认定它是一只鸭子
"""


def func1():
    print('函数1')


def func2():
    print('函数2')


def func3():
    print('函数3')


# list1 = [func1(), func2(), func3()]
# list1()

# 依次调用三个函数
# func1()
# func2()
# func3()

for i in [func1, func2, func3]:
    i()  # --> 依次调用 func1, func2, func3
