dict1 = {
    'name': '丸子',
    'age': 18,
    'gender': '女'
}

dict1['age'] = 28
print(dict1)

# 键一旦被定义, 无法进行修改
# dict1['gender'] = dict1['123']
# 如果想要重新设定键,可以先删除再设定
dict1['爱好'] = '吃喝玩乐'
print(dict1)
