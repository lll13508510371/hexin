# 导入模块
# import wo_module
# from wo_module import sum_num
# from wo_module import *
from wo_module import sum_num as gg

# 调用功能
# wo_module.sum_num(12, 23)
gg(22, 23)

# 导入模块后, 模块的查找顺序
"""
1. 会在当前导入的py同级目录中查找有没有同名的模块, 如果有, 就优先导入同级目录下同名的模块
2. 在解释器中查找模块
3. 如果解释器没有想要导入的模块, 报错--> ModuleNotFoundError: No module named 'pygame'
"""
