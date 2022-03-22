import multiprocessing
import time
import os
'''
使用multiprocessing.Process类能够创建进程对象

可在命令行使用命令  kill -9 [进程号] 杀掉进程
'''
# 定义函数
def work1():
    for i in range(10):
        print("work1...",i)
        # 获取当前进程名称
        print(multiprocessing.current_process())

        # 获取进程编号
        # 1. 通过multiprocessing.current_process().pid
        # print(multiprocessing.current_process().pid)
        # 2. 通过 import os模块的getpid()
        print(os.getpid())

        # 获取进程的父级id
        print(os.getppid())


        time.sleep(0.5)

if __name__ == '__main__':
    # 创建进程
    p1=multiprocessing.Process(group=None,target=work1,name="P1")
    p1.start()
    # 获取当前进程名称
    print(multiprocessing.current_process())    #MainProcess
    print("主线程父级",os.getppid())
    # for i in range(10):
    #     print("主进程",i)
    #     time.sleep(0.5)



