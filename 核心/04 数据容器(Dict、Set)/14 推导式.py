"""列表推导式"""
lis1 = [i for i in range(10)]  # 将遍历到的i放入列表i当中
print(lis1)

lis1 = [i ** 2 for i in range(10)]
print(lis1)

"""字典推导式"""
dict1 = {i: i ** 2 for i in range(5)}
print(dict1)

list2 = ['name', 'age', 'gender']
list3 = ['Tom', 20, 'man']
result = {list2[i]: list3[i] for i in range(len(list2))}
print(result)

"""集合推导式"""
set1 = {i ** 5 for i in range(5)}
print(set1)

'''
有没有元组推导式?
元组不能增减,所以没有
上面其他的推导式都类似于先是空的,然后一次一次遍历之后添加上去的元素
所以元组没有
'''
result2 = (i for i in range(5))
print(result2)
print(type(result2))  # generator --> 可迭代对象
