from sys import stdin, stdout
import math
import functools


def compare(x, y):
    ux = x[1] // unit
    uy = y[1] // unit
    if ux != uy:
        return ux - uy
    else:
        return x[2] - y[2]


def delete(i, a_a):
    global maxcnt
    if i == -1:
        return
    a = a_a[i]
    acnt_a[a] -= 1
    ccnt_a[acnt_a[a]] += 1
    ccnt_a[acnt_a[a]+1] -= 1

    if maxcnt == acnt_a[a] + 1 and ccnt_a[acnt_a[a]+1] == 0:
        maxcnt -= 1


def add(i, a_a):
    global maxcnt
    if i == -1:
        return
    a = a_a[i]
    acnt_a[a] += 1
    ccnt_a[acnt_a[a]] += 1
    ccnt_a[acnt_a[a]-1] -= 1

    maxcnt = max(maxcnt, acnt_a[a])


def cut_and_stick(a_a, q_a):

    r_a = [-1] * len(q_a)

    l = r = -1
    for q in q_a:
        while l < q[1]:
            delete(l, a_a)
            l += 1
        while l > q[1]:
            l -= 1
            add(l, a_a)
        while r < q[2]:
            r += 1
            add(r, a_a)
        while r > q[2]:
            delete(r, a_a)
            r -= 1
        r_a[q[0]] = max(1, maxcnt - ((r - l + 1) - maxcnt))

    return r_a


maxcnt = 0
acnt_a = [0] * (3 * 10**5 + 1)
ccnt_a = [0] * (3 * 10**5 + 1)

n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
q_a = []
unit = int(math.sqrt(n))
for i in range(q):
    l, r = map(int, stdin.readline().split())
    q_a.append([i, l-1, r-1])
q_a.sort(key=functools.cmp_to_key(lambda a, b: compare(a, b)))
r_a = cut_and_stick(a_a, q_a)
stdout.write('\n'.join(map(str, r_a)))
