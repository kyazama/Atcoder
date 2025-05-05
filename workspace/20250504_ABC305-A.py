N = int(input())

amari = N % 5
syou = N // 5

if amari < 3:
    print(syou * 5)
else:
    print((syou + 1) * 5)
