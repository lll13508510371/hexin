'''# a = 10 类与继承
# b = 20
#
# a, b = b, a
# print(a)
# print(b)'''

'''def Bubble_Sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr'''

'''
每一次i代表一个数
j循环来把i代表的那个数比较大小
'''

'''print(Bubble_Sort([3, 44, 36, 22, 123, 3334, 2222, 1341324, 222]))'''

"""def sum_number(num):
    # 如果num为1,直接返回1 --->递归函数出口
    if num == 1:
        return 1

    print(num)
    # 如果 num 不是1,重复执行累加并返回累加结果
    return num + sum_number(num - 1)
    # num + num -1 + sum_number(num -2)


print(sum_number(6))"""

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     # '''
#     # 递归出口
#     # '''
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# '''
# 人从前面往后推导
# 计算机从结果往前进行逆向推导
# '''
#
# print(fib(50))

# def return_num():
#     return 100
#
#
# var1 = lambda: 100
# print(var1)  # 函数对象
# print(var1())  # 函数执行需要函数对象名+()

fn1 = lambda x: x
print(fn1(1))

fn1 = lambda x, a, b = 100: x + a + b
print(fn1(1,2))

fn1 = lambda *args:args
print(fn1(1,234,555,2222))