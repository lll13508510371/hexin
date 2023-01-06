"""布尔类型"""
# True/False 是布尔类型的关键字
# 真/假
# 对/错
result = True
result2 = False

print(result2)
print(type(result2))

# 比较运算符, 在默认的情况下会把结果转化成布尔类型
# 判断逻辑, 也会把判断的条件转化成布尔类型
print(0 > 5)
print(5 > 0)

"""布尔类型需要注意隐式转换"""
print('--------------------------------')
# 数值类型 除了 0 之外布尔值全部是 True, 非0即真
print(bool(1))
print(bool(2))
print(bool(10000))
print(bool(-10000))
print(bool(0))

print('--------------------------------')
# 字符串类型, 除了 空字符串 布尔值全部是 True, 非空即真
print(bool('fhewuihfiu'))
print(bool('123'))
print(bool('你好'))
print(bool('       '))
print(bool(''))

# 隐式转化
if 0 > 5:
    print('yes')

# None  # Python空值类型, 无类型的结果
result5 = None
print(result5)
print(type(result5))

print(bool('fhewuihfiu'))