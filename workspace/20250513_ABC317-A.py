n, h, x = map(int, input().split())
p = list(map(int, input().split()))

target_hitpoint = x - h

for i in range(n):
    if p[i] >= target_hitpoint:
        print(i + 1)
        break

# if p[i] >= target_hitpoint: こうじゃなくて
# p[i]+H >= x: このほうが変数名一つ減って良さそう
# でも，web開発的にはわかりやすい変数名があった方が良いと思っている
