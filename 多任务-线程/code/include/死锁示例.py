import threading
# 创建锁
lock=threading.Lock()

# 定义获取列表值的函数，参数为索引值
def get_value(index):
    data_list=[1,3,5,7,9]

    lock.acquire()
    if index >=len(data_list):
        print('%d 下表越界'% index)
         # 避免死锁 ，不在此释放的话，会在线程5处阻塞
        lock.release()
        return
    print(data_list[index])
    # 释放锁
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        t1=threading.Thread(target=get_value,args=(i,))
        t1.start()