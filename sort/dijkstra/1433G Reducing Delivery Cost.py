from sys import stdin, stdout
from heapq import *


def pre_calc_shortest_path(a, dic_r, c_a):
    h_a = [[0, a]]
    c_a[a][a] = 0

    while h_a:
        cur = h_a.pop()

        for p, w in dic_r[cur[1]]:
            if c_a[a][p] != -1 and c_a[a][p] <= cur[0] + w:
                continue

            c_a[a][p] = cur[0] + w
            h_a.append([cur[0] + w, p])

    return


def pre_calc_shortest_path2(a, dic_r, c_a):
    s = set()
    h_a = [[0, a]]

    while h_a:
        cur = heappop(h_a)
        c_a[a][cur[1]] = cur[0]

        s.add(cur[1])

        for p, w in dic_r[cur[1]]:
            if p in s:
                continue
            heappush(h_a, [w + cur[0], p])

    return


def reducing_delivery_cost(m_a, c_a, k_a, ores):
    res = ores

    for m in m_a:
        cur = ores
        for k in k_a:
            r = min(c_a[k[0]][m[0]] + c_a[k[1]][m[1]], c_a[k[0]][m[1]] + c_a[k[1]][m[0]])
            if c_a[k[0]][k[1]] > r:
                cur -= c_a[k[0]][k[1]] - r
        res = min(res, cur)

    return res


def calc_shortest_path(a, b, dic_r):
    s = set()
    h_a = [[0, a]]

    while h_a:
        cur = heappop(h_a)
        if cur[1] == b:
            return cur[0]

        s.add(cur[1])

        for p, w in dic_r[cur[1]]:
            if p in s:
                continue
            heappush(h_a, [w + cur[0], p])

    return -1


def reducing_delivery_cost2(m_a, c_a, dic_r, k_a, ores):

    res = ores

    for m in m_a:
        s = set()
        s.add(m[0])
        s.add(m[1])
        a_a = [{}, {}]
        q = [[[0, m[0]]], [[0, m[1]]]]

        while q[0] or q[1]:
            t = 0
            if not q[1]:
                t = 0
            elif not q[0]:
                t = 1
            elif q[0][0] < q[1][0]:
                t = 0
            else:
                t = 1

            cur = heappop(q[t])
            a_a[t][cur[1]] = cur[0]

            s.add(cur[1])

            for p, w in dic_r[cur[1]]:
                if p in s:
                    continue
                heappush(q[t], [w + cur[0], p])

        cur = ores
        for k in k_a:
            if k[0] in a_a[0]:
                if k[1] in a_a[1]:
                    if c_a[k[0]][k[1]] != -1 and c_a[k[0]][k[1]] > a_a[0][k[0]] + a_a[1][k[1]]:
                        cur -= c_a[k[0]][k[1]] - a_a[0][k[0]] - a_a[1][k[1]]
            elif k[0] in a_a[1]:
                if k[1] in a_a[0]:
                    if c_a[k[0]][k[1]] != -1 and c_a[k[0]][k[1]] > a_a[1][k[0]] + a_a[0][k[1]]:
                        cur -= c_a[k[0]][k[1]] - a_a[1][k[0]] - a_a[0][k[1]]

        res = min(res, cur)

    return res


n, m, k = map(int,  stdin.readline().split())
dic_r = {}
c_a = [[-1 for _ in range(n+1)] for _ in range(n+1)]
m_a = []

for _ in range(m):
    x, y, w = map(int,  stdin.readline().split())
    if x not in dic_r:
        dic_r[x] = []
    if y not in dic_r:
        dic_r[y] = []
    dic_r[x].append([y, w])
    dic_r[y].append([x, w])
    m_a.append([x, y])

#for i in range(1, n+1):
#    dic_r[i].sort(key=lambda x: x[1])

for i in range(1, n+1):
    pre_calc_shortest_path(i, dic_r, c_a)

ores = 0
k_a = []
for _ in range(k):
    a, b = map(int,  stdin.readline().split())
    k_a.append([a, b])

    #if c_a[a][b] == -1:
    #    c_a[a][b] = calc_shortest_path(a, b, dic_r)
    #    c_a[b][a] = c_a[a][b]
    ores += c_a[a][b]

res = reducing_delivery_cost(m_a, c_a, k_a, ores)
stdout.write(str(res))
