'''装饰器'''
# 在不改变函数代码前提下，给函数添加新的功能

# 不修改login，增加验证功能

def fun_out(func):
    def fun_in(num):
        print("开始验证")
        func(num)
    return fun_in
# 装饰器方式
@fun_out
def login(num):
    print("开始登录！")
# 闭包调用方式
# login=fun_out(login)

# 执行
login(10)


'''多个不定长的参数'''
def fun_out(func):
    def fun_in(*args,**kwargs):
        print("开始验证")
        print(args,kwargs)
        func(*args,**kwargs)
    return fun_in
# 装饰器方式
@fun_out
def login(*args,**kwargs):
    print("开始登录！")


# 执行
login(10,20,c=100)

'''有返回值的函数'''
def fun_out(func):
    def fun_in(a,b):
        print("开始验证")
        return func(a,b)
    return fun_in
# 装饰器方式
@fun_out
def login(a,b):
    print("开始登录！")
    return a+b


# 执行
s=login(10,20)
print(s)


'''通用版装饰器'''
def fun_out(func):
    def fun_in(*args,**kwargs):
        print("开始验证")
        print(args,kwargs)
        return func(*args,**kwargs)
    return fun_in
# 装饰器方式
@fun_out
def login(*args,**kwargs):
    print("开始登录！")
    return 10


# 执行
result=login(10,20,c=100)
print(result)


