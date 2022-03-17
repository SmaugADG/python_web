import socket

# 创建套接字
tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置套接字属性
# setsockopt(套接字级别，属性名，属性值)
# socket.SOL_SOCKET 当前套接字
# socket.SO_REUSEADDR 设置地址重用 True 可以重用，False 不能重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

# 绑定地址和端口
tcp_server_socket.bind(("",6666))

# 开始监听
tcp_server_socket.listen(128)

# 开始业务
while True:
    # 等待客户端连接诶
    new_client_socket,ip_port=tcp_server_socket.accept()
    print(ip_port)

    # 接收欧客户端发来的文件名
    recv_data=new_client_socket.recv(1024)
    file_name=recv_data.decode("utf-8")
    # print(file_name)
    try:
        with open(file_name,'rb') as file:
            while True:
                file_data=file.read(1024)

                if file_data:
                    new_client_socket.send(file_data)
                else:
                    break
    except:
        print("文件下载出错：",file_name)
    else:
        print("文件下载成功",file_name)

    # 关闭客户连接
    new_client_socket.close()

# 关闭服务器链接
tcp_server_socket.close()