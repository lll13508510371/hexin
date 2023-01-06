import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
# address = ('www.baidu.com', 80)
address = ('127.0.0.1', 7788)
tcp_client_socket.connect(address)

# 3.1 给服务器发送数据
send_data = input('请输入图片的名字')
tcp_client_socket.send(send_data.encode('gbk'))

recv_data_arr = []
while True:
    # 3.2 接收服务器发送回来的数据
    recv_data = tcp_client_socket.recv(1024)  # 1024 byte 大小 数据
    if recv_data:
        # 如果有内容就继续接收
        recv_data_arr.append(recv_data)
    else:
        break

img_data = b''.join(recv_data_arr)
print('接收到的数据:\t', img_data)  # 图片数据就是二进制数据,所以不需要解码了

with open('下载' + send_data, mode='wb') as file:
    file.write(img_data)
print(open('下载' + send_data, mode='rb').read())
# 4. 关闭与服务器的链接
tcp_client_socket.close()
