import copy
# 切片拷贝 是一种浅拷贝，副本对象和源对象指向同一个空闲
# A =[1,2]
# B =[3,4]
# C =(A,B)
#
# # D = copy.copy(C)
# D=C[:]
# print("C=",C,"D=",D)
# print("C=%x,D=%x"%(id(C),id(D)))
# print("D[0]=%x,C[0]=%x,A=%x"%(id(D[0]),id(C[0]),id(A)))


# 字典拷贝
dict1={"age":[1,2]}
# 字典拷贝 是用过对象自带的copy()方法拷贝的
dict2=dict1.copy()

print(dict1,dict2)

print("dict1=%x,dict2=%x"%(id(dict1),id(dict2)))

# 修改字典dict1值
dict1["age"][1]=100
dict1["age"].append(88)

print(dict1,dict2)
