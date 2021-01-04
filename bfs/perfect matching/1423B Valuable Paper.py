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

    def add_edge(self, f, t, cap, d):
        if f not in self.dic:
            self.dic[f] = {}
        if t not in self.dic:
            self.dic[t] = {}

        # flow, cap
        self.dic[f][t] = [f, t, 0, cap, d]
        self.dic[t][f] = [t, f, 0, 0, d]

    def remove_edge(self, f, t):
        del self.dic[f][t]
        del self.dic[t][f]

    def restore(self):
        for k in self.dic:
            for k2 in self.dic[k]:
                self.dic[k][k2][2] = 0

    def bfs(self, d):

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

                    # skip bigger d
                    if edge[4] > d:
                        continue

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


    def max_flow(self, d):
        flow = 0
        while True:
            lst = self.bfs(d)
            if not lst:
                break
            flow += 1
            self.augment(lst)

        #flow = 0
        #for k in self.dic[self.src]:
        #    flow += self.dic[self.src][k][2]

        return flow


# 1 - N: factories
# N+1 - 2*N: airports
def valuable_paper(N, M, d_s, mf):

    if mf.max_flow(2**63-1) != N:
        return -1

    d_a = list(d_s)
    d_a.sort()

    l = 0
    h = len(d_a)

    while l < h:
        m = (l + h) // 2
        d = d_a[m]

        mf.restore()
        v = mf.max_flow(d)
        if v == N:
            h = m
        else:
            l = m + 1
    return d_a[h]


N, M = map(int, stdin.readline().split())
d_s = set()

mf = MaxFlow(0, 2*N+1)
for i in range(1, N+1):
    mf.add_edge(0, i, 1, 0)
    mf.add_edge(i+N, 2*N+1, 1, 0)

for _ in range(M):
    u, v, d = map(int, stdin.readline().split())
    mf.add_edge(u, v + N, 1, d)
    d_s.add(d)

res = valuable_paper(N, M, d_s, mf)
stdout.write(str(res))
