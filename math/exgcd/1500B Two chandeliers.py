from sys import stdin, stdout

# 1 2 3
# 4 3 1 2

# ax + i = by + j
# ax - by = j - i
# ax + (-b)y = j - i
# => ax + (-b)y = c
#    ax1 + (-b)y1 = gcd(a, -b)
#    ax2 + (-b)y2 = gcd(a, -b)
#    => ax1 + (-b)y1 = ax2 + (-b)y2
#       a(x1-x2) = (-b)(y2-y1)
#       (a/g)(x1-x2) = (-b/g)(y2-y1)    /* g=gcd(a, -b) */
#       => (a/g) and (-b/g) are co-prime
#          x1-x2 = (-b/g)*k, y2-y1 = (a/g)*k  /* k is integer */
#          => x1 = (-b/g)*k+x2, y1 = y2-(a/g)*k
#             min positive integer = x%(-b/g) or ((-b/g) + x%(-b/g))
#
#    => same prove for a1x1 + (-b1)y1 = c
#    (a*c/g)x1 + (-b*c/g)y1 = c
#    (a*c/g)x2 + (-b*c/g)y2 = c


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def exgcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = exgcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# ax - by = j - i
# get min x >= 0
# def minX(i, j, a, b):
def minX(i, j, a, b, g, x, y):

    b = -b
    # g, x, y = exgcd(a, b)
    c = j - i

    if c % g != 0:
        return -1

    x *= c//g
    if b < 0:
        b = -b
    b //= g

    ans = x % b
    if ans < 0:
        ans += b

    return ans


# def getPos(i, j, a, b):
def getPos(i, j, a, b, g, x, y):
    if i == j:
        return i

    mx = minX(i, j, a, b, g, x, y)
    if mx == -1:
        return mx
    return a*mx+i


def bs(p_a, k, lcm):
    l = 1
    h = 2**63-1

    while l < h:
        m = (l + h) // 2
        cnt = m
        for p in p_a:
            if p <= m:
                cnt -= (1 + (m-p) // lcm)
            if cnt < k:
                break

        if cnt >= k:
            h = m
        else:
            l = m + 1

    return h


def two_chandeliers(n, m, k, a_a, b_a):
    dic_pa = {}
    p_a = []

    for i in range(1, n+1):
        dic_pa[a_a[i-1]] = i

    g, x, y = exgcd(n, m)
    for j in range(1, m+1):
        if b_a[j-1] in dic_pa:
            p = getPos(dic_pa[b_a[j-1]], j, n, m, g, x, y)
            if p != -1:
                p_a.append(p)

    lcm = m*n//gcd(n,m)
    r = bs(p_a, k, lcm)
    return r


n, m, k = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

r = two_chandeliers(n, m, k, a_a, b_a)
stdout.write(str(r))
