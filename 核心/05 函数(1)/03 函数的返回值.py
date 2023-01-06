"""
1. 将 `y = kx + b ` 封装成一个函数，其中 `k=5` , `b=6`  , 假设 `x=5`
2. 在函数下方调用线性方程函数，打印结果
"""


def f(x):
    y = 5 * x + 6
    # return 指的是函数的返回值, 反追至一般是函数体运行的某个结果
    # 函数的return是根据代码的实际需求, 取返回结果的
    # 函数结果的唯一出口就是 return
    # 函数一旦遇到return就会立马返回结果, 停止运行
    return y
    # print('函数内部打印结果:', y)


print(f(5))

# 函数的返回值, 要根据需不需要结果来设置
f(5) + 100


def get_max(num1, num2):
    # max_num = None
    if num1 > num2:
        return num1
    else:
        return num2

    # return max_num


# print(get_max(88, 78))

print(print())

"""
总结: 
    如果在函数内部有return返回函数的某个结果, 那么证明当前函数有返回值, 后面在调用的时候返回函数执行的结果
    如果函数数内部没有有return返回函数的某个结果, 那么证明当前函数没有返回值, 后面在调用的时候返回None
"""

# 函数一旦被定义, 可以重复多次调用
print(f(6))
print(f(7))
print(f(8))
