"""
选做:
    请找出 100-999 之间的所有水仙花数
"""

for i in range(100, 1000):
    # print(i)

    g = i % 10
    # print(g)

    s = int(i / 10 % 10)
    # print(s)

    b = int(i // 100)
    # print(b)

    # print(g ** 3 + s ** 3 + b ** 3)
    # 一个 = 代表赋值
    # 两个 == 代表判断相等
    if i == g ** 3 + s ** 3 + b ** 3:
        print(f'{i} 是水仙花数')