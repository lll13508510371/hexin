# set --> 集合
# 集合默认自动去重
set1 = {1, 2, 3, 4, 5, 6, 1, 2, 3}
print(set1)
print(type(set1))

for i in set1:
    print(i)
# 集合是无序的数据结构
# !!! 所以只能通过 1. 遍历 查找数据或者 2. 成员元素符号in /not in判断元素是否在集合中
# 
print(2, 7 not in set1)
