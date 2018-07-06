'''
命令行参数处理demo程序
'''
# -*-conding:utf-8-*-
import sys
import getopt

# 打印所有参数
'''
for order in range(1, len(sys.argv)):
    print("参数{", order, "}=", sys.argv[order])
'''

# 区分参数和命令行选项打印
'''
hi:o:
"h"是一个开关选项；"i:"和"o:"则表示后面应该带一个参数。这个参数主要用于分析脚本后面带的参数的格式

opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数

[] 中为长选项参数，-i 和 -o都是短选项参数
'''
opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["version", "file="])
for opt, value in opts:
    print("选项", opt, "=", value)
