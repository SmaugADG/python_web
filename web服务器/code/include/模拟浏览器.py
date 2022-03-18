'''
1.导入模块
2.创建调节自
3.建立连接
4.拼接请求协议
5.发送请求协议
6.接收服务器相应内容
7.保存内容
8.关闭链接
'''
# 1.导入模块
import socket
# 2.创建调节自
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 3.建立连接
tcp_client_socket.connect(("test",8080))
# 4.拼接请求协议
# 4.1 请求行
request_line="GET / HTTP/1.1\r\n"
# 4.2 请求头
request_header="Host:test\r\n"
# 4.3 请求空行
request_blank="\r\n"
# 拼接整体
request_data=request_line+request_header+request_blank
print(request_data)
# 5.发送请求协议
tcp_client_socket.send(request_data.encode())
# 6.接收服务器响应内容
recv_data=tcp_client_socket.recv(4096)
recv_text=recv_data.decode()
print(recv_text)
loc=recv_text.find("\r\n\r\n")
html_data=recv_text[loc+4:]
print(html_data)
# 7.保存内容
with open("test.html",'w') as file:
    file.write(html_data)

# 8.关闭链接
tcp_client_socket.close()