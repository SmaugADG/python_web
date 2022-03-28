import multiprocessing
import threading
# 单进程死循环
# def test():
#     while True:
#         pass
#
# test()

# 多进程死循环
# def dealloop():
#     while True:
#         pass
#
# p1=multiprocessing.Process(target=dealloop)
# p1.start()
#
# dealloop()

# 多线程死循环

# 子线程死循环
def test():
    while True:
        pass
if __name__ == '__main__':

    t1=threading.Thread(target=test)
    t1.start()

    while True:
        pass




