from sys import stdin, stdout


def new_year_puzzle(n, m, rc_a):
    rc_a.sort(key=lambda x: x[1])

    cnt = 0
    i = 0
    while i < m:
        # up, down
        if i + 1 < m and rc_a[i][1] == rc_a[i + 1][1]:
            if cnt != 0:
                return 'NO'
            else:
                i += 1
        elif cnt == 1:
            cnt = 0
        elif cnt == 0:
            if i + 1 < m and (rc_a[i + 1][1] - rc_a[i][1]) % 2 == 0 and rc_a[i][0] == rc_a[i + 1][0]:
                return 'NO'
            if i + 1 < m and (rc_a[i + 1][1] - rc_a[i][1]) % 2 == 1 and rc_a[i][0] != rc_a[i + 1][0]:
                return 'NO'
            cnt = 1
        i += 1

    if cnt == 0:
        return 'YES'
    else:
        return 'NO'


t = int(stdin.readline())
for _ in range(t):
    stdin.readline()
    n, m = map(int, stdin.readline().split())
    rc_a = []
    for _ in range(m):
        r, c = map(int, stdin.readline().split())
        rc_a.append([r, c])
    r = new_year_puzzle(n, m, rc_a)
    stdout.write(str(r) + '\n')
