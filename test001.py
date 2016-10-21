import random

print ("欢迎来到xfl猜数字世界！")
secret = random.randint(1,10)
loop_cnt = 3
temp = input("请猜测一个1-10的数字：")
guess = int(temp)

assert (1 <= guess <= 10)

if guess == secret:
    print ("你猜对了，真棒！")
elif guess > secret:
    print ("你猜的有点大了！")
else:
    print ("你猜的有点小了！")
while guess != secret and loop_cnt > 1:
    temp = input("请重新猜测一个1-10的数字：")
    guess = int(temp)
    if guess == secret:
        print ("你猜对了，真棒！")
    elif guess > secret:
        print ("你猜的有点大了！")
    else:
        print ("你猜的有点小了！")

    loop_cnt = loop_cnt - 1

print ("游戏结束！")
