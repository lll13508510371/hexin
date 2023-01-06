import socket

# 1. 创建 socket 链接对象
# socket.AF_INET ipv4 版本
# socket.SOCK_STREAM  tcp 协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
address = ('127.0.0.1', 7788)
tcp_client_socket.connect(address)

while True:
    # 3.1 给服务器发送数据
    send_data = input('请输入需要发送的数据:\t')
    if send_data == '88':
        break
    tcp_client_socket.send(send_data.encode('gbk'))

    # 3.2 接收服务器发送回来的数据
    recv_data = tcp_client_socket.recv(1024)  # 1024 byte 大小 数据
    data = recv_data.decode('gbk')
    # if data == '88':
    #     break
    print('接收到的数据:\t', data)

# 4. 关闭与服务器的链接
tcp_client_socket.close()
