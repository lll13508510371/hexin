import random

print(random.randint(1, 4))

"""
1. 会在当前导入的py同级目录中查找有没有同名的模块, 如果有, 就优先导入同级目录下同名的模块
2. 在解释器中查找模块
3. 如果解释器没有想要导入的模块, 报错--> ModuleNotFoundError: No module named 'pygame'
"""

# 此后咱们在写代码的时候, 文件名千万不要用模块名字进行命名
