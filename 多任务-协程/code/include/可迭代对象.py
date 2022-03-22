from collections import Iterable
# 使用isinstance() 函数检测某个对象是否是一个可迭代对象
# 列表是可迭代对象
result=isinstance([1,2],Iterable)
print(result)  # True

result=isinstance(100,Iterable)
print(result)   # False


'''
可迭代对象的本质：一个对象所属的类中含有__iter__()方法，该对象就是一个可迭代对象
'''
class MyClass(object):
    def __iter__(self):
        return self

c1=MyClass()

result=isinstance(c1,Iterable)
print(result)   # True


'''
迭代器：使用iter()和next()函数
    如果迭代万最后一个数据后，再次调用next()函数会抛出StopIteration的异常
来告诉我们所有数据都已经迭代完成，不用再执行next()函数
'''
list=[2,3,5,1,9,6,8]
# 获取list的迭代器
list_iter=iter(list)
# 迭代获取元素
i=0
while i<=len(list):
    try:
        print(next(list_iter))
    except Exception as e:
        print(e)
        break
    else:
        i+=1

