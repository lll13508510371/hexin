"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变
"""
import os

os.chdir('code')  # 更改执行路径

print(os.listdir())

for i in os.listdir():

    name_index = i.index('.')
    new_name = i[:name_index] + '-python' + i[name_index:]
    print(new_name)

    os.rename(i, new_name)




