'''闭包引入'''
# def test():
#     print("我是一个孤独的函数。。。。")
#
# test()
#
# # 函数名是一个特殊的变量
# ret=test
# print(ret)
# print("%x"%id(test))
# # 通过ret调用函数
# ret()

# 函数名是一个特殊的变量，保存函数首地址()

'''闭包'''
def function_out(num):
    print("function_out num",num)
    def function_in(num_in):
        print("function_in---num:",num)
        print("function_in---num_in",num_in)

    return function_in

# function_out(10)    #只有  function_out num 10

# 打印入下内容
# function_out num 10
# function_in---num: 10
# function_in---num_in 100
ret=function_out(10)
ret(100)

print("-"*20)

'''闭包中的变量问题'''

def fun_out(num):
    def fun_in():
        # 如果内层函数定义了同名的变量，则不能再使用外层函数的变量
        # 如果要使用外部变量，需要声明
        nonlocal num
        print("1.fun_in num:",num)    # 10
        num=88
        print("2.fun_in num:", num)     # 88
    return fun_in

ret=fun_out(10)
ret()

