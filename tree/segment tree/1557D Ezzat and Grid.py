from sys import stdin, stdout


def push(t, lazy, v):
    if v in lazy and lazy[v] is not None:
        t[v * 2] = lazy[v]
        lazy[v * 2] = lazy[v]
        t[v * 2 + 1] = lazy[v]
        lazy[v * 2 + 1] = lazy[v]
        lazy[v] = None


def update(t, lazy, v, tl, tr, l, r, addend):
    if l > r:
        return
    if l == tl and tr == r:
        t[v] = addend
        lazy[v] = addend
    else:
        push(t, lazy, v)
        tm = (tl + tr) // 2
        update(t, lazy, v * 2, tl, tm, l, min(r, tm), addend)
        update(t, lazy, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, addend)

        c1 = get_val(t, v * 2)
        c2 = get_val(t, v * 2 + 1)
        if c1[0] > c2[0]:
            t[v] = [c1[0], c1[1]]
        else:
            t[v] = [c2[0], c2[1]]


def query(t, lazy, v, tl, tr, l, r):
    if l > r:
        return [0, -1]
    if l == tl and tr == r:
        return get_val(t, v)
    push(t, lazy, v)
    tm = (tl + tr) // 2
    q1 = query(t, lazy, v * 2, tl, tm, l, min(r, tm))
    q2 = query(t, lazy, v * 2 + 1, tm+1, tr, max(l, tm + 1), r)
    if q1[0] > q2[0]:
        return q1
    else:
        return q2


def get_val(dic, v):
    if v in dic:
        return dic[v]
    else:
        return [0, -1]


n, m = map(int, stdin.readline().split())
ilr_a = []
for _ in range(m):
    ilr_a.append(list(map(int, stdin.readline().split())))
t = {}
lazy = {}
TL = 1
TR = 1000000000

ilr_a.sort(key=lambda a:a[0])

s = set([i for i in range(1, n+1)])
cur = ilr_a[0][0]
mx = [0, -1]
gb_mx = 0
gb_c = -1
pre_d = {}
# 1,0   2,1     1,2     2,2     3,5 6 7
#
#
for i in range(len(ilr_a)):
    ilr = ilr_a[i]
    if cur != ilr[0]:
        pre_d[cur] = mx[1]
        j = i - 1
        while j >= 0 and ilr_a[j][0] == cur:
            update(t, lazy, 1, TL, TR, ilr_a[j][1], ilr_a[j][2], [mx[0] + 1, cur])
            j -= 1

        if mx[0] + 1 > gb_mx:
            gb_mx = mx[0] + 1
            gb_c = cur

        cur = ilr[0]
        mx = [0, -1]

    q = query(t, lazy, 1, TL, TR, ilr[1], ilr[2])
    if q[0] >= mx[0]:
        mx = q

pre_d[cur] = mx[1]
if mx[0] + 1 > gb_mx:
    gb_c = cur

visited = set()
while gb_c != -1:
    visited.add(gb_c)
    gb_c = pre_d[gb_c]

r_a = []
for i in range(1, n+1):
    if i not in visited:
        r_a.append(i)

stdout.write(str(len(r_a)) + '\n')
stdout.write(' '.join(list(map(str, r_a))) + '\n')
