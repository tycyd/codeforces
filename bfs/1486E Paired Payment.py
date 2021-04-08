from sys import stdin, stdout
import heapq


class Heap(object):
    # def __init__(self, initial=None, key=lambda x:x):
    def __init__(self, initial=None, key=None):
        self.key = key
        self.index = 0
        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]


def paired_payment(n, dic):
    r = [[[-1 for _ in range(51)] for _ in range(2)] for _ in range(n)]
    visited = [[[False for _ in range(51)] for _ in range(2)] for _ in range(n)]
    hp = Heap([[1, 0, 0, 0]], key=lambda x: x[2])

    while len(hp) > 0:
        i, s, w1, w2 = hp.pop()

        if visited[i - 1][s][w2]:
            continue
        visited[i - 1][s][w2] = True
        r[i-1][s][w2] = w1

        for ni, nw in dic[i]:
            ns = s ^ 1
            if ns == 0:
                nw1 = w1 + (w2 + nw)**2
            else:
                nw1 = w1
            nw2 = nw

            if r[ni - 1][ns][nw2] == -1 or r[ni - 1][ns][nw2] > nw1:
                # help reduce time
                r[ni - 1][ns][nw2] = nw1
                hp.push([ni, ns, nw1, nw2])

    MAX = 10**20
    res = []
    for i in range(n):
        m = MAX
        for j in range(51):
            if r[i][0][j] != -1:
                m = min(m, r[i][0][j])
        if m == MAX:
            m = -1
        res.append(m)

    return res


n, m = map(int, stdin.readline().split())
dic = {}
for _ in range(m):
    v, u, w = map(int, stdin.readline().split())
    if v not in dic:
        dic[v] = []
    if u not in dic:
        dic[u] = []
    dic[v].append([u, w])
    dic[u].append([v, w])

r = paired_payment(n, dic)
stdout.write(' '.join(map(str, r)))
