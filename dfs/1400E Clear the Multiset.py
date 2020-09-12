import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**9)
threading.stack_size(16*2048*2048)


def clear_the_multiset(n, a_a):
    return dfs(1, n, a_a)


def dfs(l, r, a_a):
    if l > r:
        return 0

    mval = a_a[l]
    midx = l
    mx = max(a_a[l - 1], a_a[r + 1])

    for i in range(l, r+1):
        if mval > a_a[i]:
            mval = a_a[i]
            midx = i

    r1 = r - l + 1
    r2 = mval + dfs(l, midx-1, a_a) + dfs(midx+1, r, a_a) - mx

    return min(r1, r2)


def solve():
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    a_a.insert(0, 0)
    a_a.append(0)

    ans = clear_the_multiset(n, a_a)
    stdout.write(str(ans))


threading.Thread(target=solve).start()
