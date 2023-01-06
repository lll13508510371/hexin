"""
修改 socket 的代码,使 socket 服务器能够同时给多个客户端提供服务

    接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
    与客户端进行通信的时候
        + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
        + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）

"""
import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)

        # 可以接收到很多个用户的请求
        socket_client, socket_client_addr = self.socket.accept()
        self.handle_recv(socket_client, socket_client_addr)

    def handle_recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        print('客户度的ip地址信息', clt_addr)
        recv_data = clt_socket.recv(1024)
        filename = recv_data.decode()
        print(recv_data.decode())
        # 直接发送 hello world ! 回去
        # hello world ！ 能不能从本地文件里面读取出来 ？
        # 文件的名字能不能让客户端传递过来 ？
        send_data = open(filename, mode='r', encoding='utf-8').read()
        clt_socket.send(send_data.encode())


if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
