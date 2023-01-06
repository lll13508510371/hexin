try:
    print(10 / 0)
    print(num)
except Exception as e:  # 把出现的异常取了一个别名 Exception是所有程序异常类的父类
    print('有错误')
    print(Exception)
    print(e)
