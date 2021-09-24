from sys import stdin, stdout
from collections import deque

MOD = 1000000007


# def build_cmb():
#     C = [[0]]
#     for _ in range(101):
#         cur = [1]
#         for i in range(len(C[-1])-1):
#             cur.append((C[-1][i] + C[-1][i+1]) % MOD)
#         cur.append(1)
#         C.append(cur)
#     return C

# passcal triangle
def dpfnc(dic2, k):
    n = len(dic2)
    keys = list(dic2)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        # for j in range(1, i+1):
        for j in range(1, k + 1):
            # dp[i][j] = dp[i-1][j-1] * dic2[keys[j-1]]
            dp[i][j] = dp[i - 1][j - 1] * dic2[keys[i - 1]]
            dp[i][j] %= MOD
            if j < i:
                # print(i-1)
                dp[i][j] += dp[i-1][j]
                dp[i][j] %= MOD

    return dp[n][k]


def solve(n, k, dic):
    if k == 2:
        # return C[n][k]
        return n * (n-1) // 2

    res = 0
    for i in range(1, n+1):
        res += bfs(i, n, k, dic)
        res %= MOD

    return res


def bfs(i, n, k, dic):
    visited = [False] * (n + 1)
    q = deque()
    visited[i] = True
    r = 0

    for rt in dic[i]:
        q.append((rt, rt))
        visited[rt] = True

    while len(q) > 0:
        dic2 = {}
        cnt = len(q)
        for nx, rt in q:
            if rt not in dic2:
                dic2[rt] = 1
            else:
                dic2[rt] += 1

        # cmb = 1
        # for key in dic2:
        #    cmb *= dic2[key]
        #    cmb %= MOD

        if len(dic2) >= k:
            # r += C[len(dic2)][k] * cmb
            # r %= MOD
            r += dpfnc(dic2, k)
            r %= MOD
        else:
            break

        for _ in range(cnt):
            cur, root = q.popleft()

            for nxt in dic[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                q.append((nxt, root))

    # stdout.write(str(i) + ' ' + str(r) + '\n')
    # print('-----')
    return r


# C = build_cmb()
t = int(stdin.readline())
for _ in range(t):
    stdin.readline()
    n, k = map(int, stdin.readline().split())
    dic = {}
    for _ in range(n-1):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)

    res = solve(n, k, dic)
    stdout.write(str(res) + '\n')

    #test = {1: 2, 2: 3, 3: 4, 4:2, 5:2}
    #print(dpfnc(test, 4))

