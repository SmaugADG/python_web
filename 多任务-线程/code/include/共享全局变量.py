import  threading
import time
# 定义全局变量
num=0

def work1():
    # 使用global声明全局变量，表示后续的操作，都是操作全局变量
    global num
    for i in range(1000000):
        num+=1
    print("work1 num=%d" % num)
    # time.sleep(3)
    # print("work1 after num=%d"%num)

def work2():
    global num
    for i in range(1000000):
        num+=1
    print("work2 num=%d"%num)

if __name__ == '__main__':
    t1=threading.Thread(target=work1)
    t2=threading.Thread(target=work2)

    t1.start()
    # 在t2运行之前，必须t1执行完
    # 其实就是t1优先执行
    t1.join()


    t2.start()

    while len(threading.enumerate())!=1:
        time.sleep(1)
        print("main num=",num)



