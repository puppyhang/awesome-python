'''
Python定义类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
定义类的方法包括构造器的时候会传入一个self,这个self就是java中的this

自定义构造器，但是python不推荐这种方式，可能是推荐生成器吧
def __init__(self, argAge, agBirthday):
        print("执行构造器")
        print("self is : ", self)
        print("self class is : ", self.__class__)
        self.age = argAge
        self.birthday = agBirthday
'''


class HelloPythonClass:
    age = 23
    birthday = "1994/07/08"

    def __init__(self):
        print("默认的构造器")

    def getBirthday(self): return self.birthday

    def getAge(self): return self.age
