# 需求: 使用 math 模块进行开平方运算
# 常见的内置模块, 在高级开发课程会学习 logging<日志>

# 方法1: 导入-->import 模块名; 调用-->模块名.功能
# import math
# print(math.sqrt(9))

# 方法2: 导入-->from 模块名 import 功能; 调用-->功能直接调用
# from math import sqrt
# print(sqrt(9))

# 方式3: 导入-->from 模块名 import * <*代表所有功能>; 调用-->功能直接调用
from math import *
print(sqrt(9))


# import math.sqrt
# import concurrent.futures
