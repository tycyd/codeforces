from sys import stdin, stdout


# 0 1 2 3 (4) 5
# left bound
def get_cmd(idx, clst):

    l = 0
    h = len(clst) - 1
    while l < h:
        m = (l + h + 1) // 2
        if clst[m][1] < idx:
            l = m
        else:
            h = m - 1

    return clst[l]


# a = [a] + [a]
# h[aha hah]a
def dfs(cmd, dic):
    tp = cmd[0]
    idx = cmd[1]
    hs = ''
    ts = ''
    r = 0
    if tp == 0:
        s = cmd[2]
        r = get_r(s)
        hs = s[:min(3, len(s))]
        ts = s[-min(3, len(s)):]
    else:
        s1 = cmd[2]
        s2 = cmd[3]
        if s1 == s2:
            ncmd = get_cmd(idx, dic[s1])
            r1 = r2 = dfs(ncmd, dic)
        else:
            ncmd1 = get_cmd(idx, dic[s1])
            r1 = dfs(ncmd1, dic)

            ncmd2 = get_cmd(idx, dic[s2])
            r2 = dfs(ncmd2, dic)

        hsa = r1[1] + r2[1]
        tsa = r1[2] + r2[2]
        hs = hsa[:min(3, len(hsa))]
        ts = tsa[-min(3, len(tsa)):]
        r = r1[0] + r2[0] + get_r(r1[2] + r2[1])

    return [r, hs, ts]


# haha
# end: h, ha, hah
# head: a, ah, aha

# end: aha
# head: hah
def get_r(s):
    r = 0
    h1 = a1 = h2 = 0
    for c in s:
        if c == 'h':
            h1 = 1
            h2 = a1
            a1 = 0
        elif c == 'a':
            r += h2
            a1 = h1
            h1 = 0
            h2 = 0
        else:
            h1 = a1 = h2 = 0

    return r


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    dic = {}
    for i in range(n-1):
        cmd_a = list(stdin.readline().split())
        if cmd_a[0] not in dic:
            dic[cmd_a[0]] = []

        if cmd_a[1] == ':=':
            dic[cmd_a[0]].append([0, i, cmd_a[2]])
        else:
            dic[cmd_a[0]].append([1, i, cmd_a[2], cmd_a[4]])
    cmd_a = list(stdin.readline().split())
    if cmd_a[1] == ':=':
        r = dfs([0, n-1, cmd_a[2]], dic)
    else:
        r = dfs([1, n-1, cmd_a[2], cmd_a[4]], dic)

    stdout.write(str(r[0]) + '\n')
