"""name = '小蓝'
age = 3
cartoon = '小猪佩奇'"""
# name, age, cartoon = '小蓝', 3, '小猪佩奇'
# print(name + str(age) + '岁时最喜欢的动画片是' + cartoon)
# print(type(name))
import math

c = 0
age = input("你的年龄是：")
fage = input("你朋友的年龄")
a = 2024 - int(age)
print("你是" + str(a) + "年出生的")
print(type(age))
print(int((math.fabs(int(age) - int(fage)))))
