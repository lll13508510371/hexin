import json
import pprint

'''
系统面向学生对象的封装
'''


class Student:
    """学生信息类"""

    def __init__(self, name, chinese, math, english):
        """
        :param name: 姓名
        :param chinese: 语文成绩
        :param math:数学成绩
        :param english: 英语成绩
        """
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english  # 总分


class StudentManager:
    """学生信息系统类"""

    def __init__(self):
        self.student_list = None  # 存储学员数据 -- 列表

    # 1.程序入口函数, 整个系统的逻辑都在这个主函数中调用
    def run(self):
        # 1. 加载文件里面的学员数据
        self.load_student()

        while True:
            # 2. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
            self.show_menu()

            # 3. 根据功能选择，执行不同的功能(多条件判断)
            action = input('请输入您要执行的操作:')

            if action == '1':
                print('1. 新建学生信息')
                self.add_student()

            elif action == '2':
                print('2. 显示全部信息')
                self.show_student()

            elif action == '3':
                print('3. 查询学生信息')
                self.search_student()

            elif action == '4':
                print('4. 修改学生信息')
                self.modify_student()

            elif action == '5':
                print('5. 删除学生信息')
                self.del_student()

            elif action == '0':
                print('0. 退出系统')
                self.save_student()
                break

            else:
                print('请输入正确的选择!')

    def del_student(self):
        """删除学生信息的方法"""
        del_name = input('请输入您要删除学生的姓名:')
        for stu in self.student_list:
            if del_name == stu.name:
                self.student_list.remove(stu)
                print('######## --- 删除成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def modify_student(self):
        """修改学生信息的方法"""
        modify_name = input('请输入您要修改学生的姓名:')
        for stu in self.student_list:
            if modify_name == stu.name:
                print('(回车则会使用原来的数据)')
                name = input('请重新输入学生姓名:')
                chinese = input('请重新输入学生的语文成绩:')
                math = input('请重新输入学生的数学成绩:')
                english = input('请重新输入学生的英语成绩:')

                if name:
                    stu.name = name
                if chinese:
                    stu.chinese = int(chinese)
                if math:
                    stu.math = int(math)
                if english:
                    stu.english = int(english)
                stu.total = stu.chinese + stu.math + stu.english
                print('######## --- 修改成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def search_student(self):
        """查询学生信息的方法"""
        # 1. 用户输入目标学员姓名
        search_name = input('请输入您要查询学生的姓名:')

        # # 2. 遍历列表。如果学员存在打印学员信息，否则提示学员不存在
        for stu in self.student_list:
            if search_name == stu.name:
                print('姓名\t语文\t数学\t英语\t总分')
                print(f'{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}')
                print('######## --- 查询成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def show_student(self):
        """显示全部信息的方法"""
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in self.student_list:
            print(f'{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}')

    def add_student(self):
        """新建学生信息的方法"""
        name = input('请输入学生姓名:')
        chinese = int(input('请输入学生的语文成绩:'))
        math = int(input('请输入学生的数学成绩:'))
        english = int(input('请输入学生的英语成绩:'))

        # 根据输入的信息实例化学生对象
        student = Student(name, chinese, math, english)
        # 将新建的学生对象添加到学生列表
        self.student_list.append(student)
        print('######## --- 新建成功 --- ########')
        # print(self.student_list)

    def save_student(self):
        """保存数据的方法"""
        with open('C:\\Users\\fyue\\Desktop\\PythonProject\\核心\\11 类与对象封装\\students.json', mode='w',
                  encoding='utf-8') as f:
            final_stu_list = [
                {"name": i.name, "chinese": i.chinese, "math": i.math, "english": i.english, "total": i.total, } for i
                in self.student_list]
            pprint.pprint(final_stu_list)
            data_str = json.dumps(final_stu_list, ensure_ascii=False)
            f.write(data_str)

    def show_menu(self):
        """显示系统功能菜单的方法"""
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
        print(str_info)

    def load_student(self):
        """加载文件里面的学员数据的方法"""
        with open('C:\\Users\\fyue\\Desktop\\PythonProject\\核心\\11 类与对象封装\\students.json', mode='r',
                  encoding='utf-8') as f:
            data = f.read()  # --> str
        new_list = json.loads(data)
        # print(type(data))
        # print(new_list)
        # print(type(new_list))

        # 列表推导式转化字典对象
        # print([Student(i['name'], i['chinese'], i['math'], i['english'], ) for i in new_list])
        # 转化的列表赋值给 self.student_list
        self.student_list = [Student(i['name'], i['chinese'], i['math'], i['english'], ) for i in new_list]


# 快速导入模块, 光标放置到模块名附近 Alt + Enter

StudentManager().run()

# 类名 + ()  ---> 实例化对象
