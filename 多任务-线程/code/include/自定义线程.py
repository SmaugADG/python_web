import threading
import time
# 自定义线程类：
# 1.让自定义的类集成threading.Thread类
# class Thread():
#     def start(self):
#         self.run()
#
#     def run(self):
#         pass
# 2.重写父类的run方法
class MyThread(threading.Thread):
    # 定义构造方法
    def __init__(self,num):
        # 调用父类的init方法
        super(MyThread,self).__init__()
        # 定义 属性保存 num值
        self.num=num
    def run(self):
        for i in range(5):
            # 再run方法中，self.name可以输出当前进程名
            print("正在执行run方法。。。",self.name,self.num)
            time.sleep(0.5)

    def test(self):
        pass
if __name__ == '__main__':
    mythread=MyThread(10)

    mythread.start()

    print("主线程。。。")