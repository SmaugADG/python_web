import time

def sing():
    '''唱歌函数'''
    for i in range(3):
        print("正在唱歌。。。")
        time.sleep(1)

def dance():
    '''跳舞函数'''
    for i in range(3):
        print("正在跳舞。。。")
        time.sleep(0.5)

if __name__=="__main__":
    sing()
    dance()
