import socket

# ws=WebServer()
# ws.start()
class WebServer(object):
    # 初始化
    def __init__(self):
        # 创建tcp套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        self.tcp_server_socket.bind(("", 8080))
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
        print("客户全请求"+str(ip_port))
        if not request_data:
            print("客户端已下线：%s"%str(ip_port))
            new_client_socket.close()
            return

        # 根据客户端浏览器请求的资源路径，返回请求资源
        # 1.把请求写协议解码，得到请求报文字符串
        request_text=request_data.decode()
        # 2.得到请求行
        # 2.1 查找第一个\r\n出现的位置
        loc=request_text.find("\r\n")
        # 2.2 截取字符串，从开头截取到第一个\r\n出现的位置
        request_line=request_text[:loc]
        # 3 把请求行按照空格拆分，得到列表
        request_line_list=request_line.split(" ")
        file_path=request_line_list[1]

        # 设置默认首页
        if file_path=='/':
            file_path="/test.html"

        # 拼接响应报文
        # 响应行
        response_line="HTTP/1.1 200 OK\r\n"
        # 响应头
        response_head="Server:PythonWS/2.1\r\n"
        # 响应空行
        response_blank="\r\n\r\n"
        # 响应主题
        ''''返回指定页面'''
        try:
            with open("static"+file_path,"rb") as file:
                response_body=file.read()
        except Exception as e:
            # 重新修改内容为404
            response_line="HTTP/1.1 404 Not Found\r\n"
            response_body="Error!"+str(e)
            response_body=response_body.encode()
        # 拼接返回体
        response_data=(response_line+response_head+response_blank).encode()+response_body
        # 发送响应碑文给客户端浏览器
        new_client_socket.send(response_data)
        # 关闭链接
        new_client_socket.close()

def main():
    '''主函数'''
    # 创建WebServer类的对象
    ws=WebServer()
    # 使用对象调用start()
    ws.start()


if __name__=="__main__":
    main()