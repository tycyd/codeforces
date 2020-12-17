from sys import stdin, stdout

# observation:
#    A         B
# 1,2,3,4 | 5,6,7,8
# for any p, q, index i.
# if pi belongs to A, then qi belongs to B.
# if qi belongs to A, then pi belongs to B.
# prove (contradiction):
# p: ____ i _____
# q: ____ i _____
# if both pi and qi belongs to A
# then p[0 : i] belongs to A, q[i : n-1] belongs to A.
# A has at least n + 1 elements, contradiction.

MOD = 998244353


def divide_and_sum(n, a_a):
    a_a.sort()
    s = (sum(a_a[n:2*n]) - sum(a_a[0:n])) % MOD
    c = Com(n, 2*n)
    r = (s * c) % MOD
    return r


def Com(p, t):
    c1 = 1
    c2 = 1
    for i in range(p):
        c1 *= (t-i)
        c1 %= MOD
        c2 *= (i+1)
        c2 %= MOD

    # MOD: c1 / c2 = c1 * c2^-1
    c = c1 * inverse(c2)
    c %= MOD
    return c


def inverse(a):
    return bpower(a, MOD-2)


def bpower(a, p):
    if p == 0:
        return 1

    r = bpower(a, p // 2)
    r *= r
    r %= MOD

    if p % 2 == 1:
        r *= a
    r %= MOD
    return r


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
r = divide_and_sum(n, a_a)
stdout.write(str(r))