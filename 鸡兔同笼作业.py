h = int(input("请输入有多少个头"))
f = int(input('请输入有多少个脚'))
for c in range(0 , h):
    r = h - c
    if 2 * c + 4 * r == f:
        print('鸡的数量是'+str(c))
        print('兔的数量是'+str(r))


