"""
用for语句实现九九乘法表
"""

for i in range(1, 10):  # 123456789 外层循环, 行数
    for j in range(1, i + 1):  # range 范围区间是左闭右开, 循环的列数
        print(f'{j} x {i} = {j * i}', end='\t')
    print()


