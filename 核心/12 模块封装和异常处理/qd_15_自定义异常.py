# 需求：密码长度不足，则报异常
# （用户输入密码，如果输入的长度不足3位，则报错，即抛出自定义异常，并捕获该异常）。


def main():
    try:
        password = input('请输入密码:')
        if len(password) < 3:
            # raise 主动抛出异常, 通过 Exception 自定义异常信息
            raise Exception(f'您输入的密码长度是-{len(password)}- , 密码不能少于3位数')
    except Exception as e:
        print(e)
    else:
        print('没有异常, 密码输入完成!')


main()
