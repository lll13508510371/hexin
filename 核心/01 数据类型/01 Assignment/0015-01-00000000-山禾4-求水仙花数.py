'''
选做:
    请找出 100-999 之间的所有水仙花数  for if函数
'''
'''
前面把*当作幂了，运行不了结果，幂是**，一定要注意
'''
for i in range(100, 999):
    if i == (i % 10) ** 3 + int((i / 10) % 10) ** 3 + (i // 100) ** 3:
        print(str(i) + '是水仙花数')

print('\n')

for i in range(100, 999):
    a = (i % 10)
    b = int((i / 10) % 10)
    c = (i // 100)
    if i == a ** 3 + b ** 3 + c ** 3:
        print(str(i) + '是水仙花数')
