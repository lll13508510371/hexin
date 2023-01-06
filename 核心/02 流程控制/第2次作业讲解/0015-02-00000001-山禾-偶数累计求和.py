"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果

开发步骤

1. 编写循环确认要计算的数字
2. 添加结果变量，在循环内部处理计算结果
"""
"""自己在下方编写代码实现功能"""

# sum_number = 0
# for i in range(1, 100):
#     if i % 2 == 0:  # 如果i没有余数, i 取余 2
#         # print(i)
#         sum_number += i  # 把每一个偶数进行赋值运算
#
# print(sum_number)
sum_number = 0
for i in range(0, 100, 2):
    print(i)
    sum_number += i
print(sum_number)