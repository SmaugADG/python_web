import socket

# 创建socket
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立tcp链接
tcp_client_socket.connect(("192.168.123.164",8080))

# 开始发送数据
tcp_client_socket.send("hello".encode('gbk'))


# 接收数据
recv_data=tcp_client_socket.recv(1024).decode('gbk')
print(recv_data)

# 关闭套接字
tcp_client_socket.close()