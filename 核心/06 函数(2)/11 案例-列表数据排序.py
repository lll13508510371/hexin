import pprint
'''
这道题是重点
'''
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]


def func(x):
    print(x)
    return x['age']  # 根据函数返回值结果进行排序


# !!! key 指定比较的依据, 指定的函数名, 会默认被调用
students.sort(key=func)

# students.sort(key=lambda x:x['age'])
# pprint.pprint(students)
# print('------------------------')
# students.sort(key=lambda x:x['age'], reverse=True)
# pprint.pprint(students)
