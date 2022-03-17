import socket

# 创建套接字
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立链接
tcp_client_socket.connect(("192.168.123.165",6666))

# 接受用户输入的文件名
file_name=input("请输入文件名：\n")

# 发送文件名到服务器端
tcp_client_socket.send(file_name.encode("utf-8"))

# 创建文件，准备下载文件
with open(file_name,'wb') as file:
    while True:
        recv_data=tcp_client_socket.recv(1024)
        if recv_data:
            file.write(recv_data)
        else:
            break
# 关闭套接字
tcp_client_socket.close()
