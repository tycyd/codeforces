from sys import stdin, stdout
import heapq

# (3 2) (6 1 5) (7) (8 4)
# 3 2 6 1 5 7
# 8 4

# (6 1 3) (7 4 5) (8 2)
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))

    hp = []
    for i in range(2*n):
        heapq.heappush(hp, (-p[i], i))

    s = set()
    s.add(0)
    idx = 2*n
    yes = False

    while hp:
        (v, i) = heapq.heappop(hp)

        if i > idx:
            continue
        cnt = idx - i
        if (n - cnt) in s:
            yes = True
            break

        for l in list(s):
            s.add(l + cnt)

        idx = i

    if yes:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")