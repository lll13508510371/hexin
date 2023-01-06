# 1. 无参数
fn1 = lambda: 200
print(fn1())

# 1. 一个参数
fn1 = lambda x: x
print(fn1('hello world'))

# 默认参数
fn1 = lambda x, a, b=100: x + a + b
print(fn1(1, 2))

# 不定长参数
fn1 = lambda *args: args
print(fn1(1, 2, 3, 4, 5, 6))
print(fn1(1, 2, 3, 4, 5, 6, 7, 8))

# 不定长参数
fn1 = lambda **kwargs: kwargs
print(fn1(a=1, b=2))
