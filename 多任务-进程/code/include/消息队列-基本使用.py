import multiprocessing

# 定义消息队列
# 如果不指定队列长度,或为负数，默认为最大长度，直到内存耗尽，
# 如果指定消息队列的大小，则消息队列就有上上限控制
queue=multiprocessing.Queue(3)  # 放入3条信息
# 放入内容
queue.put(1)    # 放第一个值
queue.put("hello")  # 第二个值
queue.put([1,2,3])  # 放入第三个值

# 长度为3的队列已满，如果继续put，会被阻塞,直达队列有空位
# queue.put(10)

# put_nowait()不会等待，如果没有空位值直接报错，提示queue.Full
# queue.put_nowait(10)
# 判满
print(queue.full()) # True

# 打印队列对象
# print(queue)

# 获取第二个值
value1=queue.get()
print(value1,queue.qsize()) # qsize()获取队列中消息的个数

# 获取第二个值
value2=queue.get()
print(value2,queue.qsize())

# 获取第二个值
value3=queue.get()
print(value3,queue.qsize())

# 判空
print(queue.empty())    #True

# 与上同理，如果队列为空get()也会阻塞，直到队列中有元素可取
# value4=queue.get()  # 再此处阻塞

# 使用get_nowait()，如果为空不等待直接报错，提示queue.Empty
value4=queue.get_nowait()
