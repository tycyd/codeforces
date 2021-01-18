from sys import stdin, stdout


def dfs(l, r, dp, a_a):
    if l == r:
        return a_a[l]
    if l+1 == r:
        if a_a[l] == a_a[r]:
            return a_a[l] + 1
        else:
            return -1

    if dp[l][r] != 10**6:
        return dp[l][r]

    dp[l][r] = -1
    for m in range(l, r):
        r1 = dfs(l, m, dp, a_a)
        r2 = dfs(m+1, r, dp, a_a)
        if r1 > 0 and r1 == r2:
            dp[l][r] = r1 + 1
            return dp[l][r]

    return dp[l][r]


def array_shrinking(n, a_a):
    dp = [[10**6 for _ in range(n)] for _ in range(n)]
    dp2 = [10**6 for _ in range(n)]
    for i in range(n):
        dp2[i] = min(i + 1, dp2[i])
        for j in range(i, n):
            r = dfs(i, j, dp, a_a)
            if r != -1:
                if i > 0:
                    dp2[j] = min(dp2[i-1] + 1, dp2[j])
                else:
                    dp2[j] = min(1, dp2[j])

    return dp2[n-1]


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
res = array_shrinking(n, a_a)
stdout.write(str(res))
