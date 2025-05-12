n, h, x = map(int, input().split())
p = list(map(int, input().split()))

target_hitpoint = x - h

for i in range(n):
    if p[i] >= target_hitpoint:
        print(i + 1)
        break
