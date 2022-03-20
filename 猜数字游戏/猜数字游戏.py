#引入生成随机数的模块
import random
cdsz = random.randint(1,100)
print("这是一个位于 1-100 之间的数")
for n in range(1,9):
    print("请输入猜测的数：")
    g = int(input())
    if g <= 0:
        print('猜的数字不能小于或等于0')
        break
    elif g > 100:
        print('猜的数字不能大于100')
        break
    if g < cdsz:
        print("太小啦")
    elif g > cdsz:
        print("太大啦")
    else:
        break
if g == cdsz :
    print("猜对啦，答案就是",cdsz)
elif g > 0 < cdsz:
    print("很遗憾，正确的答案应该是",cdsz)
elif g <= 0:
    pass
elif g > 100:
    pass
else:
    pass
input('按回车退出')

