import pymysql

""" 
    帮助 -> 学习 IDE 功能
    竖行模式: shift + alt + 鼠标左键拖动
    竖行模式下操作: shift + ctrl + 左右键
    快速导入: alt + entry  可以用回车键与上下键进行选择
    全选:    ctrl + a
"""


class UserDB:
    def __init__(self):
        self.conn = pymysql.connect(host='81.68.68.240', port=3306, user='windows', password='123456',
                                    database='python')
        self.cursor = self.conn.cursor()

    def search_by_name(self, name):
        sql = 'select * from user where name=%s;'
        self.cursor.execute(sql, (name,))
        # 查询结果是否需要再次进行封装
        return self.cursor.fetchall()

    def search_by_phone(self, phone):
        sql = "select * from user where phone like '%{}%';"
        self.cursor.execute(sql.format(phone))
        return self.cursor.fetchall()

    def search_by_address(self, address):
        sql = "select * from user where address like '%{}%';"
        self.cursor.execute(sql.format(address))
        results = self.cursor.fetchall()
        return [{
            'id': result[0],
            'name': result[1],
            'job': result[2],
            'company': result[3],
            'residence': result[4],
            'blood_group': result[5],
            'username': result[6],
            'sex': result[7],
            'address': result[8],
            'mail': result[9],
            'birthdate': result[10],
            'id_card': result[11],
            'phone': result[12]
        } for result in results]

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_user(self, user):
        """

        :param user: 用户字典对象
        :return:
        """
        key_str = ''
        value_str = ''
        items = list(user.items())
        for key, value in items[:-1]:
            key_str += f'{key},'
            value_str += f"'{value}',"
        key_str += items[-1][0]
        value_str += str(items[-1][1])
        sql = 'insert into user({}) values ({});'.format(key_str, value_str)
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    db = UserDB()
    # name = input('请输入需要查询的用户名:\t')
    # users = db.search_by_name(name)
    # print(users)
    phone = '182'
    users = db.search_by_phone(phone)
    for user in users:
        print(user)
    print(db.search_by_address('吉林省'))
    user = {
        'id': 0,
        'name': '正心',
        'job': '设备主管',
        'blood_group': 'A-',
        'username': 'min34',
        'sex': 'F',
        'address': '吉林省惠州县和平樊路h座 406759',
        'mail': 'yang70@yahoo.com',
        'birthdate': '1979-05-26',
        'id_card': '61092819490407596X',
        'phone': '14722525948'}
    db.add_user(user)
    db.close()
