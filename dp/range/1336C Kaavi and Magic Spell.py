from sys import stdin, stdout


def kaavi_and_magic_spell(S, T):
    MOD = 998244353
    n = len(S)
    m = len(T)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if comp(S, T, 0, i):
            dp[i][i] = 1

    for l in range(2, n+1):
        for i in range(n - l + 1):
            if comp(S, T, l-1, i):
                # front
                dp[i][i+l-1] += dp[i+1][i+l-1]
                dp[i][i+l-1] %= MOD
            if comp(S, T, l-1, i+l-1):
                # back
                dp[i][i+l-1] += dp[i][i+l-2]
                dp[i][i+l-1] %= MOD

    r = 0
    for j in range(m-1, n):
        r += dp[0][j]
        r %= MOD
    r *= 2
    r %= MOD

    return r


def comp(S, T, i, j):
    if j >= len(T):
        return True
    return S[i] == T[j]


S = stdin.readline().strip()
T = stdin.readline().strip()
r = kaavi_and_magic_spell(S, T)
stdout.write(str(r) + '\n')
