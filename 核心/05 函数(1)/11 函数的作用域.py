num = 10  # 全局变量


def foo():
    global num  # 声明num是全局变量
    num = 20
    print('这是函数内部的num值:', num)
    return num


foo()

print(num)

"""
函数操作数据的作用域仅在函数内部
能不用 global 尽量不要用
"""
