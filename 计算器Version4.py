print('若想算加法，请输入1')
print('若想算减法，请输入2')
print('若想算乘法，请输入3')
print('若想算除法，请输入4')
print('若想算阶乘，请输入5')
print('若想算乘方，请输入6')
print('若想算平方根，请输入7')
print('若求最大公因数，请输入8')
print('若求最小公倍数，请输入9')
print('若想算比例尺，请输入0')
print('若想华氏度转化摄氏度,请输入a')
print('若想摄氏度转化华氏度,请输入b')

a = input('请输入你想要的运算符')

#计算加法
if a == '1':
    q = float(input('请输入第一个加数'))
    q2 = float(input('请输入第二个加数'))
    q3 = q + q2
    print(q,'+',q2,'=',q3)

#计算减法
elif a == '2':
    w = float(input('请输入被减数'))
    w2 = float(input('请输入减数'))
    w3 = w - w2
    print(w ,'-',w2,'=',w3)

#计算乘法
elif a == '3':
    e = float(input('请输入第一个因数'))
    e2 = float(input('请输入第二个因数'))
    e3 = e * e2
    print(e,'*',e2,'=',e3)

#计算除法
elif a == '4':
    r = float(input('请输入被除数'))
    r2 = float(input('请输入除数'))
    r3 = r/r2
    print(r,'/',r2,'=',r3)

#计算阶乘
elif a == '5':
    t = int(input('请输入想要算的阶乘数'))
    num = 1
    for i in range(1,t + 1):
        num *= i
    print(t,'!为',num)

#计算乘方
elif a == '6':
    y = int(input('请输入底数'))
    y2 = int(input('请输入指数'))
    y3 = pow(y,y2)
    print(y,'的',y2,'次方为',y3)

#计算平方根
elif a == '7':
    u = int(input('请输入开根数'))
    from math import sqrt
    u2 = sqrt(u)
    print('根号',u,'为',u2)

#计算最大公因数，最小公倍数
elif a == '8':
    from math import gcd
    i = int(input('请输入第一个数:'))
    i2 = int(input('请输入二个数:'))
    i3 = gcd(i,i2)
    print(i,'和',i2,'的最大公因数为',i3)
    
elif a == '9':   
   from math import lcm
   o = int(input('请输入第一个数:'))
   o2 = int(input('请输入第二个数:'))
   o3 = lcm(o,o2)
   print(o,'和',o2,'的最小公倍数为',o3)

elif a == '0':           #计算比例尺
    print('请统一单位！')
    p = float(input('请输入图上距离'))
    p2 = float(input('请输入实际距离'))
    p3 = p2 / p
    p = 1.0
    print('这幅图的比例尺为：',p,':',p3)

elif a == 'a':
    def f(f):    #设置华氏度转摄氏度函数
        c = f - 32
        c = c / 1.8
        return c
    aa = float(input('请输入华氏度：'))
    aa1 = f(aa)
    print('{}F转化为华氏度是{}C.'.format(aa , aa1))

elif a == 'b':
    def c(c):    #设置摄氏度转华氏度函数
        f = c * 1.8
        f += 32
        return f
    s = float(input('请输入摄氏度：'))
    s1 = c(s)
    print('{}C转化为摄氏度是{}F.'.format(s , s1))

else:
    pass
input('按回车退出')
