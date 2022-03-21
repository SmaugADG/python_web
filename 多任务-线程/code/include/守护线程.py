import threading
import time

def work1():
    for i in range(10):
        print("正在执行。。。",i)
        time.sleep(0.5)

if __name__=='__main__':
    # 创建子线程
    t1=threading.Thread(target=work1)
    # 设置子线程t1为守护线程
    t1.setDaemon(True)
    # 启动子线程
    t1.start()

    # 睡2秒
    time.sleep(2)
    print("主线程结束")

    # 让程序退出
    # 档主线程睡眠2秒，开始结束字节的时候，子线程还没有结束，默认情况下，子线程继续执行
    # exit()退出无效
    #如果想让主线程结束的时候，没有执行完的子线程也一起结束，这就是线程守护
    exit()