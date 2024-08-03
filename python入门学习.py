c = input("1是相加，2是相乘")
def a(shu,bei):
    b = float(shu)*float(bei)
    print(b)
def d(n,en):
    e = float(n)+float(en)
    print(e)
if int(c)>1:
    a(str(input("输入数")),str(input("输入倍")))
else:
    d(str(input("输入数")), str(input("输入数")))