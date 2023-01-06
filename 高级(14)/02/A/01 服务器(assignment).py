"""
    修改 socket 的代码,使socket 服务器能够同时给多个客户端提供服务

        接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
        与客户端进行通信的时候
            + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
            + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）

"""
import socket
import threading
import time


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)

        # 可以接收到很多个用户的请求
        while True:  # # 能源源不断接收不同客户端的链接

            socket_client, socket_client_addr = self.socket.accept()
            '''
            不设置多线程,服务器同一时间就只能接收一个客户端发来的消息
            但服务器同一时间需要接收不同客户端发来的消息,所以要设置多线程
            '''
            # 接收到一个客户端就创建一个客户端端的接收线程
            recv_thread = threading.Thread(target=self.recv,
                                           args=(socket_client,
                                                 socket_client_addr))
            recv_thread.start()

            send_thread = threading.Thread(target=self.send,
                                           args=(socket_client,
                                                 socket_client_addr))
            send_thread.start()

    # 记录客户端发送的数据到 `{客户端地址}.txt` 文件中
    # 1.接收到客户端数据 --> 2.保存到文件当中 --> 属于服务器接收过程,用一个recv函数来来完成这两步
    def recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        print('客户端的地址', clt_addr)
        while True:  # 源源不断接受客户端信息
            recv_data = clt_socket.recv(1024)
            print(recv_data.decode('gbk'))
            # print(type(clt_addr))
            with open(str(clt_addr) + '.txt', mode='a', encoding='utf-8') as f:
                f.write(recv_data.decode('gbk'))

    def send(self, clt_socket, clt_addr):
        time.sleep(3)  # 让它晚一点运行,确保能够读取到recv函数当中的文件,不然会报错(没有当前文件)
        while True:
            with open(str(clt_addr) + '.txt', mode='r', encoding='utf-8') as f:
                # info_record = f.read()
                # info_record_list = info_record.split()
                # info_record_num = len(info_record_list)
                info_record = f.readlines()
                send_data = clt_socket.send(
                    f'你已经有{len(info_record)}条信息记录'.encode('gbk'))


if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
