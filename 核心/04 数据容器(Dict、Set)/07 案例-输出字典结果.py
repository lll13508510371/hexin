dict1 = {
    'name': '丸子',
    'age': 18,
    'gender': '女',
    '爱好': '吃喝玩乐'
}

keys_list = ['height', 'name', 'weight', '爱好']
# 需求: 取出 keys_list 列表在 dict1 有的键对应的值

for i in keys_list:
    result = dict1.get(i)
    if result:  # 如果result不为空 None 的布尔值是False
        print(result)
