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

server_address = ('127.0.0.1', 7788)

tcp_client_socket.connect(server_address)

send_info = input('请输入发给服务器的信息: ')

tcp_client_socket.send(send_info.encode('gbk'))

receive_sever_info = tcp_client_socket.recv(1024)  # 1 kb

print(receive_sever_info.decode('gbk'))

tcp_client_socket.close()
