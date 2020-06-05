from sys import stdin, stdout

# n k
# 4 2
# 1 2 1 2
#
# 4 3
# 1 2 2 1
# 2 4
#
#  6 6
#  5 2  6 1 3 4
#  9 5  7
# 10 9 12
#  5 3  2
#  8 6
#  6  1   1   7  6 3 4 6
# 12  5   4  13
# 13 11  10  14
#  7  2   2   7
# 7 7 => 8 - 14
# 1 1 => 2 - 8

# sum accumulation O(N)
def constant_palindrome_sum(n, k, a):

    sasum = [0 for i in range(2*k+2)]
    acsum = [0 for i in range(2*k+2)]

    for i in range(n//2):
        lv = min(a[i], a[n-i-1]) + 1
        hv = max(a[i], a[n - i - 1]) + k
        acsum[lv] += 1
        acsum[hv+1] -= 1
        sasum[a[i] + a[n - i - 1]] += 1

    res = 2**31 - 1
    cnt = 0
    for i in range(2, 2*k+1):
        cnt += acsum[i]
        res = min(res, (cnt - sasum[i]) + (n//2 - cnt)*2)

    #print(sasum)
    #print(acsum)

    return res


# 2    10
# 2       11
#     7      13
#     7         14
def bs_rb(v, ar):
    l = 0
    h = len(ar)-1

    while l < h:
        m = (l + h)//2
        if v <= ar[m][1]:
            h = m
        else:
            l = m+1

    return h


def bs_lb(v, ar):
    l = 0
    h = len(ar) - 1

    while l < h:
        m = (l + h + 1) // 2
        if v >= ar[m][0]:
            l = m
        else:
            h = m - 1

    return l


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        nk = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))

        stdout.write(str(constant_palindrome_sum(nk[0], nk[1], a)) + '\n')