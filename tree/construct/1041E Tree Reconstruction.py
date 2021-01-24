from sys import stdin, stdout


# 4
# 1 4
# 3 4
# 3 4
def three_reconstruction(n, ab_a):
    res = []
    cnt = [0] * (n + 1)

    for ab in ab_a:
        a, b = ab
        if (a != n and b != n) or a == b:
            return [False]
        cnt[min(a, b)] += 1

    cur = 0
    for i in range(1, n+1):
        cur += cnt[i]
        if cur > i:
            return [False]

    hs = set()
    for i in range(1, n + 1):
        hs.add(i)
    # print(hs)
    last = -1
    for i in range(1, n+1):
        if cnt[i] > 0:
            hs.remove(i)
            if last != -1:
                res.append([last, i])
            last = i
            cnt[i] -= 1
        while cnt[i] > 0:
            v = min(hs)
            res.append([last, v])
            last = v
            cnt[i] -= 1
            hs.remove(v)
    res.append([last, n])

    return [True, res]


n = int(stdin.readline())
ab_a = []
for _ in range(n-1):
    ab_a.append(list(map(int, stdin.readline().split())))
res = three_reconstruction(n, ab_a)
if res[0]:
    stdout.write('YES\n')
    for p in res[1]:
        stdout.write(str(p[0]) + ' ' + str(p[1]) + '\n')
else:
    stdout.write('NO\n')
