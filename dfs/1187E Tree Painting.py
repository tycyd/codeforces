import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**6)
threading.stack_size(32*1024)
# threading.stack_size(16*2048*2048)


def tree_painting(n, dic):
    memo = {}
    res = 0
    for i in range(1, n+1):
        r = 0
        for d in dic[i]:
            r += dfs(i, d, dic, memo)[1]
        res = max(r, res)

    return res + n


def dfs(pn, cn, dic, memo):
    if pn in memo and cn in memo[pn]:
        return memo[pn][cn]
    if pn not in memo:
        memo[pn] = {}

    r1 = 1
    r2 = 0
    for nn in dic[cn]:
        if nn == pn:
            continue
        r = dfs(cn, nn, dic, memo)
        r1 += r[0]
        r2 += r[1]
    r2 += r1

    memo[pn][cn] = [r1, r2]
    return memo[pn][cn]


def solve():
    n = int(stdin.readline())
    dic = {}
    for _ in range(n-1):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)

    r = tree_painting(n, dic)
    stdout.write(str(r) + '\n')


threading.Thread(target=solve).start()
