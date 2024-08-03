# print("欢迎来到平均数计算器")
# lest = []
# q = None
# m = 0
# a = 0
# while q !="quit":
#     q = input("请输入数字,输入‘quit’退出")
#     if q!="quit":
#         lest.append(q)
#         a = a+int(q)
#         m+=1
# print(lest)
# print(a)
# print("您输入了"+str(m)+"个数字")
# print("平均数是" + str(a/m))

print("欢迎来到平均数计算器")
lest = []
q = None
m = 0
a = 0
while True:
    q = input("请输入数字,输入‘quit’退出")
    if q!="quit":
        lest.append(q)
        a = a+int(q)
        m+=1
    else:
        break
print(lest)
print(a)
print("您输入了"+str(m)+"个数字")
print("平均数是" + str(a/m))