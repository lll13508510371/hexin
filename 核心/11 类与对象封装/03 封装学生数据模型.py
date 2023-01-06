import json
import pprint

'''
用学生管理系统封装学生数据模型(学生数据库)
'''


class StudentDB:
    """学生数据模型"""

    def __init__(self):
        self.student_list = []  # ---> 模型操作的学生信息列表 不确定可以用None
        # 启动程序的时候就加载数据  创建对象的时候，加载数据
        self.load()  # 在初始化方法中也可以调用类的其他方法

    def change(self, old_name, student):
        """
        修改学生信息的方法
        :param old_name: 需要修改的学生姓名, --> 旧的名字
        :param student: 传入当前需要修改的学生的字典对象
        :return: 修改成功就返回True, 失败返回 False
        """
        old_stu = self.search(old_name)
        if old_stu:
            index = self.student_list.index(old_stu)  # 查找对象在列表中的索引位置
            self.student_list[index].update(student)  # 根据查找的索引取值, 然后更新字典的键值对
            return True
        else:
            return False

    def search(self, name):
        """
        指定姓名查询学生信息
        :param name: 姓名
        :return: 如果找到了就返回学生字典对象, 没找到就返回 None
        """
        for stu in self.student_list:
            if name == stu['name']:  # 满足此条件就代表找到了这个学生
                return stu

    def delete(self, student):  # student --> 字典格式的学生信息
        """删除学生的方法"""
        self.student_list.remove(student)

    def insert(self, student):
        """
        增加学员的方法
        :param student: 字典格式的学生信息
        :return: None
        """
        self.student_list.append(student)

    def load(self):
        """加载数据的方法"""
        with open('/核心\\11 类与对象封装\\students.json', mode='r',
                  encoding='utf-8') as f:
            data = f.read()  # --> str
        new_list = json.loads(data)
        self.student_list = new_list

    def save(self):
        """保存数据的方法"""
        with open('/核心\\11 类与对象封装\\students.json', mode='w',
                  encoding='utf-8') as f:
            pprint.pprint(self.student_list)
            data_str = json.dumps(self.student_list, ensure_ascii=False)
            f.write(data_str)

    def all(self):
        """查看当前所有学生数据的方法"""
        return self.student_list


# 实例化学生数据模型对象, 后续在系统中只要涉及到数据模型操作, 就用这个对象操作
db = StudentDB()


class StudentManager:
    """学生信息管理系统类"""

    # def __init__(self):
    #     self.student_list = None  # 存储学员数据 -- 列表

    # 1.程序入口函数, 整个系统的逻辑都在这个主函数中调用
    def run(self, db_obj):  # 山禾老师写的时候没有传对象,直接把上面实例好的db实例对象拿下来用了
        # # 1. 加载文件里面的学员数据
        # self.load_student()
        db_obj.load()  # # 数据模型加载数据

        while True:
            # 2. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单(print)
            self.show_menu()

            # 3. 根据功能选择，执行不同的功能(多条件判断)
            action = input('请输入您要执行的操作:')

            if action == '1':
                print('1. 新建学生信息')
                self.add_student(db)

            elif action == '2':
                print('2. 显示全部信息')
                self.show_student(db)

            elif action == '3':
                print('3. 查询学生信息')
                self.search_student(db)

            elif action == '4':
                print('4. 修改学生信息')
                self.modify_student(db)

            elif action == '5':
                print('5. 删除学生信息')
                self.del_student(db)

            elif action == '0':
                print('0. 退出系统')
                self.save_student(db)
                break

            else:
                print('请输入正确的选择!')

    def del_student(self, db_obj):
        """删除学生信息的方法"""
        del_name = input('请输入您要删除学生的姓名:')
        for stu in db_obj.all():
            if del_name == stu['name']:
                # self.student_list.remove(stu)
                db_obj.delete(stu)  # 在数据模型中删除
                print('######## --- 删除成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def modify_student(self, db_obj):
        """修改学生信息的方法"""
        modify_name = input('请输入您要修改学生的姓名:')
        for stu in db_obj.all():
            if modify_name == stu['name']:
                name = input('请重新输入学生姓名:')
                chinese = input('请重新输入学生的语文成绩:')
                math = input('请重新输入学生的数学成绩:')
                english = input('请重新输入学生的英语成绩:')

                stu_dict = {'name': name, 'chinese': chinese, 'math': math, 'english': english,
                            'total': (name + chinese + english)}

                db_obj.change(stu['name'], stu_dict)
                print('######## --- 修改成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def search_student(self, db_obj):
        """查询学生信息的方法"""
        # 1. 用户输入目标学员姓名
        search_name = input('请输入您要查询学生的姓名:')

        # # 2. 遍历列表。如果学员存在打印学员信息，否则提示学员不存在
        for stu in db_obj.all():
            if search_name == stu['name']:
                print('姓名\t语文\t数学\t英语\t总分')
                print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
                print('######## --- 查询成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')

    def show_student(self, db_obj):
        """显示全部信息的方法"""
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in db_obj.all():
            print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')

    def add_student(self, db_obj):
        """新建学生信息的方法"""
        name = input('请输入学生姓名:')
        chinese = int(input('请输入学生的语文成绩:'))
        math = int(input('请输入学生的数学成绩:'))
        english = int(input('请输入学生的英语成绩:'))
        total = chinese + math + english

        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        db_obj.insert(stu)

        print('######## --- 新建成功 --- ########')
        # print(self.student_list)

    def save_student(self, db_obj):
        """保存数据的方法"""
        db_obj.save()  # 使用数据模型保存数据

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


StudentManager().run(db)
