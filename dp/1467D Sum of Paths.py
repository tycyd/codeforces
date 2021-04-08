from sys import stdin, stdout


MOD = 1000000007


def sum_of_paths(n, k, a_a):
    dp = [[0 for _ in range(k+1)] for _ in range(n+2)]
    for i in range(1, n + 1):
        dp[i][0] = 1

    for j in range(1, k + 1):
        for i in range(1, n+1):
            dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
            dp[i][j] %= MOD

    cnt_a = []
    r = 0
    for i in range(1, n + 1):
        cnt_a.append(0)
        for j in range(k+1):
            cnt_a[-1] += dp[i][j] * dp[i][k-j]
            cnt_a[-1] %= MOD
        r += cnt_a[-1] * a_a[i-1]
        r %= MOD

    return [cnt_a, r]


n, k, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
cnt_a, r = sum_of_paths(n, k, a_a)
for _ in range(q):
    i, x = map(int, stdin.readline().split())
    r += cnt_a[i-1] * (x - a_a[i-1])
    r %= MOD
    a_a[i - 1] = x
    stdout.write(str(r) + '\n')
