from sys import stdin, stdout

# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 3 4
#      |----|----|
# 1 -> 2 -> 3 -> 4
# |---------|

# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
#      |---> 5
# 1 -> 2 -> 4
# |-------3---> 6
#         |---> 7
#
#             1
#       2           3
#    (4     5     6     7)
#  8  9  10 11 12 13 14 15

#      1    2   3   4   5
#               6
#               7
#
#          | ------ |
#  1 ----- 2 ------ 3
#  |----------------|
# ind 2 = 1
# ind 3 = 2

def ski_accidents(n, dic, indgree):

    queue = []
    dis = [0 for i in range(n+1)]
    visited = [False for i in range(n + 1)]
    res = []

    for i in range(1, n+1):
        if visited[i]:
            continue

        queue.append(i)
        while len(queue) > 0:
            cur = queue.pop(-1)
            visited[cur] = True

            if dis[cur] == 2:
                res.append(cur)
                if cur in dic:
                    for nxt in dic[cur]:
                        indgree[nxt] -= 1
                    continue

            if cur in dic:
                for nxt in dic[cur]:
                    indgree[nxt] -= 1

                    dis[nxt] = max(dis[nxt], dis[cur] + 1)

                    if indgree[nxt] == 0:
                        queue.append(nxt)

    return res


if __name__ == '__main__':
    T = int(stdin.readline())
    for i in range(T):
        (n, m) = list(map(int, stdin.readline().split()))
        dic = {}
        indgree = [0 for k in range(n+1)]
        for j in range(m):
            (x, y) = list(map(int, stdin.readline().split()))
            if x not in dic:
                dic[x] = []
            dic[x].append(y)
            indgree[y] += 1
        res = ski_accidents(n, dic, indgree)
        stdout.write(str(len(res)) + '\n')
        stdout.write(" ".join(map(str, res)) + '\n')
