from sys import stdin, stdout

# 30, 10, 20
# (30x + 10y) / (x + y) = 20
# x = y || x = y+1
# 40x / 2x = 20

# (30x + 10x - 10) / (2x - 1) = 20
# (10x + 30x - 30) / (2x - 1) = 20

# (40x - 10) / (2x - 1)
# 40x/(2x-1) - 10/(2x-1)
# 40x/(2x-1) - 30/(2x-1)
# (30x + 10(x - 1)) / (2x - 1)


def mixing_water(h, c, t):

    r1 = 2
    v1 = (h + c)//2

    if h >= c:
        rv2 = bs1(h, c, t)
    else:
        rv2 = bs2(h, c, t)

    r2 = rv2[0]
    v2 = rv2[1]

    dif = abs(t-v1) - abs(t-v2)

    if dif == 0:
        return min(r1, r2)
    elif dif > 0:
        return r2
    else:
        return r1

# h >= c
def bs1(h, c, t):

    l = 1
    r = 2 ** 31 - 1

    while l < r:
        m = (l + r) // 2
        v1 = ((h + c)*m - c) / (2*m - 1)
        #print(v1)
        if v1 > t:
            l = m + 1
        else:
            r = m

    #v1 = ((h + c) * r - c) / (2 * r - 1)
    #v2 = ((h + c) * (r-1) - c) / (2 * (r-1) - 1)
    v1 = ((h + c) * r - c)
    v2 = ((h + c) * (r-1) - c)
    t1 = (2 * r - 1)
    t2 = (2 * (r-1) - 1)

    #if r > 1 and abs(t - v2) <= abs(v1 - t):
    if r > 1 and abs(t*t1*t2 - v2*t1) <= abs(v1*t2 - t*t1*t2):
        #return [(r-1)*2-1, v2]
        return [(r - 1) * 2 - 1, v2/t2]
    else:
        #return [r*2-1, v1]
        return [r * 2 - 1, v1/t1]

# h < c
def bs2(h, c, t):
    l = 1
    r = 2**31-1

    while l < r:
        m = (l + r) // 2
        v1 = ((h + c)*m - c) / (2*m - 1)

        if v1 < t:
            l = m + 1
        else:
            r = m

    #v1 = ((h + c) * r - c) / (2 * r - 1)
    #v2 = ((h + c)*(r-1) - c) / (2*(r-1) - 1)
    v1 = ((h + c) * r - c)
    v2 = ((h + c) * (r - 1) - c)
    t1 = (2 * r - 1)
    t2 = (2 * (r - 1) - 1)

    #if r > 1 and abs(v2 - t) <= abs(t - v1):
    if r > 1 and abs(v2*t1 - t*t1*t2) <= abs(t*t1*t2 - v1*t2):
        #return [(r-1)*2-1, v2]
        return [(r - 1) * 2 - 1, v2/t2]
    else:
        #return [r*2, v1]
        return [r * 2, v1/t1]


if __name__ == '__main__':
    T = int(stdin.readline())

    for i in range(T):
        hct = list(map(int, stdin.readline().split()))

        stdout.write(str(mixing_water(hct[0], hct[1], hct[2])) + '\n')