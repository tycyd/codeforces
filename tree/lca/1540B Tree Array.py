from sys import stdin, stdout


# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 2^4 = (2^3) + (2^3)
def dfs(cur, pre, d, dic, dep_a, jmp_a):

    dep_a[cur] = d
    jmp_a[cur][0] = pre
    for i in range(1, 10):
        jmp_a[cur][i] = jmp_a[jmp_a[cur][i-1]][i-1]

    for next in dic[cur]:
        if next == pre:
            continue

        dfs(next, cur, d+1, dic, dep_a, jmp_a)


def lca(a, b, dep_a, jmp_a):
    da = dep_a[a]
    db = dep_a[b]
    if da > db:
        return lca(b, a, dep_a, jmp_a)
    df = db - da

    for i in range(10):
        if ((1 << i) & df) != 0:
            b = jmp_a[b][i]

    while a != b:
        jmp = -1
        for i in range(9, -1, -1):
            if jmp_a[a][i] != jmp_a[b][i]:
                jmp = i
                break
        if jmp != -1:
            a = jmp_a[a][jmp]
            b = jmp_a[b][jmp]
        else:
            a = jmp_a[a][0]
            b = jmp_a[b][0]

    return a


# left stacks before right stacks consumed possibility
# dp[i,j] = (dp[i-1,j] + dp[i,j-1]) / 2
def get_percentage(n):
    per_a = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        per_a[0][j] = 1

    for i in range(1, n):
        for j in range(1, n):
            per_a[i][j] = (per_a[i-1][j] + per_a[i][j-1]) * bpow(2, MOD-2)
            #per_a[i][j] = (float(per_a[i - 1][j]) + float(per_a[i][j - 1])) / 2
            per_a[i][j] %= MOD
    return per_a


def bpow(a, b):
    if b == 0:
        return 1

    c = b // 2
    r = bpow(a, c)
    r *= r
    r %= MOD

    if b % 2 == 1:
        r *= a
        r %= MOD
    return r


MOD = 1000000007
dic = {}
n = int(stdin.readline())

for _ in range(n-1):
    x, y = map(int, stdin.readline().split())
    if x not in dic:
        dic[x] = []
    if y not in dic:
        dic[y] = []
    dic[x].append(y)
    dic[y].append(x)

per_a = get_percentage(n)

res = 0
for i in range(1, n+1):
    dep_a = [0] * (n + 1)
    jmp_a = [[j for _ in range(10)] for j in range(n+1)]

    # cal dep_a and jmp_a
    dfs(i, i, 0, dic, dep_a, jmp_a)

    # cal possibility
    for l in range(2, n+1):
        for r in range(l-1, 0, -1):
            node = lca(l, r, dep_a, jmp_a)
            res += per_a[dep_a[l] - dep_a[node]][dep_a[r] - dep_a[node]]
            res %= MOD

res *= bpow(n, MOD-2)
res %= MOD

stdout.write(str(res) + '\n')
