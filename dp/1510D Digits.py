from sys import stdin, stdout


n, d = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))

dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][a_a[0] % 10] = max(dp[0][a_a[0] % 10], a_a[0])

for i in range(1, n):
    for j in range(10):
        dp[i][j] = dp[i-1][j]
        if a_a[i] % 10 == j:
            dp[i][j] = max(dp[i][j], a_a[i])

    for j in range(10):
        if dp[i-1][j] > 1:
            k = (j * a_a[i]) % 10
            dp[i][k] = max(dp[i][k], dp[i-1][j] * a_a[i])

cur = dp[n-1][d]
res = []
idx = n-1
while cur > 1:
    if (cur % a_a[idx]) == 0 and (idx == 0 or (cur // a_a[idx]) == dp[idx - 1][(cur // a_a[idx]) % 10]):
        cur //= a_a[idx]
        res.append(a_a[idx])

    idx -= 1

if len(res) == 0:
    one = -1
    if d == 1:
        for a in a_a:
            if a == 1:
                one = 1
                break
    stdout.write(str(one))
else:
    stdout.write(str(len(res)) + '\n')
    stdout.write(' '.join(map(str, res)))
