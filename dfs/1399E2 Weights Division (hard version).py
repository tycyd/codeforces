import sys
import threading
from sys import stdin, stdout
import heapq

sys.setrecursionlimit(10**4)
threading.stack_size(32*1024)

#         1
#  100  /   \ 10
#      3     5
# 123 /       \ 55
#   2          4

def weights_division_hard(n, S, dic):
    d_a = []
    lcnt, sum = dfs(-1, 1, 0, 0, d_a, dic)

    ans = 0
    while sum > S:
        #ans += 1
        (ds, wl) = heapq.heappop(d_a)

        ans += wl[2]

        wl[0] //= 2
        dif = (wl[0] * wl[1]) - (wl[0]//2) * wl[1]
        if wl[2] == 1:
            ds //= 2
            dif *= 2

        heapq.heappush(d_a, (-dif, wl))

        sum += ds

    return ans


def dfs(p, idx, w, c, d_a, dic):

    lcnt = 0
    sum = 0
    for nxt in dic[idx]:
        if p != nxt[0]:
            sr = dfs(idx, nxt[0], nxt[1], nxt[2], d_a, dic)

            lcnt += sr[0]
            sum += sr[1]

    if lcnt == 0:
        lcnt = 1
    sum += w * lcnt

    if p != -1:
        dif = (w * lcnt) - (w//2) * lcnt
        if c == 1:
            dif *= 2
        heapq.heappush(d_a, (-dif, [w, lcnt, c]))

    return [lcnt, sum]


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, S = map(int, stdin.readline().split())
        dic = {}
        for i in range(n-1):
            v, u, w, c = map(int, stdin.readline().split())
            if v not in dic:
                dic[v] = []
            if u not in dic:
                dic[u] = []
            dic[v].append([u, w, c])
            dic[u].append([v, w, c])

        ans = weights_division_hard(n, S, dic)
        stdout.write(str(ans) + '\n')


threading.Thread(target=solve).start()