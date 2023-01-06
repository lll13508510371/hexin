"""
1. 将 `y = kx + b ` 封装成一个函数，其中 `k=5` , `b=6`  , 假设 `x=5`
2. 在函数下方调用线性方程函数，打印结果
"""


def f(k, x, b):
    y = k * x + b
    return y


# 根据位置传递参数, 叫做位置参数
print(f(1, 2, 3))
print(f(4, 5, 6))
print(f(7, 8, 9))

# 加入位置参数传错了, 得到的结果就会不一样
print(f(7, 9, 8))

# 根据指定的参数名字传递的参数, 叫做关键字参数
# 关键字参数一旦指定, 那么位置对结果没有影响
print(f(1, x=2, b=3))
print(f(1, b=3, x=2))  # 如果位置参数和关键字参数一起使用, 那么位置参数必须放前面
'''
# !print(f( b=3, 1,x=2, )) positional argument follows keyword argument
位置参数在关键词参数之后
'''
print(f(x=2, b=3, k=1))
