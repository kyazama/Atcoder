# s = list(map(int, input().split()))
# count = 0

# for i in range(len(s)):
#     if i < len(s) - 1 and s[i + 1] > s[i]:
#         count += 1

#     if 100 <= s[i] and s[i] <= 675:
#         count += 1

#     if s[i] % 25 == 0:
#         count += 1

# if count == len(s) * 3 - 1:
#     print("Yes")
# else:
#     print("No")
import sys

s = list(map(int, input().split()))
for i in range(8):
    if i < 7 and s[i] > s[i + 1]:
        print("No")
        sys.exit()
    if s[i] < 100 or s[i] > 675 or s[i] % 25 != 0:
        print("No")
        sys.exit()
print("Yes")
