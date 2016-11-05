class Base1():
    def base1(self):
        print("我是base1")
    def guess(self):
        print("猜猜我是谁？1")

class Base2():
    def base2(self):
        print("我是base2")
    def guess(self):
        print("猜猜我是谁？2")

class Base3(Base1,Base2):
    pass

class Base4(Base2,Base1):
    pass
