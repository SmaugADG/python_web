import socket


# 创建socket
tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定本地信息
address=('',6666)
tcp_server_socket.bind(address)

# 使用socket创建的套接字默认的属性是主动地，使用listen将其变为被动的，这样就可以接收别人的链接了
# 128是允许链接的最大数（Windows下有效）linux下不需要无效
tcp_server_socket.listen(128)

# 如果有新的客户端来链接服务器，就会产生一个新的套接字专门管理这个客户端
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他客户端的链接
client_socket,ip_port=tcp_server_socket.accept()
print("已经链接客户端：",ip_port)

# 接收对方刚发来的数据
recv_data=client_socket.recv(1024)
print(recv_data)

# 发送数据到客户端
client_socket.send("好的，已阅！".encode("gbk"))

# 关闭当前这个客户端的链接
client_socket.close()

# 关闭socket,表示不再接受新的链接，已经链接的继续服务直到结束
tcp_server_socket.close()