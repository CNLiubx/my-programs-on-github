while True:
    print('若想算加减乘除四则运算，请输入1')
    print('若想算乘法拓展运算，请输入2')
    print('若想算日常需要数学运算，请输入3')
    a = input('请输入你想要的运算符')

    if a == '1':
        print('若想算加法，请输入1')
        print('若想算减法，请输入2')
        print('若想算乘法，请输入3')
        print('若想算除法，请输入4')
        ans0 = input('请输入你想要运算符所代表数字：')
        # 计算加法
        if ans0 == '1':
            q = float(input('请输入第一个加数'))
            q2 = float(input('请输入第二个加数'))
            q3 = q + q2
            print(q, '+', q2, '=', q3)

        # 计算减法
        elif ans0 == '2':
            w = float(input('请输入被减数'))
            w2 = float(input('请输入减数'))
            w3 = w - w2
            print(w, '-', w2, '=', w3)

        # 计算乘法
        elif ans0== '3':
            e = float(input('请输入第一个因数'))
            e2 = float(input('请输入第二个因数'))
            e3 = e * e2
            print(e, '*', e2, '=', e3)

        # 计算除法
        elif ans0 == '4':
            r = float(input('请输入被除数'))
            r2 = float(input('请输入除数'))
            r3 = r / r2
            print(r, '/', r2, '=', r3)

    # 计算阶乘
    if a == '2':
        print('若想算阶乘，请输入1')
        print('若想算乘方，请输入2')
        print('若想算平方根，请输入3')
        print('若求最大公因数，请输入4')
        print('若求最小公倍数，请输入5')
        ans1 = input('请输入你想要运算符所代表数字：')

        if ans1 == '1':
            t = int(input('请输入想要算的阶乘数'))
            num = 1
            for i in range(1, t + 1):
                num *= i
            print(t, '!为', num)

        # 计算乘方
        elif ans1 == '2':
            y = int(input('请输入底数'))
            y2 = int(input('请输入指数'))
            y3 = pow(y, y2)
            print(y, '的', y2, '次方为', y3)

        # 计算平方根
        elif ans1 == '3':
            print('注：仅支持算术平方根。')
            u = int(input('请输入开根数'))
            from math import sqrt
            u2 = sqrt(u)
            print( u, '的算术平方根为', u2)

        # 计算最大公因数，最小公倍数
        elif ans1 == '4':
            from math import gcd

            i = int(input('请输入第一个数:'))
            i2 = int(input('请输入二个数:'))
            i3 = gcd(i, i2)
            print(i, '和', i2, '的最大公因数为', i3)

        elif a == '5':
            from math import lcm

            o = int(input('请输入第一个数:'))
            o2 = int(input('请输入第二个数:'))
            o3 = lcm(o, o2)
            print(o, '和', o2, '的最小公倍数为', o3)
    if a == '3':
        print('若想算比例尺，请输入1')
        print('若想华氏度转化摄氏度,请输入2')
        print('若想摄氏度转化华氏度,请输入3')
        print('若想求π值，请输入4')
        print('若想判断质合数，请输入5')
        ans2 = input('请输入你想要运算符所代表数字：')
        if ans2 == '1':  # 计算比例尺
            print('请统一单位！')
            p = float(input('请输入图上距离'))
            p2 = float(input('请输入实际距离'))
            p3 = p2 / p
            p = 1.0
            print('这幅图的比例尺为：', p, ':', p3)

        elif ans2 == '2':
            def f(f):  # 设置华氏度转摄氏度函数
                c = f - 32
                c = c / 1.8
                return c
            aa = float(input('请输入华氏度：'))
            aa1 = f(aa)
            print('{}F转化为华氏度是{}C.'.format(aa, aa1))

        elif ans2 == '3':
            def c(c):  # 设置摄氏度转华氏度函数
                f = c * 1.8
                f += 32
                return f
            s = float(input('请输入摄氏度：'))
            s1 = c(s)
            print('{}C转化为摄氏度是{}F.'.format(s, s1))

        elif ans2 == '4':
            num = int(input('请输入数字'))
            for i in range(2, num):
                if num % i == 0:
                    print('%d 不是素数！' % num)
                    break
            else:
                print('%d 是素数！' % num)

        elif ans2 == '5':
            print('注意事项：pi取两位小数。')
            pi = 3.14  # pi值
            pi0 = float(input('请输入π的个数(包括小数)'))  # 输入π的个数，把输入的数转化为浮点数，便于计算
            pi1 = pi * pi0
            print(pi0, 'π是', pi1)
