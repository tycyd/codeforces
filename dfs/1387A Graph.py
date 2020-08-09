import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**4)
threading.stack_size(32*1024)

#
# 1 ---- 2
#   \    |
#     \  |
#        3---4
#
# 0.5 0.5 1.5 -0.5
# b: 0.5 0.5 0.5 0.5
# r: 1   1   1
#
# Ax + B  (A = {-1,0,1}, )
# root:  x
#       -x + 1, -x + 2
#        x - 2
#

# 0: not possible
# 1: one solution
# 2: multiple solution
def dfs(u, c, v, dic, f_a, w_a):

    if f_a[v] is not None:
        # one solution
        #print(f_a[v])
        if f_a[v][0] == 0:
            if f_a[v][1] == -f_a[u][0]*f_a[v][2] + c - f_a[u][1]:
                return [1, f_a[v][2]]
            else:
                return [0]
        #a is same
        elif f_a[v][0] == -f_a[u][0]:
            #b is same
            if f_a[v][1] == c - f_a[u][1]:
                return [2]
            # b is not same
            else:
                return [0]
        #a is not same
        else:
            x = (c - f_a[u][1] - f_a[v][1]) / (f_a[v][0] + f_a[u][0])
            f_a[v][1] = f_a[v][0] * x + f_a[v][1]
            f_a[v][0] = 0
            f_a[v].append(x)
            return [1, x]

    w_a.append(v)

    if u == -1:
        f_a[v] = [1, 0]  # Ax + B
    else:
        f_a[v] = [-f_a[u][0], c - f_a[u][1]]

    if f_a[v][0] == 0:
        f_a[v].append(f_a[u][2])

    found = False
    x = 0
    if v in dic:
        for nxt in dic[v]:
            ans = dfs(v, nxt[1], nxt[0], dic, f_a, w_a)
            if ans[0] == 0:
                return [0]
            elif ans[0] == 1:
                found = True
                x = ans[1]

    if found:
        return [1, x]
    return [2]


def graph(N, M, dic):

    f_a = [None] * (N + 1)
    ans = [0] * N
    for i in range(1, N + 1):
        if f_a[i] is not None:
            continue

        w_a = []
        res = dfs(-1, 0, i, dic, f_a, w_a)
        if res[0] == 0:
            return ["NO"]
        elif res[0] == 1:
            #One solution
            for w in w_a:
                ans[w-1] = f_a[w][0] * res[1] + f_a[w][1]
        else:
            b = []
            for w in w_a:
                if f_a[w][0] > 0:
                    b.append(-f_a[w][1])
                else:
                    b.append(f_a[w][1])

            b.sort()
            x = (b[len(b) // 2] + b[len(b) // 2 - ((len(b) % 2) ^ 1)]) / 2

            for w in w_a:
                ans[w-1] = f_a[w][0] * x + f_a[w][1]

    return ["YES", ans]


def solve():
    N, M = map(int, stdin.readline().split())
    dic = {}
    for _ in range(M):
        a, b, c = map(int, stdin.readline().split())
        if a not in dic:
            dic[a] = []
        if b not in dic:
            dic[b] = []
        dic[a].append([b, c])
        dic[b].append([a, c])

    ans = graph(N, M, dic)
    stdout.write(ans[0] + '\n')
    if ans[0] == "YES":
        stdout.write(' '.join(map(str, ans[1])) + '\n')


threading.Thread(target=solve).start()
