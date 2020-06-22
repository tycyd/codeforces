from sys import stdin, stdout

# 1 1
# 0 1
#
# 1 0 0
# 0 0 1
def palindromic_paths(n, m, a):
    q1 = [[0, 0]]
    q2 = [[n-1, m-1]]

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    res = 0
    step = 0

    vis = [[False for j in range(m)] for i in range(n)]
    vis[0][0] = True
    vis[n-1][m-1] = True

    while step < (m+n-1)//2:
        qcnt = len(q1)

        c0 = 0
        c1 = 0
        for i in range(qcnt):
            d1 = q1.pop(0)
            d2 = q2.pop(0)

            if a[d1[0]][d1[1]] == 1:
                c1 += 1
            else:
                c0 += 1

            if a[d2[0]][d2[1]] == 1:
                c1 += 1
            else:
                c0 += 1

            for dir in dirs:
                ni = d1[0] + dir[0]
                nj = d1[1] + dir[1]

                if ni < 0 or ni >= n or nj < 0 or nj >= m or vis[ni][nj]:
                    continue

                vis[ni][nj] = True
                q1.append([ni, nj])

            for dir in dirs:
                ni = d2[0] + dir[0]
                nj = d2[1] + dir[1]

                if ni < 0 or ni >= n or nj < 0 or nj >= m or vis[ni][nj]:
                    continue
                vis[ni][nj] = True
                q2.append([ni, nj])

        res += min(c1, c0)
        step += 1

    return res


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        (n, m) = list(map(int, stdin.readline().split()))
        a = []
        for j in range(n):
            a.append(list(map(int, stdin.readline().split())))
        stdout.write(str(palindromic_paths(n, m, a)) + '\n')
