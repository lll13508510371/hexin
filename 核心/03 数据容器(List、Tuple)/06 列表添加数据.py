name_list = ['正心', '丸子', '自游', '木子']

"""将数据添加到列表末尾"""
name_list.append('思语')
name_list.append('巳月')

"""
    列表是一种可变的数据容器, 操作的都是针对自己本身
"""

"""如果追加是一个列表, 那么会把整个列表作为一个数据, 追加到列表尾部, 构建成了二维列表"""
name_list_2 = ['思语', '落落']
# name_list.append(name_list_2)
print(name_list)

"""如果不想要把整个列表作为一个元素追加, 那么需要用 extend() 列表的合并"""
name_list = ['正心', '丸子', '自游', '木子']
name_list_2 = ['思语', '落落']

name_list.extend(name_list_2)  # 把name_list_2列表中的数据合并到name_list
print(name_list)
print(name_list_2)

"""指定位置在列表中插入数据"""
name_list = ['正心', '丸子', '自游', '木子']
# 必须传递两个参数, 第一个参数是你要在列表的哪里插入数据(索引), 第二个参数你插入的数据是什么
name_list.insert(2, '思语')  # 在索引为 2 的位置插入数据
print(name_list)
