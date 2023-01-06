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
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.address)
        send_data = input('请输入发送给服务器的内容')
        self.socket.send(send_data.encode('gbk'))
        reav_data = self.socket.recv(1024 * 1024)
        # with open('aaa.txt', mode='w', encoding='utf-8') as file:
        #     file.write(reav_data.decode('gbk'))
        with open('img2.png', mode='wb') as file:
            file.write(reav_data)


if __name__ == '__main__':
    client = Client('127.0.0.1', 7788)
    client.start()
