from sys import stdin, stdout

# 4
# -
# + 1
# + 2
# -
#
# -, +1, +2, -
#        +2


# i: current idx
# j: number of numbers smaller A[k][1]
# k: target idx
def dfs(i, j, k, A, dp):
    global MOD

    if j < 0:
        return 0

    if i == len(A):
        return 1

    if dp[i][j] is not None:
        return dp[i][j]

    res = 0
    if i == k:
        res = dfs(i+1, j, k, A, dp)
    else:
        # not choose
        res = dfs(i+1, j, k, A, dp)

        # choose
        if A[i][0] == '-':
            if i < k:
                res += dfs(i + 1, max(j - 1, 0), k, A, dp)
            else:
                res += dfs(i + 1, j - 1, k, A, dp)
            res %= MOD
        elif int(A[i][1]) > int(A[k][1]):
            res += dfs(i + 1, j, k, A, dp)
            res %= MOD
        else:  # int(A[i][1]) <= int(A[k][1])
            res += dfs(i + 1, j + 1, k, A, dp)
            res %= MOD

    dp[i][j] = res
    return res


n = int(stdin.readline())
A = []
for _ in range(n):
    A.append(stdin.readline().split())

res = 0
MOD = 998244353
for k in range(n):
    if A[k][0] == '-':
        continue

    dp = [[None for _ in range(n)] for _ in range(n)]

    res += int(A[k][1]) * dfs(0, 0, k, A, dp)
    res %= MOD

stdout.write(str(res))
