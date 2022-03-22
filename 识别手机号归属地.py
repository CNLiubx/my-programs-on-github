a = input('请输入您的手机号码：')
a1 = len(a)
if a1 == 11:
    pass
else:
    print('中国号码，不加空格(例:19945678969十一位)!!')
if a[:3] <= '129':
    print('中国十一位普通号码!!')
else:
    pass
liantong = [130,131,132,155,156,186,185,1709]
yidong = [134,135,136,137,138,139,150,51,152,157,158,159,182,183,187,188,1705]
dianxin = [133,149,153,173,177,180,181,189,199,1700]
if int(a[:3]) in liantong or int(a[:4]) in liantong:
    print('你的手机号码是：联通')
elif int(a[:3]) in dianxin or int(a[:4]) in dianxin:
    print('你的手机号码是：电信')
elif int(a[:3]) in yidong or int(a[:4]) in yidong:
    print('你的手机号码是：移动')

b = input('感谢您的使用，请打分鼓励！(1,2,3,4,5星):')
if b >= '6':
    pass
elif b == '1' or '2' or '3':
    print('我们会继续努力！')
elif b == '4' or '5':
    print('感谢您的鼓励，我们会继续加油')
else:
    pass
input('按回车退出')