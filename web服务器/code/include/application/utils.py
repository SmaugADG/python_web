
def create_http_response(status,response_body):
    # 拼接响应报文
    # 响应行
    response_line = "HTTP/1.1 %s\r\n"%status
    # 响应头
    response_head = "Server:PythonWS/2.1\r\n"
    # 响应空行
    response_blank = "\r\n\r\n"
    # 拼接返回体
    response_data = (response_line + response_head + response_blank).encode() + response_body
    return response_data