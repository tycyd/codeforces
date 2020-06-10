from sys import stdin, stdout
import sys
import threading

#          1(0,1)
#     2(1,0)     5(1,0)
# 3(0,1)      4(0,0)
#
# param: node, min ancestor
# return cost, cnt(0->1), cnt(1->0)
def tree_shuffling(abc, dic):
    cc = dfs(1, -1, 2**31-1, abc, dic)

    if cc[1] > 0 or cc[2] > 0:
        return -1
    else:
        return cc[0]
    return res


def dfs(cur, pnode, pmin, abc, dic):

    cost = 0
    cnt01 = 0
    cnt10 = 0
    cabc = abc[cur-1]

    if cur in dic:
        for nxt in dic[cur]:
            if nxt != pnode:
                cc = dfs(nxt, cur, min(cabc[0], pmin), abc, dic)
                cost += cc[0]
                cnt01 += cc[1]
                cnt10 += cc[2]

    if cabc[1] == 1 and cabc[2] == 0:
        cnt10 += 1
    elif cabc[1] == 0 and cabc[2] == 1:
        cnt01 += 1

    if cabc[0] < pmin:
        pcnt = min(cnt01, cnt10)
        cost += cabc[0]*pcnt*2
        cnt01 -= pcnt
        cnt10 -= pcnt

    return [cost, cnt01, cnt10]


def main():
    n = int(stdin.readline())

    abc = []
    for i in range(n):
        abc.append(list(map(int, stdin.readline().split())))

    dic = {}
    for i in range(n - 1):
        (u, v) = list(map(int, stdin.readline().split()))
        if u not in dic:
            dic[u] = []
        if v not in dic:
            dic[v] = []
        dic[u].append(v)
        dic[v].append(u)

    stdout.write(str(tree_shuffling(abc, dic)) + '\n')


if __name__ == '__main__':

    sys.setrecursionlimit(100000)
    threading.stack_size(10240000)
    t = threading.Thread(target=main)
    t.start()
