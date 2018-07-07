'''
Python的循环结构

Python 中的循环结构的 break continue 和Java中的关键字语义一样，
而且Python中特有的else语句在break和continue执行之后不会执行

pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例
'''

# while 循环的结构


def while_test(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    else:
        print("计算结束 n=", n)
    return sum

# 测试for循环结构


def for_test(list):
    for var in list:
        print(var)
    else:
        print("列表为空")

# 测试range函数,range(x)相当于 0-x
# 还而已写成range(x,y)表示从x-y


def range_test():
    for index in range(5):
        print("index:", index)
    else:
        print("循环结束")


def range_step_test(step):
    for index in range(0, 10, step):
        print("index:", index)
    else:
        print("迭代结束")

# 结合range和len函数遍历一个集合


def iterate_collection(collections):
    for index in range(len(collections)):
        print(index, ":", collections[index])


def iterate_dict(dict):
    for item in dict:
        print(dict[item])
    else:
        pass

# print("1-10的和为:", while_test(10))

# languages = ["C", "C++", "Perl", "Python"]
# for_test(languages)

# languages = ["C", "C++", "Perl", "Python"]
# iterate_collection(languages)


# people = {"ternence": {"age": 23, "gender": "男"},
#           "linda": {"age": 22, "gender": "女"}}
# iterate_dict(people)

# range_test()
# range_step_test(2)
