from sys import stdin, stdout
import math

# -1 2 8 -3 -6 1 2 -3
# -1  10  -9    3  -3
#   9        -6    -3
#        3         -3
#
#
#  [4,-2][-2,4][2,-6]
#  [4, -4, 4][2,-6]
#         [0][2,-6]
#
#  2 -2 5 -3 6 -8
#  [2 -2] [5 -3]          [6 -8]        8
#
#    0      2               -2
#
#  segment tree
#   [+,+] [-,-] [+,-] [-,+]
#   [+,-] + [-,+] => [+,-,+] => [-] or [+]
#   [-,+] + [+,-] => [-,+,-] => [-] or [+]
#       1
#   2        3
# 4   5    6   7


class Node:
    def __init__(self, left, right):
        self.max = max(abs(left), abs(right))
        self.left = left
        self.right = right

    def __init__(self, cn):
        self.max = cn.max
        self.left = cn.left
        self.right = cn.right

    # 0
    def is_0(self):
        return self.left == self.right == 0

    # +
    def is_p(self):
        return self.left == self.right and self.left > 0

    # -
    def is_n(self):
        return self.left == self.right and self.left < 0

    # +,-
    def is_pn(self):
        return self.left > 0 > self.right

    def is_np(self):
        return self.left < 0 < self.right


def solve(c_a, l, r, p_sum):
    if p_sum[r] - p_sum[l-1] != 0:
        return -1


n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))
c_a = [0]
p_sum = [0]
for i in range(n):
    c_a.append(a_a[i] - b_a[i])
    p_sum.append(p_sum[-1] + c_a[-1])

pw = int(math.log(n, 2)) + 1
T = 2**(pw-1)
seg_a = [Node(0, 0) for _ in range(2**pw)]
for i in range(n):
    seg_a[T + i] = Node(c_a[i+1], c_a[i+1])


def get_node(lnode: Node, rnode: Node):
    node = None
    if lnode.is_0():
        node = Node(rnode)
    elif rnode.is_0():
        node = Node(lnode)
    if lnode.is_p():
        if rnode.is_p():
            # + +
            node = Node(lnode.left + rnode.left, lnode.left + rnode.left)
        elif rnode.is_n():
            # + -
            node = Node(lnode.left, rnode.left)
        elif rnode.is_pn():
            # +, + -
            node = Node(lnode.left + rnode.left, rnode.right)
        elif rnode.is_np():
            # +, - +
            mx = max(abs(lnode.max, rnode.max))
            mn = min(abs(lnode.left, rnode.max))
            node =


def build_seg(seg_a):
    for i in range(T-1, 0, -1):
        ln = seg_a[i >> 2]
        rn = seg_a[i >> 2 | 1]



build_seg(seg_a)

for _ in range(q):
    l, r = map(int, stdin.readline().split())
    res = solve(c_a, l, r, p_sum)
    stdout.write(str(res) + '\n')