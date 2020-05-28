from sys import stdin, stdout

# https://www.mathsisfun.com/algebra/sequences-finding-rule.html
# 1 2 4
# 3 5 8
# 6 9 13
#
# 1+2+4+8+13 = 28
# 1+3+6+9+13 = 32
#
# 1 + 2 + 4 + 8 + 13
# 1 + 3 + 6 + 9 + 13
# 1 + 2 + 4 + 7
# => 1 = 1+0
# => 2 = 1+1
# => 4 = 2+2
# => 7 = 4+3
# =>11 = 7+4
# 1  2  4  7
# 3  5  8 12
# 6  9 13 18
# m = 3, n = 4
# 3 + 4 - 3 = 4
# min(m,n) - 1 = 2
# (1 + 2) * 2

# 1 + 3 + 6 + 10 => 1 + 2 + 3 + 4

#1
#1 1 3 6


def printtable(m, n):

    cell = [[0 for j in range(n)] for i in range(m)]
    cell[0][0] = 1

    for i in range(m):
        for j in range(n):
            if j > 0:
                cell[i][j] = cell[i][j-1] + i + j
            elif i > 0:
                cell[i][j] = cell[i-1][j] + i + 1

            stdout.write(str(cell[i][j]))
            stdout.write(" ")

        print(" ")


def celex_update(x1, y1, x2, y2):
    return abs(x1 - x2) * abs(y1 - y2) + 1


def celex_update2(x1, y1, x2, y2):

    m = abs(x1 - x2) + 1
    n = abs(y1 - y2) + 1

    if m == 1 or n == 1:
        return 1

    r = m + n - 3
    a = min(m, n)-1
    res = (a*(a+1))//2

    if m == n:
        res += ((a-1)*a)//2
    else:
        res *= 2
        r -= 2*a
        res += r*a

    return res + 1


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):

        xy = list(map(int, stdin.readline().split()))

        stdout.write(str(celex_update(xy[0], xy[1], xy[2], xy[3])) + '\n')
