from sys import stdin, stdout


def tree_tag(n, a, b, da, db, dic):

    dis = distance(a, -1, b, dic)
    if dis <= da:
        return 'Alice'

    ln1 = dfs(1, -1, dic)
    ln2 = dfs(ln1[0], -1, dic)

    mxpath = ln2[1]
    if da*2 < db and mxpath > da*2:
        return 'Bob'

    return 'Alice'


def distance(node, pnode, b, dic):

    if node == b:
        return 0

    for nxt in dic[node]:
        if nxt != pnode:
            wk = distance(nxt, node, b, dic)
            if wk != -1:
                return 1 + wk

    return -1


def dfs(node, pnode, dic):

    sub = [-1, -1]
    for nxt in dic[node]:
        if nxt != pnode:
            wk = dfs(nxt, node, dic)
            if wk[1] > sub[1]:
                sub = wk

    if sub[0] != -1:
        return [sub[0], sub[1] + 1]
    else:
        return [node, 0]


t = int(stdin.readline())
for _ in range(t):
    n, a, b, da, db = map(int, stdin.readline().split())
    dic = {}
    for _ in range(n-1):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)
    ans = tree_tag(n, a, b, da, db, dic)
    stdout.write(ans + '\n')
