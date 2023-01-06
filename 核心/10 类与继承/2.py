class Master(object):
    def __init__(self):
        self.secret = ['煎饼果子配方']

    def make_cake(self):
        print(f'运用{self.secret}制作了果子')


class Prentice(Master):
    pass


wanzi = Prentice()
print(wanzi.secret)
wanzi.make_cake()
print(wanzi.make_cake())
