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
import threading
import time


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(128)
        # 一个服务器可以同时给多个客户端提供服务
        while True:  # 能源源不断接收不同客户端的链接
            client_socket, client_address = self.socket.accept()
            handle_recv_thread = threading.Thread(target=self.handle_recv,
                                                  args=(client_socket,
                                                        client_address))
            handle_recv_thread.start()
            send_file_thread = threading.Thread(target=self.send_file, args=(
            client_socket, client_address))
            send_file_thread.start()
            # self.handle_recv(client_socket, client_address)
            # self.send_file(client_socket, client_address)

            # client_socket.close()
            # self.socket.close()

    def handle_recv(self, client_socket, client_address):
        while True:  # 源源不断接收客户端信息
            recv_data = client_socket.recv(1024)
            filename = recv_data.decode('gbk')
            print(f'接受的数据({client_address}):\t', filename)

    def send_file(self, client_socket, client_address):
        # 服务器可以循环给客户端发送数据
        # with open('img.png', mode='rb') as file:
        #     content = file.read()
        # client_socket.send(content)
        index = 1
        while True:  # 无限给客户端发送信息
            time.sleep(3)
            print(f'第{index}次 - ({client_address})')
            client_socket.send(f'第{index}次 - ({client_address})'.encode('gbk'))
            index += 1


if __name__ == '__main__':
    server = Server('127.0.0.1', 7788)
    server.start()

'''
设置多个客户端,服务器可以看出是异步的.
'''
