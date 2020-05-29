from sys import stdin, stdout

#
# 3 2
# 1 3 1
# 1 1 2 3 1
# 1 2 3 | 4 1 2 3 4
# 1 2 3 4 1 | 2 3 4
def the_best_vacation(n, x, d):

    i = j = days = hugs = res = 0

    while j < 2*n:

        ci = i%n
        pi = (i-1+n)%n
        pj = j%n

        if d[pj] >= x:
            res = max(res, gethugs(d[pj] - x + 1, d[pj]))
            j += 1
            i = j
            continue

        r = x - days

        if days + d[pj] > x:

            if d[pi] > r:
                res = max(res, hugs + gethugs(d[pi] - r + 1, d[pi]))
            else:
                res = max(res, hugs + gethugs(1, r))

            days -= d[ci]
            hugs -= gethugs(1, d[ci])
            i += 1
        else:
            if days + d[pi] > x:
                res = max(res, hugs + gethugs(d[pi] - r + 1, d[pi]))

            days += d[pj]
            hugs += gethugs(1, d[pj])
            j += 1

    return res


# 1 2 3 => 6
def gethugs(a, b):
    return (a+b)*(b-a+1)//2


if __name__ == '__main__':
    nx = list(map(int, stdin.readline().split()))
    d = list(map(int, stdin.readline().split()))

    stdout.write(str(the_best_vacation(nx[0], nx[1], d)) + '\n')
