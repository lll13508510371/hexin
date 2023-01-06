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

pprint.pprint(students)




