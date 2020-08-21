from sys import stdin, stdout
import random as r


def dfs(l, v_a, k, wk, rnd):

    if l > k:
        return 1 if wk == rnd else 0

    res = 0
    for i in range(1, l+1):
        res += dfs(l+1, v_a, k, wk + v_a[l][i], rnd)

    return res


def boboniu_walks_on_graph(n, m, k, e_a):
    MAX = 2 ** 31 - 1
    n_a = [0] * (n + 1)
    rnd = 0
    v_a = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(1, n + 1):
        n_a[i] = r.randint(0, MAX)
        rnd += n_a[i]

    for i in range(1, n + 1):
        for j in range(1, len(e_a[i]) + 1):
            v_a[len(e_a[i])][j] += n_a[e_a[i][j-1]]

    return dfs(1, v_a, k, 0, rnd)


n, m, k = map(int, stdin.readline().split())
e_a = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, stdin.readline().split())
    e_a[u].append(v)

ans = boboniu_walks_on_graph(n, m, k, e_a)
stdout.write(str(ans) + '\n')
