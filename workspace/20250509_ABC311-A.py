n = int(input())
s = list(input())

a_count = 0
b_count = 0
c_count = 0

for i in range(n):
    if s[i] == "A":
        a_count += 1

    if s[i] == "B":
        b_count += 1

    if s[i] == "C":
        c_count += 1

    if a_count > 0 and b_count > 0 and c_count > 0:
        print(i)
        break
