# -*- coding: utf-8 -*-

f = open('text.txt', mode='r')

# 默认一次性读取所有文件数据
print(f.read())
# f.write('''
# 路
# 景
# 涵
# ''')

# 如果read()里面传参数, name就是按照字节读取
# print(f.read())

f.close()
'''
如果!!!没有设置编码方式,会以Windows默认的gbk编码,这个时候如果要读取中文只能先写入再读取
因为写入中文是以gbk形式编码.如上面
如果是没有写入直接读取会显示不可decode(破译)gbk编码.
'''
