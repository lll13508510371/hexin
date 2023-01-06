# -*- coding: utf-8 -*-
''''''
'''
我这道题的解法比山禾给的答案要好(也是我询问了一下),因为我这是随机1,2号办公室的人放入四号办公室1,2号座位
山禾的是一号办公室的人放入四号办公室一号位置,二号办公室的人放入四号办公室二号位置
'''
import pprint

'''
现有办公室座位表 seating 如下

先要求从 1号办公室、2号办公室中分别随机抽一个安排到4号办公室去

    1. 随机从1号 2号办公室中选取一个人
    2. 将其安排到4号办公室去
    3. 最后将安排好的座位表打印
'''

import random

seating = [
    ('1号办公室1位置', '戴贵富'),
    ('1号办公室2位置', '田显余'),
    ('1号办公室3位置', '李元东'),
    ('2号办公室1位置', '廖德超'),
    ('2号办公室2位置', '秦代坤'),
    ('2号办公室3位置', '杨久林'),
    ('3号办公室1位置', '邓永明'),
    ('3号办公室2位置', '张勇')
]

# 要求打印可以如下（内容一样）
"""
[
    ('1号办公室1位置', '戴贵富'), ('1号办公室3位置', '李元东'),
    ('2号办公室2位置', '秦代坤'), ('2号办公室3位置', '杨久林'), 
    ('3号办公室1位置', '邓永明'), ('3号办公室2位置', '张勇'), 
    ('4号办公室1位置', '田显余'), ('4号办公室2位置', '廖德超')
]
"""
"""自己在下方编写代码实现功能"""
# print(seating[0])
# print(type(seating[0]))
''' index = random.randint(0, 2)'''
# first_one = str(seating[index])
''' index2 = random.randint(3, 5)'''
# second_one = str(seating[index2])
# print(first_one)
# print(second_one)
'''
one = seating.pop(index)
two = seating.pop(index2)
'''
# print(one[1])
# print(two[1])
# print(seating)
'''
seating.append(('4号办公室1位置', one[1]))
seating.append(('4号办公室2位置', two[1]))
print(seating)
pprint.pprint(seating)
'''
# print(first_one)
# print(type(first_one))
# print(first_one)
# first = first_one.strip('(').strip(')').strip("''")
# print(first)
# one = first.split(',')
# print(one)

# 取1, 2号办公室的人的位置

index1 = random.randint(0, 2)
index2 = random.randint(2, 4)

# 删除相应1,2号办公室的人和位置

one = seating.pop(index1)

'''
搞错了,one 删掉了一个数据,二号办公室的索引向前移一位,所以index2 = random.randint(2,4),或者先取index2 = random.randint(3,5)
'''

two = seating.pop(index2)

list1 = [one[1], two[1]]

# print(list1)

first_person = random.choice(list1)

# print(first_person)

list1.remove(first_person)

# print(list1)

second_person = list1[0]

# print(second_person)
# 将取到的1,2号办公室的人放到4号办公室

seating.append(('4号办公室1位置', first_person))
seating.append(('4号办公室2位置', second_person))

print(seating)
pprint.pprint(seating)


