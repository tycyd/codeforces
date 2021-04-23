from sys import stdin, stdout


def cut(n, a_a):
    N = max(a_a)
    p_a = seive_a(N)
    dic = {}
    # up to 2**20
    b_a = [[-1 for j in range(20)] for i in range(n)]
    b_a[n-1][0] = n
    for i in range(n-1, -1, -1):
        if i == n - 1:
            r = n
        else:
            r = b_a[i+1][0]
        for p in p_a[a_a[i]]:
            if p in dic:
                r = min(r, dic[p])
            dic[p] = i
        b_a[i][0] = r

    for i in range(1, 20):
        for j in range(n):
            if b_a[j][i-1] == -1 or b_a[j][i-1] == n or b_a[b_a[j][i-1]][i-1] == -1:
                continue

            b_a[j][i] = b_a[b_a[j][i-1]][i-1]
    return b_a


def solve(b_a, l, r):
    res = 0
    for step in range(19, -1, -1):
        if b_a[l][step] != -1 and b_a[l][step] <= r:
            # print(step)
            res += (1 << step)
            l = b_a[l][step]

    return res + 1


def seive_a(n):
    p_a = [[] for i in range(n+1)]

    for i in range(2, n + 1):
        if len(p_a[i]) > 0:
            continue
        j = i
        while j <= n:
            p_a[j].append(i)
            j += i

    return p_a


n, q = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = cut(n, a_a)
for _ in range(q):
    l, r = map(int, stdin.readline().split())
    res = solve(b_a, l-1, r-1)
    stdout.write(str(res) + '\n')
