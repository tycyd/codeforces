from sys import stdin, stdout


def solve(n, a_a):
    INF = 10000000000000
    dp = [[INF for _ in range(2001)] for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(0, n):
        for left in range(2001):
            if dp[i][left] == INF:
                continue

            # add to left side
            lidx = max(0, left - a_a[i])
            dp[i+1][lidx] = min(dp[i+1][lidx], dp[i][left] + a_a[i])

            # add to right side
            ridx = left + a_a[i]
            if ridx <= 2000:
                dp[i+1][ridx] = min(dp[i+1][ridx], max(dp[i][left] - a_a[i], 0))

    res = 10000000000000
    for left in range(2001):
        res = min(res, left + dp[n][left])
    return res


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    res = solve(n, a_a)
    stdout.write(str(res) + '\n')
