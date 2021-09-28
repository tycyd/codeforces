from sys import stdin, stdout


def update_bit(i, bit_a, v):
    while i < len(bit_a):
        bit_a[i] += v
        i += i & -i


def query_bit(i, bit_a):
    r = 0
    while i > 0:
        r += bit_a[i]
        i -= i & -i
    return r


def solve(n, a_a):
    sa_a = list(set(a_a))
    sa_a.sort()
    dic = {}
    for i in range(1, len(sa_a) + 1):
        dic[sa_a[i-1]] = i

    res = 0
    ttl = 0
    bit_a = [0] * (len(sa_a) + 1)
    for a in a_a:
        idx = dic[a]
        res += min(query_bit(idx-1, bit_a), ttl - query_bit(idx, bit_a))
        ttl += 1
        update_bit(idx, bit_a, 1)

    return res


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    res = solve(n, a_a)
    stdout.write(str(res) + '\n')
