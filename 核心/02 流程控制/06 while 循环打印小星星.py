"""打印直角三角形
*
**
***
****
*****
"""

# i = 1
# while i < 6:
#     print('*' * i)
#     i += 1

# 不能使用字符串的乘法，循环打印直角三角形

# j = 1
# while j <= 3:
#     print('*', end='')
#     j += 1


# 循环嵌套
i = 1
while i < 6:  # i = 12345
    # print(f'外层循环: i值为{i}')

    j = 1
    while j <= i:
        # print(f'内层循环:{j}')
        print('*', end='')
        j += 1

    i += 1
    print()  # 在外层循环中加print实现换行

