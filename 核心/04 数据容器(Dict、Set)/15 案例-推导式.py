"""
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
https://movie.douban.com/top250?start=75&filter=
https://movie.douban.com/top250?start=100&filter=
https://movie.douban.com/top250?start=125&filter=
https://movie.douban.com/top250?start=150&filter=
https://movie.douban.com/top250?start=175&filter=
https://movie.douban.com/top250?start=200&filter=
https://movie.douban.com/top250?start=225&filter=
https://movie.douban.com/top250?start=250&filter=
"""
import pprint

# 用列表推导式构建以上地址
print([i for i in range(0, 251, 25)])
print([i * 25 for i in range(11)])


result = [f'https://movie.douban.com/top250?start={i}&filter=' for i in range(0, 251, 25)]
pprint.pprint(result)