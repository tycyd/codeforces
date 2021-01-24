from sys import stdin, stdout


# 2 2 2 3 1
# 0 r X X X
# 0 0 r X X
# 0 0 0 r X
# 0 0 0 0 r
def cleaning(n, a_a):
    l_a = [-1] * n
    r_a = [-1] * n

    l_a[0] = a_a[0]
    for i in range(1, n):
        if a_a[i] < l_a[i-1]:
            break
        l_a[i] = a_a[i] - l_a[i-1]

    if l_a[n-1] == 0:
        return 'YES'

    r_a[n-1] = a_a[n-1]
    for i in range(n-2, -1, -1):
        if a_a[i] < r_a[i+1]:
            break
        r_a[i] = a_a[i] - r_a[i+1]

    for i in range(0, n-1):
        r = a_a[i]
        l = a_a[i+1]
        if i > 0:
            if l_a[i-1] < 0:
                continue
            l -= l_a[i-1]
        if i+2 < n:
            if r_a[i+2] < 0:
                continue
            r -= r_a[i+2]
        if 0 <= l == r >= 0:
            return 'YES'

    return 'NO'


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    r = cleaning(n, a_a)
    stdout.write(r + '\n')
