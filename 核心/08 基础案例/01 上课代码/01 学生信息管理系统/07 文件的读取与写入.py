# 5. 如果查询到指定的学生信息，用户可以选择 修改 或者 删除 信息 --> 分支
import pprint
import json  # Python对象的转换模块, 内置


students = [
    {'name': '丸子', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '正心', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
    {'name': '自游', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
]

# 转字符串以后写入文件
# with open('students.json', mode='w', encoding='utf-8') as f:
#     # f.write(students)
# #     # 保存数据的时候需要字符串
# #     # students对象 --> 字符串, ensure_ascii=False 关闭默认编码
#     student_str = json.dumps(students, ensure_ascii=False)
# #     print(student_str)
# #     print(type(student_str))
#     f.write(student_str)

# 读取文件中的数据
with open('students.json', mode='r', encoding='utf-8') as f:
    student_str = f.read()

# 读取出来的数据后续要用于整个系统中
# json.loads(str)  --> list
students = json.loads(student_str)
print(students)
print(type(students))


