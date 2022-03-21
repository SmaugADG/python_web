import  threading
import time
'''
threading模块中定义了Lock类，可以方便处理互斥锁
mutex=threading.Lock()  # 创建锁
mutex.acquire() # 锁定
mutex.release() #释放

如果之前没有锁，acquire不会阻塞
如果已经上锁，此时acquire会被阻塞，直到锁被解锁为止
'''

# 定义全局变量
num=0
# 创建锁
mutex=threading.Lock()

def work1():
    # 使用global声明全局变量，表示后续的操作，都是操作全局变量
    global num
    for i in range(1000000):
        mutex.acquire()
        num+=1
        mutex.release()
    print("work1 num=%d" % num)
    # time.sleep(3)
    # print("work1 after num=%d"%num)

def work2():
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
    print("work2 num=%d"%num)

if __name__ == '__main__':
    t1=threading.Thread(target=work1)
    t2=threading.Thread(target=work2)

    t1.start()

    t2.start()

    while len(threading.enumerate())!=1:
        time.sleep(2)
        print("main num=",num)



