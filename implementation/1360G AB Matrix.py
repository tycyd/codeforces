from sys import stdin, stdout

# n m a b
# 3 6 2 1
# 1 1 0 0 0 0
# 0 0 1 1 0 0
# 0 0 0 0 1 1
# a*n = b*m => a/b = m/n

# n m a b
# 5 5 2 2
# 1 1 0 0 0
# 0 0 1 1 0
# 1 0 0 0 1
# 0 1 1 0 0
# 0 0 0 1 1


def ab_matrix(n, m, a, b):

    if a*n != b*m:
        return None

    res = [[0 for j in range(m)] for i in range(n)]

    cur = 0
    for i in range(n):
        for j in range(a):
            res[i][cur] = 1
            cur = (cur + 1) % m

    return res


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        (n, m, a, b) = list(map(int, stdin.readline().split()))
        res = ab_matrix(n, m, a, b)

        if res is None:
            stdout.write("No" + '\n')
        else:
            stdout.write("Yes" + '\n')
            for r in res:
                for c in r:
                    stdout.write(str(c))
                stdout.write('\n')
