from sys import stdin, stdout


def identify_the_operations(n, k, a_a, b_a):
    MOD = 998244353
    idx_a = [0] * (n+1)
    bit_a = [0] * (n+1)
    res = 1
    for i in range(n):
        idx_a[a_a[i]] = i
        bit_update(bit_a, i, 1)

    b_s = set(b_a)
    for b in b_a:
        b_s.remove(b)

        cv = bit_query(bit_a, idx_a[b])
        h = right_bs(idx_a[b] + 1, n - 1, cv, bit_a)
        l = left_bs(0, idx_a[b] - 1, cv, bit_a)
        if l != -1 and a_a[l] in b_s:
            l = -1
        if h != -1 and a_a[h] in b_s:
            h = -1

        mul = 0
        if h == -1 and l == -1:
            return 0
        elif h == -1:
            mul = 1
            bit_update(bit_a, l, -1)
        elif l == -1:
            mul = 1
            bit_update(bit_a, h, -1)
        else:
            mul = 2
            bit_update(bit_a, h, -1)

        res *= mul
        res %= MOD

    return res


def right_bs(l, h, cv, bit_a):
    if l > h or cv == bit_query(bit_a, h):
        return -1

    while l < h:
        m = (l + h) // 2
        if bit_query(bit_a, m) != cv:
            h = m
        else:
            l = m + 1
    return h


def left_bs(l, h, cv, bit_a):
    if l > h or cv == bit_query(bit_a, l):
        return -1

    while l < h:
        m = (l + h + 1) // 2
        if bit_query(bit_a, m) != cv:
            l = m
        else:
            h = m - 1
    return l


def bit_update(bit_a, i, delta):
    i += 1
    while i < len(bit_a):
        bit_a[i] += delta
        i += (i & -i)


def bit_query(bit_a, i):
    i += 1
    r = 0
    while i > 0:
        r += bit_a[i]
        i -= (i & -i)
    return r


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    a_a = list(map(int, stdin.readline().split()))
    b_a = list(map(int, stdin.readline().split()))
    res = identify_the_operations(n, k, a_a, b_a)
    stdout.write(str(res) + '\n')
