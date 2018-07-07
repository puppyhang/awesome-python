'''
使用Python的sys模块
'''
import sys

for arg in sys.argv:
    print(arg)

print("Python的路径为:", sys.path)

sys.exit(0)
