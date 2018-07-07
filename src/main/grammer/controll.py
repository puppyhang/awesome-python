'''
Python的顺序控制结构

就只有一个条件控制结构

'''
import sys


def test_if(opts):
    for item in opts:
        if(item == 'skip'):
            print("即将执行skip操作")
            continue
        elif(item == "stop"):
            print("即将执行stop操作")
            break
        print(item)
    else:
        pass


opts = {"ternence", "charse", "linda", "skip", "mahana", "kangkang", "stop"}

test_if(opts)
