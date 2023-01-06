# f = open('text.txt', mode='r')  # ---> 读取完指针在文件末尾
# contend = f.read()  # 读取文件数据
# print(contend)
# f.close()

# with 打开一个文件对象, 用 as 将这个文件对象取了一个名字(自定义)
# with 表示上下文管理器, 当文件对象引用完毕的时候, 会帮助我们自动关闭
# with 有缩进, 有代码块
with open('text.txt', mode='r') as f:
    print(f.read())

with open('../../../核心/07 文件与深浅拷贝/01 上课代码/text2.txt', mode='w',
          encoding='utf-8') as f2:
    f2.write('111\n')
    f2.write('2212\n')
    f2.write('333')
