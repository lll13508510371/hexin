"""
### 作业2

1、创建一个房子类,
+ 分别有以下属性
  名字（name）, 房子面积(area), 家具<列表>（furniture）

+ 每个房子都有添加家具的方法
    # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
    # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
    # 否则：提示用户家具太大，剩余面积不足，无法容纳

2、实例化房子操作
    实例化一个房子， 面积50平米
    添加家具：（沙发，占地15平米）
    添加家具：（餐桌，占地8平米）
    添加家具：（大床，占地20平米）
    添加家具：（浴缸，占地8平米）

"""
"""请在下方编辑代码"""
'''
联系现实情况 --> 家具是一个一个搬入房子的 --> 搬入一个家具算房子剩余面积,再根据之后搬入房子的家具来判断是否还能添加家具
'''

class House:
    def __init__(self, name, area, furniture):
        self.name = name
        self.area = area
        self.furniture = furniture

    def add_furniture(self, furniture_name, furniture_area):
        if self.area >= furniture_area:
            self.furniture.append(furniture_name)
            self.area -= furniture_area
            print(f'{furniture_name}添加成功')
            print(f'{self.name}目前面积为{self.area}')

        else:
            print(f'{furniture_name}太大，剩余面积不足，无法容纳')


house1 = House('house1', 50, [])
house1.add_furniture('沙发', 15)
house1.add_furniture('餐桌', 8)
house1.add_furniture('浴缸', 8)
house1.add_furniture('大床', 20)
print(f"{house1.name}添加了{','.join(house1.furniture)}这些家具")


'''
house1 实例对象 House 类对象
'''
'''
定义类属性最好是固定的一些值例如人只有一个头 两只手这样的时候定义类属性
'''

'''
核心有些人把类里面封装的函数当成普通函数来设计了, 没有联系上设置类的初衷
'''

'''
实例化房子类得到house1实例对象 --> 就想添加家具到house1
--> 调用类当中封装(encapsulation)好的add_furniture()函数来判断是否能添加家具
--> 传入家具名称和家具的占地面积来判断该家具是否能够添加进house1
'''