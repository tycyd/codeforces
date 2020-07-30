from sys import stdin, stdout


# 4 4 3
# 1 2
# 2 3
# 3 4
# 4 1
#
# 1 - 2
# |   |
# 4 - 3
if __name__ == '__main__':

    def dfs(i, pos, p, pnode, col, dic):

        pos[i] = p
        pnode[pos[i]] = i
        col[p%2].append(i)

        low = -1
        for v in dic[i]:
            if pos[v] != -1 and pos[i] - pos[v] > 1:
                low = max(low, pos[v])

        if low != -1:
            cyc = []
            for k in range(low, pos[i]+1):
                cyc.append(pnode[k])
            return cyc
        else:
            for v in dic[i]:
                if pos[v] == -1:
                    cyc = dfs(v, pos, p+1, pnode, col, dic)
                    if cyc is not None:
                        return cyc
        return None


    def ehabs_last_corolary(n, m, k, dic):
        pos = [-1] * (n+1)
        pnode = [-1] * (n+1)
        col = [[] for i in range(2)]
        cyc = dfs(1, pos, 1, pnode, col, dic)

        res = []
        if cyc is None:
            # tree
            k = k //2 + k % 2
            res.append(1)
            rc = []
            if len(col[0]) >= k:
                rc = col[0]
            else:
                rc = col[1]

            res.append([])
            for i in range(k):
                res[1].append(rc[i])

        else:
            # cycle
            if len(cyc) <= k:
                res.append(2)
                res.append([])
                for i in range(k):
                    res[1].append(cyc[i])
            else:
                res.append(1)
                res.append([])
                k = k // 2 + k % 2
                for i in range(k):
                    res[1].append(cyc[i*2])

        return res


    n, m, k = map(int, stdin.readline().split())
    dic = {}
    for i in range(m):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)

    res = ehabs_last_corolary(n, m, k, dic)
    stdout.write(str(res[0]) + '\n')
    if res[0] == 1:
        stdout.write(" ".join(map(str, res[1])) + '\n')
    else:
        stdout.write(str(len(res[1])) + '\n')
        stdout.write(" ".join(map(str, res[1])) + '\n')