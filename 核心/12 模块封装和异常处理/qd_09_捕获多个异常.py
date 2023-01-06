

try:
    print(10 / 0)
    print(num)
except (NameError, ZeroDivisionError, ):  # 捕获 NameError ZeroDivisionError异常
    print('有错误')
