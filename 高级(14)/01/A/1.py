import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 7788)

tcp_client_socket.connect(server_address)

send_info = input('请输入发给服务器的信息: ')

tcp_client_socket.send(send_info.encode('gbk'))

receive_sever_info = tcp_client_socket.recv(1024)

print(id(receive_sever_info))
print(id(tcp_client_socket.recv(1024)))

'''
两个tcp_client_socket.recv(1024)的id并不相同
'''
