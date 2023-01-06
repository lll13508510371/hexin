"""
编写一个函数，计算传入的数值序列的最大值、最小值和平均值，并一起返回，然后调用该函数
"""


# 数学式编程
def count_array(array):
    """最小值"""
    min_num = array[0]
    for i in array:
        if i < min_num:
            min_num = i

    """最大值"""
    max_num = array[0]
    for j in array:
        if j > max_num:
            max_num = j

    """平均值"""
    total = 0
    for k in array:
        total += k

    average_num = total / len(array)

    return min_num, max_num, average_num  # 如果返回多个值, 那么会将多个值放入元组进行返回


result = count_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)

"""内置方法调用解决"""


def count_array_2(array):
    min_num = min(array)
    max_num = max(array)
    average_num = sum(array) / len(array)

    return min_num, max_num, average_num


result = count_array_2([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
