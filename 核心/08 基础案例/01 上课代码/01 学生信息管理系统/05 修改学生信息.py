# 5. 如果查询到指定的学生信息，用户可以选择 修改 或者 删除 信息 --> 分支
import pprint

students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '自游', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '益达', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '金克斯', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '欧阳正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

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

pprint.pprint(students)
