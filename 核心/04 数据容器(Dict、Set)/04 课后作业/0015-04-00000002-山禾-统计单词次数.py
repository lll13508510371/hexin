# -*- coding: utf-8 -*-
"""
作业4：
统计Python之禅中所有**单词**(注意是单词)出现的次数
"""
# python 之禅
s = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
Readability counts
Special cases aren't special enough to break the rules
Although practicality beats purity
Errors should never pass silently
Unless explicitly silenced
In the face of ambiguity, refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it
Although that way may not be obvious at first unless you're Dutch
Now is better than never
Although never is often better than *right* now
If the implementation is hard to explain, it's a bad idea
If the implementation is easy to explain, it may be a good idea
Namespaces are one honking great idea -- let's do more of those
"""

"""自己在下方编写代码实现功能"""
import pprint

list1 = s.split()

dict1 = {}

for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

print(dict1)
pprint.pprint(dict1)

dict2 = {'key1': '2'}
if '2' in dict2:
    print('Ok')
else:
    print('Not Ok')

if 'key1' in dict2:
    print('yes')
else:
    print('no')
'''
!!! 从上面可以看出字典当中 in / not in 只能判断key存不存在而不能判断值存不存在
    所以循环中if i in dic1指的是dic1当中有没有i这个key,没有的话就创建一个key
'''