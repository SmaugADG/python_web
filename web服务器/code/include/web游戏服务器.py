import socket
from application import app
import sys


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

        # 初始化项目
        self.projects_dict=dict()
        self.current_dir=""
        # 初始化字典
        self.projects_dict['植物大战僵尸-普通版']='zwdzjs-v1'
        self.projects_dict['植物大战僵尸-外挂板']='zwdzjs-v2'
        self.projects_dict['保卫萝卜']='tafang'
        self.projects_dict['2048']='2048'
        self.projects_dict['读心术']='dxs'

        # 初始化菜单
        self.init_project()

    def init_project(self):
        # 获得字典所有的key
        dick_keys=tuple(self.projects_dict.keys())
        # 输出提示信息
        print("请选择要发布的项目\n")
        # 循环输出项目列表
        for index,value in enumerate(dick_keys):
            print("%d,%s"%(index,value))
        # 接收用户输入的编号
        sel_num=int(input("请输入要发布的游戏编号\n"))
        # 根据编号的到字典key
        sel_key=dick_keys[sel_num]
        print("已经成功发布:%s ,刷新页面"%sel_key)
        # 根据字典key获取当前的项目目录
        # 保存项目目录到实例变量中
        self.current_dir=self.projects_dict[sel_key]



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
        response_data=app.application(self.current_dir,request_data)
        # 发送响应碑文给客户端浏览器
        new_client_socket.send(response_data)
        # 关闭链接
        new_client_socket.close()

def main():
    # 判断参数个数是否合法
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