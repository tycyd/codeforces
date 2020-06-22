from sys import stdin, stdout

# 3
#    1       3       5
# 0001    0011    0101
#    1    0001    0111
#  3   011
#  9  1001
#  5  0101
# 25 11001
# 5^2 + 5^2  =  4^2 + 6^2
# (3-2)^2 + (5+2)^2
# 3^2-2*2*3+2^2  +  5^2 + 2*2*5 + 2^2
#  1  2   4
# 01 10 100
def and_or_and_square_sum(n, a):

    bcnt = [0 for i in range(32)]

    for v in a:
        for i in range(32):
            if v & (1 << i) > 0:
                bcnt[i] += 1

    res = 0
    cur = -1

    while cur != 0:
        cur = 0
        for i in range(32):
            if bcnt[i] > 0:
                cur += (1 << i)
                bcnt[i] -= 1
        res += (cur * cur)

    return res


if __name__ == '__main__':
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    print(and_or_and_square_sum(n, a))
