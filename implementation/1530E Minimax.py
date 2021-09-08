from sys import stdin, stdout
import sys


# a a b a b a
# a a b a b
# a a b b
#
# 1. if a has less or equal than half + 1
#   a a x a x a x a
# 2. if a has more than half + 1
#       2.1 only two chars
#       b a a a a a a a b b
#       2.2 more than two chars
#       a b a a a a a a c b b c c
# 3. if x has one cnt
#   x a a a a b b b c c c

# uttttttttttttttttttuuuuuuuuvvvvv
# tutttttttttttttttttvuuuuuuuuvvvv
def solve(s):

    r = []
    c_a = [0] * 26
    i = ord(s[0]) - ord('a')

    for c in s:
        c_a[ord(c) - ord('a')] += 1
        i = min(i, ord(c) - ord('a'))

    k = get1cnt(c_a)
    if k != -1:
        r.append(chr(k + ord('a')))
        c_a[k] -= 1

    elif c_a[i] <= len(s) // 2 + 1:
        r.append(chr(i + ord('a')))
        c_a[i] -= 1
        m = i + 1

        while c_a[i] > 0:
            r.append(chr(i + ord('a')))
            c_a[i] -= 1
            while m < 26 and c_a[m] == 0:
                m += 1
            if m == 26:
                break
            r.append(chr(m + ord('a')))
            c_a[m] -= 1

    else:
        nxt = getnext(i, c_a)
        if nxt == -1:
            r.append(chr(i + ord('a')))
            c_a[i] -= 1
        elif getnext(nxt, c_a) == -1:
            r.append(chr(i + ord('a')))
            c_a[i] -= 1
            for _ in range(c_a[nxt]):
                r.append(chr(nxt + ord('a')))
                c_a[nxt] -= 1
        else:
            nnxt = getnext(nxt, c_a)
            r.append(chr(i + ord('a')))
            c_a[i] -= 1
            r.append(chr(nxt + ord('a')))
            c_a[nxt] -= 1
            for _ in range(c_a[i]):
                r.append(chr(i + ord('a')))
                c_a[i] -= 1
            r.append(chr(nnxt + ord('a')))
            c_a[nnxt] -= 1

    for l in range(26):
        for _ in range(c_a[l]):
            r.append(chr(l + ord('a')))
    return r


def get1cnt(c_a):
    for i in range(len(c_a)):
        if c_a[i] == 1:
            return i
    return -1


def getnext(i, c_a):
    for j in range(i+1, len(c_a)):
        if c_a[j] > 1:
            return j
    return -1

try:
    t = int(stdin.readline())
    for _ in range(t):
        s = str(stdin.readline().strip())
        r = solve(s)
        stdout.write(''.join(r) + '\n')
except:
    print(sys.exc_info())
