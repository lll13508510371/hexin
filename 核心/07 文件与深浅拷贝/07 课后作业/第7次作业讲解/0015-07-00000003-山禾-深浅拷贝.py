"""
作业2：
运行代码之后，请找出下面代码错误并且修正

提示：深浅拷贝
"""
import pprint
import copy

data = {
    'cate': '童书馆',
    'sub_cate': None
}
sub_cate = ['科普百科', '儿童文学', '幼儿启蒙', '动漫卡通', '少儿英语']

all_cate = []

for cate in sub_cate:
    data['sub_cate'] = cate  # 键值对的复制
    all_cate.append(copy.deepcopy(data))  # 浅拷贝<作用域一维>

print(all_cate)

# pprint.pprint(all_cate)
# 对象引用, 与深浅拷贝