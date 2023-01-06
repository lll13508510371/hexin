# -*- coding: utf-8 -*-
"""
### 作业1：

运行网络调试工具代码，使用 Python 给网络调试工具发送文字信息，并接受网络调试工具发送过来的数据

+ 打开网络调试工具，选择 `tcp` 服务器并启动
+ 编写 Python 代码给 `tcp` 服务器发送一条信息（hello world ！）
+ 之后等待服务器发送一条信息回来并接受打印，然后断开连接
"""
import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客户端没有用多线程
tcp_client_socket.connect(('127.0.0.1', 7788))
index = 0
while True:
    index += 1
    tcp_client_socket.send(f'第{index}次发送数据'.encode('gbk'))
    recv_data = tcp_client_socket.recv(1024)
    recv_data = recv_data.decode('gbk')
    if recv_data == '拜拜':
        break
    print('接受的数据:\t', recv_data)

tcp_client_socket.close()
