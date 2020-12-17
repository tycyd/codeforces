import sys
import threading
from sys import stdin, stdout


sys.setrecursionlimit(10**9)
threading.stack_size(16*2048*2048)
# 1 - 2 - 3
#     |   |
#     | - 4
g_set = set()
g_res = 0


def number_of_simple_paths(n, dic):
    global g_set
    global g_res

    g_set = set()
    g_res = 0

    s = set()
    lst = []
    findloop(1, -1, dic, s, lst)

    if len(g_set) == n:
        return (n-1)*n

    v_a = []
    for node in g_set:
        lr = dfs(node, -1, dic)
        v_a.append(lr)

    ts = sum(v_a)
    for v in v_a:
        ts -= v
        g_res += (v * ts * 2)

    return g_res


def findloop(node, pnode, dic, s, lst):
    global g_set

    if node in s:
        return True

    s.add(node)
    lst.append(node)
    for nnode in dic[node]:
        if nnode == pnode:
            continue

        r = findloop(nnode, node, dic, s, lst)
        if r:  # loop
            if len(g_set) == 0:
                while lst[-1] != nnode:
                    g_set.add(lst.pop())
                g_set.add(lst.pop())

            return True
    lst.pop()

    return False


def dfs(node, pnode, dic):
    global g_set
    global g_res

    count = 1
    c_a = []
    for nnode in dic[node]:
        if nnode == pnode or nnode in g_set:
            continue
        c_a.append(dfs(nnode, node, dic))
        count += c_a[-1]

    tc = count - 1
    lr = 0

    for c in c_a:
        tc -= c
        lr += c * tc
        lr += c

    g_res += lr

    return count


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        dic = {}
        for _ in range(n):
            u, v = map(int, stdin.readline().split())
            if u not in dic:
                dic[u] = []
            if v not in dic:
                dic[v] = []
            dic[u].append(v)
            dic[v].append(u)

        r = number_of_simple_paths(n, dic)
        stdout.write(str(r) + '\n')


threading.Thread(target=solve).start()