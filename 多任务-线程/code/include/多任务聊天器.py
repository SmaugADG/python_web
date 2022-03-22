import socket
import threading
# 聊天器主要功能
# 1.发送信息
# 2.接收信息
# 3.退出信息

def sen_msg(udp_socket):
    '''发送信息的方法'''
    # 1. 输入接收方的IP地址
    ipaddr=input("请输入接收方IP：\n")
    if len(ipaddr)==0:
        ipaddr="192.168.123.165"
        print("默认地址：%s"%ipaddr)
    # 2.输入接收方端口
    port=input("请输入接收方段口：\n")
    if len(port)==0:
        port="9090"
        print("默认端口：%s"%port)

    # 3.输入要发送的内容
    content=input("请输入要发送的内容：\n")
    # 4.发送数据
    udp_socket.sendto(content.encode('gbk'),(ipaddr,int(port)))

def recv_msg(udp_socket):
    while True:
        # 1.接收数据
        recv_data=udp_socket.recvfrom(1024)
        # 2. 解码信息并显示出来
        re_text=recv_data[0].decode('gbk')
        ip_port=recv_data[1]
        # 打印显示对方的和端口信息
        print("收到用户%s:%s"%(ip_port,re_text))
        # print(re_text)

if __name__=='__main__':
    # 创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定端口号 6666
    udp_socket.bind(("",6666))

    # 创建线程，用于接收信息
    recvmsg_thread=threading.Thread(target=recv_msg,args=(udp_socket,))
    recvmsg_thread.setDaemon(True)
    recvmsg_thread.start()
    while True:
        # 菜单栏
        print("--------------------------")
        print("---------1,发送信息---------")
        print("---------2.退出系统---------")
        print("---------------------------")
        try:
            # 1. 提示用户选择功能
            num=int(input("请输入选型：\n"))
            # 2.开始业务
            if num==1:
                sen_msg(udp_socket)
            elif num==2:
                print("程序退出！")
                break
            else:
                print("请输入正确选项！")
        except Exception as e:
            print(e)
        # else:
        #     pass

    udp_socket.close()