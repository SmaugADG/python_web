import time
from greenlet import greenlet
import gevent
from gevent import monkey
monkey.patch_all()


def work1():
    '''任务1'''
    while True:
        print("work1.。。")
        time.sleep(0.5)
        yield

def work2():
    '''任务2'''
    while True:
        print("work2...")
        time.sleep(0.5)
        yield

if __name__ == '__main__':
    w1=work1()
    w2=work2()
    while True:
        next(w1)
        next(w2)

'''可以使用greenlet实现协程'''
# generator 实现的协程只能将yield value返回给调用者
# 在greenlet中，target.switch(value)可以切换到指定的协程（target），然后yield value
# greenlet使用switch切换协程，从一个协程切换到另一个协程需要显示指定

def work1():
    '''任务1'''
    while True:
        print("work1.。。")
        time.sleep(0.5)
        # 切换到gr2执行
        gr2.switch()
        time.sleep(0.5)

def work2():
    '''任务2'''
    while True:
        print("work2...")
        # 切换到gr1执行
        gr1.switch()
        time.sleep(0.5)
if __name__ == '__main__':

    gr1=greenlet(work1)
    gr2=greenlet(work2)

    # 指派gr1先运行
    gr1.switch()

'''gevent实现协程'''
# 当一个协程遇到IO操作时，会自动切换到其他协程，
# 等到IO结束的时候，在在合适的时间切换回来，
# 这样能保证总有协程在运行

def work1():
    '''任务1'''
    for i in range(5):
        # 可以使用gevent,getcurrent()查看当前执行的协程号
        print("work1.。。",gevent.getcurrent())
        # 默认情况下time.sleep()不能被认为是耗时操作
        # 使用gevent.sleep()
        # gevent.sleep(0.5)

        # 打了monkey补丁后，gevent会识别time.sleep()
        time.sleep(0.5)

def work2():
    '''任务2'''
    for i in range(5):
        print("work2...")
        time.sleep(0.5)
        # gevent.sleep(0.5)


if __name__ == '__main__':

    g1=gevent.spawn(work1)
    g2=gevent.spawn(work2)

    # 等待协程执行完任务在结束主进程
    g1.join()
    g2.join()


# 猴子补丁
# 在运行时替换方法，属性等
# 在不修改第三方代码的情况下增加原来不支持的功能
# 在运行时为内存中的对象增加patch而不是在磁盘的源代码中增加

# from gevent import monkey
# monkey.patch_all()

