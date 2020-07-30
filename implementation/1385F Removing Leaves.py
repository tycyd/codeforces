from sys import stdin, stdout
from collections import deque

if __name__ == '__main__':

    t = int(stdin.readline())

    for x in range(t):
        n, k = map(int, stdin.readline().split())

        dic = {}
        for i in range(n-1):
            x, y = map(int, stdin.readline().split())
            x -= 1
            y -= 1
            if x not in dic:
                dic[x] = set()
            if y not in dic:
                dic[y] = set()
            dic[x].add(y)
            dic[y].add(x)

        if k == 1:
            print(n - 1)
            continue

        isleaf = set()
        leaves = [0 for _ in range(n)]
        for i in range(n):
            if len(dic[i]) == 1:
                isleaf.add(i)
                p = next(iter(dic[i]))
                leaves[p] += 1

        q = deque()
        frd = [set() for _ in range(n)]
        for l in range(n):
            if leaves[l] >= k:
                q.append(l)
            for v in dic[l]:
                if v not in isleaf:
                    frd[l].add(v)

        ans = 0
        while len(q) > 0:
            u = q.popleft()
            ans += leaves[u] // k
            leaves[u] %= k
            if leaves[u] == 0 and len(frd[u]) == 1:
                p = frd[u].pop()
                frd[p].remove(u)

                leaves[p] += 1
                if leaves[p] >= k:
                    q.append(p)

        print(ans)

