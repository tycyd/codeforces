from sys import stdin, stdout
import sys

sys.setrecursionlimit(1500)

# 7 3
# n % 2 % 3 % 4 = n % 3 % 2 % 4
# 8 % 3 % 6 = 2 = 8 % 6 % 3 =
# 8 % 5 % 10 = 3 = 8 % 10 % 5 = 3
# 8 % 2 % 5, 8 % 5 % 2

# 1 => (2 3) 4 5 6 =>2
# 1 => (2, 3) 4 => 3*2 / 2
# 1 => any
# 2 => 2*1, 2*2, 2*3, 2*4
# 3 => 3*1, 3*2, 3*3, 3*4
# 4 => 4*1, 4*2, 4*3, 4*4

# prove
# `(x mod (ba)) mod a = (x-k*(ba) mod a`
#                     = x mod a`
MOD = 998244353
def modular_stability(n, k):
    if k > n:
        return 0

    res = 0
    # 1
    res = add(res, com(n - 1, k - 1))
    for i in range(2, n + 1):
        cnt = n // i

        if cnt == k:
            res = add(res, 1)
        elif cnt > k:
            res = add(res, com(cnt - 1, k - 1))

    return res


def add(x, y):
    x += y
    while x >= MOD:
        x -= MOD
    while x < 0:
        x += MOD
    return x


def mul(x, y):
    return (x * y) % MOD


def binpow(x, y):

    z = 1
    while y > 0:
        if y % 2 == 1:
            z = mul(z, x)
        x = mul(x, x)
        y //= 2
    return z


def inv(x):
    return binpow(x, MOD - 2)


def divide(x, y):
    return mul(x, inv(y))


faca = [1, 1]
def com(p1, p2):
    return divide(fac(p1), mul(fac(p1 - p2), fac(p2)))


def fac(n):
    if len(faca) > n:
        return faca[n]
    r = mul(n, fac(n - 1))
    faca.append(r)

    return r


if __name__ == '__main__':
    (n, k) = list(map(int, stdin.readline().split()))
    for i in range(1, n + 1):
        fac(i)

    print(modular_stability(n, k))
