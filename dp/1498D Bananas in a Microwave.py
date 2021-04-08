from sys import stdin, stdout
import math


DIV = int(1e5)


def ceil(x, y):
    return (x + y - 1) // y


n, m = map(int, stdin.readline().split())
r_a = [-1] * (m + 1)
d_a = [[-1, -1] for _ in range(m + 1)]

d_a[0] = [0, 0]
for i in range(1, n+1):
    #t, x, y = map(float, stdin.readline().split())
    #t = int(t)
    #x /= 10**5
    #y = int(y)
    t, x, y = map(int, stdin.readline().split())

    for j in range(m + 1):
        nj = 0
        if t == 1:
            # nj = int(math.ceil(j + x))
            nj = j + ceil(x, DIV)
        else:
            # nj = int(math.ceil(j * x))
            nj = ceil(j*x, DIV)
        if nj > m:
            break

        if d_a[j][1] != -1:
            if d_a[j][0] == i and d_a[j][1] < y and d_a[nj][0] == -1:
                r_a[nj] = i
                d_a[nj] = [i, d_a[j][1] + 1]
            elif d_a[j][0] != i and d_a[nj][0] == -1:
                r_a[nj] = i
                d_a[nj] = [i, 1]
r_a.pop(0)
stdout.write(' '.join(map(str, r_a)))
