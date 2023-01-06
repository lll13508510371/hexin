dict1 = {
    'name': '丸子',
    'age': 18,
    'gender': '女'
}

"""新增键值对"""
# 如果指定一个字典中不存在的键进行赋值操作, 就会新增这个键值对
dict1['hobby'] = '吃喝玩乐'
print(dict1)

# 如果键存在, 赋值的话就会修改这个键的值
dict1['gender'] = '男'
print(dict1)

"""字典合并"""
dict2 = {'name': '丸子', 'age': 18, 'gender': '男', 'hobby': '吃喝玩乐'}
dict3 = {'学校': '青灯教育', 'hobby': ['吃', '喝', '玩', '乐']}
dict4 = {'name': '丸', 'age': 1, 'gender': '男', 'hobby': '喝玩乐'}

# 合并特性: 1.如果原字典中没有的键, 那么就会新增; 有的键就数据覆盖
dict2.update(dict3)  # 将dict3的键值对合并到dict2中
# dict2.update(dict4)

print(dict2)
