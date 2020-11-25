from sys import stdin, stdout


def the_hard_work_of_paparazzi(r, n, txy_a):
    MIN = -2**64
    dp = [MIN] * n
    ans = 0

    for i in range(n):

        if abs(txy_a[i][1] - 1) + abs(txy_a[i][2] - 1) <= txy_a[i][0]:
            dp[i] = 1

        lower = max(0, i - 2*r)
        for j in range(lower, i):
            dif_p = abs(txy_a[i][1] - txy_a[j][1]) + abs(txy_a[i][2] - txy_a[j][2])
            dif_t = txy_a[i][0] - txy_a[j][0]
            if dif_p <= dif_t and dp[j] != MIN:
                dp[i] = max(dp[i], 1 + dp[j])

        ans = max(ans, dp[i])

    return ans


r, n = map(int, stdin.readline().split())
txy_a = [[0, 1, 1]]

MIN = -2**64
dp = [MIN] * (n+1)
dp[0] = 0
ans = 0

for i in range(1, n+1):
    txy_a.append(list(map(int, stdin.readline().split())))

    lower = max(0, i - 2 * r)
    for j in range(lower, i):
        dif_p = abs(txy_a[i][1] - txy_a[j][1]) + abs(txy_a[i][2] - txy_a[j][2])
        dif_t = txy_a[i][0] - txy_a[j][0]

        if dif_p <= dif_t and dp[j] != MIN:
            dp[i] = max(dp[i], 1 + dp[j])

    ans = max(ans, dp[i])

#res = the_hard_work_of_paparazzi(r, n, txy_a)
#stdout.write(str(res))
stdout.write(str(ans))
