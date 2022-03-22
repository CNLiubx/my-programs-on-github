a = input('请输入您的手机号码：')
a1 = len(a)
if a1 == 11:
    pass
elif a1 != 11:
    print('中国号码，不加空格(例:19945678969十一位)!!')
    
elif a[:3] <= '129':
    print('中国十一位普通号码!!')
else:
    pass
liantong = [130,131,132,145,155,156,166,171,175,176,186,185,196,1709]
yidong = [134,135,136,137,138,139,1440,147,148,150,151,152,157,158,159,167,171,172,178,182,183,184,187,188,195,197,198,1703,1706,1705]
dianxin = [133,149,153,162,173,177,180,181,189,199,1700,1701,1702]
guangdian = [192]
weixingtx = [1349,174]
wulian = [140,141,144,146,148]
weixingtx = [1349,174]
if int(a[:3]) in liantong or int(a[:4]) in liantong:
    print('你的手机号码的运营商是：联通')
elif int(a[:3]) in dianxin or int(a[:4]) in dianxin:
    print('你的手机号码的运营商是：电信')
elif int(a[:3]) in yidong or int(a[:4]) in yidong:
    print('你的手机号码的运营商是：移动')
elif int(a[:3])in wulian:
    print('您的手机号是物联网区段')
elif int(a[:3]) in guangdian:
    print('您的手机号为中国广电号段')
elif int(a[:3]) in weixingtx or int(a[:4]) in weixingtx:
    print('你的手机号码为卫星通信')

b = input('感谢您的使用，请打分鼓励！(1,2,3,4,5星):')
if b >= '6':
    print('感谢您的大力支持!(手动狗头)')
elif b == '1' or '2' or '3':
    print('我们会继续努力！')
elif b == '4' or '5':
    print('感谢您的鼓励，我们会继续加油')
else:
    pass
input('按回车退出')
