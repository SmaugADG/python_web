'''多个装饰器装饰同一个函数'''
# 定义 一个让文字加粗的函数
def markBlod(func):
    def fun_in():
        return "<b>"+func()+"</b>"
    return fun_in

# 定义 一个让文字倾斜的函数
def markItalic(func):
    def fun_in():
        return "<i>"+func()+"</i>"
    return fun_in


# <b>helloworld-1</b>
@markBlod
def test():
    return "hello world-1"

@markItalic
def test2():
    return "hello world-2"

@markItalic
@markBlod
def test3():
    return "helloworld-3"


# print(test())   # <b>hello world-1</b>
# print(test2())  #   <i>hello world-2</i>
print(test3())  #   <i><b>helloworld-3</b></i>





