import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**9)
#threading.stack_size(32*1024)
#threading.stack_size(1024*1024)
threading.stack_size(16*2048*2048)


def dfs(node, depth, n, visited, dic, plist, dep_a):

    if node in visited:
        return

    visited.add(node)
    plist.append(node)

    if depth > 0:
        dep_a[depth].append(node)

    if len(plist) > n//2:
        return plist

    for ch in dic[node]:
        res = dfs(ch, depth + 1, n, visited, dic, plist, dep_a)
        if res:
            return res

    plist.pop()

    return []


def pairs_of_pairs(n, m, dic):

    dep_a = [[] for i in range(n//2 + 1)]
    ans = dfs(1, 0, n, set(), dic, [], dep_a)

    if ans:
        return [1, ans]
    else:
        ans2 = []
        for dep in dep_a:
            while len(dep) > 1:
                ans2.append([dep.pop(), dep.pop()])
        return [2, ans2]


def solve():
    try:
        t = int(stdin.readline())
        for _ in range(t):
            dic = {}
            n, m = map(int, stdin.readline().split())

            for _ in range(m):
                u, v = map(int, stdin.readline().split())
                if u not in dic:
                    dic[u] = []
                if v not in dic:
                    dic[v] = []
                dic[u].append(v)
                dic[v].append(u)

            ans = pairs_of_pairs(n, m, dic)
            if ans[0] == 1:
                stdout.write('PATH\n')
                stdout.write(str(len(ans[1])) + '\n')
                stdout.write(' '.join(map(str, ans[1])) + '\n')
            else:
                stdout.write('PAIRING\n')
                stdout.write(str(len(ans[1])) + '\n')
                for p in ans[1]:
                    stdout.write(' '.join(map(str, p)) + '\n')
    except Exception as e:
        print("".join(str(e).split()))


threading.Thread(target=solve).start()

#solve()
