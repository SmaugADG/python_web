#!/usr/bin/python3
import psutil
import datetime
import yagmail

def linux_monitor(time):
    # 1.定义变量保存cpu硬件信息
    cpu_info=psutil.cpu_percent(interval=time)

    # 2.定义变量保存内存使用信息
    memory_info=psutil.virtual_memory()

    # 3.保存磁盘使用信息
    disk_info =psutil.disk_usage("/")

    # 4.获取网络收发数量
    net_info=psutil.net_io_counters()

    # 5.获取系统时间
    current_time=datetime.datetime.now().strftime("%Y-%m-%d %T")

    # 6 开始记录信息的字符串
    log_str ="|-------------------|-------------------|-------------------|-------------------|-------------------|\n"
    log_str+="|      监控时间      |      CPU使用率     |     内存使用率      |      硬盘使用率     |     网络使用率      |\n"
    log_str+="|                   |      (共%d核)       |      (共计%dG内存)  |     （共%d内存）    |                    |\n"%(psutil.cpu_count(logical=False),memory_info.total/1024/1024/1024,disk_info.total/1024/1024/1024)
    log_str+="|-------------------|-------------------|-------------------|-------------------|--------------------|\n"
    log_str+="|%s|        %s%%       |         %s%%     |        %s%%      |  收：%dMB;发：%dkB |\n"%(
        current_time,
        cpu_info,
        memory_info.percent,
        disk_info.percent,
        net_info.bytes_recv/8/1024/1024,
        net_info.bytes_sent/8/1024)
    log_str+="|-------------------|-------------------|-------------------|-------------------|--------------------|\n"

    print(log_str)

    # 保存到日志文件
    with open('log.txt','a') as file:
        file.write(log_str+'\n\n')

def main():
    while True:
        linux_monitor(5)    # 设置5秒钟执行一次

'''关于__name__'''
# 如果当前文件（linux系统监控.py）被别的文件引用，则__name__的值为：linux系统监控.py
# 如果未被引用，则默认值是：__main__
# 这个方法长用来检测本文见是否被别的文件引用

if __name__=='__main__':
    main()