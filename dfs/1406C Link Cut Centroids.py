import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**9)
threading.stack_size(16*2048*2048)

res = []
mx = 0


def link_cut_centroids(n, dic):
    global res
    global mx

    res = []
    mx = 2**31-1

    dfs(1, -1, dic, n)
    if len(res) == 1:
        x1 = 1
        y1 = dic[1][0]
        x2 = 1
        y2 = dic[1][0]
    else:
        n1 = res[0]
        n2 = res[1]
        for nxt in dic[n2]:
            if nxt != n1:
                x1 = n2
                y1 = nxt
                break
        x2 = n1
        y2 = nxt

    return [[x1, y1], [x2, y2]]


def dfs(node, pnode, dic, n):
    global res
    global mx

    cnt = 1
    mxcnt = 0
    for nxt in dic[node]:
        if nxt != pnode:
            lcnt = dfs(nxt, node, dic, n)
            mxcnt = max(lcnt, mxcnt)
            cnt += lcnt

    mxcnt = max(mxcnt, n - cnt)

    if mxcnt < mx:
        res = [node]
        mx = mxcnt
    elif mxcnt == mx:
        res.append(node)

    return cnt


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        dic = {}
        for _ in range(n-1):
            x, y = map(int, stdin.readline().split())
            if x not in dic:
                dic[x] = []
            if y not in dic:
                dic[y] = []
            dic[x].append(y)
            dic[y].append(x)

        res = link_cut_centroids(n, dic)
        stdout.write(' '.join(map(str, res[0])) + '\n')
        stdout.write(' '.join(map(str, res[1])) + '\n')


threading.Thread(target=solve).start()