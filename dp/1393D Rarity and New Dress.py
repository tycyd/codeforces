from sys import stdin, stdout


def rarity_and_new_dress(n, m, s_a):
    dp = [[1 for j in range(m)] for i in range(n)]
    res = 0

    for i in range(n):
        for j in range(m):
            if i > 1 and 0 < j < m - 1 and s_a[i][j] == s_a[i-1][j-1] == s_a[i-1][j] == s_a[i-1][j+1] == s_a[i-2][j]:
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1], dp[i-2][j])

            res += dp[i][j]

    return res


n, m = map(int, stdin.readline().split())
s_a = []
for _ in range(n):
    s_a.append(stdin.readline().strip())

ans = rarity_and_new_dress(n, m, s_a)
stdout.write(str(ans) + '\n')
