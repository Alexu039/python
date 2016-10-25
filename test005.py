def hanoi(n, x, y, z):
    if n == 1:
        # 直接从x移动到z
        print(x, '⇒', z)
    else:
        hanoi(n-1, x, z, y) # 将n-1个盘子从x移动到y
        print(x, '⇒', z)   # 将第n个盘子从x移动到z
        hanoi(n-1, y, x, z) # 将n-1个盘子从y移动到z

n = int(input("请输入要放到汉诺塔的盘子数目："))
hanoi(n, 'A','B','C')

