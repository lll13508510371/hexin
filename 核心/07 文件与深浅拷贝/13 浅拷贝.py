import copy  # 深浅拷贝的模块, 内置模块

array = [1, 2, 3, 4, 5]

result = copy.copy(array)  # 将array浅拷贝一份, 区分原有的拷贝对象

print(id(array))
print(id(result))

array[0] = 'a'
print(array)
print(result)

print('---------------浅拷贝的作用域---------------------')
array2 = [1,
          ['a', 'b', 'c'],
          3]
arr2 = copy.copy(array2)

array2[1][0] = 100

print(array2)
print(arr2)

# 浅拷贝的作用域仅限在一维的维度

