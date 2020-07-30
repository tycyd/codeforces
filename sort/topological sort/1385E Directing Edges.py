from sys import stdin, stdout


if __name__ == '__main__':
    def directing_edges(n, m, ind, dic, seq):
        q = []
        res = []

        for i in range(n):
            if ind[i] == 0:
                q.append(i)

        #while len(q) > 0:
        while q:
            #cnt = len(q)

            #for i in range(cnt):
            cur = q.pop()
            res.append(cur)

            if cur in dic:
                for next in dic[cur]:
                    ind[next] -= 1
                    if ind[next] == 0:
                        q.append(next)

        #print(res)

        if len(res) < n:
            stdout.write("NO\n")
        else:
            stdout.write("YES\n")

            pos = [0]*n
            for i in range(n):
                pos[res[i]] = i

            #print(pos)

            for sq in seq:
                if pos[sq[0]] < pos[sq[1]]:
                    #stdout.write(str(sq[0]+1) + " " + str(sq[1]+1) + '\n')
                    print(sq[0]+1, sq[1]+1)
                else:
                    #stdout.write(str(sq[1]+1) + " " + str(sq[0]+1) + '\n')
                    print(sq[1] + 1, sq[0] + 1)

    t = int(stdin.readline())
    for i in range(t):
        n, m = map(int, stdin.readline().split())
        dic = {}
        ind = [0] * n
        seq = []
        for j in range(m):
            t, x, y = map(int, stdin.readline().split())
            x -= 1
            y -= 1
            seq.append([x, y])

            if t == 1:
                if x not in dic:
                    dic[x] = []
                dic[x].append(y)
                ind[y] += 1

        directing_edges(n, m, ind, dic, seq)