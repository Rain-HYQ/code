s = int(input("数字"))
s += 1
for n in range(1,s):
    for j in range(1, n+1):
        print(f'{n} x {j} = {n * j}\t ',end='')