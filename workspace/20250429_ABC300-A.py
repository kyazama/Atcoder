N, A, B = map(int, input().split())
ans_list = list(map(int, input().split()))

ans = A + B

for i in range(len(ans_list)):
    if ans_list[i] == ans:
        print(i + 1)
