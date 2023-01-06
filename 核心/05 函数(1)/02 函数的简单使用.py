"""# 利用函数求两个数的最大值"""


# 这两个数字可以是任意的数字

# 参数的作用: 在执行函数的时候, 会根据参数传递的不同的值, 得到不同的结果

def get_max(num1, num2):  # 在定义函数的时候设置的参数叫做形式参数
    # 如果在定义的时候设置了参数, 那么在调用的时候就需要传参
    '''
    利用函数求两个数的最大值
    :param num1: 传进来的第一个数字
    :param num2: 传进来的第二个数字
    :return: 返回两个数中的最大值
    '''

    max_num = None
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2

    return max_num


# 01
# print(get_max([print], [False]))  # 在调用函数的时候传递的参数叫做实际参数
number1 = int(input('请输入第一个数字:'))
number2 = int(input('请输入第二个数字:'))

print(get_max(number1, number2))
# print(get_max(1052031, 1056231))
