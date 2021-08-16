from sys import stdin, stdout


#   2   3
#               5    6
#          4             7
# 1                         8
n = int(stdin.readline())
xys_a = []
for _ in range(n):
    xys_a.append(list(map(int, stdin.readline().split())))
xys_a.sort(key=lambda a: a[0])

q_a = [xys_a[0][0] - xys_a[0][1]]
qs_a = [xys_a[0][0] - xys_a[0][1]]

MOD = 998244353
for i in range(1, n):
    l = 0
    h = i

    while l < h:
        m = (l + h) // 2
        if xys_a[i][1] <= xys_a[m][0]:
            h = m
        else:
            l = m + 1

    qr = xys_a[i][0] - xys_a[i][1]
    if l < i:
        qr += qs_a[i-1]
        qr %= MOD
        if l - 1 >= 0:
            qr -= qs_a[l-1]
            qr = (qr + MOD) % MOD
    q_a.append(qr)
    qs_a.append((qs_a[-1] + q_a[-1]) % MOD)

ans = 0
for i in range(n):
    if xys_a[i][2] == 1:
        ans += q_a[i]
        ans %= MOD
ans += xys_a[-1][0] + 1
ans %= MOD

stdout.write(str(ans))
