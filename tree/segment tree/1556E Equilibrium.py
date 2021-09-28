from sys import stdin, stdout
import math


# a - b
# -1 2 8 -3 -6 1 2 -3
# -1 1 9  6  0 1 2  0
#  ( ) ) (   ( ) )  (
#
#  0  1  2  9  3  2  7  5
#  2  2  1  9  4  1  5  8
# -2 -1  1  0 -1  1  2 -3
# -2 -3 -2 -2 -3 -2  0 -3   p_sum
#     l     r(r)
# -3 -1  0 -1 -1  0 -1 -3   s_sum
#     l (l) r
#


n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))
lr_a = [0] * (n+1)
rl_a = [0] * (n+1)

pw = int(math.log(n, 2)) + 2
T = 2**(pw-1)
seg_psum_a = [[-10000000000000, 10000000000000] for _ in range(2**pw)]
seg_ssum_a = [[-10000000000000, 10000000000000] for _ in range(2**pw)]
p_sum = [0]
s_sum = [0 for _ in range(n+2)]

for i in range(n):
    c = a_a[i] - b_a[i]
    p_sum.append(p_sum[-1] + c)
    seg_psum_a[T + i] = [p_sum[-1], p_sum[-1]]
    if c <= 0:
        lr_a[i+1] = i+1
    else:
        lr_a[i+1] = lr_a[i]

for i in range(n-1, -1, -1):
    c = a_a[i] - b_a[i]
    s_sum[i+1] = s_sum[i+2] + c
    seg_ssum_a[T + i] = [s_sum[i+1], s_sum[i+1]]
    if c >= 0:
        rl_a[i+1] = i+1
    else:
        if i+2 <= n:
            rl_a[i+1] = rl_a[i+2]
        else:
            rl_a[i+1] = n+1


def build_seg(seg_a):
    for i in range(T-1, 0, -1):
        seg_a[i][0] = max(seg_a[i << 1][0], seg_a[i << 1 | 1][0])
        seg_a[i][1] = min(seg_a[i << 1][1], seg_a[i << 1 | 1][1])


def query(l, r, seg_a, offset):
    res = [-10000000000000, 10000000000000]
    l += T - 1
    r += T
    while l < r:
        if l & 1 > 0:
            res[0] = max(res[0], seg_a[l][0] - offset)
            res[1] = min(res[1], seg_a[l][1] - offset)
            l += 1
        if r & 1 > 0:
            r -= 1
            res[0] = max(res[0], seg_a[r][0] - offset)
            res[1] = min(res[1], seg_a[r][1] - offset)
        l >>= 1
        r >>= 1
    return res


build_seg(seg_psum_a)
build_seg(seg_ssum_a)


def solve(l, r):
    if p_sum[r] - p_sum[l-1] != 0:
        return -1
    if l > lr_a[r] or rl_a[l] > r:
        return -1

    [lmax, lmin] = query(l, lr_a[r], seg_psum_a, p_sum[l-1])

    [rmin, rmax] = query(rl_a[l], r, seg_ssum_a, s_sum[r+1])

    if lmax > 0 or rmin < 0:
        return -1

    return abs(lmin)


for _ in range(q):
    l, r = map(int, stdin.readline().split())
    res = solve(l, r)
    stdout.write(str(res) + '\n')
