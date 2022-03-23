class Fibonacci():
    def __init__(self,num):
        # 构造方法，保存奴骂道类中
        self.num=num
        # 定义数列前两个值
        self.a=1
        self.b=1
        # 记录当前位置
        self.current_index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_index<self.num:
            result=self.a

            self.a,self.b=self.b,self.a+self.b

            self.current_index+=1

            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    fib_iterator=Fibonacci(5)

    # for value in fib_iterator:
    #     print(value)

    # 可以使用list或者tuple等接收
    li=list(Fibonacci(5))
    print(li)

    tu=tuple(Fibonacci(5))
    print(tu)
