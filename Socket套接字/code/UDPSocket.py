
'''
1.导入模块 socaket
2. 创建套接字，使用IPV4 UDP方式
3.数据的传递
4.关闭套接字
'''

# 导入模块
import  socket
# 两个参数：协议类型，传输方式
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# # 绑定发送端 端口号
# # local_addr=('192.168.123.165',8888)
# udp_socket.bind(("192.168.123.165",8888))
# # 发送数据
# # 两个参数：二进制数据内容，接收方IP
# # 字符串.encond() 将字符串转换成二进制
# # 要求IP和端口号是一个元祖，IP地址为字符串类型，端口号为整数类型
# # dest_addr=("192.168.123.164",8080)
# test=input("alan:")
# udp_socket.sendto(test.encode("gbk"),("192.168.123.164",8080))
#

# 接收数据
# 绑定接收端 端口
udp_socket.bind(("192.168.123.165",6666))
# recvfrom会造成程序的阻塞，
# 接收到数据后自动解除，如果没有发送数据局，会一直等待
recv_data=udp_socket.recvfrom(1024)
# 接收到的数据是一个元祖：第一个是接收到的数据（二进制）
# 第二个是元祖，发送方 的IP和端口
print("candice:"+recv_data[0].decode('gbk'))
# print(recv_data[1])



# 关闭套接字
udp_socket.close()