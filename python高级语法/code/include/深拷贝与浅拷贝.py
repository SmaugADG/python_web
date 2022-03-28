'''
1.浅拷贝：引用拷贝，不产生新的空间，如果拷贝的是对象，原对象和拷贝对象都指向
同一块内存空间，只拷贝父对象，不会拷贝对象的内部子对象
2.深拷贝：会产生新的空间。如果拷贝的是对象，源对象与拷贝对象指向不同的内存空间
会拷贝对象及其子对象
3.对于简单可变类型，浅拷贝和深拷贝都会产生新空间，保证数据的独立性
'''
import copy
# 浅拷贝
#
# list1=[1,2]
# print("list1内存地址%x"%id(list1))
#
# # 正对可变类型，浅拷贝会创建新空间
# list2=copy.copy(list1)
#
# # 癌变list2添加新元素
# list2.append(88)
# print("list2内存地址%x"%id(list2))
#
# print(list2)
# print(list1)

# 深拷贝
# list1=[1,2]
# print("list1内存地址%x"%id(list1))
#
# # 正对可变类型，浅拷贝会创建新空间
# list2=copy.deepcopy(list1)
#
# # 癌变list2添加新元素
# list2.append(88)
# print("list2内存地址%x"%id(list2))
#
# print(list2)
# print(list1)

'''复杂可变类型的深浅拷贝'''
# 复杂类型的浅拷贝，实际就是引用拷贝，无法保持独立性
# A =[1,2]
# B =[3,4]
# C =[A,B]
# print("A的地址:%x"%id(A))
# print("B的地址:%x"%id(B))
# print("C[0]的地址:%x"%id(C[0]))
# print("C[1]的地址:%x"%id(C[1]))
#
# D = copy.copy(C)
# print("A的地址:%x"%id(A))
# print("C[0]的地址:%x"%id(C[0]))
# print("D[0]的地址:%x"%id(D[0]))


# 复杂类型的深拷贝，会产生新的空间
# A =[1,2]
# B =[3,4]
# C =[A,B]
# print("A的地址:%x"%id(A))
# print("B的地址:%x"%id(B))
# print("C[0]的地址:%x"%id(C[0]))
# print("C[1]的地址:%x"%id(C[1]))
#
# D = copy.deepcopy(C)
# print("A的地址:%x"%id(A))
# print("C[0]的地址:%x"%id(C[0]))
# print("D[0]的地址:%x"%id(D[0]))


'''不可变类型-简单类型的深浅拷贝'''
# 不可变类型，不论是深拷贝还是浅拷贝，都不会开辟新的空间，而是直接引用

# 不可变类型 浅拷贝
# 定义元祖
# a=(1,2,3)
# a1=copy.copy(a)
#
# print(a,a1)
#
# print("a:%x,a1:%x"%(id(a),id(a1)))

# 不可变类型 深拷贝
# a=(1,2,3)
#
# a1=copy.deepcopy(a)
#
# print(a,a1)
#
# print("a:%x,a1:%x"%(id(a),id(a1)))


# 不可变类型-嵌套类型

# 浅拷贝
# A =[1,2]
# B =[3,4]
# C =(A,B)
#
# D = copy.copy(C)
#
# print("C=",C,"D=",D)
# print("C=%x,D=%x"%(id(C),id(D)))
# print("D[0]=%x,C[0]=%x,A=%x"%(id(D[0]),id(C[0]),id(A)))

# 深拷贝
A =[1,2]
B =[3,4]
C =(A,B)

D = copy.deepcopy(C)

print("C=",C,"D=",D)
print("C=%x,D=%x"%(id(C),id(D)))
print("D[0]=%x,C[0]=%x,A=%x"%(id(D[0]),id(C[0]),id(A)))