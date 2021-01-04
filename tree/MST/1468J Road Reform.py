from sys import stdin, stdout


def road_reform(n, m, k, xys_a, d1):
    xys_a.sort(key=lambda x: x[2])
    ua = [i for i in range(0, n+1)]

    res = 0
    d2 = 0
    for xys in xys_a:
        rx = ufind(ua, xys[0])
        ry = ufind(ua, xys[1])
        if rx != ry:
            union(ua, rx, ry)
            res += max(0, xys[2] - k)
            d2 = xys[2] - k

    if d2 < 0:
        if abs(d2) < d1:
            res = abs(d2)
        else:
            res = d1

    return res


def ufind(ua, i):
    if ua[i] != i:
        ua[i] = ufind(ua, ua[i])
    return ua[i]


def union(ua, i, j):
    ri = ufind(ua, i)
    rj = ufind(ua, j)
    ua[ri] = rj


t = int(stdin.readline())
for _ in range(t):
    n, m, k = map(int, stdin.readline().split())

    xys_a = []
    d1 = 10**9
    for _ in range(m):
        x, y, s = map(int, stdin.readline().split())
        xys_a.append([x, y, s])
        d1 = min(d1, abs(k - s))

    res = road_reform(n, m, k, xys_a, d1)
    stdout.write(str(res) + '\n')
