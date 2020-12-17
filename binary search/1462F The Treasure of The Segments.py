from sys import stdin, stdout
from heapq import heappop, heappush


# 1 2
#     3         8
#       4 5
#           6 7
#                  9  10
def the_treasure_of_the_segments(n, lr_a):
    lr_a.sort(key=lambda x: (x[0], x[1]))
    res = 0
    hp = []
    for i in range(n):
        lr = lr_a[i]
        while hp and hp[0] < lr[0]:
            heappop(hp)
        heappush(hp, lr[1])

        if i != n - 1 and lr_a[i+1][0] <= lr[1]:
            l = i + 1
            h = n - 1
            while l < h:
                m = (l + h + 1) // 2
                if lr_a[m][0] <= lr[1]:
                    l = m
                else:
                    h = m - 1
            res = max(res, len(hp) + l - i)
        else:
            res = max(res, len(hp))

    return n - res


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    lr_a = []
    for _ in range(n):
        lr_a.append(list(map(int, stdin.readline().split())))
    res = the_treasure_of_the_segments(n, lr_a)
    stdout.write(str(res) + '\n')
