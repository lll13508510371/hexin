"""
学生信息管理系统, 自己跟着案例录播实现一遍
"""
"""请在下方实现"""
'''
1.新增
2.显示所有信息
3.查询
4.修改
5.删除
6.退出
'''
import json
import pprint

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""

with open('1.json', mode='r', encoding='utf-8') as f:
    student_str = f.read()
    # print(student_str)

student_list = json.loads(student_str)

# action = input('请选择你想要进行的操作: ')
# while True 应该表示一直为真 设置死循环
while True:
    print(str_info)
    action = input('请选择你想要进行的操作: ')
    # 1.新增
    if action == '1':
        name = input('请输入你的姓名: ')
        chinese = int(input('请输入你的语文成绩: '))
        math = int(input('请输入你的数学成绩: '))
        english = int(input('请输入你的英语成绩: '))
        total = chinese + math + english
        dict1 = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        # 用字典装入一个学生的数据  列表装学生们数据
        student_list.append(dict1)
        # print(student_list)


    # 2.显示所有信息
    elif action == '2':
        print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
        for stu in student_list:
            print(f'{stu["name"]}\t\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

    # 3.查询
    elif action == '3':
        name = input('请输入你的名字: ')

        for stu in student_list:
            if name == stu['name']:
                print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                break
        else:
            print('名字输入错误')

    # 4.修改
    elif action == '4':
        name = input('请输入你的名字: ')
        for stu in student_list:
            if name == stu['name']:
                name = input('请重新输入你的姓名: ')
                chinese = input('请重新输入你的语文成绩: ')
                math = input('请重新输入你的数学成绩: ')
                english = input('请重新输入你的英语成绩: ')
                if name:
                    stu['name'] = name
                if chinese:
                    stu['chinese'] = int(chinese)
                if math:
                    stu['math'] = int(math)
                if english:
                    stu['english'] = int(english)

                stu['total'] = stu['chinese'] + stu['math'] + stu['english']

                print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                print('修改成功')
                break
        else:
            print('无当前学生')

    # 5.删除
    elif action == '5':
        name = input('请输入你的名字: ')
        for stu in student_list:
            if name == stu['name']:
                student_list.remove(stu)
                print('删除成功')
                break
        else:
            print('无当前学生')

    # 6.退出系统并修改文件
    elif action == '0':
        with open('1.json', mode='w', encoding='utf-8') as f:
            students = json.dumps(student_list, ensure_ascii=False)
            f.write(students)
        print('已退出系统')
        break
