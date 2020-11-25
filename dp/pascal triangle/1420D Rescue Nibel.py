from sys import stdin, stdout
import heapq

MOD = 998244353


def rescue_nibel(n, k, lr_a):

    res = 0
    pt = build_pascal_triangle(k, n)

    tail = []
    lr_a.sort(key=lambda x: (x[0], x[1]))

    for lr in lr_a:
        while tail and tail[0] < lr[0]:
            heapq.heappop(tail)

        if len(tail) >= k - 1:
            res += pt[len(tail)][k-1]
            res %= MOD

        heapq.heappush(tail, lr[1])

    return res

#        1
#      1   1
#     1  2  1
#    1  3 3  1
#   1 4  6  4 1
#  1 5 10 10 5 1
def build_pascal_triangle(k, n):
    pt = [[1]]

    for i in range(n):
        row = [1]
        for j in range(min(k + 2, len(pt[-1]) - 1)):
            row.append(pt[-1][j] + pt[-1][j + 1])
        row.append(1)
        pt.append(row)

    return pt


n, k = map(int, stdin.readline().split())
lr_a = []
for _ in range(n):
    l, r = map(int, stdin.readline().split())
    lr_a.append([l,r])
res = rescue_nibel(n, k, lr_a)
stdout.write(str(res) + '\n')
