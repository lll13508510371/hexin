""""""
#
"""
ip 地址

127.0.0.1       本地回环地址(只能本地访问)
192.168.0.53    本地局域网的地址(本地局域网才能进行访问)
81.68.68.240    ipv4 腾讯云服务器的地址(只要能够访问互联网都可以访问)
0.0.0.0         开放地址,只要能够访问到本机,就能访问到这个服务
"""

"""
单位
1024
1   bit   0 与 1
1   byte  8 bit         0000 0000 - 1111 1111 (255)
1   kb    1024 byte     
1   mb    1024 kb       
1   gb    1024 mb
....

gbk   utf-8
在 utf-8 编码里面,一个汉字是 4 byte

一本小说 10 mb, 大概有多少个字?
"""

"""
编码解码
二进制:    0000 0000 - 1111 1111
十六进制:  00        -  ff  (0-9-a-f)
"""
message = '你吃晚饭了没?'  # 字符串对象
print(message.encode('utf-8'))  # \x 表示16进制  十六进制就是二进制
print(message.encode('gbk'))
print(message.encode('utf-8').decode('utf-8'))  # \x 表示16进制  十六进制就是二进制
print(message.encode('gbk').decode('gbk'))
# print(message.encode('gbk').decode('utf-8'))
