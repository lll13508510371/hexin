info_str = """龙猫

主演：秦岚,糸井重里,岛本须美

上映时间：2018-12 模块封装和异常处理 模块封装和异常处理-14"""
"""
需求：
    1. 拿到主演的姓名（列表）
    2. 将主演名字合并为字符串，中间用中文的逗号隔开
"""

name_str = info_str.split()
print(name_str)
# print(name_str[1].split('：')[1])
# print(name_str[1].strip('主演：'))
name_str = name_str[1].strip('主演：')
print(name_str)
print(type(name_str))

print(name_str.split(','))
print('，'.join(name_str.split(',')))