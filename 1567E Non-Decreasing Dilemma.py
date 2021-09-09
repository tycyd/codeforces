from sys import stdin, stdout


#
# 1 3 5 7 2 1 3
# 1 2 3 4   2  1  3
# 0 0 0 4   1  0  2 s_a
# 0 0 0 10 11 11 14 b_a
#
# update i
# right most => r, left most => l, cnt = (r - l) + 1,
# next right most => rr
# if num[i] at r
#   if num[i-1] > num[i] and cnt > 1:
#       w = s_a[i]
#       s_a[i-1] = w-1, b_a[i-1] += w*(w-1)/2
#       s_a[i] = 1, b_a[i] -= w*(w+1)/2
#
#   if num[i] <= num[i+1]   #union
#       w = s_a[i]
#       w2 = s_a[rr]
#       s_a[i] -= w, b_a[i] -= w*(w+1)/2
#       s_a[rr] += w, b_a[rr] += (w+w2)*(w+w2+1)/2 - w2*(w2+1)/2
#       r = rr
#
# if num[i] at l
#   if num[i] > num[i+1] and cnt > 1:
#       w = s_a[r]
#       s_a[r] = s_a[r] - 1, b_a[r] -= w
#       s_a[i] = 1, b_a[i] += 1
#       r = i
#
#   if num[i-1] <= num[i]:  #union
#       w = s_a[i-1]
#       w2 = s_a[r]
#       s_a[i-1] -= w, b_a[i-1] -= w*(w+1)/2
#       s_a[r] += w, b_a[r] += (w+w2)*(w+w2+1)/2 - w2*(w2+1)/2
#
# if num[i] between l and r:
#   if num[i] > num[i+1]:
#       lcnt = i - l + 1, rcnt = r - i
#       w = s_a[r]
#       s_a[r] -= lcnt, b_a[r] += rcnt*(rcnt+1)/2 - w*(w-1)/2
#       s_a[i] = lcnt, b_a[i] += lcnt*(lcnt+1)/2
#   if num[i-1] > num[i]:
#       lcnt = i - l, rcnt = r - i + 1
#       w = s_a[r]
#       s_a[i-1] = lcnt, b_a[i-1] += lcnt*(lcnt+1)/2
#       s_a[r] -= lcnt, b_a[r] += rcnt*(rcnt+1)/2 - w*(w-1)/2
#
# get:
#   lrb = left_right bound, rlb = right_left bound
#   res = b_a[rlb-1] - b_a[lrb] + (lrb-l+1)*(lrb-l+2)/2 + (r-rlb+1)*(r-rlb+2)/2
#


def init_s_a(a_a):
    s_a = []
    c = 1
    for i in range(len(a_a)-1):
        if a_a[i] <= a_a[i+1]:
            s_a.append(0)
            c += 1
        else:
            s_a.append(c)
            c = 1
    s_a.append(c)

    return s_a


def init_b_a(s_a):
    b_a = [0] * (len(s_a) + 1)
    for i in range(len(s_a)):
        if s_a[i] > 0:
            update_b_a(b_a, i, s_a[i]*(s_a[i]+1)//2)
    return b_a


def query_b_a(b_a, i):
    i += 1
    r = 0
    while i > 0:
        r += b_a[i]
        i -= (i & -i)
    return r


def query_b_a_range(b_a, i, j):
    return query_b_a(b_a, j) - query_b_a(b_a, i)


def update_b_a(b_a, i, d):
    i += 1
    while i < len(b_a):
        b_a[i] += d
        i += (i & -i)


def get_left_bound(s_a, b_a, i):
    if i == 0:
        return i
    if s_a[i] > 0:
        if s_a[i-1] > 0:
            return i
        i -= 1

    r = i
    l = 0
    v = query_b_a(b_a, i)

    while l < r:
        m = (l + r) // 2
        if v > query_b_a(b_a, m):
            l = m + 1
        else:
            r = m

    if v == 0:
        return r
    return min(i, r + 1)


def get_right_bound(s_a, b_a, i):
    if s_a[i] > 0:
        return i

    # 1 2 3 4   2  1  3
    # 0 0 0 4   1  0  2 s_a
    # 0 0 0 10 11 11 14 b_a
    l = i
    r = len(b_a) - 1
    v = query_b_a(b_a, i)

    while l < r:
        m = (l + r) // 2
        if v < query_b_a(b_a, m):
            r = m
        else:
            l = m + 1
    return l


def update(a_a, i, y, s_a, b_a):
    n = len(a_a)
    if a_a[i] == y:
        return

    a_a[i] = y

    # right most => r, left most => l, cnt = (r - l) + 1,
    # next right most => rr
    # if num[i] at r
    #   if num[i-1] > num[i] and cnt > 1:
    #       w = s_a[i]
    #       s_a[i-1] = w-1, b_a[i-1] += w*(w-1)/2
    #       s_a[i] = 1, b_a[i] -= 1+w*(w+1)/2
    #
    #   if num[i] <= num[i+1]   #union
    #       w = s_a[i]
    #       w2 = s_a[rr]
    #       s_a[i] -= w, b_a[i] -= w*(w+1)/2
    #       s_a[rr] += w, b_a[rr] += (w+w2)*(w+w2+1)/2 - w2*(w2+1)/2
    #       r = rr
    l = get_left_bound(s_a, b_a, i)
    r = get_right_bound(s_a, b_a, i)

    cnt = r - l + 1
    if i == r:
        if i > 0 and a_a[i-1] > a_a[i] and cnt > 1:
            w = s_a[i]
            s_a[i-1] = w - 1
            update_b_a(b_a, i-1, w*(w-1)//2)
            s_a[i] = 1
            update_b_a(b_a, i, 1-(w * (w + 1) // 2))
            l = i

        if i < n-1 and a_a[i] <= a_a[i+1]:
            rr = get_right_bound(s_a, b_a, i+1)
            w = s_a[i]
            w2 = s_a[rr]
            s_a[i] -= w
            update_b_a(b_a, i, -(w * (w+1) // 2))
            s_a[rr] += w
            update_b_a(b_a, rr, (w+w2)*(w+w2+1)//2 - w2*(w2+1)//2)
            r = rr

    # if num[i] at l
    #   if num[i] > num[i+1] and cnt > 1:
    #       w = s_a[r]
    #       s_a[r] = w - 1, b_a[r] -= w
    #       s_a[i] = 1, b_a[i] += 1
    #       r = i
    #
    #   if num[i-1] <= num[i]:  #union
    #       w = s_a[i-1]
    #       w2 = s_a[r]
    #       s_a[i-1] -= w, b_a[i-1] -= w*(w+1)/2
    #       s_a[r] += w, b_a[r] += (w+w2)*(w+w2+1)/2 - w2*(w2+1)/2

    cnt = r - l + 1
    if i == l:
        if i < n-1 and a_a[i] > a_a[i+1] and cnt > 1:
            w = s_a[r]
            s_a[r] = w - 1
            update_b_a(b_a, r, -w)
            s_a[i] = 1
            update_b_a(b_a, i, 1)
            r = i
        if i > 0 and a_a[i-1] <= a_a[i]:
            w = s_a[i-1]
            w2 = s_a[r]
            s_a[i-1] -= w
            update_b_a(b_a, i-1, -(w*(w+1)//2))
            s_a[r] += w
            update_b_a(b_a, r, (w+w2)*(w+w2+1)//2 - w2*(w2+1)//2)
            l = get_left_bound(s_a, b_a, i-1)

    # if num[i] between l and r:
    #   if num[i] > num[i+1]:
    #       lcnt = i - l + 1, rcnt = r - i
    #       w = s_a[r]
    #       s_a[r] -= lcnt, b_a[r] += rcnt*(rcnt+1)/2 - w*(w+1)/2
    #       s_a[i] = lcnt, b_a[i] += lcnt*(lcnt+1)/2
    #   if num[i-1] > num[i]:
    #       lcnt = i - l, rcnt = r - i + 1
    #       w = s_a[r]
    #       s_a[i-1] = lcnt, b_a[i-1] += lcnt*(lcnt+1)/2
    #       s_a[r] -= lcnt, b_a[r] += rcnt*(rcnt+1)/2 - w*(w+1)/2
    if l < i < r:
        if a_a[i] > a_a[i+1]:
            lcnt = i - l + 1
            rcnt = r - i
            w = s_a[r]
            s_a[r] -= lcnt
            update_b_a(b_a, r, rcnt*(rcnt+1)//2 - w*(w+1)//2)
            s_a[i] = lcnt
            update_b_a(b_a, i, lcnt*(lcnt+1)//2)
        if a_a[i-1] > a_a[i]:
            lcnt = i - l
            rcnt = r - i + 1
            w = s_a[r]
            s_a[i-1] = lcnt
            update_b_a(b_a, i-1, lcnt*(lcnt+1)//2)
            s_a[r] -= lcnt
            update_b_a(b_a, r, rcnt*(rcnt+1)//2 - w*(w+1)//2)


def solve(a_a, c_a, s_a, b_a):
    if c_a[0] == 1:
        update(a_a, c_a[1]-1, c_a[2], s_a, b_a)
        return -1
    else:
        l = c_a[1]-1
        r = c_a[2]-1

        # get:
        #   lrb = left_right bound, rlb = right_left bound
        #   res = b_a[rlb-1] - b_a[lrb] + (lrb-l+1)*(lrb-l+2)/2 + (r-rlb+1)*(r-rlb+2)/2
        lrb = get_right_bound(s_a, b_a, l)
        rlb = get_left_bound(s_a, b_a, r)

        if lrb >= rlb:
            res = (r-l+1)*(r-l+2)//2
        else:
            res = query_b_a_range(b_a, lrb, rlb-1) + (lrb-l+1)*(lrb-l+2)//2 + (r-rlb+1)*(r-rlb+2)//2
        return res


n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
s_a = init_s_a(a_a)
b_a = init_b_a(s_a)
res = []

for k in range(q):
    c_a = list(map(int, stdin.readline().split()))
    res = solve(a_a, c_a, s_a, b_a)
    if res > -1:
        stdout.write(str(res) + '\n')
