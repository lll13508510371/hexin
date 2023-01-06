"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变
"""
import os

flag = 1
print(os.getcwd())
os.chdir('code')
file_list = os.listdir()
'''
listdir() --> Return a list containing the names of the files in the directory.
虽然内置函数最后是pass结尾,但是介绍中有return,说明函数最后是有return关键字的,用print把相应的
return值打印出来就好
'''
print(file_list)
for i in file_list:
    index = i.index('.')
    if flag == 1:
        new_name = i[:index] + '-python' + i[index:]
        # i = new_name
        os.rename(i, new_name)
        # print(i)
    elif flag == 2:
        num = len('-python')
        old_name = i[:(index-num)] + i[index:]
        os.rename(i, old_name)
'''
负索引的应用
'''