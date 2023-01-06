arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 保存到本地文件

文件名为: hello.txt
文件内容: 1,2,3,4,5,6,7
"""

# print(','.join(arr))
print(str(arr))
print(','.join([str(i) for i in arr]))

with open('hello.txt', mode='w') as f:
    f.write(str(arr))  # open函数的文件操作只能写入字符串和二进制数数据


