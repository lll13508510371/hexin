# 将需要备份的文件名按照要求进行备份:
# 文件名修改: 原有的文件名 + [备份], 尾缀不变
# 文件中的数据不变


old_name = input('请输入您要备份的文件名:')

# 准备新文件名
index = old_name.index('.')  # 找 . 所在的索引位置

print(old_name[:index])
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)

# 读取旧文件数据
with open(old_name, mode='rb') as f:  # 二进制数据没有编码
    old_data = f.read()

# 写入数据到新文件
with open(new_name, mode='wb') as f:  # 二进制数据没有编码
    f.write(old_data)
'''
相对路径
'''
