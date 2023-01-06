arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 保存到本地文件

文件名为: hello.txt
文件内容: 1,2,3,4,5,6,7
"""

# with open('hello.txt', mode='w') as f:
#     for i in arr:
#         if i == str(arr[-1]):
#             f.write(i)
#             break
#         f.write(str(i)+',')
'''
!!!负索引的应用
'''
str_list = [str(i) for i in arr]
print(str_list)
print(','.join(str_list))
str1 = ','.join(str_list)
with open('hello.txt', mode='w') as f:
    f.write(str1)
