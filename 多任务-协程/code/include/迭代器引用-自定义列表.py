from collections import Iterable

'''
一个类实现了__iter__()和__next__()函数，就是一个迭代器
1）实现__iter__()方法
2）实现__next__()方法
当调用iter时，会调用对象的__iter__()方法
当调用next时，会调用对象的__next__()方法

迭代器自身也是一个迭代器，所以迭代器的__iter__()方法返回自身即可
'''
class MyList():
    # 定义构造方法，用于初始化示例属性
    def __init__(self):
        # 定义实例属性item 并初始化值为空列表
        self.item=list()
    # 添加元素
    def addIteam(self,data):
        # 保存数据到实例属性中
        self.item.append(data)
    # 获取对象的迭代器
    def __iter__(self):
        # 返回迭代器随想
        mylist_iterator=MyListIterator(self.item)
        return mylist_iterator


# 自定义迭代器类
class MyListIterator():
    # 定义构造方法
    def __init__(self,item):
        self.item=item
        # 保存数据到当前类的实例变量中
        self.current_index=0
    # 必须含有的方法
    def __iter__(self):
        pass
    def __next__(self):
        if self.current_index<len(self.item):
            # 获取值
            data1=self.item[self.current_index]
            # 序列自增
            self.current_index+=1
            # 返回列表值
            return data1
        else:
            raise StopIteration # 主动抛出异常



if __name__ == '__main__':
    mylist=MyList()
    mylist.addIteam("张三")
    mylist.addIteam("李四")
    mylist.addIteam("王五")

    result=isinstance(mylist,Iterable)
    print(result)

    for value in mylist:
        print(value)

