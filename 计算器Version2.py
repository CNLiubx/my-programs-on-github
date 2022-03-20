import math

print('若想算加法，请输入1')
print('若想算减法，请输入2')
print('若想算乘法，请输入3')
print('若想算除法，请输入4')
print('若想算阶乘，请输入5')
print('若想算乘方，请输入6')
print('若想算平方根，请输入7')
print('若求最大公因数，请按8')
print('若求最小公倍数，请按9')
a = input('请输入你想要的运算符')

#计算加法
if a == '1':
    q = float(input('请输入第一个加数'))
    q2 = float(input('请输入第二个加数'))
    print(q + q2)

#计算减法
elif a == '2':
    w = float(input('请输入被减数'))
    w2 = float(input('请输入减数'))
    print(w - w2)

#计算乘法
elif a == '3':
    e = float(input('请输入第一个因数'))
    e2 = float(input('请输入第二个因数'))
    print(e * e2)

#计算除法
elif a == '4':
    r = float(input('请输入被除数'))
    r2 = float(input('请输入除数'))
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

#计算最大公因数，最小公倍数
elif a == '8':
    from math import gcd
    a = int(input('请输入第一个数:'))
    a2 = int(input('请输入二个数:'))
    a3 = gcd(a,a2)
    print(a,'和',a2,'的最大公因数为',a3)
    
elif a == '9':   
   from math import lcm
   b = int(input('请输入第一个数:'))
   b2 = int(input('请输入第二个数:'))
   b3 = lcm(b,b2)
   print(b,'和',b2,'的最小公倍数为',b3)

else:
    pass




input('按回车退出')
