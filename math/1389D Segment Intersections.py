from sys import stdin, stdout


def segment_intersections(n, k, l1, r1, l2, r2):
    lmx = max(l1, l2)
    rmn = min(r1, r2)
    I = max(rmn - lmx, 0) * n

    if I >= k:
        return 0

    k -= I

    lmn = min(l1, l2)
    rmx = max(r1, r2)
    cov = (rmx - lmn) - max(rmn - lmx, 0)

    if cov == 0:
        return k*2

    steps = (lmx - lmn) + (rmx - rmn)
    if steps / cov >= 2:
        if k > cov:
            return steps + (k-cov)*2
        else:
            return (rmx - rmn) + k

    d = min(k // cov, n)
    ans = steps * d

    if (k // cov) < n:
        subans1 = (k % cov)
        if rmn - lmx < 0:
            subans1 += abs(rmn - lmx)

        subans2 = 10 ** 10
        if k // cov > 0:
            subans2 = (k % cov) * 2

        ans += min(subans1, subans2)
    else:
        ans += (k - cov * d)*2

    return ans


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    l1, r1 = map(int, stdin.readline().split())
    l2, r2 = map(int, stdin.readline().split())

    ans = segment_intersections(n, k, l1, r1, l2, r2)
    stdout.write(str(ans) + '\n')
