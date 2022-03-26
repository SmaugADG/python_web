'''
装饰器写法
1、存在闭包
2.存在带修饰的函数

'''
def test(path):
    print(path)
    def fun_out(func):
        '''外层函数'''
        print("fun_out path:",path)
        def fun_in():
            print("开始验证")
            func()
        return fun_in
    return fun_out

# @test("login.py")分为两步
# 1）执行test("login.py")  -->fun_out 引用
# 2） @第一步 的结果   -->@fun_out 装饰器
# login=fun_out(login)

# @ func_out
# login=fn_out(login)
@test("login.py")
def login():
    print("开始登录")

@test("redister.py")
def register():
    print("开始注册")

login()
register()