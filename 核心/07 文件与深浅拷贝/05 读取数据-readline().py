# encoding:utf-8
f = open('text.txt', mode='r')

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

'''
创建一个死循环
'''
while True:
    contend = f.readline()
    if contend == '':  # 内容为空代表该文件中没有字符串数据要读取了
        break
    else:
        print(contend)

f.close()

# readline 调用一次此方法就只读取一行数据
# 比较适合大文件的读取
# 可以用死循环, 一次读取每一行数据, 直到读取完成
