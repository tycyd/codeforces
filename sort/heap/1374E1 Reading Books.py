from heapq import heappush, heappop
from sys import stdin, stdout


if __name__ == '__main__':

    def reading_books(n, k, ta, tb, tab):

        res = 0
        for i in range(k):
            if len(tab) == 0 and (len(ta) == 0 or len(tb) == 0):
                return -1
            t1 = 100000
            t2 = 100000
            t3 = 100000

            if len(tab) > 0:
                t1 = tab[0]
            if len(ta) > 0:
                t2 = ta[0]
            if len(tb) > 0:
                t3 = tb[0]

            if t1 <= t2+t3:
                res += heappop(tab)
            else:
                res += heappop(ta) + heappop(tb)

        return res

    n, k = map(int, stdin.readline().split())
    ta = []
    tb = []
    tab = []
    for i in range(n):
        t, a, b = map(int, stdin.readline().split())
        if a == 1 and b == 1:
            heappush(tab, t)
        elif a == 1:
            heappush(ta, t)
        elif b == 1:
            heappush(tb, t)

    res = reading_books(n, k, ta, tb, tab)
    stdout.write(str(res) + '\n');
