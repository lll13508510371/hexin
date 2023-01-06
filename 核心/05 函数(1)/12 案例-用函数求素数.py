# 用函数求素数

def get_result(number):
    """
    判断传入的数字是不是素数
    :param number: 传进来的数字
    :return: None
    """

    for j in range(2, number):  # 找某个数字从2开始到这个数字中间范围内的数字 9 --> 2345678
        if number % j == 0:  # 这个数字除了1和它本身外有因数
            print(number, '不是素数')
            break  # 循环的中断 break continue 结束的是离他最近的那一层循环

    else:
        print(number, '是素数')


get_result(13)
get_result(24)
