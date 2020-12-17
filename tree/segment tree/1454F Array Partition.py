from sys import stdin, stdout
from math import log, ceil


# 1
# 9
# 2 1  |  4 2 4 3 3  |  1 2
def array_partition(n, a_a):
    lm = [a_a[0]]
    rm = [a_a[-1]]

    for i in range(1, n):
        lm.append(max(lm[-1], a_a[i]))
        rm.append(max(rm[-1], a_a[-(i+1)]))

    r = n - 1
    for l in range(n - 2):
        left = lm[l]
        while r > l + 1 and rm[n - 1 - r] <= left:
            r -= 1
        if r < n - 1:
            r += 1

        if left == rm[n - 1 - r]:
            mm = query(0, 0, n - 1, l + 1, r - 1)
            if left == mm:
                return [l + 1, r - l - 1, n - r]
            elif mm < left:
                pass
            elif r < n - 1:
                r += 1
                if left == rm[n - 1 - r] and query(0, 0, n - 1, l + 1, r - 1) == left:
                    return [l + 1, r - l - 1, n - r]
    return []


def build(cur, l, r):
    if l == r:
        segTree[cur] = a_a[l]
        return a_a[l]
    mid = l + (r - l) // 2
    segTree[cur] = min(build(2 * cur + 1, l, mid), build(2 * cur + 2, mid + 1, r))
    return segTree[cur]


def query(cur, sl, sr, l, r):
    if l <= sl and r >= sr:
        return segTree[cur]
    elif l > sr or r < sl:
        return float('inf')
    else:
        mid = sl + (sr - sl) // 2
        return min(query(cur * 2 + 1, sl, mid, l, r), query(cur * 2 + 2, mid + 1, sr, l, r))


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))

    size = int(2 ** (ceil(log(n, 2)) + 1) - 1)
    segTree = [float('inf') for i in range(size)]
    build(0, 0, n - 1)
    r = array_partition(n, a_a)
    if r:
        stdout.write('YES\n')
        stdout.write(' '.join(map(str, r)) + '\n')
    else:
        stdout.write('NO\n')