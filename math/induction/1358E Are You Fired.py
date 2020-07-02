from sys import stdin, stdout

# 3
# 2 -1
# 2
# 2 -1 2 2

# 6
# -2 -2 6
# -1
# -2 -2 6 -1 -1 -1

# 3 1 -5 6

# if k is result, k*2 is also result
# upper bound  n/2 <= k*2^t <= n
# then k >= n/2
# p[k] = a[0] + a[1] + a[2] + ... + a[k-1] => s[0]
# then p[k] + x - p[1] > 0                 => s[1]
#      p[k] + 2x - p[2] > 0                => s[2]
#      p[k] + 3x - p[3] > 0                => s[3]
#      p[k] + i*x - p[i] > 0  ,      0 <= i <= n-k
#      p[i] - i*x < p[k]
#  max( p[i] - i*x ) < p[k]

# 1 2 3 4 5
# 1 2
#   2 3
#     3 4
#       4 5
# 1 2 3 4
#   2 3 4 5
if __name__ == '__main__':
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    x = int(stdin.readline())

    def are_you_fired(n, a, x):
        p = [0 for i in range(n+1)]
        for i in range(n):
            if i >= len(a):
                p[i+1] = p[i] + x
            else:
                p[i+1] = p[i] + a[i]

        mx = -2**31
        idx = 0
        for k in range(n, n//2, -1):
            mx = max(mx, p[idx] - idx*x)
            if p[k] > mx:
                return k
            idx += 1

        return -1

    print(str(are_you_fired(n, a, x)))


