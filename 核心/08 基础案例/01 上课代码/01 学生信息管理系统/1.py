"""
ѧ����Ϣ����ϵͳ, �Լ����Ű���¼��ʵ��һ��
"""
"""�����·�ʵ��"""
'''
1.����
2.��ʾ������Ϣ
3.��ѯ
4.�޸�
5.ɾ��
6.�˳�
'''
# coding=gbk
# import json
# import pprint

# str_info = """**************************************************
# ��ӭʹ�á�ѧ����Ϣ����ϵͳ��V1.0
# ��ѡ������Ҫ���еĲ���
# 1. �½�ѧ����Ϣ
# 2. ��ʾȫ����Ϣ
# 3. ��ѯѧ����Ϣ
# 4. �޸�ѧ����Ϣ
# 5. ɾ��ѧ����Ϣ
#
# 0. �˳�ϵͳ
# **************************************************"""

# with open('1.json', mode='r', encoding='utf-8') as f:
#     student_str = f.read()
#     # print(student_str)
#
# student_list = json.loads(student_str)

# action = input('��ѡ������Ҫ���еĲ���: ')
#
# while True:
#     print(str_info)
#     action = input('��ѡ������Ҫ���еĲ���: ')
#     # 1.����
#     if action == '1':
#         name = input('�������������: ')
#         chinese = int(input('������������ĳɼ�: '))
#         math = int(input('�����������ѧ�ɼ�: '))
#         english = int(input('���������Ӣ��ɼ�: '))
#         total = chinese + math + english
#         dict1 = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
#         # ���ֵ�װ��һ��ѧ��������  �б�װѧ��������
#         student_list.append(dict1)
#         # print(student_list)

# 2.��ʾ������Ϣ
# students = [
#     {'name': '����', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
#     {'name': '����', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
#     {'name': '����', 'chinese': 66, 'math': 77, 'english': 88, 'total': 231},
# ]
# print('����\t\t����\t\t��ѧ\t\tӢ��\t\t')
# for stu in student:
#     print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}')

# 3.��ѯ
# name = input('�������������: ')
#
# for stu in student:
#     if name == stu['name']:
#         print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}')
#         break
# else:
#     print('�����������')

# 4.�޸�
# ������(�ո�)���ᱨ��
# name = input('�������������: ')
# for stu in students:
#     if name == stu['name']:
#         name = input('�����������������: ')
#         chinese = input('����������������ĳɼ�: ')
#         math = input('���������������ѧ�ɼ�: ')
#         english = input('�������������Ӣ��ɼ�: ')
# #         if name:
# #             stu['name'] = name
# #         if chinese:
# #             stu['chinese'] = int(chinese)
# #         if math:
# #             stu['math'] = int(math)
# #         if english:
# #             stu['english'] = int(english)
# #
#         stu['total'] = stu['chinese'] + stu['math'] + stu['english']
#
#         print(f'{stu["name"]}\t{stu["chinese"]}\t\t{stu["math"]}\t\t{stu["english"]}\t\t{stu["total"]}')
#         break
# else:
#     print('�޵�ǰѧ��')
#
# '''
# ���ﲻ����elif �������һ��Ϊ��, �Ͳ�������ж�elif�� ��elif ���������Ϊ�˵õ�Ψһһ��Ϊ�����
# '''

# 5.ɾ��
# name = input('�������������: ')
# for stu in student:
#     if name == stu['name']:
#         student.remove(stu)
#         break
# else:
#     print('�޵�ǰѧ��')
#
# print(student)

# �ļ���ȡ��д��


# д���ļ�
# with open('1.json', mode='w', encoding='utf-8') as f:
#     student_str = json.dumps(students, ensure_ascii=False)
#     print(student_str)
#     f.write(student_str)

# ��ȡ�ļ�
# with open('1.json', mode='r', encoding='utf-8') as f:
#     student_str = f.read()
#     # print(student_str)
#
# student_list = json.loads(student_str)
#
# print(student_list)
# print(type(student_list))
i = print("")
print(type(i))
# �ַ����� ' '  "" ���� """  """
j = print(' ')
print(type(j))