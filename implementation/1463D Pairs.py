from sys import stdin, stdout


def pairs(n, b_a):
    x_a = []
    b_s = set(b_a)
    for i in range(1, 2*n+1):
        if i not in b_s:
            x_a.append(i)

    #print(x_a)
    idx = 0
    x = 0
    for b in b_a:
        while idx < n and x_a[idx] < b:
            idx += 1
        if idx >= n:
            break
        x += 1
        idx += 1
    idx = n - 1
    y = 0
    for i in range(n-1, -1, -1):
        while idx >= 0 and x_a[idx] > b_a[i]:
            idx -= 1
        if idx < 0:
            break
        y += 1
        idx -= 1
    return x + 1 - (n - y)


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    b_a = list(map(int, stdin.readline().split()))
    r = pairs(n, b_a)
    stdout.write(str(r) + '\n')
