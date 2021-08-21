from sys import stdin, stdout

# gcd observation:
# f(x) => number of g(x), 2*g(x), 3*g(x)....
# g(x) => number of gcd(..) is exact x
#
# formula:
# g(i) = f(i) - g(i*2) - g(i+3) ....
# g(m) = f(m)
# g(m-1) = f(m-1) - g((m-1)*2)..
# g(m-2) = f(m-2) - g((m-2)*2) - g((m-2)*3)..
# ...
# g(1) = f(1) - g(m) - g(m-1) ... - g(2)

# (m + m/2 + m/3 ... + 1) => O(logM)
# solve l, r, m counts by dp O(N*M)
# total time complexity: O(N*M*logM)


# 0, 3, 6, 9, 12
def calc(d, lr_a2, m, g_a, ks_a):
    M = m // d

    ks_a[0] = 1
    for i in range(1, M+1):
        ks_a[i] = 0

    for i in range(len(lr_a2)):
        l, r = map(int, lr_a2[i])

        for j in range(0, M+1):





n, m = map(int, stdin.readline().split())
lr_a = []
lr_a2 = [[-1,-1] for _ in range(n)]
for _ in range(n):
    lr_a.append(list(map(int, stdin.readline().split())))

ks_a = [0] * (m+1)
g_a = [0] * (m+1)
for d in range(m, 0, -1):
    # find l <= m <= high(xm) <= r
    check = True
    for i in range(n):
        if lr_a[0] <= m <= lr_a[1]:
            lr_a2[i][0] = m
            lr_a2[i][1] = m * (((lr_a[1] - m) // m) + 1)
        else:
            check = False
            break

    if check:
        calc(d, lr_a2, m, g_a, ks_a)

