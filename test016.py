import time as t
class MyTimer:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '还未开始计时。'

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt

    def __add__(self, other):
        temp_prompt = '两个计时器一共经过了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                temp_prompt += (str(result[index])  + self.unit[index])
        return temp_prompt

    def start(self):
        if self.begin:
            print('计时已经开始，请调用stop()方法结束计时！')
        else:
            self.begin = t.localtime()
            print('计时开始！')

    def stop(self):
        if self.begin:
            self.end = t.localtime()
            self._calc()
            print('计时结束！')
        else:
            print('计时还未开始，请调用start()方法开始计时！')

    def _calc(self):
        self.prompt = '一共经过了'
        self.lasted = []
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])  + self.unit[index])

        # 初始化
        self.begin = 0
        self.end = 0

