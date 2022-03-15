# 1.导入psutil模块
import psutil
import datetime
# 2.获取cpu信息
# 2.1 获取cpu的核心数
print(psutil.cpu_count())
# 2.2 获取cpu的使用率
print(psutil.cpu_percent(interval=0.5,percpu=True))

# 获取开机时见
print(psutil.boot_time())
# 转换成标准时间
print(datetime.datetime.fromtimestamp(psutil.boot_time()))
