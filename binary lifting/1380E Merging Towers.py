from sys import stdin, stdout


if __name__ == '__main__':

    T = 0
    L = 20

    def dfs(a, b, tin, tout, dic, p, up):
        global T, L

        tin[a] = T
        T += 1
        p[a] = b
        up[a][0] = b

        for i in range(1, L):
            up[a][i] = up[up[a][i - 1]][i - 1]

        if a in dic:
            for c in dic[a]:
                dfs(c, a, tin, tout, dic, p, up)

        tout[a] = T
        T += 1

    def is_ancestor(a, b, tin, tout):
        return tin[a] <= tin[b] and tout[a] >= tout[b]

    def lca(a, b, tin, tout, p, up):
        if is_ancestor(a, b, tin, tout):
            return a

        for i in range(L-1, -1, -1):
            if not is_ancestor(up[a][i], b, tin, tout):
                a = up[a][i]

        return p[a]

    n, m = map(int, stdin.readline().split())
    idx = list(map(int, stdin.readline().split()))
    idx.insert(0, 0)

    cur = [0]*(m+1)
    for i in range(1, m+1):
        cur[i] = i

    dic = {}
    for i in range(m-1):
        a, b = map(int, stdin.readline().split())
        nidx = m+1+i
        dic[nidx] = [cur[a], cur[b]]
        cur[a] = nidx

    root = m*2-1
    tin = [0] * (2 * n + 1)
    tout = [0] * (2 * n + 1)
    p = [0] * (2 * n + 1)
    up = [[0 for j in range(L)] for i in range((2 * n + 1))]
    dfs(root, root, tin , tout, dic, p, up)

    psum = [0] * (m+2)
    for i in range(1, n):
        t = lca(idx[i], idx[i+1], tin, tout, p, up)
        if t <= m:
            psum[1] += 1
        else:
            psum[t - m + 2] += 1

    #print(psum)
    for i in range(1, m+1):
        psum[i+1] += psum[i]

    #print(psum)

    for i in range(2, m+2):
        stdout.write(str(n - 1 - psum[i]) + '\n')
