from sys import stdin, stdout
from collections import deque


def moving_to_the_capital(n, m, dic):
    step_a = [n] * (n + 1)
    fill_step_a(step_a, dic)

    memo = [[None, None] for _ in range(n+1)]

    for i in range(1, n+1):
        dfs(i, 0, dic, memo, step_a)

    res = [0] * n
    for i in range(n):
        if memo[i+1][0] is None:
            res[i] = memo[i+1][1]
        elif memo[i+1][1] is None:
            res[i] = memo[i+1][0]
        else:
            res[i] = min(memo[i+1][0], memo[i+1][1])
    return res


def dfs(i, st, dic, memo, step_a):

    if memo[i][st]:
        return memo[i][st]

    memo[i][st] = -1
    r = step_a[i]
    for nxt in dic[i]:
        if st == 1 and step_a[i] >= step_a[nxt]:
            continue

        lr = -1
        if step_a[i] >= step_a[nxt]:
            lr = dfs(nxt, 1, dic, memo, step_a)
        else:
            lr = dfs(nxt, st, dic, memo, step_a)

        if lr != -1:
            r = min(r, lr)

    memo[i][st] = r
    return r


def fill_step_a(step_a, dic):
    q = deque()
    s = set()

    q.append(1)
    s.add(1)
    step = 0

    while q:
        n = len(q)
        for _ in range(n):
            v = q.popleft()
            step_a[v] = step

            for nxt in dic[v]:
                if nxt in s:
                    continue
                s.add(nxt)
                q.append(nxt)

        step += 1


t = int(stdin.readline())
for _ in range(t):
    stdin.readline()
    n, m = map(int, stdin.readline().split())
    dic = {}
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []

        dic[u].append(v)

    res = moving_to_the_capital(n, m, dic)
    stdout.write(' '.join(map(str, res)) + '\n')
