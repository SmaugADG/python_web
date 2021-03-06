import multiprocessing
import time

def write_queue(queue):
    # 循环写入数据
    for i in range(10):
        if queue.full():
            print("队列已满！")
            break
        # 向队列中放入数据
        queue.put(i)

        time.sleep(0.5)

def read_queue(queue):
    while True:
        if queue.empty():
            print("队列空")
            break
        result=queue.get()
        print(result)

if __name__ == '__main__':
    # 创建消息队列
    queue=multiprocessing.Queue(3)

    # 创建子进程
    p1=multiprocessing.Process(target=write_queue,args=(queue,))
    p1.start()
    p1.join()
    p2=multiprocessing.Process(target=read_queue,args=(queue,))
    p2.start()




