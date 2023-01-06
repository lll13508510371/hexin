# lambda 两个数字比大小，谁大返回谁
# 无命名函数对象lambda

fn1 = lambda a, b: a if a > b else b
print(fn1(89, 97))
print(fn1(100, 99))

# lambda 只能写简单的函数逻辑,最难的就像上面的三元表达式

