import sys

n = int(input())
p = list(map(int, input().split()))
one = p[0]
p = p[1:n]

if n == 1:
    print(0)
    sys.exit()


if one == max(p):
    print(1)
elif one < max(p):
    print(max(p) - one + 1)
else:
    print(0)
