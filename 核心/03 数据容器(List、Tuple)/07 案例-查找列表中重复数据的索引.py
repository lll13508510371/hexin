list1 = [4, 2, 1, 0, 6, 2, 1]

list2 = []
for index in range(len(list1)):  # 循环列表的索引
    # print(index)
    if list1[index] not in list2: # 如果数据没有在list2里面
        list2.append(list1[index])
    else:  # 走else逻辑就代表是重复数据
        print('重复的数据:', list1[index])
        print('重复的数据索引:', index)
        print('第一次出现的索引: ', list1.index(list1[index]))

# for index in range(len(list1)):  # 循环列表的索引
#     print(list1[index])

