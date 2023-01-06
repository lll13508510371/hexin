# encoding:utf-8
f = open('text.txt', mode='r')

print(f.readlines())

f.close()

# readlines 可以按照行的方式把整个文件中的内容一次性读取
# 并且返回一个列表, 区中每一行的数据就是列表中的元素
