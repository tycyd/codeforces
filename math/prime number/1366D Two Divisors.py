from sys import stdin, stdout

# 10
# 2 3 4 5 6 7 8 9 10 24
# 6 = 2,3
# 10 = 2,5
# 24 = 2,3
# 30 = 2,3,5
# a = 30
# 1. get all prime numbers
# 2. put into two groups, {p1}, {p2*p3*p4...pn}
# 3. then p1 and p2*p3*p4...pn are the answer
# proof:
#        then (p1 + p2*p3*p4...pn)%p1 != 0
#        then (p1 + p2*p3*p4...pn)%p2 != 0
#        then (p1 + p2*p3*p4...pn)%p3 != 0
#        .....
#        then (p1 + p2*p3*p4...pn)%pn != 0


def two_divisors(a, div):
    r1 = []
    r2 = []

    for v in a:
        p = getprimelist(v, div)
        if len(p) < 2:
            r1.append(-1)
            r2.append(-1)
        else:
            r1.append(p[0])
            d = 1
            for i in range(1, len(p)):
                d *= p[i]
            r2.append(d)

    return [r1, r2]


def getprimelist(a, div):
    p = []

    while a > 1:
        if len(p) == 0 or p[-1] != div[a]:
            p.append(div[a])

        a //= div[a]

    return p


def getmindiv(max):

    max += 1

    div = [i for i in range(max)]

    for k in range(2, max):
        if div[k] != k:
            continue

        curv = k
        while curv < max:
            div[curv] = k
            curv += k

    return div


if __name__ == '__main__':
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    div = getmindiv(max(a))
    r = two_divisors(a, div)

    print(' '.join(map(str, r[0])))
    print(' '.join(map(str, r[1])))
    #stdin.write(' '.join(r[1]) + '\n')
