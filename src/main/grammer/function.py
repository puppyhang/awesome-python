'''
Python函数测试代码
'''


def testFunc(width, height):
    return width * height


# 区分是执行文件还是被其他模块调用
if __name__ == "__main__":
    print("执行main方法")
else:
    print(__name__)

# 这行代码没有被区分是执行文件还是被调用，所以如果被其他模块引入的时候会执行
# print("5 * 5 =",testFunc(5, 5))
