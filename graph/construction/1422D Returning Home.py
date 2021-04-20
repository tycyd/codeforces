from sys import stdin, stdout
from heapq import *


def returning_home(n, m, sx, sy, fx, fy, x_a, y_a):
    x_sa = sorted(enumerate(x_a), key=lambda x: x[1])
    y_sa = sorted(enumerate(y_a), key=lambda x: x[1])

    # 0: starting point
    # 1-m: jumping point (x_a, y_a)
    # m+1-2m: x_sa
    # 2m+1-3m: y_sa
    # 3m+1: ending point
    g_a = [[] for _ in range(3*m+2)]

    # connect starting point to ending point
    add(0, 3*m+1, abs(sx-fx) + abs(sy-fy), g_a)

    for i in range(1, m+1):
        # connect sx, sy to x_sa, y_sa
        add(0, m + i, abs(sx-x_sa[i][1]), g_a)
        add(0, 2*m + i, abs(sy-y_sa[i][1]), g_a)

        # connect jumping point to ending point
        add(i, 3 * m + 1, abs(fx - x_a[i]) + abs(fy - y_a[i]), g_a)

        # connect jumping point to x_sa, y_sa
        px = x_sa[i][0]
        py = y_sa[i][0]

        add(px, i + m, 0, g_a)
        add(i + m, px, 0, g_a)
        add(py, i + 2 * m, 0, g_a)
        add(i + 2 * m, py, 0, g_a)

        # connect x_sa, y_sa
        if i != m:
            add(m + i, m + i + 1, x_sa[i + 1][1] - x_sa[i][1], g_a)
            add(m + i + 1, m + i, x_sa[i + 1][1] - x_sa[i][1], g_a)
            add(2 * m + i, 2 * m + i + 1, y_sa[i + 1][1] - y_sa[i][1], g_a)
            add(2 * m + i + 1, 2 * m + i, y_sa[i + 1][1] - y_sa[i][1], g_a)

    # connect x_sa, y_sa
    #for i in range(1, m):
    #    add(m + i, m + i + 1, x_sa[i + 1][1] - x_sa[i][1], g_a)
    #    add(m + i + 1, m + i, x_sa[i + 1][1] - x_sa[i][1], g_a)
    #    add(2*m + i, 2*m + i + 1, y_sa[i + 1][1] - y_sa[i][1], g_a)
    #    add(2*m + i + 1, 2*m + i, y_sa[i + 1][1] - y_sa[i][1], g_a)

    # connect jumping point to ending point
    #for i in range(1, m+1):
    #    add(i, 3*m + 1, abs(fx - x_a[i]) + abs(fy - y_a[i]), g_a)

    # connect jumping point to x_sa, y_sa
    #for i in range(1, m + 1):
    #    px = x_sa[i][0]
    #    py = y_sa[i][0]

    #    add(px, i+m, 0, g_a)
    #    add(i+m, px, 0, g_a)
    #    add(py, i + 2*m, 0, g_a)
    #    add(i + 2*m, py, 0, g_a)

    return dijkstra(g_a)


# i -> j
def add(i, j, c, g_a):
    g_a[i].append([j, c])


def dijkstra(g_a):
    q = [[0, 0]]
    # s = set()
    cal = [10**20] * (3*m+2)

    while len(q) > 0:
        w, i = heappop(q)
        # s.add(i)
        if i == 3*m + 1:
            return w

        if len(g_a[i]) == 0:
            continue

        for g in g_a[i]:
            # if g[0] in s or w + g[1] >= cal[g[0]]:
            if w + g[1] >= cal[g[0]]:
                continue
            cal[g[0]] = w + g[1]
            heappush(q, [w + g[1], g[0]])

    return -1


n, m = map(int, stdin.readline().split())
sx, sy, fx, fy = map(int, stdin.readline().split())
x_a = [-1]
y_a = [-1]
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    x_a.append(x)
    y_a.append(y)
r = returning_home(n, m, sx, sy, fx, fy, x_a, y_a)
stdout.write(str(r))
