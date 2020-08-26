from sys import stdin, stdout


# i   j k   l
# 1 3 3 1 2 3
def zigzags(n, a_a):

    ans = 0
    freq = [0 for _ in range((n+1)*(n+1))]
    for j in range(n-3, 0, -1):
        k = j+1
        for l in range(k+1, n):
            freq[a_a[k]*n + a_a[l]] += 1
        for i in range(j):
            ans += freq[a_a[i]*n + a_a[j]]
    return ans


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    ans = zigzags(n, a_a)
    stdout.write(str(ans) + '\n')
