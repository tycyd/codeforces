from sys import stdin, stdout


# 2 5 7 9 11,   10
# 7 9, 11
# 2 2 3 4,     8
#

if __name__ == '__main__':

    def dfs(idx, a, x, memo):
        if idx >= len(a):
            return 0

        if memo[idx] != -1:
            return memo[idx]

        r = x // a[idx]
        if x % a[idx] != 0:
            r += 1

        r1 = 0
        if idx + r - 1 < len(a):
            r1 = 1 + dfs(idx + r, a, x, memo)
        r2 = dfs(idx + 1, a, x, memo)

        memo[idx] = max(r1, r2)

        return memo[idx]

    # dfs
    def create_the_teams2(n, x, a):
        a.sort()
        memo = [-1]*n

        return dfs(0, a, x, memo)

    # greedy
    def create_the_teams(n, x, a):
        a.sort(reverse=True)

        res = 0
        cnt = 0
        for i in range(n):
            cnt += 1

            if a[i]*cnt >= x:
                res += 1
                cnt = 0

        return res


    t = int(stdin.readline())

    for i in range(t):
        n, x = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        res = create_the_teams(n, x, a)
        stdout.write(str(res) + '\n')
