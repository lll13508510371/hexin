"""
作业2：
运行代码之后，请找出下面代码错误并且修正

提示：深浅拷贝
"""
import copy
data = {
    'cate': '童书馆',
    'sub_cate': None
}
sub_cate = ['科普百科', '儿童文学', '幼儿启蒙', '动漫卡通', '少儿英语']

all_cate = []

for cate in sub_cate:
    data['sub_cate'] = cate
    # print(data)
    all_cate.append(copy.copy(data))
    # print(all_cate)
    # copy.copy(all_cate)
print(all_cate)
# print(data)

'''
参考 https://blog.csdn.net/a999999123/article/details/110814784
Python中对象之间赋值是按引用传递的
all_cate = [data] 第一次传入的data
all_cate = [data,data] 第二次传入的data
all_cate = [data,data,data] 第三次传入的data
all_cate = [data,data,data,data] 第四次传入的data
all_cate = [data,data,data,data,data] 第五次传入的data

copy之后就不会改变了
类似于
all_cate = [copy(data)1] 第一次传入的data
all_cate = [copy(data)1,copy(data)2] 第二次传入的data
all_cate = [copy(data)1,copy(data)2,copy(data)3] 第三次传入的data
all_cate = [copy(data)1,copy(data)2,copy(data)3,copy(data)4] 第四次传入的data
all_cate = [copy(data)1,copy(data)2,copy(data)3,copy(data)4,copy(data)5] 第五次传入的data

'''



