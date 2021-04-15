from sys import stdin, stdout


def gcd_and_mst(n, p, a_a):
    ai_a = [[a_a[i], i] for i in range(n)]
    ai_a.sort()
    res = (n-1)*p

    visited = set()

    for ai in ai_a:
        if ai[0] >= p:
            break

        if ai[1] in visited:
            continue
        visited.add(ai[1])

        l = r = ai[1]
        while l - 1 >= 0 and gcd(a_a[l-1], ai[0]) == ai[0]:
            l -= 1
            res -= (p - ai[0])
            if l in visited:
                break
            visited.add(l)

        while r + 1 < n and gcd(a_a[r+1], ai[0]) == ai[0]:
            r += 1
            res -= (p - ai[0])
            if r in visited:
                break
            visited.add(r)

    return res


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


t = int(stdin.readline())
for _ in range(t):
    n, p = map(int, stdin.readline().split())
    a_a = list(map(int, stdin.readline().split()))
    r = gcd_and_mst(n, p, a_a)
    stdout.write(str(r) + '\n')
