n = int(input())
s = input()

takahashi_win_num = 0
aoki_win_num = 0

for i in s:
    if i == "T":
        takahashi_win_num += 1
    else:
        aoki_win_num += 1

if takahashi_win_num > aoki_win_num:
    print("T")
elif takahashi_win_num < aoki_win_num:
    print("A")
elif s[-1] == "A":
    print("T")
else:
    print("A")
