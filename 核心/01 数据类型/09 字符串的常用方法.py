'''
!!!!对象就具有对象的方法和属性
'''

# \n 换行符, 空白字符
s = '\n # hello world ! # \n'
print(s)
print(type(s))

"""strip 去除字符串两端的空白字符"""
print('-------------strip 去除字符串两端的空格-------------')
print(s.strip())
print(type(s.strip()))

# 支持链式调用(只要你的结果是字符串)
print(s.strip().strip('#').strip())  # strip只针对字符串前后两端

""" replace 替换"""
print('-------------replace 替换-------------')
# replace('字符串中需要替换的字符', '替换成什么内容')
print(s.replace('#', '?'))
print(type(s.replace('#', '?')))

print(s.replace('#', '?').strip())

"""split 分割"""
print('-------------split 分割-------------')
# split 默认以空白字符进行分割, 返回一个列表
print(s.split())
# 可以指定字符进行分割
print(s.split('#'))
# print(type(s.split('#')).replace())

"""join 合并字符串"""
print('-------------join把列表中的字符串 合并 成一个新的字符串-------------')
s = '张三，李四，王五'
# python区分大小写, 以及中英文符号
print(s.split('，'))
print(s.split(','))  # 因为用英文逗号，所以没有合并成功


# 用 ? 号作为分割符把列表里面的元素合并成一个新的字符串
# join是列表方法
print('?'.join(s.split('，')))
print('?'.join(s.split(',')))  # 因为用的英文逗号，所以没有合并成功
print(' '.join(s.split('，')))
print(''.join(s.split('，')))
print('-'.join(s.split('，')))
