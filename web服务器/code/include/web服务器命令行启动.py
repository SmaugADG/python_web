import socket
from application import app
import sys

# ws=WebServer()
# ws.start()
class WebServer(object):
    # 初始化
    def __init__(self,port):
        # 创建tcp套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        self.tcp_server_socket.bind(("", port))
        # 设置监听
        self.tcp_server_socket.listen(128)

    def start(self):
        '''启动服务'''
        while True:
            # 等待客户端链接
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            self.request_handler(new_client_socket, ip_port)


    def request_handler(self,new_client_socket,ip_port):
        '''接收信息并做出响应'''
        # 接收浏览器请求，并判断请求是否为空
        request_data=new_client_socket.recv(1024)
        print("客户请求"+str(ip_port))
        if not request_data:    # 客户浏览器关闭
            print("客户端已下线：%s"%str(ip_port))
            new_client_socket.close()
            return

        # 使用aplication文件夹调用app模块调用application（）方法
        response_data=app.application("static",request_data)
        # 发送响应碑文给客户端浏览器
        new_client_socket.send(response_data)
        # 关闭链接
        new_client_socket.close()

def main():
    # 判断参数个数是否合法
    list=sys.argv
    print(list)
    if len(sys.argv)!=2:
        print("启动失败，参数错误！")
        return
    # 判断端口是否是数字
    if not sys.argv[1].isdigit():
        print("启动失败，端口非法！")
        return
    # 保存端口
    port=int(sys.argv[1])


    '''主函数'''
    # 创建WebServer类的对象
    ws=WebServer(port)
    # 使用对象调用start()
    ws.start()


if __name__=="__main__":
    main()