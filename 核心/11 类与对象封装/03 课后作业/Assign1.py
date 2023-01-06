import json

'''
系统面向学生对象的封装
'''

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = int(chinese)
        self.math = int(math)
        self.english = int(english)
        self.total = int(chinese) + int(math) + int(english)


class Student_System:
    '''
     !!!! 主函数 run()
     1.加载学生数据
     -->把学生字典数据转换成学生属性
     2.初始化界面
     3.增删改查 所有数据
     -->把学生属性转换成字典数据
    4.退出保存
    '''

    def __init__(self):
        self.stu_obj_list = []

    # 学生信息系统类的主函数
    def run(self):
        self.load_data()

        while True:
            self.interface()

            action = input('请输入你想进行的操作: ')

            if action == '1':
                self.add()

            elif action == '2':
                self.all_info()

            elif action == '3':
                self.query()

            elif action == '4':
                self.change()

            elif action == '5':
                self.delete()

            elif action == '0':
                self.save()
                break
            # 如果上面全都用 if 除了if action =='0'  else都会运行  \n 属于空字符串 是字符串类型
            # 所以要用 elif
            else:
                print('请输入正确的选择')

    def load_data(self):
        with open('C:\\Users\\fyue\\Desktop\\PythonProject\\核心\\11 类与对象封装\\03 课后作业\\students.json', mode='r',
                  encoding='utf-8') as f:
            data = f.read()
            students = json.loads(data)
        self.stu_obj_list = [Student(stu['name'], stu['chinese'], stu['math'], stu['english']) for stu in students]

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

    def add(self):
        name = input('请输入你的名字: ')
        chinese = input('请输入你的语文成绩: ')
        math = input('请输入你的数学成绩: ')
        english = input('请输入你的英语成绩: ')
        total = chinese + math + english

        stu = Student(name, chinese, math, english)
        self.stu_obj_list.append(stu)
        print('######## --- 添加成功 --- ########')

    def query(self):
        name = input('请输入你的名字: ')

        for stu in self.stu_obj_list:
            if name == stu.name:
                print('姓名\t语文\t数学\t英语\t总分')
                print(f'{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}')
                print('######## --- 查询成功 --- ########')

            else:
                print('该学生不存在或者姓名输入错误！')
                break

    def change(self):
        old_name = input('请输入名字: ')
        for stu in self.stu_obj_list:
            if old_name == stu.name:
                print('(回车保留原有数据)')
                name = input('请输入你的名字: ')
                chinese = input('请输入你的语文成绩: ')
                math = input('请输入你的数学成绩: ')
                english = input('请输入你的英语成绩: ')

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
            '''
                index = self.stu_obj_list.index(stu)
                self.stu_obj_list[index].update(stu)
                上述过程已经修改了对象的值了 --> 还是理解有问题 这两步是03用的
                '''



    def delete(self):
        name = input('请输入你的名字: ')
        for stu in self.stu_obj_list:
            if name == stu.name:
                self.stu_obj_list.remove(stu)
                print('######## --- 删除成功 --- ########')
                break
        else:
            print('该学生不存在或者姓名输入错误！')


    def all_info(self):
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in self.stu_obj_list:
            print(f'{stu.name}\t{stu.chinese}\t{stu.math}\t{stu.english}\t{stu.total}')

    def save(self):
        stu_dic_list = [
            {'name': stu.name, 'chinese': stu.chinese, 'math': stu.math, 'english': stu.english, 'total': stu.total}
            for stu in self.stu_obj_list]
        with open('C:\\Users\\fyue\\Desktop\\PythonProject\\核心\\11 类与对象封装\\03 课后作业\\students.json', mode='w',
                  encoding='utf-8') as f:
            stu_str_list = json.dumps(stu_dic_list, ensure_ascii=False)
            f.write(stu_str_list)


Student_System().run()
