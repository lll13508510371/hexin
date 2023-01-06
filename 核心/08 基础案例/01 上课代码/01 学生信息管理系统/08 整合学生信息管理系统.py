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

with open('students.json', mode='r', encoding='utf-8') as f:
    student_str = f.read()

students = json.loads(student_str)  # ---> 学生信息列表

while True:
    # 1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
    print(str_info)

    # 2. 用户用数字选择不同的功能(input)
    action = input('请输入您要执行的功能:')  # --> str

    # 3. 根据功能选择，执行不同的功能(多条件判断)
    if action == '1':
        print('1. 新建学生信息')
        name = input('请输入学生姓名:')
        chinese = int(input('请输入学生的语文成绩:'))
        math = int(input('请输入学生的数学成绩:'))
        english = int(input('请输入学生的英语成绩:'))
        total = chinese + math + english

        # 新的学生
        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        students.append(stu)
        print('######## --- 新建成功 --- ########')

    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t英语\t总分')

        for stu in students:
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

    elif action == '3':
        print('3. 查询学生信息')
        # 指定姓名查询学生信息
        name = input('请输入您要查询的学生姓名:')

        # 先遍历所有的学生, 一一比对
        for stu in students:
            if name == stu['name']:  # 排除同名的情况
                print('姓名\t语文\t数学\t英语\t总分')
                print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                print('######## --- 查询成功 --- ########')
                break  # 因为没有同名的学生, 所有找到了就可以结束当前的循环任务了

        # 如果走else的逻辑, 那么代表没有找到这个学生
        else:
            print('该学生不存在, 请检查名字是否输入正确!')


    elif action == '4':
        print('4. 修改学生信息')
        # 指定姓名查询学生信息
        name = input('请输入您要修改的学生姓名:')

        # 先遍历所有的学生, 一一比对
        for stu in students:
            if name == stu['name']:  # 排除同名的情况
                print('(回车则会使用原来的数据)')
                name = input('请重新输入学生姓名:')
                chinese = input('请重新输入学生的语文成绩:')
                math = input('请重新输入学生的数学成绩:')
                english = input('请重新输入学生的英语成绩:')
                # total = chinese + math + english

                if name:  # 字符串的布尔值--> 非空即真
                    stu['name'] = name
                if chinese:
                    stu['chinese'] = int(chinese)
                if math:
                    stu['math'] = int(math)
                if english:
                    stu['english'] = int(english)

                stu['total'] = stu['chinese'] + stu['math'] + stu['english']

                print('######## --- 修改成功 --- ########')
                break  # 因为没有同名的学生, 所有找到了就可以结束当前的循环任务了

        # 如果走else的逻辑, 那么代表没有找到这个学生
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '5':
        print('5. 删除学生信息')
        # 指定姓名查询学生信息
        name = input('请输入您要删除的学生姓名:')

        # 先遍历所有的学生, 一一比对
        for stu in students:
            if name == stu['name']:  # 排除同名的情况
                # pop 找字典的索引 remove
                students.remove(stu)
                print('######## --- 删除成功 --- ########')
                break  # 因为没有同名的学生, 所以找到了就可以结束当前的循环任务了

        # 如果走else的逻辑, 那么代表没有找到这个学生
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            student_str = json.dumps(students, ensure_ascii=False)
            f.write(student_str)
            pprint.pprint(students)
        break

    else:
        print('请输入正确的选择!')
