from sys import stdin, stdout

# 4 7 9 [2] [3]
# 3 4 7 9 [2]
# 2 3 4 7 9
# 4 7 9 [2 3]

# [4 7 9] 2 3
# [4] 7 9 2 3
# [7] 9 2 3 4
# [9] 2 3 4 7
# 2 3 4 7 9

# 4 [7 9] 3 3 10
# 1  2 3  0 0  4
# 1  2 3       4
# find longest subseq that already sorted

# 1
# 1 2
# 1 2 3
# 10, 9, 1, 7, 0, 8, 0, 7, 3, 6, 2, 5, 4, 5, 11, 6, 7, 12, 0, 6
#                                   5     5      6            6

# 2 2 3 3
# dp:
# dp[i,0]: counts of a[i],   ex 3 [3]
# dp[i,1]: still has a[i],   ex 2 2 [3]
# dp[i,2]: no a[i]           ex 2 2 3 [3]

def flying_sort(n, a):

    b = sorted(a)

    dic = {}
    seq = 1

    dic[b[0]] = seq

    num = [0 for i in range(n + 1)]
    head = [0 for i in range(n + 1)]
    tail = [-1 for i in range(n+1)]
    pos = [0 for i in range(n+1)]

    for i in range(1, len(b)):
        if b[i] != b[i-1]:
            seq += 1
            dic[b[i]] = seq

    for i in range(len(a)):
        a[i] = dic[a[i]]
        num[a[i]] += 1
        tail[a[i]] = i+1
        if head[a[i]] == 0:
            head[a[i]] = i+1

    # find longest subseq
    dp = [[0, 0, 0] for i in range(n+1)]
    maxseq = 0

    #print(a)

    for i in range(1, n+1):

        v = a[i-1]
        dp[i][0] = dp[pos[v]][0] + 1

        #print(v)

        dp[i][1] = max(dp[pos[v]][1] + 1, dp[pos[v - 1]][0] + 1, dp[pos[v - 1]][2] + 1)

        if tail[v] == i:
            dp[i][2] = dp[head[v]][1] + num[v] - 1

        pos[v] = i

        for k in range(3):
            maxseq = max(maxseq, dp[i][k])

    #for i in range(len(dp)):
    #    print(a[i-1])
    #    print(dp[i])

    res = len(a) - maxseq
    return res


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        stdout.write(str(flying_sort(n, a)) + '\n')
