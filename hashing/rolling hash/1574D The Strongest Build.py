from sys import stdin, stdout

# rolling hash
MOD = 1000000007
P = 200001


def get_key(ka):
    k = 0
    for i in range(len(ka)):
        k *= P
        k += ka[i]
        k %= MOD
    return k


def pow(a, b):
    if b == 0:
        return 1
    c = pow(a, b//2)
    c *= c
    c %= MOD
    if b % 2 == 1:
        c *= a
        c %= MOD
    return c


n = int(stdin.readline())
c_a = []
res = 0
key = 0
r_a = []
for _ in range(n):
    c_a.append(list(map(int, stdin.readline().split())))
    res += c_a[-1][-1]
    key *= P
    key += len(c_a[-1]) - 1
    key %= MOD
    r_a.append(len(c_a[-1]) - 1)
m = int(stdin.readline())
b_a = []
b_s = set()
for _ in range(m):
    b_a.append(list(map(int, stdin.readline().split())))
    b_s.add(get_key(b_a[-1]))

if key in b_s:
    res = 0
    r_a = []

    #print(b_s)

    for b in b_a:
        bsum = 0
        for i in range(n):
            bsum += c_a[i][b[i]]

        bk = get_key(b)
        for i in range(n):
            idx = b[i]
            if idx > 1:
                k = bk - pow(P, n-1-i)
                k %= MOD
                if k not in b_s:
                    lres = bsum - c_a[i][b[i]] + c_a[i][b[i]-1]
                    if lres > res:
                        b[i] -= 1
                        r_a = b.copy()
                        res = lres
                        b[i] += 1

            if idx < len(c_a[i]) - 1:
                k = bk + pow(P, n-1-i)

                k %= MOD
                if k not in b_s:
                    lres = bsum - c_a[i][b[i]] + c_a[i][b[i]+1]
                    if lres > res:
                        b[i] += 1
                        r_a = b.copy()
                        res = lres
                        b[i] -= 1


stdout.write(' '.join(map(str, r_a)))
