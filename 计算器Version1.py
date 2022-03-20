import math


print('若想算加法，请输入1')
print('若想算减法，请输入2')
print('若想算乘法，请输入3')
print('若想算除法，请输入4')
print('若想算阶乘，请输入5')
print('若想算乘方，请输入6')
print('若想算平方根，请输入7')

a = input('请输入你想要的运算符')

#计算加法

if a == '1':
    q = input('请输入第一个加数')
    q2 = input('请输入第二个加数')
    q = float(q)
    q2 = float(q2)
    print(q + q2)

    #计算减法

elif a == '2':
    w = input('请输入被减数')
    w2 = input('请输入减数')
    w = float(w)
    w2 = float(w2)
    print(w - w2)

#计算乘法
elif a == '3':
    e = input('请输入第一个因数')
    e2 = input('请输入第二个因数')
    e = float(e)
    e2 = float(e2)
    print(e * e2)

#计算除法

elif a == '4':
    r = input('请输入被除数')
    r2 = input('请输入除数')
    r = float(r)
    r2 = float(r2)
    print(r / r2)

#计算阶乘
elif a == '5':
    t = int(input('请输入想要算的阶乘数'))
    num = 1
    for i in range(1,t + 1):
        num *= i
    print(num)

#计算乘方
elif a == '6':
    y = int(input('请输入底数'))
    y2 = int(input('请输入乘方数'))
    print(pow(y,y2))

#计算平方根
elif a == '7':
    u = int(input('请输入开根数'))
    from math import sqrt
    print(sqrt(u))

else:
    pass

input('按回车退出')