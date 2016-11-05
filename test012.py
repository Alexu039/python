import random as r
class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self) # 继承父类的init
        #super().__init__()  # 继承父类的init
        self.hungry = True  # 添加父类没有的属性

    def eat(self):
        if self.hungry:
            print("吃东西啦！")
            self.hungry = False
        else:
            print("已经吃饱了！")



        
