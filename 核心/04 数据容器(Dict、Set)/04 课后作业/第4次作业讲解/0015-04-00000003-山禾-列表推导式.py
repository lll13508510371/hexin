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

# print([f'https://www.maoyan.com/board/4?offset={i * 10 类与继承}' for i in range(10 类与继承)])
# pprint.pprint([f'https://www.maoyan.com/board/4?offset={i * 10 类与继承}' for i in range(10 类与继承)])
# pprint([f'https://www.maoyan.com/board/4?offset={i * 10 类与继承}' for i in range(10 类与继承)])

# import random
#
# random.randint()

from pprint import pprint

pprint([f'https://www.maoyan.com/board/4?offset={i * 10}' for i in range(10)])