"""add()"""
s1 = {10, 20}
s1.add(100)
s1.add('你好')
print(s1)

"""update() 追加的数据是序列-->列表元组字符串"""
s1 = {10, 20}
s1.update([100, 200])
s1.update((100, 300))
s1.update('abc')
print(s1)


"""remove 删除"""
# 删除集合中的指定数据，如果数据不存在则报错。
s1 = {10, 20}
s1.remove(10)
# s1.remove(10 类与继承)
print(s1)

""" discard 删除"""
# 删除集合中的指定数据，如果数据不存在也不会报错。
s1 = {10, 20}
s1.discard(10)
s1.discard(10)
print(s1)

"""查找"""
s1 = {10, 20, 30, 40, 50}
print('abc' in s1)

for i in s1:
    if i == 30:
        print(i)

