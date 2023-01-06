name_list = ['正心', '丸子', '自游', '木子']

name = input('请输入要查找的名字:')

if name in name_list:
    print(f'{name}', "存在")
else:
    print(f'{name}', "不存在")

