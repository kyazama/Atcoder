n = int(input())
sa = [input().split() for _ in range(n)]

s = []
a = []

for x, y in sa:
    s.append(x)
    a.append(int(y))

p = a.index(min(a))
s = s[p:] + s[0:p]

for name in s:
    print(name)
