from sys import stdin, stdout


def graph_coloring(n, n1, n2, n3, dic):
    s = [-1] * (n + 1)
    n13 = n1 + n3
    # [grp][cnt2], [grp][cnt-cnt2],   res = [True or False, [vertices]]
    dp = []
    res = []
    ttlcnt = 0

    for i in range(1, n+1):
        if s[i] != -1:
            continue

        v = dfs(i, 0, dic, s)
        l = len(v[0])
        r = len(v[1])
        if not v[2]:
            res.append('NO')
            return res

        ttlcnt += (l + r)

        cur = {}
        if len(dp) == 0:

            if l <= n2 and (ttlcnt - l) <= n13:
                cur[l] = [True, v[0]]

            if r <= n2 and (ttlcnt - r) <= n13:
                cur[r] = [True, v[1]]

        else:
            for k in dp[-1]:
                if k + l <= n2 and (ttlcnt - k - l) <= n13:
                    cur[k + l] = [True, v[0]]
                if k + r <= n2 and (ttlcnt - k - r) <= n13:
                    cur[k + r] = [True, v[1]]

        dp.append(cur)

    if n2 not in dp[-1]:
        res.append('NO')
    else:
        res.append('YES')

        c_a = [0] * n
        grp = len(dp)
        for grp in range(grp-1, -1, -1):
            cnt = len(dp[grp][n2][1])
            for vtx in dp[grp][n2][1]:
                c_a[vtx-1] = 2

            n2 -= cnt

        for i in range(len(c_a)):
            if c_a[i] == 0:
                if n1 > 0:
                    c_a[i] = 1
                    n1 -= 1
                elif n3 > 0:
                    c_a[i] = 3
                    n3 -= 1

        res.append(''.join(map(str, c_a)))

    return res


def dfs(vtx, color, dic, s):
    # 0's vertices, 1's vertices,
    res = [[], [], True]

    if s[vtx] != -1:
        if s[vtx] != color:
            res[2] = False
        return res

    s[vtx] = color

    res[color].append(vtx)
    if vtx in dic:
        for nxt in dic[vtx]:
            subres = dfs(nxt, color ^ 1, dic, s)
            if not subres[2]:
                return [[], [], False]

            res[0].extend(subres[0])
            res[1].extend(subres[1])

    return res


n, m = map(int, stdin.readline().split())
n1, n2, n3 = map(int, stdin.readline().split())

dic = {}
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    if u not in dic:
        dic[u] = []
    if v not in dic:
        dic[v] = []
    dic[u].append(v)
    dic[v].append(u)

res_a = graph_coloring(n, n1, n2, n3, dic)
for res in res_a:
    stdout.write(res + '\n')
