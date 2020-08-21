from sys import stdin, stdout

MOD = 10**9+7


def fac(n, f):
    f.append(1)

    res = 1
    for i in range(1, n+1):
        res *= i
        res %= MOD
        f.append(res)


def inv(a):
    return bp(a, MOD - 2, MOD)


def bp(x, y, m):
    if y == 0:
        return 1

    p = bp(x, y // 2, m) % m
    p = (p * p) % m

    if y % 2 == 0:
        return p
    else:
        return (x * p) % m


def C(n, c, f):
    p1 = f[n]
    p2 = (f[n-c] * f[c]) % MOD
    invp = inv(p2)
    res = (p1 * invp) % MOD
    #res = p1 // p2

    return res


def cyclic_permutations(n, f):
    res = f[n] - 1
    res %= MOD

    for i in range(1, n):
        res -= C(n-1, i, f)
        res %= MOD

    return res


def cyclic_permutations2(n):
    a = 1
    f = 1
    for i in range(1, n):
        a *= 2
        f *= i
        a %= MOD
        f %= MOD
    f *= n
    f %= MOD
    res = (f - a) % MOD

    return res

n = int(stdin.readline())
#f = []
#fac(n, f)
#ans = cyclic_permutations(n, f)
ans = cyclic_permutations2(n)
stdout.write(str(ans) + '\n')
