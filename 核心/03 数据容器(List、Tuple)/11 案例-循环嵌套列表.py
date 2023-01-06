"""
随机取10次 1 到 10 类与继承 范围内的整数数据, 添加到列表
"""

# 模块  内置模块<Python解释器的时候自带的模块>--> 不需要安装, 直接使用
#       第三方模块<受官方认证的其他程序员写的模块> 终端中使用 pip install 模块名

# 随机数模块
# 模块的使用   import + 模块名
import random  # 内置模块, 随机数模块

# print(random.randint(1, 3))  # 1 是起始值, 3 是结束值 闭区间

list1 = []
for i in range(10):
    list1.append(random.randint(1, 10))

print(list1)