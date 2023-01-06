# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         break  # 在循环任务中, 结束当前的任务, 执行后续的任务
#
#     print(i)
#
# else:  # 如果致循环任务是正常结束的, 就执行else逻辑
#     print('循环正常结束!')

"""
break 在循环中会导致循环任务不是正常结束的
"""

for i in range(10):
    if i == 6:
        continue
    print(i)
else:
    print('循环正常结束!')