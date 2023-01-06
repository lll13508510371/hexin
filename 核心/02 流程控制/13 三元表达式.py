a = int(input("请输入数字1："))
b = int(input("请输入数字2："))
max_number = None

# if a > b:
#     max_number = a
# else:
#     max_number = b
#
# print(max_number)

"""三元表达式"""
# 三元表达式  if ... else 的简写
# 结果1 if 条件 else 结果2
# 满足条件返回左边的结果1, 不满足条件返回右边的结果2
# max_number = a if a > b else b
# print(max_number)

result = a if a < b else b
print(result)

c = 5
d = 10
result1 = c if c > d else d
print(result1)
