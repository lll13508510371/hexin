'''
ctrl + /
'''
'''
ctrl + / 注释
ctrl + alt + l 格式化
标识符 （变量）：不能数字开头
Python中一切皆对象
<>为一个对象 such as <class 'int'> class：类  int:类别类型
+ - * / // % **
""就近原则匹配,所以"" '' 
字符串数据'str'不能和其它数据一起连用，要强制改为'str'才能用
'''
ddd = "sdfw"
my_name = '小龙'
print(my_name, ddd)

# 手动输入
your_name = input('请输入您的名字：')
print(your_name)

one = 1
a = 1.2
print(type(one))

print(int(a))
print(float(one))

print(10 // 3)  # 取整
print(10 % 3)  # 取余
print(10 ** 3)  # 幂

b = 3 ** 3 + 7 ** 3 + 1 ** 3
print(b)

three = 3
ten = 10
ten += three
print(ten)

ten -= three
print(ten)

num = 371

g = num % 10
print(g)
k = int(num / 10 % 10)
print(k)
x = num // 100
print(x)
if num == g ** 3 + k ** 3 + x ** 3:
    print('是水仙花数')

name = '张三'
age = 19
nickname = '法外狂徒'
print('姓名：' + name + '，年龄：' + str(age) + '，外号：' + nickname)
# f 直接带字符串里面插入变量 山禾推荐
print(f'姓名：{name},年龄:{age},外号{nickname}')

# {} 字符串里面有多少个{}占位符，format当中就需要几个变量
print('姓名：{},年龄:{},外号:{}'.format(name, age, nickname))

# %s字符串占位符
print('姓名：%s,年龄:%s,外号:%s' % (name, age, nickname))
print('姓名：%s' % name)

print('\n姓名：%s\n' % name)

s = '\n # hello world ! # \n'
print(s)
print(type(s))

# strip 去除两端
print(s.strip())
print(type(s.strip()))
# 只要还是字符串，就可以继续用字符串的方法
print(s.strip().strip('#'))  # strip只针对字符串前后两端
print(s.strip().strip('#').strip())

# replace替换
print(s.replace('#', '?'))
print(s.replace('#', '?').strip().strip('?'))

# split默认以空格分割，返回列表数据
print(s.split())

print(type(s.split()))
# 也可以指定符号
print(s.split('#'))

# Python区分中英文 中英文逗号是不一样的
# join列表操作
w = '张三，李四，王五'
print(w.split('，'))
print(''.join(w.split('，')))
print(' '.join(w.split('，')))
print('?'.join(w.split('，')))

# \\转义字符
print('hello \\n world')

# 常见的特殊字符 / \(反斜杠) ? [] {}

# r 在字符串前面加上，表示原生字符串
print(r'hello \n world')

na = input('请输入你的名字：')
print(f'你好,{na}')

result = True  # T F 布尔类型关键字
print(type(result))
print(0 < -10)  # 比较运算符默认把结果转换成布尔类型

'''
布尔类型需要注意隐式转化transform
例如 0 < 5 就是你看不到它的过程,计算机处理了给你返回T F,即为隐式转化
'''
if 0:
    print(1)
else:
    print(0)

if"":
    print(1)
else:
    print(0)

# None 空值类型,无类型的结果
result = None
print(type(result))
print(1 is True)