from application import utils

def parse_request(request_data):
    '''解析请求的报文'''
    # 根据客户端浏览器请求的资源路径，返回请求资源
    # 1.把请求写协议解码，得到请求报文字符串
    request_text = request_data.decode()
    # 2.得到请求行
    # 2.1 查找第一个\r\n出现的位置
    loc = request_text.find("\r\n")
    # 2.2 截取字符串，从开头截取到第一个\r\n出现的位置
    request_line = request_text[:loc]
    # 3 把请求行按照空格拆分，得到列表
    request_line_list = request_line.split(" ")
    file_path = request_line_list[1]

    # 设置默认首页
    if file_path == '/':
        file_path = "/test.html"
    return file_path


def application(current_dir,request_data):
    # 调用parase_request函数，解析请求协议
    file_path=parse_request(request_data)
    resource_path=current_dir+file_path

    # 响应主题
    ''''返回指定页面'''
    try:
        with open(resource_path, "rb") as file:
            response_body = file.read()
        response_data=utils.create_http_response("200 OK",response_body)
    except Exception as e:
        # 重新修改内容为404
        response_body = "Error!" + str(e)
        response_body = response_body.encode()
        response_data=utils.create_http_response("404 Not found",response_body)

    return response_data