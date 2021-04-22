from sys import stdin, stdout


def garden_of_the_sun(n, m, s_a):
    if m == 1:
        for i in range(n):
            s_a[i][0] = 'X'
        return s_a

    j = 1
    while j < m:
        for i in range(n):
            s_a[i][j] = 'X'

        j += 3

    j = 3
    while j < m - 1:
        found = False
        for i in range(n):
            if s_a[i][j] == 'X':
                s_a[i][j-1] = 'X'
                found = True
                break
            if s_a[i][j-1] == 'X':
                s_a[i][j] = 'X'
                found = True
                break

        if not found:
            s_a[0][j] = 'X'
            s_a[0][j-1] = 'X'

        j += 3

    if j == m - 1:
        for i in range(n):
            if s_a[i][j] == 'X':
                s_a[i][j-1] = 'X'

    return s_a


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    s_a = []
    for _ in range(n):
        s_a.append(list(stdin.readline().strip()))
    r_a = garden_of_the_sun(n, m, s_a)
    for i in range(n):
        stdout.write(''.join(r_a[i]) + '\n')
