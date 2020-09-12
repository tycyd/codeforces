from sys import stdin, stdout


def two_platforms(n, k, x_a):
    x_a.sort()

    #print(x_a)

    la = [0] * n
    ra = [0] * n

    hi = 0
    mx = 0
    for i in range(n):
        while hi < i and x_a[i] - x_a[hi] > k:
            hi += 1
        mx = max(mx, i - hi + 1)
        la[i] = mx

    #print(la)

    tj = n - 1
    mx = 0
    for j in range(n-1, -1, -1):
        while tj > j and x_a[tj] - x_a[j] > k:
            tj -= 1
        mx = max(mx, tj - j + 1)
        ra[j] = mx

    ans = ra[0]
    for i in range(0, n-1):
        ans = max(ans, la[i] + ra[i+1])

    #print(ra)

    return ans


t = int(stdin.readline())
for num in range(t):
    n, k = map(int, stdin.readline().split())
    x_a = list(map(int, stdin.readline().split()))
    y_a = list(map(int, stdin.readline().split()))
    ans = two_platforms(n, k, x_a)
    stdout.write(str(ans) + '\n')
