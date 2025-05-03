N = input()
S = input()
T = input()

S = S.replace("1", "l").replace("0", "o")
T = T.replace("1", "l").replace("0", "o")

if S == T:
    print("Yes")
else:
    print("No")
