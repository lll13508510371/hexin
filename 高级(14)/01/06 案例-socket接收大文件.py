import socket

# 1. 创建 socket 链接对象
# socket.AF_INET ipv4 版本
# socket.SOCK_STREAM  tcp 协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
# address = ('www.baidu.com', 80)
address = ('14.215.177.39', 80)
tcp_client_socket.connect(address)

# 3.1 给服务器发送数据
send_data = b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n'
'''
二进制数据不需要编码和解码了,想看结果的时候decode就行了
'''
tcp_client_socket.send(send_data)

receive_data_arr = []
while True:
    # 3.2 接收服务器发送回来的数据`
    receive_data = tcp_client_socket.recv(1024)  # 1024 byte 大小 数据
    if receive_data:
        # 如果有内容就继续接收
        receive_data_arr.append(receive_data)
    else:
        break

print('接收到的数据:\t', b''.join(receive_data_arr).decode('utf-8'))

# 4. 关闭与服务器的链接
tcp_client_socket.close()
