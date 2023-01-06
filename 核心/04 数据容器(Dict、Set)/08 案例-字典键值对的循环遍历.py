dict1 = {
    'name': '丸子',
    'age':  18,
    'gender': '女',
    '爱好': '吃喝玩乐'
}

# for key in dict1.keys():
#     print(key)
#
# for value in dict1.values():
#     print(value)

"""解包"""
# dict1.items()  遍历出来是一个个元组<其中有两个数据(第一个是键, 第二个是值)>
print(list(dict1.items()))
# for i in dict1.items():
#     print(i)

# key  代表元组的第一个元素<键>
# value  代表元组的第二个元素<值>
# for key,value in dict1.items():
#     print(value)

for cate1, cate2, cate3 in [(11, 22, 33), (11, 22, 33), (11, 22, 33)]:
    print(cate3)
