n, p, q = map(int, input().split())
d = list(map(int, input().split()))

if min(d) + q < p:
    print(min(d) + q)
else:
    print(p)
