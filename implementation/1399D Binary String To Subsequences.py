from sys import stdin, stdout

# 0011
# 01 01
# 01010000
# 01010 0 0 0
# 01011001
# 0101 10 01
# 01010 01 1
# 000110

# 111000

def ufind(u_a, i):
    if i == u_a[i]:
        return i
    u_a[i] = ufind(u_a, u_a[i])
    return u_a[i]


def union(u_a, i, j):
    ri = ufind(u_a, i)
    rj = ufind(u_a, j)
    u_a[ri] = u_a[rj]


# union find
def binary_string_to_subsequences2(n, s):
    u_a = [i for i in range(n)]
    q_a = [[] for _ in range(2)]

    q_a[ord(s[0]) - ord('0')].append(0)

    for i in range(1, n):
        v = ord(s[i]) - ord('0')
        if q_a[v^1]:
            union(u_a, i, q_a[v^1].pop())
        q_a[v].append(i)

    ans1 = len(q_a[0]) + len(q_a[1])
    ans2 = []
    for i in range(n):
        ans2.append(ufind(u_a, i) + 1)

    return [ans1, ans2]


def binary_string_to_subsequences(n, s):

    g = 1
    q_a = [[] for _ in range(2)]
    q_a[ord(s[0]) - ord('0')].append(g)

    ans2 = [g]
    for i in range(1, n):

        v = ord(s[i]) - ord('0')
        if q_a[v^1]:
            q_a[v].append(q_a[v^1].pop())
        else:
            g += 1
            q_a[v].append(g)

        ans2.append(q_a[v][-1])

    ans1 = len(q_a[0]) + len(q_a[1])

    return [ans1, ans2]


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = stdin.readline().strip()

    ans = binary_string_to_subsequences(n, s)
    stdout.write(str(ans[0]) + '\n')
    stdout.write(' '.join(map(str, ans[1])) + '\n')
