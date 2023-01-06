import os  # 内置模块

# rename(): 重命名, 路径在重命名的时候不能找不到文件
# os.rename('text.txt', '123.txt')

# remove(): 删除文件
# os.remove('123.txt')

# mkdir()：创建文件夹, 当文件已存在时，无法创建该文件
# os.mkdir('aa')

# rmdir(): 删除文件夹
# os.rmdir('aa')

# getcwd(): 返回当前py文件当前工作目录 current work directory --> cwd
# print(os.getcwd())

# # chdir():改变目录路径
# os.mkdir('bb')
# # 需求：在aa里面创建bb文件夹: 1. 切换目录到aa，2创建bb
# os.chdir('aa')
# os.mkdir('bb')
#
# os.mkdir('aa\\gg')  # 建议绝对路径
# os.mkdir('bb')
print(os.getcwd())
os.chdir('bb')
os.mkdir('g1')
os.mkdir('aa/ggg')
# os.chdir('..')  # .. 取上一级目录
# os.mkdir('ff')

# listdir(): 获取某个文件夹下所有文件，返回一个列表
print(os.listdir())

# os.rename('bb', '123')

# 判断文件夹是否存在
print(os.path.exists('查找'))
print(os.path.exists('aa'))  # 存在返回True, 不存在返回 False

if not os.path.exists('查找'):
    os.mkdir('查找')
