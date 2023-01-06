"""创建字符串"""
s1 = 'hello world'
s2 = "hello world"
s3 = """hello world
hello world
hello world
"""
s4 = '''hello world
hello world
hello world
'''

"""
    三引号可以跨行吗字符串内容较多的情况下用三引号
    三引号主要是区分有没有用变量(s4)接受, 如果有那么是字符串类型, 如果没有那么是注释
"""

print(s3)
# <class 'str'>  str --> 字符串类型
print(type(s3))

# 字符串与字符串之间可以用 + 号进行拼接, 字符串不能与数字或其他数据类型直接相加
print('5' + '2' + '0')
print(type('5' + '2' + '0'))

# print('5' + '2' + 0)
print('5' + '2' + str(0))

print('我叫"山禾"')
# print("我叫"山禾"")
print("我叫'山禾'")
print("""我叫'山禾'""")
