import time
import threading

# def sayHello():
#     print("hello")
#     time.sleep(1)
#
# if __name__=='__main__':
#     for i in range(5):
#         # 子线程创建步骤
#         thread_obj=threading.Thread(target=sayHello)
#         # 导入threading模块
#         # 指定子线程的执行分支
#         # 启动子线程start()
#         thread_obj.start()
#     print("主线程结束")



def sing():
    '''唱歌函数'''
    for i in range(3):
        print("正在唱歌。。。")
        thread_info = threading.current_thread()
        print("当前线程名称：%s" % thread_info)
        time.sleep(0.5)

def dance():
    '''跳舞函数'''
    for i in range(3):
        print("正在跳舞。。。")
        thread_info=threading.current_thread()
        print("当前线程名称：%s"%thread_info)
        time.sleep(0.5)

if __name__=="__main__":
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        # enumerate()获取当前所有线程的列表，
        # 使用len()对列表长度可以看到当前活跃的线程个数
        lenth=len(threading.enumerate())
        print("当前线程数量%d"%lenth)
        # threading.current_thread()获取当前线程信息，包括以线程名
        thread_info=threading.current_thread()
        print("当前线程名称：%s"%thread_info)
        if lenth<=1:
            break

        time.sleep(0.5)



