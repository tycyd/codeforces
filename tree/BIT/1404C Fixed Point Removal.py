from sys import stdin, stdout


def query(bit_a, i):
    i += 1
    r = 0
    while i > 0:
        r += bit_a[i]
        i -= i & -i
    return r


def update(bit_a, i, d):
    i += 1
    while i < len(bit_a):
        bit_a[i] += d
        i += i & -i


# 1 2 3 4 5 6 7 8 9 10 11  12  13
# 2 2 3 9 5 4 6 5 7  8  3  11  13
#   0 0   0 2 1 3 2  2  8   1   0
# 0 1 1   1 0
def solve(n, q, a_a, q_a):
    r = [0] * q
    bit_a = [0] * n
    t = 0

    q_a.sort(key=lambda x: -x[1])

    j = 0
    for i in range(n):
        a_a[i] = i + 1 - a_a[i]
        if a_a[i] == 0:
            update(bit_a, i, 1)
            t += 1
        elif 0 < a_a[i] <= t:
            l = 0
            h = i-1
            while l < h:
                m = (l + h) // 2
                v = query(bit_a, m)
                if a_a[i] >= t - v + 1:
                    h = m
                else:
                    l = m + 1
            update(bit_a, h, 1)
            t += 1

        while j < q and q_a[j][1] == n - i - 1:
            r[q_a[j][2]] = t - query(bit_a, q_a[j][0] - 1)
            j += 1
    return r


n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
q_a = []
for i in range(q):
    x, y = map(int, stdin.readline().split())
    q_a.append([x, y, i])

r_a = solve(n, q, a_a, q_a)
for r in r_a:
    stdout.write(str(r) + '\n')
