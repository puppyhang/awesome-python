'''
Python的异常处理
'''
import sys
# try:
#     print(10/0)
# except (RuntimeError, TypeError, NameError, ZeroDivisionError):
#     print("发生了除0异常")
#     # pass 什么都不做


# try:
#     print(10/0)
# except ZeroDivisionError as error:
#     print("发生了除0异常", format(error))
# except RuntimeError as error:
#     print("发生了运行时异常", format(error))
# except Exception as error:
#     print("Unexpected error:", format(error))
# else:
#     print("将在try块没有发生任何异常情况下调用,不同于Java的finally子句")

# 抛出异常
def test_ex(arg):
    if (arg == 0):
        raise NameError("传入的参数值不正确")


try:
    test_ex(0)
except NameError as e:
    print("发生了异常", format(e))
finally:
    print("无论发生不发生异常，这里都会执行，Python也有finally子句哦")

sys.exit(0)
