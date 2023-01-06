import json
import pprint


def insert_student():
    """录入学生信息, 并且返回"""
    name = input('请输入学生姓名:')
    chinese = input('请输入学生的语文成绩:')
    math = input('请输入学生的数学成绩:')
    english = input('请输入学生的英语成绩:')

    stu = {}
    if name:  # 字符串的布尔值--> 非空即真
        stu['name'] = name
    if chinese:
        stu['chinese'] = int(chinese)
    if math:
        stu['math'] = int(math)
    if english:
        stu['english'] = int(english)

    stu['total'] = stu['chinese'] + stu['math'] + stu['english']
    return stu  # --> dict


# 查找, 修改, 删除都需要找学生的这个代码逻辑
def search_student(stu_name, student_s):
    """
    查找学生, 找到了就返回学生的字典对象
    :param stu_name: 学生的名字
    :param student_s: 学生信息列表
    :return: 学生的字典对象  --> None
    """
    for stu in student_s:
        if stu_name == stu['name']:
            return stu


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
        stu = insert_student()
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
        stu = search_student(name, students)

        if stu:
            print('姓名\t语文\t数学\t英语\t总分')
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
            print('######## --- 查询成功 --- ########')

        # 如果走else的逻辑, 那么代表没有找到这个学生
        else:
            print('该学生不存在, 请检查名字是否输入正确!')


    elif action == '4':
        print('4. 修改学生信息')
        # 指定姓名查询学生信息
        name = input('请输入您要修改的学生姓名:')
        stu = search_student(name, students)

        if stu:
            # 找到了就修改
            new_stu = insert_student()
            stu.update(new_stu)
            print('######## --- 修改成功 --- ########')

        # 如果走else的逻辑, 那么代表没有找到这个学生
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '5':
        print('5. 删除学生信息')
        # 指定姓名查询学生信息
        name = input('请输入您要删除的学生姓名:')
        stu = search_student(name, students)

        if stu:
            students.remove(stu)
            print('######## --- 删除成功 --- ########')

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
