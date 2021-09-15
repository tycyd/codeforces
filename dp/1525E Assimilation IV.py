from sys import stdin, stdout

# 1: {}
# 2: {}
# 3: 1
# 4: 2
# 5: 3
#
#  1  2  3 4 5 6
#        1         F5
# (1)(1)   2       F2 * F3
#          1       F5
#            3
#
# 1 2 3 4 5     DP
# X X           2
# Y Y Y         2*2
# Z Z Z Z       2*2*2
#
#
# 3 5
# 1 4 4 3 4
# 1 4 1 4 2
# 1 4 4 4 3

# 2 of 10,  10 * 9 = F10 / F8
MOD = 998244353
FA = [1]
for i in range(1, 21):
    FA.append((i*FA[-1]) % MOD)


def bpow(a, b):
    if b == 0:
        return 1
    c = bpow(a, b//2)
    c *= c
    c %= MOD
    if b % 2 == 1:
        c *= a
        c %= MOD
    return c


def solve(n, m, d_a):
    res = 0
    for j in range(m):
        wk = []
        for i in range(n):
            wk.append(d_a[i][j])
        wk.sort()
        #  1  2  3 4 5      total F4 = 5*4*3*2*1 = 120
        #        1 1 1      F4 * 3  = 24 * 3   = 72
        # (1)(1) 2 2 2      2*F3 * 3 = 12 * 3 = 36
        # (1)(2)     3     2*1 * F2  = 2 * 2 = 4
        #
        #  1  2  3 4 5      total F4 = 5*4*3*2*1 = 120
        #        1 1 1      F4 * 3  = 24 * 3   = 72
        # (1)(1)   2 2      2*F3 * 2 = 12 * 2 = 24
        # (1)(2)(2)  3      2*(3-1) * F2  = 4 * 2 = 8

        dp = 1
        for k in range(1, len(wk) + 1):
            d = wk[k-1]
            # exceed max distance
            if d > n:
                break

            r = FA[n - k] * dp
            r %= MOD
            r *= n - d + 1
            r %= MOD

            res += r
            res %= MOD

            dp *= d - 1 - (k - 1)
            if dp <= 0:
                break

    res *= bpow(FA[n], MOD-2)
    res %= MOD
    return res


n, m = map(int, stdin.readline().split())
d_a = []
for _ in range(n):
    d_a.append(list(map(int, stdin.readline().split())))
res = solve(n, m, d_a)
stdout.write(str(res))
