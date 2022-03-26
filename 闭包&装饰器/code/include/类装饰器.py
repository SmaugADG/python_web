'''使用一个类做装饰器'''
# 类的调用
# class Test(object):
#     def __init__(self):
#         print("__init__")
#     def run(self):
#         print("runing...")
#     def __call__(self, *args, **kwargs):
#         print("--call--")
# # 创建对象
# test=Test()
# # 当 对象名（）此时会去调用__call__()函数
# test()

'''类做装饰器'''
class Test(object):
    def __init__(self,func):
        print("__init__")
        print("func:",func)
        self.func=func
    def run(self):
        print("runing...")
    def __call__(self, *args, **kwargs):
        print("--call--")
@Test
def login():
    print("开始登录")

login()
