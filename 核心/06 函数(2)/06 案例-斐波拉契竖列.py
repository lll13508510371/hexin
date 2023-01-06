"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，因数学家莱昂纳多·斐波那契（Leonardo Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，

指的是这样一个数列：1、1、2、3、5、8、13、21、34、……无穷大

在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
"""


def fib(n):  # 给一个数字, 就求斐波拉契数列中第 n 个数字
    if n == 1 or n == 2:  # 递归出口
        return 1
    print(n)
    return fib(n - 1) + fib(n - 2)


print(fib(2))
print(fib(3))
print(fib(6))
print(fib(9))
print(fib(10))
print(fib(20))
print(fib(30))
