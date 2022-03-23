'''生成器中使用return的问题'''

def fibonacci(n):
    a=0
    b=1

    current_index=0

    while current_index<n:
        result=a

        a,b=b,a+b

        current_index+=1
        print("before yield")
        value=yield result
        print("after yield")
        if value==1:
            return "我是return"

f=fibonacci(5)
# try:
#     print(next(f))
#     print(next(f))
#     print(f.send(1))
# except Exception as e:
#     print(e)    # return 的内容存放在异常中
# yield阻塞停止后需要next唤醒，send也可以唤醒yield，而且可以传递参数
# 生成器中的return用来让生成器再需要的时候停止，如上例中：
# 在两次输出后，我们使用send传递参数1，value就会被赋值为1，
# 此时if条件成立，执行return，中断生成器继续执行，return后不能有任何语句

# 可以使用send来启动生成器
print(f.send(None)) # 首次启动生成器必须参数必须使用None

print(f.send(2))
print(f.send(1))    # 返回return内容
# 一般首次启动使用next