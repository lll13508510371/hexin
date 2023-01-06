"""
open(file, mode='r',  encoding=None,  )
    file: 文件的路径
    mode: 文件的操作模式
        w   --> write 以只写的模式打开文件
        a   --> append 往文件的末尾追加数据
        r   --> read 以只读的方式打开文件
        b   --> binary 二进制写入模式  wb  rb  ab
    encoding: 文件数据编码
        windows 系统下默认的编码是 gbk
        mac  linux 编码是 utf-8

"""

# text.txt  --> 指代文件路径
#   相对路径: 相对于当前编辑的py文件来说
#   绝对路径: 从盘符的根目录开始找的位置
#   根据系统的不同, 文件路径的分隔符号是不同的
"""1. 打开文件"""
file = open(file='text.txt', mode='w')
print(file)

"""2. 操作文件"""
# 写入( write ) 和 读取( read )文件
# 文件的相关操作, 需要根据打开时的文件模式来操作
# 文件只能写入两种类型的数据: 字符串  二进制数据, 除此以外任何Python对象都不能写入
'''
像Linux Mac os 系统文件都是/分开,不存在类似\t这样的情况 但Windows是以\分开文件

但IDE 类似Pycharm 专业版直接用/这样的形式帮你把文件夹形式直接改变了,在IDE 类似Pycharm上 指定文件可以用/ ,07后面的.py文件中有实践

因为可能会遇到类似\t这样的情况
不建议用r转义字符 例如r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' 特殊情况下路径指定会有错误
应该用-->C:\\Program Files (x86)\\Google\\hrome\\Application\\chrome.exe这样的形式  
'''
file.write('aaa\n')
file.write('bbb\n')
file.write('ccc\n')
# file.write(['grenuiabg'])

"""3. 关闭文件"""
# 文件操作完以后, 一定要记得关闭文件, 垃圾回收机制
file.close()
