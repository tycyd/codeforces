from sys import stdin, stdout


# dp[i,j,cnt0]
def subsequences_of_length_two(n, k, s, t):
    dp = [[[-2**31 for _ in range(n+1)] for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0] = 0

    t1 = t[0]
    t2 = t[1]
    #if t1 == t2:
    #    cnt = 0
    #    for c in s:
    #        if c == t1:
    #            cnt += 1
    #    cnt = min(n, cnt + k)
    #    return cnt*(cnt-1)//2

    for i in range(1, n+1):
        for j in range(k+1):
            for cnt0 in range(i+1):
                c = s[i-1]

                # no action
                dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i-1][j][cnt0])

                if c == t2:
                    dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j][cnt0] + cnt0)
                    if c == t1 and cnt0 > 0:
                        dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j][cnt0-1] + cnt0-1)

                if c == t1 and cnt0 > 0:
                    dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j][cnt0 - 1])

                #change to t1
                if j > 0 and cnt0 > 0:
                    dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j - 1][cnt0 - 1])

                #change to t2
                if j > 0:
                    if t1 != t2:
                        dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j - 1][cnt0] + cnt0)
                    elif cnt0 > 0:
                        dp[i][j][cnt0] = max(dp[i][j][cnt0], dp[i - 1][j - 1][cnt0 - 1] + cnt0 - 1)

    res = 0
    for j in range(k + 1):
        for cnt0 in range(n + 1):
            res = max(res, dp[n][j][cnt0])

    return res


n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()
t = stdin.readline().strip()

ans = subsequences_of_length_two(n, k, s, t)
stdout.write(str(ans) + '\n')
