a = [1, 2, 3]
b = [4, 5, 6]
c = [6, 7, 8, 9]

result = zip(a, b)
print(result)
print(list(result))  # 数据一一组合后会返回一个列表嵌套元组的对象

result2 = zip(b, c)  # 序列中数据长度不一样的时候, 以最短的数据一一组包
print(result2)
print(list(result2))

result3 = zip(c, b)  # 序列中数据长度不一样的时候, 以最短的数据一一组包
print(result3)
print(list(result3))

result4 = zip(a, c, b)  # 序列中数据长度不一样的时候, 以最短的数据一一组包
print(result4)
print(list(result4))


