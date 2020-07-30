from sys import stdin, stdout

# 3 8
# 2
# 1 1 0
# 0 1 1
# 0 0 1

# 1 0 0
# 0 1 0
# 0 0 1

# f(A) = (max(R) - min(R))^2 + (max(C) - min(C))^2
if __name__ == '__main__':

    def grid_00100(n, k):
        a = [[0 for j in range(n)] for i in range(n)]
        f = 0 if k == 0 or (k % n) == 0 else 2

        i = j = 0
        while k > 0:
            a[i][j] = 1
            i += 1
            j += 1
            j %= n

            if i == n:
                i = 0
                j += 1
                j %= n
            k -= 1

        return [f, a]


    t = int(stdin.readline())
    for i in range(t):
        n, k = map(int, stdin.readline().split())
        ans = grid_00100(n, k)
        stdout.write(str(ans[0]) + '\n')
        for j in range(n):
            stdout.write("".join(map(str, ans[1][j])) + '\n')
