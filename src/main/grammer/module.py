'''
测试Python的模块功能
'''
# 这种导入的方法会把被导入的模块的名称放在当前的字符表中
import loop

# 这种导入的方法不会把被导入的模块的名称放在当前的字符表中
from function import testFunc

print("3 * 5 = ", testFunc(3, 5))

# print("1-10的和为:",loop.while_test(10))
