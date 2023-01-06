name = '张三'
age = 18
nickname = '法外狂徒'

# 姓名: 张三, 年龄: 18, 外号: 法外狂徒
print('姓名: ' + name + ', 年龄: ' + str(age) + ', 外号: ' + nickname)

print('--------------------- f表达式 -------------------------')
# # f 直接带字符串,里面插入变量
print(f'姓名: {name}, 年龄: {age}, 外号: {nickname}')
print(f'姓名: {name}')

print('---------------------format方法-------------------------')
# 字符串中有几个 {} 占位符, 那么 format 方法里面就需要有几个变量
print('姓名: {}, 年龄: {}, 外号: {}'.format(name, age, nickname))


print('---------------------%占位符/格式化操作符-------------------------')
print('姓名: %s, 年龄: %s, 外号: %s' % (name, age, nickname))
print('姓名: %s' % name)
