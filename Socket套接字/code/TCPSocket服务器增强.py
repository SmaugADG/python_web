import socket

# 创建socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定本地信息
address = ('', 6666)
tcp_server_socket.bind(address)

tcp_server_socket.listen(128)
while True:
    client_socket, ip_port = tcp_server_socket.accept()
    print("已经链接客户端：", ip_port)
    while True:
        # 接收对方刚发来的数据
        recv_data = client_socket.recv(1024)
        if recv_data:
            # 保存客户端信息
            re_text = recv_data.decode('gbk')
            print(re_text)
            # 发送数据到客户端
            client_socket.send("好的，已阅！".encode("gbk"))
        else:  # 如果收到空信息，认为链接断开
            print("客户端链接断开")
            break

    # 关闭当前这个客户端的链接
    client_socket.close()

# 关闭socket,表示不再接受新的链接，已经链接的继续服务直到结束
tcp_server_socket.close()