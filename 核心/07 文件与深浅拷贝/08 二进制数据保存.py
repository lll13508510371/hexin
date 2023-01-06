import requests

response = requests.get(
    'https://www.baidu.com/img/pc_675fe66eab33abff35a2669768c43d95.png')
img_data = response.content
print(img_data)

with open('../../../核心/07 文件与深浅拷贝/02 上课课件/baidu.png', mode='wb') as f:
    f.write(img_data)
