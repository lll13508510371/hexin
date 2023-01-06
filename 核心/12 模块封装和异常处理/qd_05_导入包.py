# 导入包
# 方式1:  import 包名.模块名
# 方式2:  from 包名.模块名 import 功能
# import mypackegs.my_module1
from 核心.mypackegs.my_module1 import info_print1

# 调用
# 调用方式1: 包名.模块名.函数名()
# 调用方式2: <功能名>函数名()
# mypackegs.my_module1.info_print1()
# info_print1()

from 核心.mypackegs.my_module2 import info_print2

info_print2()

from selenium.webdriver.common.by import By
