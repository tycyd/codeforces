# 2
# 3
# 1 1 1
# 5
# 2 3 1 2 2
from sys import stdin, stdout


def young_explorers(e):

    e.sort()

    res = 1
    cur = e[0]-1

    for i in range(1, len(e)):

        if cur == 0:
            cur = e[i]-1
            res += 1
        else:
            cur -= 1
            cur += e[i] - e[i-1]

    if cur > 0:
        res -= 1

    return res


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N = int(stdin.readline())
        e = list(map(int, stdin.readline().split()))

        stdout.write(str(young_explorers(e)) + '\n')
