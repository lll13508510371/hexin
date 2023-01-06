# 有序列的类型: 字符串  列表  元组
# 有序列的类型可以直接互相转化


str1 = 'abcdefg'

print(str1[5])
print(str1[1:5])

result = list(str1)
print(result)

result2 = tuple(result)
print(result2)

result3 = str(result2)
print(result3)

# 有序列的数据容器可以索引和切片取值, 可以互相之间转化
# list1 = ['sss','ss','s']
# print(type(list1))
# result11 = ','.join(list1)
# print(result11)