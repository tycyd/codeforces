from sys import stdin, stdout
from heapq import *


class RemovableHeap:
    def __init__(self, max_heap_type=None):
        if max_heap_type:  # element's class
            class Transform(max_heap_type):
                def __lt__(self, other):
                    return self >= other

            self._T = Transform
        else:
            self._T = lambda x: x
        self.heap = []
        self.rem = []
        self.dict = {}
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        self.__trim()
        return self.heap[index]

    def push(self, val):
        val = self._T(val)
        heappush(self.heap, val)
        if val in self.dict:
            self.dict[val] += 1
        else:
            self.dict[val] = 1
        self.size += 1

    def pop(self):
        self.__trim()
        if not self.heap:
            return None
        self.size -= 1
        val = heappop(self.heap)
        if self.dict[val] == 1:
            del self.dict[val]
        else:
            self.dict[val] -= 1
        return val

    def remove(self, val):
        val = self._T(val)
        if val not in self.dict:
            return
        self.size -= 1
        if self.dict[val] == 1:
            del self.dict[val]
        else:
            self.dict[val] -= 1
        heappush(self.rem, val)

    def __trim(self):
        while self.rem and self.rem[0] == self.heap[0]:
            heappop(self.heap)
            heappop(self.rem)


class SegementNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.ln = None
        self.rn = None
        self.v = 0

        if self.l < self.r:

            m = (self.l + self.r) // 2
            self.ln = SegementNode(self.l, m)
            self.rn = SegementNode(m+1, self.r)


    def update(self, idx, v):
        if idx < self.l or idx > self.r:
            return

        if self.l == self.r:
            if self.l == idx:
                self.v = v
            return

        self.ln.update(idx, v)
        self.rn.update(idx, v)

        self.v = self.ln.v + self.rn.v

    def getVal(self, l, r):
        if l >= self.l and self.r <= r:
            return self.v
        if self.l > r or self.r < l:
            return 0

        v1 = self.ln.getVal(max(self.l, l), min(self.r, r))
        v2 = self.rn.getVal(max(self.l, l), min(self.r, r))

        return v1 + v2

    def getIdx(self, v):
        if self.l == self.r:
            if self.v == v:
                return self.l
            else:
                return -1

        if self.v < v:
            return -1

        li = self.ln.getIdx(v)
        ri = self.rn.getIdx(v - self.ln.v)

        if li != -1:
            return li
        if ri != -1:
            return ri
        return -1


def query(segroot, hp, discrete_data):
    if not hp:
        return 0

    l = segroot.getIdx(1)
    r = segroot.getIdx(segroot.v)

    if l == -1 or r == -1 or len(hp) <= 1:
        return 0

    return discrete_data[r] - discrete_data[l] - hp[0]


def trash_problem(n, q, p_a, q_a):
    p_a.sort()
    res = []

    discrete_data = []
    hp = RemovableHeap()

    for i in range(len(p_a)):
        p = p_a[i]
        discrete_data.append(p)
        if i > 0:
            hp.push(p_a[i] - p_a[i-1])

    for q in q_a:
        if q[0] == 1:
            discrete_data.append(q[1])

    dic_m = {}
    discrete_data.sort()
    for i in range(len(discrete_data)):
        dic_m[discrete_data[i]] = i

    segroot = SegementNode(0, len(discrete_data) - 1)
    for p in p_a:
        segroot.update(dic_m[p], 1)

    res.append(query(segroot, hp, discrete_data))

    for q in q_a:

        idx = dic_m[q[1]]
        val = segroot.getVal(0, idx)
        if q[0] == 0:
            li = segroot.getIdx(val - 1)
            ri = segroot.getIdx(val + 1)
            lintv = q[1] - discrete_data[li]
            rintv = discrete_data[ri] - q[1]

            if li != idx and idx != ri:
                hp.remove(lintv)
                hp.remove(rintv)
                hp.push(lintv + rintv)
            elif li == idx:
                hp.remove(rintv)
            else:
                hp.remove(lintv)

            segroot.update(idx, 0)
        else:

            li = segroot.getIdx(val)
            ri = segroot.getIdx(val + 1)
            lintv = q[1] - discrete_data[li]
            rintv = discrete_data[ri] - q[1]

            hp.remove(lintv + rintv)
            hp.push(lintv)
            hp.push(rintv)

            segroot.update(idx, 1)

        res.append(query(segroot, hp, discrete_data))

    return res


n, q = map(int, stdin.readline().split())
p_a = list(map(int, stdin.readline().split()))
q_a = []
for _ in range(q):
    t, x = map(int, stdin.readline().split())
    q_a.append([t, x])

res_a = trash_problem(n, q, p_a, q_a)
for res in res_a:
    stdout.write(str(res) + '\n')
