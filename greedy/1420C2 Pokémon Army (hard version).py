from sys import stdin, stdout


def pkemon_amy(n, q, a_a, lr_a):
    res_a = []

    a_a.insert(0, -1)
    a_a.append(-1)

    res = [0]
    for i in range(1, n+1):
        add(a_a, i, res)
    res_a.append(res[0])

    for lr in lr_a:
        l, r = lr
        earse(a_a, l, res)
        earse(a_a, l-1, res)
        earse(a_a, l+1, res)

        if r-1 > l+1:
            earse(a_a, r-1, res)
        if r > l+1:
            earse(a_a, r, res)
        earse(a_a, r+1, res)

        tmp = a_a[l]
        a_a[l] = a_a[r]
        a_a[r] = tmp

        add(a_a, l, res)
        add(a_a, l - 1, res)
        add(a_a, l + 1, res)

        if r-1 > l+1:
            add(a_a, r-1, res)
        if r > l+1:
            add(a_a, r, res)
        add(a_a, r+1, res)

        res_a.append(res[0])

    return res_a


def earse(a_a, i, res):
    if i == 0 or i == len(a_a) - 1:
        return

    if a_a[i - 1] < a_a[i] > a_a[i + 1]:
        res[0] -= a_a[i]
    elif a_a[i - 1] > a_a[i] < a_a[i + 1]:
        res[0] += a_a[i]


def add(a_a, i, res):
    if i == 0 or i == len(a_a) - 1:
        return

    if a_a[i-1] < a_a[i] > a_a[i+1]:
        res[0] += a_a[i]
    elif a_a[i-1] > a_a[i] < a_a[i+1]:
        res[0] -= a_a[i]


t = int(stdin.readline())
for _ in range(t):
    n, q = map(int, stdin.readline().split())
    a_a = list(map(int, stdin.readline().split()))
    a_a.insert(0, -1)
    a_a.append(-1)

    res = [0]
    for i in range(1, n+1):
        add(a_a, i, res)
    stdout.write(str(res[0]) + '\n')

    #lr_a = []
    for _ in range(q):
        l, r = map(int, stdin.readline().split())

        earse(a_a, l, res)
        earse(a_a, l - 1, res)
        earse(a_a, l + 1, res)

        if r - 1 > l + 1:
            earse(a_a, r - 1, res)
        if r > l + 1:
            earse(a_a, r, res)
        earse(a_a, r + 1, res)

        tmp = a_a[l]
        a_a[l] = a_a[r]
        a_a[r] = tmp

        add(a_a, l, res)
        add(a_a, l - 1, res)
        add(a_a, l + 1, res)

        if r - 1 > l + 1:
            add(a_a, r - 1, res)
        if r > l + 1:
            add(a_a, r, res)
        add(a_a, r + 1, res)

        stdout.write(str(res[0]) + '\n')
        #lr_a.append([l,r])
    #res_a = pkemon_amy(n, q, a_a, lr_a)
    #for res in res_a:
        #stdout.write(str(res) + '\n')
