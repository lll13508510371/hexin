# for i in 'dfaniofnweo':
#     print(i)

# for i in range(10 类与继承):
#     print(i)

"""
- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""
"""range"""
print(list(range(0, 8)))  # 指定起始值和数据值, 范围是一个左闭右开的区间
print(list(range(8)))  # 起始值默认是从0开始, 可以省略
print(list(range(0, 8, 1)))  # 第三个参数是步长, 默认为1,
print(list(range(0, 8)))  # 第三个参数是步长, 默认为1, 可以省略

print(list(range(0, 8, 2)))
print(list(range(-1, -8, -1)))  # 逆序取值, 范围和步长(负数步长)都要倒着取
print(list(range(-1, -8, 1)))
print(list(range(-8, -1, 1)))