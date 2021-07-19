from sys import stdin, stdout

# a0,a1,a2,a3,a4,a5....
# gcd(a0, a1), gcd(a1, a2)....
# gcd(gcd(a0, a1), gcd(a1, a2)), gcd(gcd(a2, a3), gcd(a3, a4))....
# gcd(gcd(a1, a2), gcd(a2, a3)), gcd(gcd(a3, a4), gcd(a4, a5))....

# gcd(gcd(gcd(a0, a1), gcd(a1, a2)), gcd(gcd(a2, a3), gcd(a3, a4)))....


# segment tree + binary search
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


#      1
#   2     3
# 4   5 6   7
def build(n, sega):
    for i in range(n-1, -1, -1):
        sega[i] = gcd(sega[i*2], sega[i*2 + 1])


# 0, 3
# 4, 8
def query(n, sega, l, r):
    l += n
    r += n
    res = -1
    while l < r:
        if l & 1 == 1:
            if res == -1:
                res = sega[l]
            else:
                res = gcd(res, sega[l])
            l += 1
        if r & 1 == 1:
            r -= 1
            if res == -1:
                res = sega[r]
            else:
                res = gcd(res, sega[r])

        l //= 2
        r //= 2
    return res


N = 400000
sega = [0] * N

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))

    # build segment tree
    for i in range(n):
        sega[n+i] = a_a[i]
    build(n, sega)

    # binary search
    l = 0
    h = n-1
    while l < h:
        m = (l + h) // 2

        flag = True
        r = query(n, sega, 0, m+1)

        for i in range(1, n):
            tmp = query(n, sega, i, min(n, i + m + 1))
            if i + m + 1 > n:
                tmp = gcd(tmp, query(n, sega, 0, i + m + 1 - n))

            if r != tmp:
                flag = False
                break
        if flag:
            h = m
        else:
            l = m + 1
    stdout.write(str(h) + '\n')
