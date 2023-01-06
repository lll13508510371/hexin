import time

from selenium import webdriver  # 导入浏览器对象  pip install selenium

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

input()  # 阻塞浏览器关闭
driver.quit()

time.sleep(30)

"""
Python代码报错具有异常的传递性, 原因是因为在代码编辑汇总会有模块的引用, 
模块与模块之间可能也会有引用关系, 如果引用关系出错了, 就会引发一连串的报错信息

1. 找自己编辑的代码哪里出错了 ---> 绝大多数情况下是从自己找原因
2. 在源码中找错误 --> 修改源码 --> 不建议
    有基于源码做二次开发  
"""

