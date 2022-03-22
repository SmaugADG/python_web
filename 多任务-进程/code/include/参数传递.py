import multiprocessing
import time
import os
'''
进程之间是不共享全局变量的
'''
num=100

# 定义函数
def work1(a,b,c):
    print("参数：",a,b,c)
    global num
    for i in range(10):
        num+=1
    print("work1:",num)
    time.sleep(0.5)

def work2():
    global num
    print("work2:",num)

if __name__ == '__main__':
    # 创建进程
    # 传递参数-元祖 args=
    # p1=multiprocessing.Process(group=None,target=work1,name="P1",args=(1,2,3))
    # 传递参数-字典 kwargs=
    p1=multiprocessing.Process(group=None,target=work1,name="P1",kwargs={"a":1,"b":2,"c":3})
    p1.start()
    # 第一种：设置守护进程
    # p1.daemon=True

    p2=multiprocessing.Process(group=None,target=work2,name="P2")
    p2.start()

    print("主进程：",num)

    # 第二种 在主进程结束之前结子进程
    p1.terminate()
    p2.terminate()
    exit()