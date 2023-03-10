"""
1. 将 `y = kx + b ` 封装成一个函数，其中 `k=5` , `b=6`  , 假设 `x=5`
2. 在函数下方调用线性方程函数，打印结果
"""


# 在定义函数的时候, 设置了参数的默认值
def f(k, x=5, b=6):
    y = k * x + b
    return y


# 如果没有特殊指定默认参数的值, 那么就会使用定义参数的时候设置的默认值, x默认等于5,  b默认等于6
print(f(6))

# 如果用位置参数把所有的函数参数都传递了, 那么会修改默认参数的值
print(f(6, 10, 11))

# 如果只需要修改一个默认参数的值, 那么就按照位置参数在前, 关键字参数灾后进行修改
print(f(6, b=10))

# 如果按照位置指定不完全的参数, 那就是按照其位置一一对应的传参, 没有传递的就使用默认参数
print(f(6, 11))
