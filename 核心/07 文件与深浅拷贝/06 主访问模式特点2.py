""" + 增加文件的权限: 可读可写 """
f = open('text.txt', mode='r+')  # ---> 读取完指针在文件开头
f.write('ddd')  # 报错
contend = f.read()  # 读取文件数据
print(contend)
f.close()

"""不推荐用 + 增加文件权限"""
