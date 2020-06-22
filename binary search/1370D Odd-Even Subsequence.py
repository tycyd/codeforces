from sys import stdin, stdout

# min( max(s1, s3..), max(s2, s4..) )
# 6 4
# 5 3 50 2 4 5
# 3, 50, 2, 4
# min( max(3, 2), max(50, 4) )


if __name__ == '__main__':

    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))


    def odd_even_subsequence(n, k, a):

        res1 = 10000000000
        res2 = 10000000000

        if k % 2 == 0:
            v = a.pop(-1)
            res1 = subsequence(n, k//2 + k%2, a)
            a.append(v)
        else:
            res1 = subsequence(n, k//2 + k%2, a)

        if k % 2 == 0:
            a.pop(0)
            res2 = subsequence(n, k//2, a)
        else:
            a.pop(0)
            a.pop(-1)
            res2 = subsequence(n, k // 2, a)

        return min(res1, res2)


    def subsequence(n, k, a):

        l = 0
        h = 10**9

        while l < h:
            m = (l + h)//2

            if calc(a, m, k):
                h = m
            else:
                l = m + 1

        return h

    # p2 p1 cr
    #  1  2  3
    #
    def calc(a, v, k):

        pre1 = 0
        pre2 = 0
        for i in range(len(a)):
            cur = pre1
            if a[i] <= v:
                cur = max(1 + pre2, pre1)
            pre2 = pre1
            pre1 = cur

        return pre1 >= k


    print(str(odd_even_subsequence(n, k, a)))
