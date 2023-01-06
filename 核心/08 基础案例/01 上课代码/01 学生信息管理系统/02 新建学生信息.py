"""
讨论: 用什么数据结构保存学生信息?
    --> 姓名(str)、语文成绩(数值)、数成学绩(数值)、英语成绩(数值) 、总分(数值)

    在一个系统中, 学生要方便查找和修改?  --> 用什么数据容器取保存所有的学生

        系统--> 要把所有的学生放到一个数据容器里面  [{学生1}, {学生2}, {学生3}....]
        一个学生 --> 包含具体的学生信息  列表x 字典√ 元组x 集合x
"""

# 4. 需要记录学生的 姓名、语文成绩、数成学绩、英语成绩 、总分 (input --> 数据容器存放)
name = input('请输入学生姓名:')
chinese = int(input('请输入学生的语文成绩:'))
math = int(input('请输入学生的数学成绩:'))
english = int(input('请输入学生的英语成绩:'))
total = chinese + math + english

students = [
    {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
]

print(students)
