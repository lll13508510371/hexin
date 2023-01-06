# def f(x):
#     y = 5 * x + 3
#     print(y)
#
#
# print(f(5))
# # print(y)


# 列表操作的都是本身
list1 = [1, 2, 3, 4]


def func(number):
    # global list1
    number.append(16)
    print(number)


func(list1)
print(list1)
'''
# Python内存机制
# num1 = 1

# num2 = 1
# 垃圾回收机制

列表不一样,内部列表在函数以外一样可见
'''
# Python内存机制

# num1 = 1
# num2 = 1
# 垃圾回收机制
