# \n  换行符

print('hello \nworld')
print('hello \n world')
# \ 是转义字符, 作用的将后面的特殊字符转义成普通的字符串
print('hello \\n world')

"""
    转义字符是一些特殊的字符串, 有特殊功能
    常见的特殊字符
    /(斜杠) \(反斜杠) ? [ ] ( ) { }

    \t      制表符
    \n      换行符
"""

# 特殊的字符如果想作为字符串处理, 用反斜杠(\)进行转义

# r 在字符串前面加上, 表示原生字符串
print(r'hello \n world')
