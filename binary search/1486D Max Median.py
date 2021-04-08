from sys import stdin, stdout


def max_median(n, k, a_a):
    l = 1
    h = 2*(10**5)

    while l < h:
        pre_sum = [0] * (n+1)
        min_sum = [0] * (n+1)
        found = False

        m = (l + h + 1) // 2
        for i in range(n):
            v = 1 if a_a[i] >= m else -1
            pre_sum[i+1] = v + pre_sum[i]
            min_sum[i+1] = min(min_sum[i], pre_sum[i+1])

            if i + 1 - k >= 0 and pre_sum[i+1] - min_sum[i+1-k] > 0:
                found = True
                l = m
                break

        if not found:
            h = m - 1

    return l


n, k = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
r = max_median(n, k, a_a)
stdout.write(str(r) + '\n')
