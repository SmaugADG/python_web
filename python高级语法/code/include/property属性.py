# @property 的作用是将对象的某个方法封装为一个属性，
# 实例对象只需要像调用属性一样调用方法
# class Foo:
#     def __init__(self):
#         self.num=100
#     @property
#     def prop(self):
#         return self.num
#
# f=Foo()
# print(f.prop)

'''property属性的两种方法'''
# 经典类和新式类：继承自object的类为新式类，Python3默认所有类都是新式类
# 经典类
# class Goods:
#     @property
#     def price(self):
#         return "laowang"
# obj=Goods()
# result=obj.price  # 自动执行 @property修饰的price方法，并获取返回值
# print(result)

# 新式类
class Goods:
    @property
    def price(self):
        print("@property")
    @price.setter
    def price(self,value):
        print("@price.setter")
    @price.deleter
    def price(self):
        print("@price.delete")


obj=Goods()
# 自动执行@property修饰的price方法，并获取方法的返回值
obj.price
# 自动执行@price.setter修饰price方法，将123赋值给price
obj.price=123
# 自动执行@price.delete修饰price方法
del obj.price
