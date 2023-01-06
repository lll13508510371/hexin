"""
请用列表推导式构建以下地址规律

    https://www.maoyan.com/board/4?offset=0
    https://www.maoyan.com/board/4?offset=10
    https://www.maoyan.com/board/4?offset=20
    https://www.maoyan.com/board/4?offset=30
    https://www.maoyan.com/board/4?offset=40
    https://www.maoyan.com/board/4?offset=50
    https://www.maoyan.com/board/4?offset=60
    https://www.maoyan.com/board/4?offset=70
    https://www.maoyan.com/board/4?offset=80
    https://www.maoyan.com/board/4?offset=90
请在下方编辑代码:
"""
import pprint
print([i for i in range(0, 91, 10)])
print([i * 10 for i in range(10)])

# 把遍历到的i放到列表i当中
result = [f'https://www.maoyan.com/board/4?offset={i}' for i in range(0, 91, 10)]
print(result)
pprint.pprint(result)