from sys import stdin, stdout
from heapq import heappush, heappop

# 5 3 1, 6
# 2 3 3 1
# 2 2 1 3 1
# 2 2 1 2 1 1


# 10, 3 => 3, 3, 4
def calc(x, y):
    a = x // y
    l = x - y * a
    r = a * a * (y - l) + (a + 1) * (a + 1) * l
    return r


n, k = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))

res = 0
hpa = []
for i in range(n):
    res += a_a[i] * a_a[i]
    heappush(hpa, [calc(a_a[i], 2) - calc(a_a[i], 1), 2, i])

for i in range(k-n):
    m_a = heappop(hpa)
    res += m_a[0]

    heappush(hpa, [calc(a_a[m_a[2]], m_a[1] + 1) - calc(a_a[m_a[2]], m_a[1]), m_a[1] + 1, m_a[2]])

stdout.write(str(res))
