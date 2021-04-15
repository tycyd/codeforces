from sys import stdin, stdout


def glass_half_spilled(n, ab_a, a_a, sa, sb):

    dp = [[-1 for _ in range(sa + 1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for k in range(i, 0, -1):
            for A in range(a_a[i], -1, -1):
                if dp[k-1][A - ab_a[i-1][0]] == -1:
                    continue
                dp[k][A] = max(dp[k][A], dp[k-1][A - ab_a[i-1][0]] + ab_a[i-1][1])

    # print(dp)
    r_a = []
    for k in range(1, n+1):
        r = 0
        for A in range(sa, -1, -1):
            if dp[k][A] == -1:
                continue
            r = max(r, min(dp[k][A] / 2 + sb / 2, A))
        r_a.append(r)

    return r_a


n = int(stdin.readline())

ab_a = []
a_a = [0]
sb = 0
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    ab_a.append([a, b])
    a_a.append(a + a_a[-1])
    sb += b

r_a = glass_half_spilled(n, ab_a, a_a, a_a[-1], sb)
stdout.write(' '.join(map(str, r_a)))
