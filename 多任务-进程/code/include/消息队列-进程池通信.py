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
        print("正在写入：",i)
        time.sleep(0.5)

def read_queue(queue):
    while True:
        if queue.qsize()==0:
            print("队列空")
            break
        result=queue.get()
        print("正在读取：",result)
        time.sleep(0.5)

if __name__ == '__main__':
    # 创建进程池
    pool=multiprocessing.Pool(2)
    # 不能使用multiprocessing.Queue()
    queue=multiprocessing.Manager().Queue(5)

    # 在进程池中的进程间进行通信
    # 使用线程池同步的方式，先写后读
    # pool.apply(write_queue,(queue,))
    # pool.apply(read_queue,(queue,))

    # 使用异步方法进行通信
    # apply_async()会返回ApplyResult对象
    result=pool.apply_async(write_queue,(queue,))
    # ApplyResult对象的wait()方法，表示后续进程必须等待当前进程执行完在再继续
    result.wait()
    pool.apply_async(read_queue,(queue,))

    pool.close()
    pool.join()

