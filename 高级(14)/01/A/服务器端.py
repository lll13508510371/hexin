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
        self.address = (host, port)
        self.socket = None

    # start 启动服务器方法（创建socket、绑定端口、提供服务）
    def start(self, family, type_):
        self.socket = socket.socket(family, type_)
        self.socket.bind(self.address)
        print('服务器已经启动在' + self.host, self.port)
        # 设置最大客户端链接为5
        self.socket.listen(5)
        # 客户端链接成功之后会得到这两个对象
        # 等待客户端的链接 --> 返回该客户端的 socket和 address
        client_socket, client_address = self.socket.accept()
        # 通过一个主函数来调用其它函数,实例对象就不再显示调用其它函数了
        self.handle_recv(client_socket)

        '''
        self.send_file(client_socket, client_socket.recv(1024 * 1024))
        这里不能这么直接调用send_file,不知道什么原因,要把它放到下面的handle_recv函数
        当中进行调用
        --> 两个client_socket.recv(1024 * 1024) 不是同一个对象 id 都不相同,
            所以这里得把send_file()放入handle_recv()调用才能够用到handle_recv()
            当中用到的那个client_socket.recv(1024*1024)
        '''

    # handle_recv 处理客户端请求 但这一步好像就多余了

    def handle_recv(self, client_socket):
        client_request_data = client_socket.recv(1024 * 1024)
        self.send_file(client_socket, client_request_data)

    # send_file（发送文件方法）
    def send_file(self, client_socket, client_request_data):
        print('服务器接收的数据', client_request_data.decode('gbk'))

        with open(client_request_data.decode('gbk'), mode='rb') as f:
            data = f.read()

        client_socket.send(data)

        client_socket.close()
        self.socket.close()


server1 = Server('127.0.0.1', 7788)
server1.start(socket.AF_INET, socket.SOCK_STREAM)
