
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue  # 在循环任务中, 结束当前的任务, 执行后续的任务
    print(i)
else:
    print('循环结束')
