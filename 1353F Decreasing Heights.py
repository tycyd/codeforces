from sys import stdin, stdout


def decreasing_heights(n, m, a_2d):
    MAX = 2**63 - 1
    res = MAX

    dp = [[MAX for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            v = a_2d[r][c] - r - c
            if a_2d[0][0] - v < 0:
                continue

            dp[0][0] = a_2d[0][0] - v
            for i in range(n):
                exit = True
                for j in range(m):
                    if i != 0 or j != 0:
                        dp[i][j] = MAX

                    cv = v + i + j
                    dif = a_2d[i][j] - cv
                    if dif < 0:
                        continue

                    if i > 0 and dp[i-1][j] != MAX:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + dif)

                    if j > 0 and dp[i][j-1] != MAX:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + dif)

                    if dp[i][j] != MAX:
                        exit = False
                if exit:
                    break

            res = min(res, dp[n-1][m-1])

            #print(dp)

    return res


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    a_2d = []
    for _ in range(n):
        a_2d.append(list(map(int, stdin.readline().split())))

    res = decreasing_heights(n, m, a_2d)
    stdout.write(str(res) + '\n')
