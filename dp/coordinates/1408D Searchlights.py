from sys import stdin, stdout


def search_lights(n, m, ab, cd):
    y_a = [0] * (10**6 + 1)
    for i in range(n):
        for j in range(m):
            if ab[i][0] > cd[j][0] or ab[i][1] > cd[j][1]:
                continue
            x = cd[j][0] - ab[i][0]
            y = cd[j][1] - ab[i][1] + 1
            y_a[x] = max(y_a[x], y)

    r = 10 ** 9
    mx = 0
    for i in range(10**6, -1, -1):
        mx = max(mx, y_a[i])
        r = min(r, mx + i)

    return r


n, m = map(int, stdin.readline().split())
ab = []
cd = []
for _ in range(n):
    ab.append(list(map(int, stdin.readline().split())))
for _ in range(m):
    cd.append(list(map(int, stdin.readline().split())))

res = search_lights(n, m, ab, cd)
stdout.write(str(res) + '\n')
