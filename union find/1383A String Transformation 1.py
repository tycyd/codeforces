from sys import stdin, stdout

# aab
# bcc
# a -> b
#   |  |
#   |  \/
#   -->c
# aabd
# cccd
# a -> b -> c -> d -> e


def ufind(ua, i):
    if ua[i] == i:
        return i
    ua[i] = ufind(ua, ua[i])
    return ua[i]


def union(ua, i, j):
    res = 0

    ri = ufind(ua, i)
    rj = ufind(ua, j)
    if ri != rj:
        res = 1
        ua[ri] = rj

    return res


def string_transformation_1(n, A, B):
    ans = 0
    ua = [i for i in range(20)]
    for i in range(n):
        a = ord(A[i]) - ord('a')
        b = ord(B[i]) - ord('a')
        if a > b:
            return -1
        ans += union(ua, a, b)

    return ans


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    A = stdin.readline().strip()
    B = stdin.readline().strip()

    ans = string_transformation_1(n, A, B)
    stdout.write(str(ans) + '\n')

