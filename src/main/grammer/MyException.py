# 自定义的异常


class MyException(Exception):

    def __init__(self, message):
        self.value = message

    def __str__(self):
        return repr(self.value)


try:
    raise MyException("这是我自己定义的异常")
except MyException as e:
    print("捕获到自定义的异常", format(e))
