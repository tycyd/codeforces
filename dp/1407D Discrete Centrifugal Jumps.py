from sys import stdin, stdout


def discrete_centrifugal_jumps(n, h_a):
    jump_a1 = [[] for _ in range(n)]
    jump_a2 = [[] for _ in range(n)]
    st1 = []
    st2 = []

    for i in range(n):
        # h l l l h
        if not st1 or h_a[i] <= st1[-1][1]:
            st1.append([i, h_a[i]])
        else:
            pre = -1
            while st1 and st1[-1][1] < h_a[i]:
                p = st1.pop()
                if pre != p[1]:
                    jump_a1[p[0]].append(i)
                pre = p[1]

            if st1:
                jump_a1[st1[-1][0]].append(i)

            st1.append([i, h_a[i]])

        # l h h h l
        if not st2 or h_a[i] >= st2[-1][1]:
            st2.append([i, h_a[i]])
        else:
            pre = -1
            while st2 and st2[-1][1] > h_a[i]:
                p = st2.pop()
                if pre != p[1]:
                    jump_a2[p[0]].append(i)
                pre = p[1]

            if st2:
                jump_a2[st2[-1][0]].append(i)

            st2.append([i, h_a[i]])

    #memo = [-1 for _ in range(n)]
    #res = dfs(0, jump_a1, jump_a2, n, memo)
    #return res

    dp = [2**31-1 for _ in range(n)]
    dp[n-1] = 0
    for i in range(n-2, -1, -1):
        dp[i] = 1 + dp[i+1]
        for nxt in jump_a1[i]:
            dp[i] = min(dp[i], 1 + dp[nxt])
        for nxt in jump_a2[i]:
            dp[i] = min(dp[i], 1 + dp[nxt])

    return dp[0]


def dfs(i, jump_a1, jump_a2, n, memo):
    if i == n-1:
        return 0
    if memo[i] != -1:
        return memo[i]

    res = 2**31-1
    for nxt in jump_a1[i]:
        res = min(res, 1 + dfs(nxt, jump_a1, jump_a2, n, memo))

    for nxt in jump_a2[i]:
        res = min(res, 1 + dfs(nxt, jump_a1, jump_a2, n, memo))

    res = min(res, 1 + dfs(i+1, jump_a1, jump_a2, n, memo))
    memo[i] = res

    return res


n = int(stdin.readline())
h_a = list(map(int, stdin.readline().split()))
k = discrete_centrifugal_jumps(n, h_a)
stdout.write(str(k) + '\n')
