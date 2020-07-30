from sys import stdin, stdout

# 4 3
# 2 3 5 6
# x upper bound: 6
# x lower bound: 3
#
# 4 3
# 1 3 5 6
# 2 => 1 3 5 6
#
# 3 2
# 1 999999999 1000000000
# l: 999999998
# h: 999999999
#
# 4 2
# x = 3,
# 2 5 5 5 6
# x=4:
# P0 (x=4) = len(2, 3, 4)
# P1 (x=5) = len(2, 3, 4, 5) - 1
# P2 (x=6) = len(2, 3, 4, 5, 6) - 2
# C = b - i
#
# 1 1 3
if __name__ == '__main__':

    def asterism(n, p, a):
        res = []

        a.sort()

        l = a[n-1]
        for i in range(n-1, -1, -1):
            l = max(a[i], l)
            l -= 1
        l += 1
        minl = l

        if check(bs(minl, a), minl, a, p):
            return res

        h = max(minl, a[n-1]-1)

        while l < h:
            m = (l + h + 1)//2
            idx = bs(m, a)

            if not check(idx, m, a, p):
                l = m
            else:
                h = m - 1

        for i in range(minl, l+1):
            res.append(i)

        return res

    def check(idx, v, a, p):

        for i in range(len(a)):
            if (idx + 1 - i) >= p:
                return True
            v += 1
            idx += 1
            if idx == len(a):
                break

            while idx < len(a) and a[idx] <= v:
                idx += 1
            idx -= 1

        return False


    def bs(v, a):
        l = 0
        h = len(a)-1

        while l < h:
            m = (l + h + 1)//2
            if a[m] > v:
                h = m - 1
            else:
                l = m

        return l

    n, p = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    res = asterism(n, p, a)
    stdout.write(str(len(res)) + '\n')
    if len(res) > 0:
        stdout.write(" ".join(map(str, res)) + '\n')
