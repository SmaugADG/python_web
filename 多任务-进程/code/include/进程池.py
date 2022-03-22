import time
import multiprocessing

# 创建函数，模拟文件拷贝
def copy_work():
    print("正在拷贝文件。。。")
    time.sleep(0.5)




if __name__ == '__main__':
    # 创建一个进程池，长度3
    pool=multiprocessing.Pool(3)
    for i in range(10):

        # 同步方式拷贝文件
        # pool.apply(函数名，（参数1，参数2。。。）)
        # pool.apply(copy_work)

        # 异步的方式拷贝文件
        # 必须使用pool.close(),表示不在接收新的任务
        # 主进程不在等待进程池结束，会结束执行，需要让进程池join，让主进程等待
        pool.apply_async(copy_work)

    pool.close()
    pool.join()