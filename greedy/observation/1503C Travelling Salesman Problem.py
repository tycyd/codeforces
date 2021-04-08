from sys import stdin, stdout

# a
def travelling_salesman(n, ac_a):
    ac_a.sort()
    pre = 0
    lmax = ac_a[0][0] + ac_a[0][1]
    r = ac_a[0][1]

    for i in range(1, n):
        if lmax < ac_a[i][0] + ac_a[i][1]:
            pre = i
            r += max(0, ac_a[i][0] - lmax)
            lmax = ac_a[i][0] + ac_a[i][1]
        r += ac_a[i][1]

    if pre != n-1:
        r += max(0, ac_a[n-1][0] - lmax)

    return r


n = int(stdin.readline())
ac_a = []
for _ in range(n):
    a, c = map(int, stdin.readline().split())
    ac_a.append([a,c])
r = travelling_salesman(n, ac_a)
stdout.write(str(r) + '\n')
