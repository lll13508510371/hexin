# -*- coding: utf-8 -*-
"""
### 作业3:

2. 客户端（Client）类

    实例属性：
        + 服务器端口、服务器地址、socket

    实例方法：
        + start 启动服务器方法（创建socket、链接服务器）
        + recv_file（发送请求、接收文件方法）
"""
import socket


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = None

    # start 启动服务器方法（创建socket、链接服务器）
    def start(self, family, type):
        self.socket = socket.socket(family, type)
        address = (self.server_ip, self.server_port)
        self.socket.connect(address)
        self.receive_file()
    # receive_file（发送请求、接收文件方法）
    def receive_file(self):
        data_list = []
        request = input('请输入向服务发送的请求: ')

        self.socket.send(request.encode('gbk'))
        while True:
            recv_data = self.socket.recv(1024)
            if recv_data:
                data_list.append(recv_data)
            else:
                break

        with open('[下载]' + request, mode='wb') as f:
            f.write(b''.join(data_list))

        self.socket.close()



client1 = Client('127.0.0.1', 7788)
client1.start(socket.AF_INET, socket.SOCK_STREAM)

