def factorial(n):
    if n == 1 or n == 2:
        return 1
    else:
        return factorial(n - 1) + factorial(n - 2)

number = int(input("请输入一个正整数表示经过的月数(递归)："))
result = factorial(number)
print("经过%d 个月之后一共有：%d 对兔子(递归)" % (number, result))

def factorial1(n):
    sum = 0
    cnt = 1
    n1 = 1
    n2 = 1
    while (cnt <= n):
        if cnt == 1:
            n1 = 1
            sum = n1
        elif cnt == 2:
            n2 = 1
            sum = n2
        else:
            sum = n1 + n2
            n1 = n2
            n2 = sum
        cnt += 1

    return sum

number = int(input("请输入一个正整数表示经过的月数(迭代)："))
result = factorial1(number)
print("经过%d 个月之后一共有：%d 对兔子(迭代)" % (number, result))
