import socket

# 创建套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 发送信息
# 套接字默认不允许发送广播，需要设置权限
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
send_conten="集合！集合！"
udp_socket.sendto(send_conten.encode('gbk'),("255.255.255.255",9090))

# 关闭套接字
udp_socket.close()