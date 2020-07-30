from sys import stdin, stdout


if __name__ == '__main__':

    def tree_modification(n, dic):
        wflg = True
        wcnt = bcnt = 0
        vs = set()
        qu = [1]
        vs.add(1)

        while len(qu) > 0:

            cnt = len(qu)

            if wflg:
                wcnt += cnt
            else:
                bcnt += cnt

            wflg = not wflg

            for i in range(cnt):
                cur = qu.pop(0)

                for nxt in dic[cur]:
                    if nxt not in vs:
                        vs.add(nxt)
                        qu.append(nxt)

        return min(wcnt, bcnt) - 1


    n = int(stdin.readline())
    dic = {}
    for i in range(n-1):
        u, v = map(int, stdin.readline().split())
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)

    stdout.write(str(tree_modification(n, dic)) + '\n')