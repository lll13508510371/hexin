"""打印5遍 我喜欢 python"""
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')
# print('我喜欢 python')


# 写循环的第一件事情就是设置成立条件,防止进入死循环
"""
while 成立条件(最终返回一个布尔类型):
    循环里面重复执行的代码
"""
# while True:
#     print('我喜欢 python')

i = 0
while i < 5:
    print('我喜欢 python')
    i += 1   # 赋值运算符
    print(i)

