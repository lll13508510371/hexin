# + - * /

"""算术运算符"""
three = 3
ten = 10

# 10 类与继承 取整除 3, 结果为3
print(ten // three)

# 10 类与继承 取余除 3, 结果为1
print(ten % three)

# 10 类与继承 的 3 次幂 = 10 类与继承 x 10 类与继承 x 10 类与继承
print(ten ** three)

"""赋值运算符"""
print('-------------------------------')
# ten = ten + three
# print(ten)
ten += three  # # 两个变量相加, 通过赋值运算把结果赋给左边的变量
print(ten)

ten -= three
print(ten)
