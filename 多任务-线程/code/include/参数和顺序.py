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



def sing(a,b,c):
    '''唱歌函数'''
    for i in range(3):
        print("参数：%d,%d,%d"%(a,b,c))
        print("正在唱歌。。。")
        time.sleep(0.5)

def dance():
    '''跳舞函数'''
    for i in range(3):
        print("正在跳舞。。。")
        time.sleep(0.5)

if __name__=="__main__":
    # 线程传递参数有三种方式
    # 1.使用元祖 threading.Thread(target=xxx,args=(参数一，参数二，。。。))
    # t1=threading.Thread(target=sing,args=(1,2,3))
    # 2.使用字典  threading.Thread(target=xxx,kwargs=("形参名1":参数一，...))
    # t1=threading.Thread(target=sing,kwargs={"a":1,"b":2,"c":3})
    # 3.混合使用元祖和字典
    t1=threading.Thread(target=sing,args=(1,),kwargs={"c":3,"b":2})

    t2=threading.Thread(target=dance)
    t1.start()
    t2.start()





