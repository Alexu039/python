def test(num):
    try:
        int(num)
    except ValueError as reason:
        print('出错了：' + str(reason))
    else:
        print('没有问题！')

num = input('请输入一个数字：')
test(num)
