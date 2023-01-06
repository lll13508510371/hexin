students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '自游', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '巳月', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '益达', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '金克斯', 'chinese': 66, 'math': 77, 'english': 100, 'total': 231},
    {'name': '欧阳正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]
print('姓名\t语文\t数学\t英语\t总分')

for stu in students:
    print(f'{stu["name"]}\t{stu["chinese"]}\t{stu["math"]}\t{stu["english"]}\t{stu["total"]}')
