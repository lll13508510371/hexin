"""
try:  --> 异常捕获的关键字, 具有代码块
    可能发生异常的代码
    在此代码块中的代码不管有多少, 只要在执行的过程中发生了异常, 就会被捕获到

except:
    有代码块
    被捕获到的异常就会交给except做处理

"""
try:
    f = open('test.txt', mode='r')

except:
    f = open('test.txt', mode='w')

"""
异常会影响代码的执行, 一旦在出现异常的时候, 代码执行就会中断, 后续的代码就不会执行了

咱们可以用异常捕获, 针对异常进行处理, 处理后的异常不会影响后续代码的执行
"""
