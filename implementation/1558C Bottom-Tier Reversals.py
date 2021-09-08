from sys import stdin, stdout


#  x x 9 x x x x
#  9 x x x x 8 x
#  x x x x 9 8 x
#  x 8 9 x x x x
#  9 8 x x x x x
#  x x x x x 8 9

def solve(n, a_a):
    p_a = [-1] * n
    for i in range(n):
        a_a[i] -= 1
        p_a[a_a[i]] = i
        if (a_a[i]) % 2 != i % 2:
            return [-1]

    res = []
    for i in range(n//2, 0, -1):
        cur = i*2

        # reverse cur to head
        res.append(p_a[cur]+1)
        reverse(a_a, p_a, p_a[cur])

        # reverse cur before smaller one
        res.append(p_a[cur-1])
        reverse(a_a, p_a, p_a[cur-1]-1)

        # reverse after smaller one
        res.append(p_a[cur-1]+2)
        reverse(a_a, p_a, p_a[cur - 1] + 1)

        # reverse cur to head
        res.append(p_a[cur] + 1)
        reverse(a_a, p_a, p_a[cur])

        # reverse cur to end
        res.append(cur + 1)
        reverse(a_a, p_a, cur)

    return [len(res), res]


def reverse(a_a, p_a, i):
    l = 0
    r = i
    while l < r:
        swap(a_a, l, r)
        swap(p_a, a_a[l], a_a[r])
        l += 1
        r -= 1


def swap(a_a, i, j):
    tmp = a_a[i]
    a_a[i] = a_a[j]
    a_a[j] = tmp


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    res = solve(n, a_a)
    stdout.write(str(res[0]) + '\n')
    if res[0] > 0:
        stdout.write(' '.join(map(str, res[1])) + '\n')
