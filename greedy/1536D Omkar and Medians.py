from sys import stdin, stdout
import heapq


def omkar_and_medians(n, b_a):
    ql = []
    qr = []
    m = b_a[0]

    for i in range(1, n):
        if b_a[i] == m:
            continue
        elif b_a[i] > m:
            if qr and qr[0] < b_a[i]:
                return 'NO'

            if qr and qr[0] == b_a[i]:
                heapq.heappop(qr)

            heapq.heappush(ql, -m)
        else:
            if ql and -ql[0] > b_a[i]:
                return 'NO'

            if ql and -ql[0] == b_a[i]:
                heapq.heappop(ql)

            heapq.heappush(qr, m)

        m = b_a[i]
    return 'YES'


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    b_a = list(map(int, stdin.readline().split()))
    res = omkar_and_medians(n, b_a)
    stdout.write(res + '\n')
