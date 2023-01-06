name_list = ['Tom', 'Lily', 'Rose']

i = 0
while i < len(name_list):  # while循环必须得索引取值, 用得少
    print(name_list[i])
    i += 1

# name_list = ['Tom', 'Lily', 'Rose']

for i in name_list:  # 直接循环/遍历列表内容
    print(i)

for i in range(len(name_list)):  # 循环/遍历列表索引, 根据索引取值
    print(name_list[i])
