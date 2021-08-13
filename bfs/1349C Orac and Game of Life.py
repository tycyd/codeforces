from sys import stdin, stdout
from collections import deque
import sys


def union(u_a, i, j):
    ri = ufind(u_a, i)
    rj = ufind(u_a, j)
    u_a[ri] = rj


def ufind(u_a, i):
    if u_a[i] != i:
        u_a[i] = ufind(u_a, u_a[i])
    return u_a[i]


try:
    n, m, t = map(int, stdin.readline().split())
    s_a = []
    for _ in range(n):
        s_a.append(stdin.readline().strip())

    u_a = []
    o_a = []
    for i in range(n):
        for j in range(m):
            u_a.append(i*m + j)
            o_a.append(0)

    for i in range(n):
        for j in range(m):
            if i > 0 and s_a[i][j] == s_a[i-1][j]:
                union(u_a, (i-1)*m + j, i*m + j)
            if j > 0 and s_a[i][j] == s_a[i][j-1]:
                union(u_a, i*m + j-1, i*m + j)

    dic = {}
    q = deque()
    for i in range(len(u_a)):
        r = ufind(u_a, i)
        if r not in dic:
            dic[r] = [0, i] # 0: no adjacent, 1: has adjacent
        else:
            q.append(i)
            if dic[r][0] == 0:
                q.append(dic[r][1])
                dic[r][0] = 1

    step = 0
    da = [[1,0], [-1,0], [0,1], [0,-1]]
    unchange = False
    if len(q) == 0:
        unchange = True

    # 01011
    # 10110
    # 01101
    # 11010
    # 10101
    while len(q) > 0:
        l = len(q)
        for _ in range(l):
            cv = q.popleft()
            ci = cv // m
            cj = cv % m

            o_a[cv] = step
            for d in da:
                ni = ci + d[0]
                nj = cj + d[1]
                nv = ni * m + nj

                if 0 <= ni < n and 0 <= nj < m and dic[ufind(u_a, nv)][0] == 0:
                    q.append(nv)
                    dic[ufind(u_a, nv)][0] = 1

        step += 1

    for _ in range(t):
        ri, rj, p = map(int, stdin.readline().split())
        rv = (ri-1)*m + (rj-1)
        color = int(s_a[ri-1][rj-1])
        if unchange:
            res = color
        else:
            change = max(p - o_a[rv], 0)
            res = color ^ (change % 2)
        stdout.write(str(res) + '\n')
except:
    # print ["Unexpected error:", sys.exc_info()[0][1, 8].replace(' ', '')]
    print(sys.exc_info()[1])
    print(sys.exc_info()[0])
    print(sys.exc_info()[2])
