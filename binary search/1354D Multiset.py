from sys import stdin, stdout

# 5 4
# 1 2 3 4 5
# -5 -1 -3 -1
# -5: 1 2 3 4
# -1: 2 3 4
# -3: 2 3
# -1: 3
# 1 2 3 4 5
# 1 1 1 1 1
# 1 1 1 1
# 4 4 4 4

# binary search (MLE), only count smaller set
def multiset(n, a, q):

    l = 1
    r = n + 1

    #find right bound
    while l < r:
        m = (l + r)//2

        cnt = getcount(a, q, m)

        if cnt > 0:
            r = m
        else:
            l = m+1

    if r == n + 1:
        return 0
    else:
        return r


def getcount(a, q, v):

    cnt = 0
    for av in a:
        if av <= v:
            cnt += 1

    for qv in q:
        if qv > 0 and v <= qv:
            cnt += 1

        if qv < 0 and abs(qv) <= cnt:
            cnt -= 1

    return cnt


# binary indexed tree + binary search (MLE)
def multiset2(n, a, q):

    ba = [0 for i in range(0, n+1)]
    for i in a:
        ba[i] += 1

    bit = BIT(ba)
    #print(ba)
    #print(bit.bita)

    for qv in q:
        if qv > 0:
            bit.update(qv, 1)
        elif qv < 0:
            ri = bs_rb(abs(qv), bit, n)
            bit.update(ri, -1)

    pre = bit.query(n)
    for i in range(n-1, -1, -1):
        if bit.query(i) != pre:
            return i+1

    return 0


def bs_rb(v, bit, n):
    l = 1
    r = n

    while l < r:
        m = (l + r)//2
        q = bit.query(m)
        if v > q:
            l = m + 1
        else:
            r = m

    return r


class BIT:

    def __init__(self, ba):
        self.bita = [0 for i in range(len(ba))]

        for i in range(1, len(ba)):
            self.update(i, ba[i])

    def update(self, i, dif):
        while i < len(self.bita):
            self.bita[i] += dif
            i += (i & -i)

    def query(self, i):
        r = 0
        while i > 0:
            r += self.bita[i]
            i -= (i & -i)

        return r


if __name__ == '__main__':
    nq = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    q = list(map(int, stdin.readline().split()))

    stdout.write(str(multiset(nq[0], a, q)) + '\n')
