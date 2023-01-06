"""

假设有以下地址:

    https://www.bbsmax.com/A/?user=7001&id=1305
    https://www.bbsmax.com/A/?user=7002&id=1306
    https://www.bbsmax.com/A/?user=7003&id=1307
    https://www.bbsmax.com/A/?user=7004&id=1308
    https://www.bbsmax.com/A/?user=7005&id=1309
    https://www.bbsmax.com/A/?user=7006&id=1310
    https://www.bbsmax.com/A/?user=7007&id=1311
    https://www.bbsmax.com/A/?user=7008&id=1312
    https://www.bbsmax.com/A/?user=7009&id=1313
    https://www.bbsmax.com/A/?user=7010&id=1314

观察以上地址规律, 将以上规律用循环构建出来
"""
import pprint


# Method 1 **kwargs
def func(**kwargs):
    print(kwargs)
    return kwargs


for i in range(0, 10):
    result = func(user=7001 + i, id=1305 + i)
    # print(type(result))
    print(f'https://www.bbsmax.com/A/?user={result["user"]}&id={result["id"]}')

'''
参考了 05_08 不定长参数搞出来的
def 刚开始用的print kwargs, 然后 # print(type(result))得到了None-type,发现没用return,hh
'''

'''
# Method 2   map()  
# print(list(range(0, 10 类与继承)))
list1 = list(range(7001, 7011))
list2 = list(range(1305, 1315))

print(list(map(lambda x, y: f'https://www.bbsmax.com/A/?user={x}&id={y}', list1, list2)))

url = '\n'.join(list(map(lambda x, y: f'https://www.bbsmax.com/A/?user={x}&id={y}', list1, list2)))
print(url)
'''

'''
# Method 3 zip() range()是一个range对象,是一个可迭代对象,可迭代就可以组包
print(type(range(0, 2)))

print(list(zip(range(7001, 7011), range(1305, 1315))))

result = list(zip(range(7001, 7011), range(1305, 1315)))

for user, Id in result:  # !!!这是一个解包过程 result是一个二元对象 -->列表里面是元组
    print(f'https://www.bbsmax.com/A/?user={user}&id={Id}')

for i in result:
    print(i)
'''

'''
用一个变量遍历列表当中的元组和用两个变量遍历列表当中的元组得到的结果是不同的
如上
'''

'''
# Method 4 推导式
result = list(zip(range(7001, 7011), range(1305, 1315)))
pprint.pprint([f'https://www.bbsmax.com/A/?user={user}&id={Id}' for user, Id in result])
'''

'''
# Method 5 函数递归
def fun(x, y):
    if x == 7011 or y == 1315:
        return

    print(f'https://www.bbsmax.com/A/?user={x}&id={y}')

    fun(x + 1, y + 1)

fun(7001, 1305)
'''

'''
# Method 6 创建普通函数
def fun(num, user, Id):
    for i in range(num):
        print(i)
        print(f'https://www.bbsmax.com/A/?user={user + i}&id={Id + i}')

fun(10 类与继承, user=7001, Id=1305)
'''
'''
把user={user + i}&id={Id + i}搞成user={user + num}&id={Id + num},发现结果一样,才意识道num是
固定的,是i,hh,小细节问题,反映自己还是没有特别到位
'''
