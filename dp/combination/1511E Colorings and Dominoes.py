from sys import stdin, stdout


MOD = 998244353
b1 = 0
b2 = 0
b3 = 0


def colorings_and_dominoes(n, m, s_a):
    r = 0
    c = sum(s.count('o') for s in s_a)
    b_a = [1 for _ in range(c+1)]

    if c >= 2:
        b_a[2] = bpow(c-2)
    if c >= 3:
        b_a[3] = bpow(c-3)

    for i in range(4, c+1, 1):
        if i % 2 == 0:
            b_a[i] = b_a[i-1] + bpow(c-i)
        else:
            b_a[i] = b_a[i-2] + bpow(c-i)
        b_a[i] %= MOD

    for i in range(n):
        uc = 0
        for j in range(m):
            if s_a[i][j] == 'o':
                uc += 1
            else:
                uc = 0

            if uc >= 2:
                r += b_a[uc]
                r %= MOD

    for j in range(m):
        uc = 0
        for i in range(n):
            if s_a[i][j] == 'o':
                uc += 1
            else:
                uc = 0

            if uc >= 2:
                r += b_a[uc]
                r %= MOD

    return r


def bpow(c):
    if c == 0:
        return 1

    r = bpow(c // 2)
    r *= r
    r %= MOD

    if c % 2 == 1:
        r *= 2
        r %= MOD

    return r


n, m = map(int, stdin.readline().split())
s_a = []
for _ in range(n):
    s_a.append(stdin.readline().strip())
r = colorings_and_dominoes(n, m, s_a)
stdout.write(str(r) + '\n')
