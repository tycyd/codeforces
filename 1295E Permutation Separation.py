from sys import stdin, stdout
# 3,5,1 | 6,2,4
# 9,1,9 | 9,1,9
#   1    3   |  5
#     2   |  4    6
#   1    3   4  5
#     2   |  6
#  (1) (2)  3
#          (3)
#  (1) (2)  3  (4)  5
#          (3)     (5)
#   1  (2)  3  (4)  5
#      (2)         (5)
#   1  (2)  3  (4)  5   6
#      (2)         (5) (6)


def pushup(node):
    seg_a[node] = min(seg_a[node*2], seg_a[node*2+1])


def pushdown(node):
    if lazy_a[node] > 0:
        lazy_a[node*2] += lazy_a[node]
        lazy_a[node*2 + 1] += lazy_a[node]
        seg_a[node * 2] += lazy_a[node]
        seg_a[node * 2 + 1] += lazy_a[node]
        lazy_a[node] = 0


def update(st, ed, val, l, r, node):
    if st <= l and r <= ed:
        lazy_a[node] += val
        seg_a[node] += val
        return

    pushdown(node)
    mid = (l + r) // 2
    if st <= mid:
        update(st, ed, val, l, mid, node*2)
    if ed >= mid + 1:
        update(st, ed, val, mid+1, r, node*2 + 1)
    pushup(node)


# N = 200005 * 4
N = 2**19
n = int(stdin.readline())
p_a = list(map(int, stdin.readline().split()))
a_a = list(map(int, stdin.readline().split()))

lazy_a = [0] * N
seg_a = [0] * N

for i in range(1, n+1):
    # left max is p_a[i-1]
    update(p_a[i-1], n, a_a[i-1], 0, n, 1)
    #update(1, p_a[i-1], a_a[i-1], 0, n, 1)
ans = 10**20
for i in range(1, n):
    #update(p_a[i-1], n, -a_a[i-1], 0, n, 1);
    update(p_a[i-1], n, -a_a[i-1], 0, n, 1);
    #update(0, p_a[i-1] - 1, a_a[i-1], 0, n, 1);
    update(0, p_a[i-1] - 1, a_a[i-1], 0, n, 1);
    ans = min(ans, seg_a[1])
stdout.write(str(ans) + '\n')
