import ctypes
import threading

# 加载动态库
my_lib=ctypes.cdll.LoadLibrary("./libtest.so")

# 创建子线程
t=threading.Thread(target=my_lib)
t.start()

while True:
    pass