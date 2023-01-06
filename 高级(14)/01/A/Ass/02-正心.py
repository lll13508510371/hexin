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
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = None

    # @property
    # def address(self):
    #     return self.host, self.port

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(128)
        client_socket, client_address = self.socket.accept()
        self.handle_recv(client_socket, client_address)
        self.send_file(client_socket, client_address)

        client_socket.close()
        self.socket.close()

    def handle_recv(self, client_socket, client_address):
        recv_data = client_socket.recv(1024)
        filename = recv_data.decode('gbk')
        print('服务器接受的数据', filename)

    def send_file(self, client_socket, client_address):
        # 发送文件
        # with open('hello.txt', mode='r', encoding='utf-8') as file:
        #     text = file.read()
        # client_socket.send(text.encode('gbk'))
        with open('img.png', mode='rb') as file:
            content = file.read()
        client_socket.send(content)


if __name__ == '__main__':
    server = Server('127.0.0.1', 7788)
    server.start()
