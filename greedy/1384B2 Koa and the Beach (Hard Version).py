from sys import stdin, stdout


# 5 2 3
# 1 2 3 2 2
#
def koa_and_beach(n, k, l, d_a):
    sp_a = []

    for i in range(len(d_a)):
        if d_a[i] + k <= l:
            sp_a.append(i)
        if d_a[i] > l:
            return 'No'
    sp_a.append(n)

    pre = -1
    for i in sp_a:
        down = True
        ct = k
        for j in range(pre + 1, i):
            if down:
                ct -= 1
            else:
                ct += 1

            if d_a[j] + ct > l:
                if down:
                    ct = l - d_a[j]
                else:
                    return 'No'

            if ct == k:
                down = True
            elif ct == 0:
                down = False

        pre = i

    return 'Yes'


# d + p[i] <= l
t = int(stdin.readline())
for _ in range(t):
    n, k, l = map(int, stdin.readline().split())
    d_a = list(map(int, stdin.readline().split()))

    res = koa_and_beach(n, k, l, d_a)
    stdout.write(str(res) + '\n')
