"""
统计Python之禅中所有字符出现的次数
"""
# python 之禅
this_str = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

d = {}
for s in this_str:
    print(s)
    if s not in d.keys():  # 如果s字符没有在d字典的键中(第一次出现)
        d[s] = 1

    else:  # 如果字符是重复出现的, 就会走else代码逻辑
        d[s] += 1

    print(d)