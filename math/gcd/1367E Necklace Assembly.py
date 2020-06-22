from sys import stdin, stdout


# 6 3
# abc abc
# a b a a a
#      a            a
#   b      b    b       a
#     a  a        a   b
#
# a   a   a
# abc
#   a
# b   c
#
#   a
# a   a
# k , r
# k %= r
# for every a[(i + k)%n] = a[i]
# 6 3
# 1 2 3 1 2 3
# 6 4
# [1 2] [1 2] [1 2]
def necklace_assembly(n, k, s):

    res = 0
    cna = [0 for i in range(26)]
    for i in range(len(s)):
        cna[ord(s[i]) - ord('a')] += 1

    for i in range(n, 0, -1):
        g = gcd(i, k%i)
        if g != 0:
            d = 0
            need = i // g

            for v in cna:
                d += (v // need) * need
            if d >= i:
                res = i
                break

    return res


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        (n, k) = list(map(int, stdin.readline().split()))
        s = stdin.readline().strip()
        stdout.write(str(necklace_assembly(n, k, s)) + '\n')