from sys import stdin, stdout
import heapq


class Heap(object):
    def __init__(self, initial=None, key=lambda x:x):
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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def cmp(x):
    return x[0]*N + x[1]


def playlist(n, a_a):
    hp = Heap(key=cmp)
    next_a = []
    for i in range(n):
        if gcd(a_a[i], a_a[(i+1) % n]) == 1:
            hp.push([0, i, (i+1) % n])
        next_a.append((i+1) % n)

    s = set()
    ans = []
    while len(hp) > 0:
        l, i, j = hp.pop()
        if i in s or j in s:
            continue

        s.add(j)
        ans.append(j+1)
        nj = next_a[j]
        if nj not in s and gcd(a_a[i], a_a[nj]) == 1:
            hp.push([l+1, i, nj])

    # print(ans)

    if len(ans) > 0:
        return [len(ans)] + ans
    else:
        return [0]


#def union(ua, i, j):
#    ri = ufind(i)
#    rj = ufind(j)


#def ufind()


N = 10**5
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    r = playlist(n, a_a)
    stdout.write(' '.join(map(str, r)) + '\n')
