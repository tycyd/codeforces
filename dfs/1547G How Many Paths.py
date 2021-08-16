import sys
import threading
from sys import stdin, stdout
from collections import deque

sys.setrecursionlimit(10**5)
threading.stack_size(16*2048*2048)


# bfs + dfs (find loop)
def solve(n, dic):
    r_a = [0] * n
    q = deque([0])

    # bfs
    while len(q) > 0:
        c = q.popleft()
        if r_a[c] == 2:
            continue
        r_a[c] += 1
        if c not in dic:
            continue

        for nxt in dic[c]:
            q.append(nxt)

    visited = set()
    lst = []
    # dfs
    dfs(0, dic, r_a, visited, lst)

    stdout.write(' '.join(map(str, r_a)) + '\n')


def dfs2(c, r_a, dic):
    if r_a[c] == -1:
        return
    r_a[c] = -1
    if c in dic:
        for nxt in dic[c]:
            dfs2(nxt, r_a, dic)


def dfs(c, dic, r_a, visited, lst):

    if r_a[c] == -1:
        return

    if c in visited:
        # loop
        i = len(lst) - 1

        dfs2(c, r_a, dic)
        while lst[i] != c:
            dfs2(lst[i], r_a, dic)
            i -= 1
        return

    visited.add(c)
    lst.append(c)
    if c in dic:
        for nxt in dic[c]:
            dfs(nxt, dic, r_a, visited, lst)

    visited.remove(c)
    lst.pop()


def main():
    t = int(stdin.readline())
    for _ in range(t):
        stdin.readline()
        n, m = map(int, stdin.readline().split())
        dic = {}
        for _ in range(m):
            a, b = map(int, stdin.readline().split())
            if a-1 not in dic:
                dic[a-1] = []
            dic[a-1].append(b-1)
        solve(n, dic)


threading.Thread(target=main).start()
