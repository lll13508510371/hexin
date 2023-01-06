class Student:
    """学生信息类"""

    def __init__(self, name, chinese, math, english):
        """
        :param name: 姓名
        :param chinese: 语文成绩
        :param math:数学成绩
        :param english: 英语成绩
        """
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english  # 总分
