from sys import stdin, stdout


def string_reversal(n, s):
    a = [[] for _ in range(26)]
    bit_a = [0] * (n + 1)
    t = n
    res = 0
    for i in range(len(s)):
        bit_update(bit_a, i, 1)
        a[ord(s[i]) - ord('a')].append(i)

    for i in range(len(s)):
        j = a[ord(s[i]) - ord('a')].pop()
        res += t - bit_get(bit_a, j)
        bit_update(bit_a, j, -1)

        t -= 1

    return res


def bit_update(bit_a, i, delta):
    i += 1

    while i < len(bit_a):
        bit_a[i] += delta
        i += (i & -i)


def bit_get(bit_a, i):
    i += 1
    v = 0

    while i > 0:
        v += bit_a[i]
        i -= (i & -i)

    return v


n = int(stdin.readline())
s = stdin.readline().strip()
r = string_reversal(n, s)
print(r)