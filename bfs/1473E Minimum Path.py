from sys import stdin, stdout
import heapq

MAX = 100000000000000000


def solve(n, dic):
    # 00 sum
    # 01 sum+min
    # 10 sum-max
    # 11 sum+min-max
    dp = [[[MAX for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
    visited = [[[False for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]

    q = [(0, 1, 0, 0)]

    while len(q) > 0:

        # print(q)
        # print('----------------')

        v, i, st1, st2 = heapq.heappop(q)
        # dp[i][st1][st2] = v
        if visited[i][st1][st2]:
            continue

        visited[i][st1][st2] = True
        for next in dic[i]:
            w = next[1]
            ni = next[0]

            for nst1 in range(st1, 2):
                for nst2 in range(st2, 2):
                    nv = v + w
                    if st1 != nst1:
                        nv -= w
                    if st2 != nst2:
                        nv += w
                    if nv < dp[ni][nst1][nst2]:
                        dp[ni][nst1][nst2] = nv
                        heapq.heappush(q, (nv, ni, nst1, nst2))

    return dp


n, m = map(int, stdin.readline().split())
dic = {}
for _ in range(m):
    v, u, w = map(int, stdin.readline().split())
    if v not in dic:
        dic[v] = []
    if u not in dic:
        dic[u] = []
    dic[v].append([u, w])
    dic[u].append([v, w])

res = solve(n, dic)
for i in range(2, n + 1):
    stdout.write(str(res[i][1][1]) + ' ')
