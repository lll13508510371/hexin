"""逻辑运算符"""
"""
    and --> 条件1 and 条件2 两个条件都成立,返回True,否则返回False
    or  --> 条件1 or  条件2 两个条件中的一个条件成立,就返回True
    not --> not 条件, 条件会直接逆转
"""

print(5>4 and 3>0)
print(5<4 and 3>0)
print(5>4 and 3<0)
print('-----------------------')
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print('-----------------------')
print(not True)
print(not False)
print('-----------------------')
print(1 is 1)
print(True is 1)
print(1 is True)
print(int(True) is 1)
print(1 is int(True))