from sys import stdin, stdout


MOD = 998244353
f_a = []


def build_fac(n):
    f_a.append(1)
    for i in range(1, n+1):
        r = i*f_a[-1]
        r %= MOD
        f_a.append(r)


def fac(n):
    return f_a[n]


def inv(n):
    return bpow(n, MOD-2)


def bpow(a, b):
    if b == 0:
        return 1
    r = bpow(a, b // 2)
    r *= r
    r %= MOD
    if b % 2 == 1:
        r *= a
        r %= MOD
    return r


def C(n, c):
    r1 = fac(n)
    r2 = inv(fac(c))
    r3 = inv(fac(n-c))
    r = r1 * r2
    r %= MOD
    r *= r3
    r %= MOD
    return r


def placing_rooks(n, k):

    if k > n:
        return 0

    r = 0
    for i in range(n - k):
        r1 = bpow(n-k-i, n)
        r1 *= C(n-k, i)
        r1 %= MOD
        if i % 2 == 0:
            r += r1
        else:
            r -= r1
        r %= MOD
    r *= C(n, n-k)
    r %= MOD

    if k > 0:
        r *= 2
        r %= MOD

    return r


n, k = map(int, stdin.readline().split())
build_fac(n)
r = placing_rooks(n, k)
stdout.write(str(r) + '\n')
