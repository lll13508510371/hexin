# -*- coding: utf-8 -*-
"""
### 作业2:

将tcp文件下载案例中的代码，用面向对象思想进行封装。

1. 服务器（Server）类
    实例属性：
        + 端口、地址、socket

    实例方法：
        - start 启动服务器方法（创建socket、绑定端口、提供服务）
        - handle_recv 处理客户端请求
        - send_file（发送文件方法）

实现两个对象的通信
"""
import socket


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None

    # start 启动服务器方法（创建socket、绑定端口、提供服务）
    def start(self, family, type):
        self.socket = socket.socket(family, type)
        self.socket.bind((self.ip, self.port))
        print('服务器已经启动在' + self.ip, self.port)
        self.socket.listen(5)

    # handle_recv 处理客户端请求 但这一步好像就多余了
    def handle_recv(self):
        client_socket, client_address = self.socket.accept()
        client_request_data = client_socket.recv(1024).decode('gbk')

    # send_file（发送文件方法）
    def send_file(self):
        client_socket, client_address = self.socket.accept()
        client_request_data = client_socket.recv(1024).decode('gbk')

        with open(client_request_data, mode='rb') as f:
            data = f.read()

        client_socket.send(data)

        client_socket.close()
        self.socket.close()


server1 = Server('127.0.0.1', 7788)
server1.start(socket.AF_INET, socket.SOCK_STREAM)
server1.send_file()
