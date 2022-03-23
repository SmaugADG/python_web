'''
两种方法创建生成器(generator)
1） 把一个列表生成式的[]改成()
2) 使用yield关键字
'''
'''使用列表生成式'''
# 普通列表推导式
L=[x*2 for x in range(5)]
print(L)

# 变成生成式
G=(x*2 for x in range(5))
print(G)    # object <genexpr>
g=G
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("-"*20)

'''使用yield关键字'''
# 使用了yield的函数不在是函数，而是生成器
# yield关键字有两点作用：
# 保存当前的运行状态，然后暂停执行，即将生成器挂起
# 将yield关键字后面的表达式作为返回值返回，此时可以理解为收到了return的作用


# 普通函数
# def test():
#     return 10
#
# t=test()
# print(t)

def test():
    yield 10

t=test()
print(t)    # object <genexpr>

print(next(t))  # 可以使用迭代器

print("-"*20)
'''实现斐波那契数列'''
def fibonacci(n):
    a=0
    b=1

    current_index=0

    while current_index<n:
        result=a

        a,b=b,a+b

        current_index+=1

        yield result

fib = fibonacci(5)

# value=next(fib)
# print(value)
for i in fib:
    print(i)