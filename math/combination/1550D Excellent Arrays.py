from sys import stdin, stdout
import sys

# 1 2 3 4
#
# 1+k, 2+k | 3-k, 4-k
# 1-k >= l => k <= 1-l
# n+k <= r => k <= r-n
# if k <= min(1-l, r-n)
# then C(n,n/2) even, C(n,n/2) + C(n, n/2+1)
#

MOD = 1000000007


def bpow(a, b):
    global MOD

    if b == 0:
        return 1
    c = bpow(a, b//2)
    c *= c
    c %= MOD
    if b % 2 == 1:
        c *= a
        c %= MOD
    return c


def factorial():
    global MOD

    fa = [1]
    for i in range(1, 200001):
        fa.append(fa[-1]*i)
        fa[-1] %= MOD

    return fa


def inv(fa):
    global MOD

    iv = [1]
    for i in range(1, 200001):
        iv.append(bpow(fa[i], MOD-2))

    return iv


def C(fa, iv, a, b):
    if a < b or a < 0 or b < 0:
        return 0

    global MOD
    r = fa[a] * iv[a-b]
    r %= MOD
    r *= iv[b]
    r %= MOD

    return r


def solve(n, l, r):
    global MOD, fa, iv
    res = 0

    k = min(1-l, r-n)
    if k >= 1:
        res = k * C(fa, iv, n, n//2)
        res %= MOD

        if n % 2 == 1:
            res += k * C(fa, iv, n, n//2 + 1)
            res %= MOD

    # 1 2 3 4
    lf = 1
    rt = n
    while True:
        k += 1
        #lf = max(1, l + k)
        #rt = min(n, r - k)
        while lf - k < l:
            lf += 1
        while rt + k > r:
            rt -= 1

        if rt - lf + 1 < 0:
            break

        res += C(fa, iv, rt - lf + 1, n//2 - lf + 1)
        res %= MOD

        if n % 2 == 1:
            res += C(fa, iv, rt - lf + 1, n//2 + 1 - lf + 1)
            res %= MOD

    return res


try:
    fa = factorial()
    iv = inv(fa)
    t = int(stdin.readline())

    for _ in range(t):
        n, l, r = map(int, stdin.readline().split())
        res = solve(n, l, r)
        stdout.write(str(res) + '\n')
except:
    print(sys.exc_info())
