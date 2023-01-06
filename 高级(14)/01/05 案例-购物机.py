""""""
import socket

goods = {
    '矿泉水': '2 rmb',
    '可乐': '2.5 rmb',
    '雪碧': '2.5 rmb',
    '果粒橙': '4 rmb',
}

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 7788)
tcp_server_socket.bind(address)

tcp_server_socket.listen(128)  # 理论上最大只可以链接 128
print('服务已经启动,运行在', address)
client_socket, client_address = tcp_server_socket.accept()

client_socket.send('欢迎光临售货机,你需要购买什么物品'.encode('gbk'))

while True:
    recv_data = client_socket.recv(1024)
    data = recv_data.decode('gbk')
    if data == '88':
        client_socket.send('欢迎下次光临'.encode('gbk'))
        break
    price = goods.get(data)
    if price:
        client_socket.send(f'{data}-{price}'.encode('gbk'))
    else:
        client_socket.send(
            f'你需要购买的物品 {data} 不存在,请重新选择:{list(goods.keys())}'.encode('gbk'))
client_socket.close()
tcp_server_socket.close()
