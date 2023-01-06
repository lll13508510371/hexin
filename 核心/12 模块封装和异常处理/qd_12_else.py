

try:
    print('aaaaaa')
    print('bbbbbb')
except Exception as e:  # 把出现的异常取了一个别名
    print('有错误')
    print(e)
else:
    print('我是else, try代码块当没有异常的时候, 我会被执行')


