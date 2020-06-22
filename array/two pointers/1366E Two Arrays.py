from sys import stdin, stdout


#  6 3
# 12 10 | 20 20 25 30
#  0  4  3  2  1  0
#  0  1  0  2  0  0
#
# 10 12 [10] 50 30 [20] 40 [30]
# 10 20 30
def two_arrasy(n, m, a, b):

    r = n-1
    res = 1
    for i in range(m-1, -1, -1):
        #print(b[i])
        while r >= 0 and a[r] > b[i]:
            r -= 1

        if r < 0 or b[i] != a[r]:
            return 0

        l = r
        while l >= 0 and a[l] >= b[i]:
            l -= 1

        if l < 0 and i != 0:
            return 0

        if i == 0:
            if l >= 0 and a[l] < b[i]:
                return 0
            else:
                break

        res *= (r-l)
        res %= 998244353
        r = l

    return res


if __name__ == '__main__':
    (n, m) = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    res = two_arrasy(n, m, a, b)

    stdout.write(str(res) + '\n')