from sys import stdin, stdout


def solve(s1, s2, next):
    # i => s1, j => s2
    dp = [[INF for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    dp[0][0] = 0
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if dp[i][j] == INF:
                continue

            if i < len(s1) and dp[i][j] < len(next) and next[dp[i][j]][ord(s1[i]) - ord('a')] < INF:
                dp[i+1][j] = min(dp[i+1][j], next[dp[i][j]][ord(s1[i]) - ord('a')] + 1)
            if j < len(s2) and dp[i][j] < len(next) and next[dp[i][j]][ord(s2[j]) - ord('a')] < INF:
                dp[i][j+1] = min(dp[i][j+1], next[dp[i][j]][ord(s2[j]) - ord('a')] + 1)

    return dp[len(s1)][len(s2)]


INF = 1e20
T = int(stdin.readline())
for _ in range(T):
    s = stdin.readline().strip()
    rs = stdin.readline().strip()
    next = [[INF for _ in range(26)] for _ in range(len(s))]

    for i in range(len(s)-1, -1, -1):
        if i < len(s)-1:
            for j in range(26):
                next[i][j] = next[i+1][j]
        next[i][ord(s[i]) - ord('a')] = i

    found = False

    if len(rs) == 1:
        if rs in s:
            found = True
    else:
        for p in range(1, len(rs)):
            s1 = rs[:p]
            s2 = rs[p:]

            if solve(s1, s2, next) < INF:
                found = True
                break

    if found:
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')

