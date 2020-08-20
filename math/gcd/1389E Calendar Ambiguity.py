from sys import stdin, stdout


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def calender_ambiguity(m, d, w):
    K = (w - d % w) % w
    D = min(d, m)

    if (K + 1) % w == 0:
        if D == 1:
            return 0

        # D-1, D-2 ... 0
        res = D*(D-1) // 2
    else:
        # 0 + 0 + 0 + 1 + 1
        # 0/4 + 1/4 + 2/4 + 3/4 + 4/4 + 5/4 + 6/4 + 7/4 + 8/4 + 9/4
        #  0    0     0      0     1     1     1     1     2     2
        g = gcd(w, K + 1)
        w //= g

        L = (D-1) // w
        M = (D-1) % w + 1

        res = ((L-1) * L * w // 2) + (L * M)

    return res


t = int(stdin.readline())
for _ in range(t):
    m, d, w = map(int, stdin.readline().split())
    ans = calender_ambiguity(m, d, w)
    stdout.write(str(ans) + '\n')
