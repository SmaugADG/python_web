import socket
import threading

def recv_msg(new_client_socket,ip_port):
    while True:
        # 接收客户端信息
        recv_data=new_client_socket.recv(1024)
        if recv_data:
            # 解码数据并进行数据输出
            recv_text=recv_data.decode('gbk')
            print("收到用户%s:%s"%(ip_port,recv_text))
        else:
            print("用户：%s下线"%ip_port)
            break
    # 关闭当前客户端的链接
    new_client_socket.close()


# 导入模块
# 创建套接字
tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 设置地址可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# 绑定端口
tcp_server_socket.bind(("",8080))
# 设置监听
tcp_server_socket.listen(128)
while True:
    # 接收客户端连接
    new_client_socket,ip_port=tcp_server_socket.accept()
    print("用户：%s上线"%ip_port)
    # 调用函数处理
    # recv_msg(new_client_socket, ip_port)
    # 创建线程
    thread_recvmsg=threading.Thread(target=recv_msg,args=(new_client_socket,ip_port))
    thread_recvmsg.setDaemon(True)
    thread_recvmsg.start()
# tcp_server_socket.close()
