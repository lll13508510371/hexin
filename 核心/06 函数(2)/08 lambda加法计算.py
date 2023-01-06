# 需求：计算任意两个数字的累加和

def add(a, b):
    return a + b
'''
lambada只是一个函数对象,需要命名一个函数对象来调用它,如下
'''

# print(add(2, 4))
fn1 = lambda a, b: a + b
print(fn1(3, 4))
