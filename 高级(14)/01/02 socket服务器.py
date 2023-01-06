import socket

# 1. 创建 socket 链接对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地ip以及端口 '127.0.0.1'改成'localhost'也是可以的
address = ('127.0.0.1', 7788)
tcp_server_socket.bind(address)

# 3. 等待客户端的链接
tcp_server_socket.listen(5)  # 理论上最大只可以链接 128 大部分应用程序设为5就够用了
print('服务已经启动,运行在', address)

# 4. 客户端连接上之后
# 客户端的链接, 客户端的地址
# client_socket和客户端的 tcp_client_socket是同一个对象
client_socket, client_address = tcp_server_socket.accept()

# 5.1 给客户端发送数据
client_socket.send('欢迎光临服务器'.encode('gbk'))

# 5.2 接受客户端的数据
receive_data = client_socket.recv(1024)
print('接受客户端的数据:\t', receive_data.decode('gbk'))

# 6. 关闭链接
client_socket.close()
tcp_server_socket.close()
