"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果

开发步骤

1. 编写循环确认要计算的数字
2. 添加结果变量，在循环内部处理计算结果
"""
"""自己在下方编写代码实现功能"""

# 0 + 2 + 4 + 6 + ... + 100
# 0 - 100之间不包括0， 100
result = 0
i = 0

while i < 100:
    if i % 2 == 0:
        result += i
        # print(result)
        # even_number += 2
        # print(even_number)
    i += 1
    # print(i)
print(result)
