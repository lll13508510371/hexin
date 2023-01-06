import pprint

dict1 = {
    'age': {'年龄': 18},
    'gender': '女',
    'name': '丸子',

}

"""根据建取对应的值"""
print(dict1['name'])
# print(dict1['myname'])  # 键不存在就会报错


"""get() 方法进行取值"""
print(dict1.get('age'))  # get(键)
print(dict1.get('myname'))  # 键如果用get()取值, 不存在的话不会报错, 但是会返回 None

"""keys() 取出字典中所有的键"""
print(list(dict1.keys()))

"""values() 取出字典中所有的值"""
print(list(dict1.values()))

"""items()"""
# 将字典中的所有的键值对全部取出来, 返回嵌套的数据容器 [ (键1, 值1), (键2, 值2), (键3, 值3), ....]

print(list(dict1.items()))

# 字典是一个无序的数据容器, 就不能用索引取值, 以及键值对排列没有顺序
# print(dict1[5])

students = [
    {'name': '正心', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '张三', 'chinese': 60, 'math': 59, 'english': 59, 'total': 177},
    {'name': '李四', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177},
    {'name': '王五', 'chinese': 59, 'math': 59, 'english': 59, 'total': 177}
]

pprint.pprint(students)
# print(students)

"""None 类型"""
# 属于空类型, 啥也不是
print(bool(None))
