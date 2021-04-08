from sys import stdin, stdout
from collections import defaultdict
from heapq import *


class RemovableHeap:
    def __init__(self):
        self.hp = []
        self.rem = []
        self.s = {}
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        if i: return None
        self.__trim()
        return self.hp[0]

    def peek(self):
        self.__trim()
        return self.hp[0]

    def push(self, val):
        heappush(self.hp, val)
        if val in self.s:
            self.s[val] += 1
        else:
            self.s[val] = 1
        self.size += 1
        return True

    def pop(self):
        self.__trim()
        if not self.hp: return None
        self.size -= 1
        val = heappop(self.hp)
        if self.s[val] == 1:
            del self.s[val]
        else:
            self.s[val] -= 1
        return val

    def remove(self, val):
        if val not in self.s: return False
        self.size -= 1
        if self.s[val] == 1:
            del self.s[val]
        else:
            self.s[val] -= 1
        heappush(self.rem, val)
        return True

    def __trim(self):
        while self.rem and self.rem[0] == self.hp[0]:
            heappop(self.hp)
            heappop(self.rem)


def sieve(mx):
    sv_a = [0] * (mx + 1)
    for i in range(2, mx + 1):
        if sv_a[i] == 0:
            sv_a[i] = i
            j = i*i
            while j <= mx:
                if sv_a[j] == 0:
                    sv_a[j] = i
                j += i
    return sv_a


def add(i, x):
    global ans
    while x != 1:
        feq = 0
        div = sv_a[x]

        while sv_a[x] == div:
            feq += 1
            x //= div

        oldFreq = 0
        if div in cnt_a[i]:
            oldFreq = cnt_a[i][div]
        cnt_a[i][div] = oldFreq + feq

        oldMinCnt = 0
        if pp[div].size == n:
            oldMinCnt = pp[div].peek()

        if oldFreq != 0:
            pp[div].remove(oldFreq)
        pp[div].push(cnt_a[i][div])

        if pp[div].size == n:
            newMinCnt = pp[div].peek()
            for k in range(oldMinCnt, newMinCnt):
                ans *= div
                ans %= 1000000007


try:
    sv_a = sieve(200005)
    pp = defaultdict(RemovableHeap)
    n, q = map(int, stdin.readline().split())
    a_a = list(map(int, stdin.readline().split()))
    q_a = []
    cnt_a = [{} for _ in range(len(a_a))]
    ans = 1

    for i in range(len(a_a)):
        add(i, a_a[i])

    for _ in range(q):
        i, x = map(int, stdin.readline().split())
        add(i-1, x)
        print(ans)
except Exception as e:
    print(str(e).replace(" ", "_"))



