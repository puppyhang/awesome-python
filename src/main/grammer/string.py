'''
string测试
'''

import sys

str = "Hello world !"

# 1:使用for循环测试根据下表访问字符串中的字符,python中的字符串实际上就是相当于一个字符数组
'''
for index in range(len(str)):
    print(index,str[index])
'''
#打印[1,5)不包含第五个字符串
#print(str[1:5])

#从后面开始打印
#print(str[-4:-3])

'''
for c in str:
    print(c)
'''

#--------------------------------------------------------------------------------------------

# 2:python字符串转义，如果你需要在字符串中使用其他特殊字符的话比如换行回车时候，应该用一个反斜杠
#   \\表示一个\，如果单独用一个反斜杠，那么后面的内容都不会打印

'''
str_1 = "te\\fsd \n\r"
print(str_1)

str_2 = '\'hello world \''
print(str_2)

str_2 = '\"hello world \"'
print(str_2)
'''

#---------------------------------------------------------------------------------------------

# 3:python字符串运算 + [] [:] in not-in r/R % *

'''
str_3 = 'hello world'
print(str_3 + ' added character !')
print("第一个字符串",str_3[0])
print("第1-5个字符",str_3[1:6])
print("h在字符串中?",'h' in str_3)
print("A不在字符串中?",'A' in str_3)
print (r'\n\r\t\b')
print (R'\n')
print("防守打法"*2)
'''

# 4:python多行字符串"""
# str_4 = """this is a 
# multi lines words ! hh
# jj kk 
# ll l l j  fasd 
# """
# html = """
# <DOCTYPE html>
# <html>
#     <head>
#         <title>这是一个html</title>
#     </head>
#     <body>
#         ....
#     </body>
# </html>
# """

# sql = """"
# use test;
# drop table is exists some_table;
# create table some_table(....);
# """
# print(str_4)

# 5:python格式化打印字符串
# print("格式化打印:%s,%d,体重:%f"%('我今年',23,65.00999))

# 6:字符串常用函数

#这个函数需要注意的是它不仅仅把首字母转换成大写，他也会
#把其他字母转换为小写
#print("hello world".capitalize())
#print("123 HELLO WORLD".capitalize())
#print("hELLO WORLD".capitalize())

#返回一个指定的字符串长度,width并居中字符串，不足的部分用fillchar填充
#如果宽度小于字符串的长度就直接返回字符串本身
#fillchar 只能是单个字符
#fillchar 默认是空格
#width 小于字符串长度时候不会截断，会全部返回
#print("test".center(16,"*"))
