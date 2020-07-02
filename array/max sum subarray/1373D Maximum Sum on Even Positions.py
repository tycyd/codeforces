from sys import stdin, stdout

# 8
# 1 7 3 4 7 6 2 9
# X   X   X   X
# 9 2 6 7 4 3 7 1
# 26
#
# 10
# 7 8 4 5 7 6 8 9 7 3
# X   X   X   X   X         =>33
#
# fact 1: odd subarray doesn't affect result
# fact 2: even subarray switch all positions.

if __name__ == '__main__':

    def maxium_sum_on_even_positions(n, a):

        esum = 0

        res1 = 0
        dif1 = 0

        res2 = 0
        dif2 = 0
        for i in range(0, n, 2):
            esum += a[i]

            if i+1 < n:
                dif1 = max(0, dif1 + a[i+1] - a[i])
                res1 = max(res1, dif1)
            if i > 0:
                dif2 = max(0, dif2 + a[i-1] - a[i])
                res2 = max(res2, dif2)

        return max(esum, esum + max(res1, res2))

    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        stdout.write(str(maxium_sum_on_even_positions(n, a)) + '\n')
