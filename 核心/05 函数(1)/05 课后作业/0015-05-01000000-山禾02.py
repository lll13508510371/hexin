"""
定义一个函数, 实现登录的功能

    要求: 现在有用户名(user_name)  密码(password)  两个变量
        如果用户输入正确的用户名和密码, 提示 "登录成功"
        如果用户输入错误的用户名和密码, 提示 "用户名或密码输入错误"
        如果用户输入三次错误, 提示 "您输入错误的次数过多,登录异常", 退出函数运行
        
    提示: 循环  +   逻辑判断
"""

user_name = 'shanhe'
password = '123456'

"""请在下方实现代码"""

'''
无参
'''


def fuc1():
    time = 0

    for i in range(3):
        user = input('请输入你的名字: ')
        pw = input('请输入你的密码: ')
        if user == user_name and pw == password:
            return "登录成功"

        else:
            print("用户名或密码输入错误")

        time += 1

        if time == 3:
            return "您输入错误的次数过多,登录异常"


fuc1()
print(fuc1())

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!
山禾上课讲过print(print()),当时懂了但没明白用意,这里明白了
如果是这种形式
return print ("登录成功")
return print ("您输入错误的次数过多,登录异常")
print(fun1())得到的结果就是
"登录成功"
None
"您输入错误的次数过多,登录异常"
None

因为其形式就是print(print ("登录成功"))
             print(print ("您输入错误的次数过多,登录异常"))

内部是打印字符串,外部是打印函数
函数想要在外部打印结果只能靠return, 但ctrl看print()可以看到print()并没用return,
打印一个没有return的函数得到的值就是None
'''
print(print())
