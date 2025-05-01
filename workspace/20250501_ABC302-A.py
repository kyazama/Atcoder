A, B = map(int, input().sprlt())

remainder = A % B
ans = A // B

if remainder == 0:
    print(ans)
else:
    print(ans + 1)
