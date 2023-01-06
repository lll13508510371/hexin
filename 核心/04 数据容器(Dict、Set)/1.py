dict1 = {}
print(dict1)
print(type(dict1))

dict1 = {
    'name': '正心',
    2: 3,
    'name1': None
}

print(dict1['name'])
print(dict1[2])
print(dict1)
# 关键字
# del dict1[2]
del (dict1[2])
print(dict1)

hh = dict1.get('name1')
print(hh)
print(dict1.keys())
print(type(dict1.keys()))
print(list(dict1.keys()))
print(dict1.values())
print(type(dict1.values()))
print(list(dict1.values()))
print(dict1.items())
print(type(dict1.items()))
print(list(dict1.items()))

se = set('2')
print(se)
se.add(4)
print(se)