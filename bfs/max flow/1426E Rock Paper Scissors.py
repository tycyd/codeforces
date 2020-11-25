from sys import stdin, stdout
from collections import deque


# max flow
#      A0 ---------> B0
#
#  S   A1 ---------> B1  S
#
#      A2 ---------> B2
#
#
class MaxFlow:

    def __init__(self, src, snk):
        self.src = src
        self.snk = snk
        self.dic = {}

    def add_edge(self, f, t, cap):
        if f not in self.dic:
            self.dic[f] = {}
        if t not in self.dic:
            self.dic[t] = {}

        # flow, cap
        self.dic[f][t] = [f, t, 0, cap]
        self.dic[t][f] = [t, f, 0, 0]


    def bfs(self):

        q = deque()
        q.append([self.src, []])
        s = set()

        s.add(self.src)
        while q:
            cnt = len(q)
            for _ in range(cnt):
                cur = q.popleft()
                for k in self.dic[cur[0]]:
                    if k in s:
                        continue

                    edge = self.dic[cur[0]][k]
                    # flow >= cap
                    if edge[2] >= edge[3]:
                        continue
                    s.add(k)

                    if k == self.snk:
                        cur[1].append(edge)
                        return cur[1]
                    q.append([k, cur[1] + [edge]])

        return None


    def augment(self, lst):

        delta = 2**63-1

        for edge in lst:
            delta = min(delta, edge[3] - edge[2])
        for edge in lst:
            edge[2] += delta
            f = edge[0]
            t = edge[1]
            self.dic[t][f][2] -= delta


    def max_flow(self):

        while True:
            lst = self.bfs()
            if not lst:
                break
            self.augment(lst)

        flow = 0
        for k in self.dic[self.src]:
            flow += self.dic[self.src][k][2]

        return flow


def rock_paper_scissors(n, a_a, b_a):

    MAX_C = 2**63-1
    mf = MaxFlow(0, 7)

    mf.add_edge(0, 1, a_a[0])
    mf.add_edge(0, 2, a_a[1])
    mf.add_edge(0, 3, a_a[2])

    # a[0] -> b[0]
    mf.add_edge(1, 4, MAX_C)
    # a[0] -> b[2]
    mf.add_edge(1, 6, MAX_C)
    # a[1] -> b[0]
    mf.add_edge(2, 4, MAX_C)
    # a[1] -> b[1]
    mf.add_edge(2, 5, MAX_C)
    # a[2] -> b[1]
    mf.add_edge(3, 5, MAX_C)
    # a[2] -> b[2]
    mf.add_edge(3, 6, MAX_C)

    mf.add_edge(4, 7, b_a[0])
    mf.add_edge(5, 7, b_a[1])
    mf.add_edge(6, 7, b_a[2])

    mxflow = mf.max_flow()

    return n - mxflow


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

res2 = min(a_a[0], b_a[1]) + min(a_a[1], b_a[2]) + min(a_a[2], b_a[0])
res1 = rock_paper_scissors(n, a_a, b_a)

stdout.write(str(res1))
stdout.write(' ')
stdout.write(str(res2))
