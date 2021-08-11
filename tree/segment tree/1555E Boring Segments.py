from sys import stdin, stdout
from math import log, ceil

#              10  11
#  1  4
#                  11
#     4       9


# def pushup(seg_a, node):
#     seg_a[node] = min(seg_a[node * 2], seg_a[node * 2 + 1])
#
#
# def pushdown(seg_a, lazy_a, node):
#     if lazy_a[node] > 0:
#         lazy_a[node * 2] += lazy_a[node]
#         lazy_a[node * 2 + 1] += lazy_a[node]
#         seg_a[node * 2] += lazy_a[node]
#         seg_a[node * 2 + 1] += lazy_a[node]
#         lazy_a[node] = 0
#
#
# def update(seg_a, lazy_a, st, ed, val, l, r, node):
#
#     if r < st or ed < l or l > r:
#         return
#
#     if st <= l and r <= ed:
#         lazy_a[node] += val
#         seg_a[node] += val
#         return
#
#     pushdown(seg_a, lazy_a, node)
#     mid = (l + r) // 2
#     if st <= mid:
#         update(seg_a, lazy_a, st, ed, val, l, mid, node * 2)
#     if ed >= mid + 1:
#         update(seg_a, lazy_a, st, ed, val, mid + 1, r, node * 2 + 1)
#     pushup(seg_a, node)


def push(t, lazy, v):
    t[v*2] += lazy[v]
    lazy[v*2] += lazy[v]
    t[v*2+1] += lazy[v]
    lazy[v*2+1] += lazy[v]
    lazy[v] = 0


def update(t, lazy, v, tl, tr, l, r, addend):
    if l > r:
        return
    if l == tl and tr == r:
        t[v] += addend
        lazy[v] += addend
    else:
        push(t, lazy, v)
        tm = (tl + tr) // 2
        update(t, lazy, v*2, tl, tm, l, min(r, tm), addend)
        update(t, lazy, v*2+1, tm+1, tr, max(l, tm+1), r, addend)
        t[v] = min(t[v*2], t[v*2+1])


def debug(seg_a):
    n = len(seg_a)
    c = 1
    bc = 1
    while c < n:
        stdout.write(str(seg_a[c]))
        stdout.write(' ')
        if c == bc:
            bc = 2*c + 1
            stdout.write('\n')
        c += 1


n, m = map(int, stdin.readline().split())
lrw = []
for _ in range(n):
    l, r, w = map(int, stdin.readline().split())
    lrw.append([l, r-1, w])

lrw.sort(key=lambda k: k[2])

N = int(2 ** (ceil(log(m-1, 2)) + 1))
L = 1
R = int(2 ** (ceil(log(m-1, 2))))
seg_a = [0] * N
lazy_a = [0] * N

# fill 1
if R > m - 1:
    # update(seg_a, lazy_a, m, R, 1, L, R, 1)
    update(seg_a, lazy_a, 1, L, R, m, R, 1)
#update(seg_a, lazy_a, 1, L, R, 1, 1, 1)
#debug(seg_a)


i = j = 0
res = 10000000000
while i < n:
    while j < n and seg_a[1] == 0:
        l = lrw[j][0]
        r = lrw[j][1]
        # update(seg_a, lazy_a, l, r, 1, L, R, 1)
        update(seg_a, lazy_a, 1, L, R, l, r, 1)
        j += 1

    if seg_a[1] > 0:
        res = min(res, lrw[j-1][2] - lrw[i][2])
    l2 = lrw[i][0]
    r2 = lrw[i][1]
    # update(seg_a, lazy_a, l2, r2, -1, L, R, 1)
    update(seg_a, lazy_a, 1, L, R, l2, r2, -1)
    i += 1

stdout.write(str(res) + '\n')
