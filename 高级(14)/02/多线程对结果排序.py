liens = open('data.txt', mode='r', encoding='utf-8').read().split()
print(liens)


def func(item):
    return int(item.split('=')[-1])


liens.sort(key=func)
print(liens)

'''
liens 是列表, 列表就有列表的方法, (既然是列表方法,这个方法就会将列表当中的元素一个一个拿出来来比较) 
'''
