"""
把列表中所有人都变成sb,比方: Tencent_sb
"""
name = ['Tencent', 'Zhihu', 'Baidu']

"""请在下方编辑代码"""
# map(fuc,list)

print(list(map(lambda x: x + '_sb', name)))
# def change_name(x):
#     x = 'Tencent_sb'
#     return x

# print(change_name(name))
'''
map内部将每一个List元素传进设置的函数中,然后将新值放入原有列表
得到新的列表
'''
