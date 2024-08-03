# waether = input('请输入今天的天气')
# if waether == '晴' or waether == '多云':
#     print('去公园玩')
# else:
#     print('在家写代码')
# boy = input("请输入男生的人数")
# girl = input("请输入女生的人数")
# team = int(boy) + int(girl)
# if int(team) < 5:
#     print("来打扫街道")
# if int(team)>= 5 and int(boy) > int(girl):
#     print("负责种树")
# if int(team) > 5 and int(boy) <= int(girl):
#    print("负责采茶")
# 我们计算从0加到100的值
# a = 0
# x = 0
# while a < 101:
#     x += a
#     a += 1
# print(x)
# 我要做一个徒步的程序，徒步5公里结束

print("欢迎来徒步，输入yes/no，继续或者休息")
for km in range(0,6):
    if km == 0:
        print(f'以徒步{km}公里')
    else:
        print(f'以徒步{km}公里')
        if km < 5:
            n = input("需要休息吗？")
            if n=='no':
                continue
            else:
                print("你休息了10分钟")
        else:
            print('到达终点')
            break
