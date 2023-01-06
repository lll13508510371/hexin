array = [1, 2, 3, 4, 5]

result = array  # 将列表数据赋值给result

# 对象的引用(对象赋值), 实际上是同一个对象
print(id(array))
print(id(result))

array[0] = 'a'
print(array)
print(result)
