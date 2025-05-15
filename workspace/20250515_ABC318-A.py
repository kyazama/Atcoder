n, m, p = map(int, input().split())
count = 0

while True:
    if n < m + count * p:
        break
    count += 1

print(count)


# n, m, p = map(int, input().split())
# res = 0
# while m <= n:
#     res += 1
#     m += p
# print(res)
