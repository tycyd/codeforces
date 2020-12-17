from sys import stdin, stdout
from collections import deque

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 2 2 2 3 3
# 2 2 2 3 3
def binary_table(n, m, tbl):
    r_a = []
    # 1
    for i in range(n-2):
        for j in range(m):
            if tbl[i][j] == 0:
                continue
            r = [i + 1, j + 1, i + 2, j + 1, i + 2]
            if j == m - 1:
                r.append(j)
            else:
                r.append(j + 2)
            r_a.append(r)
            change_tbl(r, tbl)

    # 2
    for j in range(m-2):
        for i in range(n-2, n):
            if tbl[i][j] == 0:
                continue
            r = [i + 1, j + 1, i + 1, j + 2]
            if i == n-2:
                r.append(i + 2)
            else:
                r.append(i)
            r.append(j + 2)
            r_a.append(r)
            change_tbl(r, tbl)

    # 3
    a0 = deque()
    a1 = deque()
    for i in range(n-2, n):
        for j in range(m - 2, m):
            if tbl[i][j] == 0:
                a0.append([i + 1, j + 1])
            else:
                a1.append([i + 1, j + 1])

    #print(a0)
    #print(a1)
    tbl_corner(a0, a1, r_a)

    return r_a


def tbl_corner(a0, a1, r_a):
    cnt1 = len(a1)
    if cnt1 == 0:
        return
    if cnt1 == 3:
        return step_1(a0, a1, r_a)
    if cnt1 == 2:
        return step_2(a0, a1, r_a)
    if cnt1 == 1:
        return step_3(a0, a1, r_a)
    if cnt1 == 4:
        return step_4(a0, a1, r_a)


def step_1(a0, a1, r_a):
    r = []
    while a1:
        c = a1.popleft()
        r.append(c[0])
        r.append(c[1])
        a0.append(c)
    r_a.append(r)


def step_2(a0, a1, r_a):
    c0_0 = a0.popleft()
    c0_1 = a0.popleft()
    c1_0 = a1.popleft()

    r = [c0_0[0], c0_0[1], c0_1[0], c0_1[1], c1_0[0], c1_0[1]]
    r_a.append(r)

    a1.append(c0_0)
    a1.append(c0_1)
    a0.append(c1_0)
    step_1(a0, a1, r_a)


def step_3(a0, a1, r_a):
    c1_0 = a1.popleft()
    c0_0 = a0.popleft()
    c0_1 = a0.popleft()

    r = [c1_0[0], c1_0[1], c0_0[0], c0_0[1], c0_1[0], c0_1[1]]
    r_a.append(r)

    a0.append(c1_0)
    a1.append(c0_0)
    a1.append(c0_1)
    step_2(a0, a1, r_a)


def step_4(a0, a1, r_a):
    c1_0 = a1.popleft()
    c1_1 = a1.popleft()
    c1_2 = a1.popleft()

    r = [c1_0[0], c1_0[1], c1_1[0], c1_1[1], c1_2[0], c1_2[1]]
    r_a.append(r)

    a0.append(c1_0)
    a0.append(c1_1)
    a0.append(c1_2)
    step_3(a0, a1, r_a)


def change_tbl(r, tbl):
    tbl[r[0] - 1][r[1] - 1] ^= 1
    tbl[r[2] - 1][r[3] - 1] ^= 1
    tbl[r[4] - 1][r[5] - 1] ^= 1


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    tbl = []
    for _ in range(n):
        s = stdin.readline().strip()
        tbl.append([ord(c) - ord('0') for c in s])
    r_a = binary_table(n, m, tbl)
    stdout.write(str(len(r_a)) + '\n')
    for r in r_a:
        stdout.write(' '.join(map(str, r)) + '\n')
