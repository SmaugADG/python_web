import re

# 使用match()方法进行匹配操作，匹配成功返回Match对象，匹配失败None
# 需要三个参数
# 1)正则表达式
# 2）要匹配的源字符串
# 3） 匹配模式
result=re.match("smaug","smaugADG")

if result:
    #如果上一步匹配到数据，使用group方法来提取数据
    print(result.group())
'''search'''
# re.search()函数会在字符串内查找模式匹配，只要找到第一个匹配然后返回，如果没有返回None
# 与match()的区别：match只从字符串0位置开始匹配，如果不匹配返回None
# search（）会扫描整个字符串，成功就返回字符串，不成功返回None
result=re.search(r"\d+","阅读次数 9999")
print(result.group())

'''findall'''
# findall 查找所有，返回列表
# findall 遍历匹配，查找到的字符串全部一列表的形式返回
result=re.findall(r"\d+","阅读次数:9999次,转发次数:883次,评论次数:3次")
print(result)

'''sub'''
# sub替换字符串中每一个匹配的子串后返回替换后的字符串
result=re.sub(r"\d+","1000","阅读次数:9999次,转发次数:883次,评论次数:3次")
print(result)

'''split'''
# 根据匹配进行切割字符串，并返回一个列表
# 按照格式来分割字符串
result=re.split(r":| ","info:xiaoZhang 33 shandong")
print(result)

'''r的作用'''

# 正则表达式总使用到\的时候，在Python中需要使用转义字符，即需要写成\\，
# 为避免造成混乱，可在正则表达式前面加r
# r"\d" 和 "\\d"  等价

