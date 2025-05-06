n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    sum = 0
    for j in range(7):
        sum += a[i * 7 + j]
    if i == n - 1:
        print(sum, end="\n")
    else:
        print(sum, end=" ")
