from sys import stdin, stdout


def ab_graph(n, m, sa):
    r = []
    if m % 2 == 1:
        r.append('YES')
        r.append([])
        for i in range(m+1):
            r[-1].append(i % 2 + 1)
        return r

    dicF = {}
    for i in range(n):
        for j in range(i+1, n):
            if sa[i][j] == sa[j][i]:
                r.append('YES')
                r.append([])
                for k in range(m + 1):
                    if k % 2 == 0:
                        r[-1].append(i + 1)
                    else:
                        r[-1].append(j + 1)
                return r

            if i not in dicF:
                dicF[i] = {}
            dicF[i][sa[i][j]] = j

            if j not in dicF:
                dicF[j] = {}
            dicF[j][sa[j][i]] = i

            p1 = 0
            p2 = 0
            p3 = 0
            if sa[i][j] in dicF[j]:
                p1 = i+1
                p2 = j+1
                p3 = dicF[j][sa[i][j]]+1
            elif sa[j][i] in dicF[i]:
                p1 = j+1
                p2 = i+1
                p3 = dicF[i][sa[j][i]]+1

            if p1 != 0 and p2 != 0 and p3 != 0:
                r.append('YES')
                r.append([])
                for k in range(m // 2):
                    if k % 2 == 0:
                        r[-1].append(p2)
                    else:
                        r[-1].append(p1)
                r[-1].reverse()
                for k in range(m // 2):
                    if k % 2 == 0:
                        r[-1].append(p2)
                    else:
                        r[-1].append(p3)
                return r

    r.append('NO')
    return r


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    sa = []
    for _ in range(n):
        sa.append(stdin.readline().strip())
    try:
        r = ab_graph(n, m, sa)
    except Exception as e:
        print(str(e).replace(" ", "_"))
    stdout.write(str(r[0]) + '\n')
    if len(r) > 1:
        stdout.write(' '.join(map(str, r[1])) + '\n')
