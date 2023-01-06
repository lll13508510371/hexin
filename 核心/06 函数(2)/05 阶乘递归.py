# 需求: 计算数字的累加结果, 累乘
# 3 --> 3 * 2 * 1 =
# 6 --> 6 * 5 * 4 * 3 * 2 * 1 =
# 5 --> 5 * 4 * 3 * 2 * 1 =

def sum_number(num):
    # 如果num为1, 直接返回1 ---> 递归函数的出口
    if num == 1:
        return 1

    return num * sum_number(num - 1)


print(sum_number(5))
print(sum_number(2))
print(sum_number(6))

# 递归的特点: 函数内部调用自己本身;  递归一般需要设置出口 --->避免超过函数递归的最大任务数
