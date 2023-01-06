from json import *


class Student_db:
    def __init__(self):
        self.student_list = None
        self.load()

    def load(self):
        # 可能会有一样名字但路径不同的文件
        with open('/核心\\11 类与对象封装\\03 课后作业\\students.json',
                  mode='r', encoding='utf-8') as f:
            student_str = f.read()
        self.student_list = loads(student_str)  # 通过赋值更新列表
        # self.student_list.append(student_list)
        # 这里搞错了,勾八不是append,append就把列表读取到的列表嵌套在self.student_list当中了
        # self.student_list = student_list  # 通过赋值更新列表

    def add(self, student):
        # 传学生字典数据
        self.student_list.append(student)

    def delete(self, student):
        self.student_list.remove(student)

    def query(self, student_name):
        for stu in self.student_list:
            if student_name == stu['name']:
                return stu  # 这里就返回函数结果了,所以不需要break了
            # 问题 else:
            #     return '没有当前学生'

    def change(self, old_name, student):
        old_student = self.query(old_name)

        if old_student:  # 如果有这个人
            index = self.student_list.index(old_student)
            self.student_list[index].update(student)
            return True
        else:
            return False

    def save(self):
        with open('/核心\\11 类与对象封装\\03 课后作业\\students.json',
                  mode='w', encoding='utf-8') as f:
            student_str = dumps(self.student_list,
                                ensure_ascii=False)  # 关闭默认编码
            f.write(student_str)


db = Student_db()


class Student_system:
    def interface(self):
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

    def run(self, db_obj):
        db_obj.load()
        while True:
            self.interface()

            action = input('请输入你想进行的操作: ')

            if action == '1':
                print('1. 新建学生信息')
                self.add_student(db_obj)

            elif action == '2':
                print('2. 显示全部信息')
                self.show_all_student(db_obj)

            elif action == '3':
                print('3. 查询学生信息')
                self.query_student(db_obj)

            elif action == '4':
                print('4. 修改学生信息')
                self.change_student(db_obj)

            elif action == '5':
                print('5. 删除学生信息')
                self.delete_student(db_obj)

            elif action == '0':
                print('0. 退出系统')
                self.save_student(db_obj)
                break
            # 如果上面全都用 if 除了if action =='0'  else都会运行  \n 属于空字符串 是字符串类型
            # 所以要用 elif
            else:
                print('请输入正确的选择')

    def add_student(self, db_obj):
        name = input('请输入你的名字: ')
        chinese = int(input('请输入语文成绩: '))
        math = int(input('请输入数学成绩: '))
        english = int(input('请输入英语成绩: '))
        total = chinese + math + english
        stu = {'name': name, 'chinese': chinese, 'math': math,
               'english': english,
               'total': total}
        db_obj.add(stu)
        print('############ ---添加成功--- ############')

    def show_all_student(self, db_obj):
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in db_obj.student_list:
            print(
                f'{stu["name"]}\t{stu["chinese"]}\t{stu["math"]}\t{stu["english"]}\t{stu["total"]}')

    def delete_student(self, db_obj):
        name = input('请输入你的名字: ')
        for stu in db_obj.student_list:
            if name == stu['name']:
                db_obj.delete(stu)
                print('############ ---删除成功--- ############')
                break

    def query_student(self, db_obj):
        name = input('请输入你的名字: ')
        stu = db_obj.query(name)
        if stu:
            print('姓名\t语文\t数学\t英语\t总分')
            print(
                f'{stu["name"]}\t{stu["chinese"]}\t{stu["math"]}\t{stu["english"]}\t{stu["total"]}')
        else:
            print('该学生不存在或姓名输入错误')

        # name = input('请输入你要查询的名字: ')
        # for stu in db_obj.student_list:
        #     if name == stu['name']:
        #         print('姓名\t语文\t数学\t英语\t总分')
        #         print(
        #             f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
        #         print('######## --- 查询成功 --- ########')
        #         break
        #     else:
        #         print('该学生不存在或者姓名输入错误！')

    def change_student(self, db_obj):
        old_name = input('请输入你的名字: ')
        for stu in db_obj.student_list:
            if old_name == stu['name']:
                name = input('请重新输入你的名字: ')
                chinese = int(input('请输入语文成绩: '))
                math = int(input('请输入数学成绩: '))
                english = int(input('请输入英语成绩: '))
                total = chinese + math + english

                stu = {'name': name, 'chinese': chinese, 'english': english,
                       'total': total}
                db_obj.change(old_name, stu)
                print('############ ---修改成功--- ############')
                break

    def save_student(self, db_obj):
        db_obj.save()


Student_system().run(db)
