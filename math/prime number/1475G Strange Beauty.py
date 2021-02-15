from sys import stdin, stdout


def strange_beauty(n, a_a):
    mx = max(a_a)
    dp = [0] * (mx + 1)
    cnt = [0] * (mx + 1)
    r = 0

    for a in a_a:
        cnt[a] += 1

    for i in range(1, mx + 1):
        if cnt[i] == 0:
            continue

        dp[i] += cnt[i]
        j = i * 2
        while j <= mx:
            dp[j] = max(dp[j], dp[i])
            j += i

    for a in a_a:
        # print(dp[a])
        r = max(r, dp[a])

    return n - r


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    r = strange_beauty(n, a_a)
    stdout.write(str(r) + '\n')
