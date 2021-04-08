from sys import stdin, stdout


def triangular_paths(n, r_a, c_a):
    rc_a = [[1, 1]]
    for i in range(n):
        rc_a.append([r_a[i], c_a[i]])
    rc_a.sort(key=lambda x: x[0])

    res = 0
    for i in range(1, n+1):
        r1 = rc_a[i-1][0]
        c1 = rc_a[i-1][1]
        r2 = rc_a[i][0]
        c2 = rc_a[i][1]

        if (r1+c1)%2 == 1 and (r2+c2)%2 == 1:
            res += cal_1(r1, c1, r2, c2)
        elif (r1+c1)%2 == 1 and (r2+c2)%2 == 0:
            res += cal_2(r1, c1, r2, c2)
        elif (r1+c1)%2 == 0 and (r2+c2)%2 == 1:
            res += cal_3(r1, c1, r2, c2)
        elif (r1+c1)%2 == 0 and (r2+c2)%2 == 0:
            res += cal_4(r1, c1, r2, c2)

        # print(str(r1) + ' ' + str(c1) + ' , ' + str(r2) + ' ' + str(c2))
        # print(res)
        # print('-------------')
    return res


# odd, odd
def cal_1(r1, c1, r2, c2):
    return (r2 - (c2 - c1) - r1) // 2


# odd, even
def cal_2(r1, c1, r2, c2):
    return cal_1(r1, c1, r2 - 1, c2) + 1


# even, odd
def cal_3(r1, c1, r2, c2):
    return cal_1(r1 + 1, c1, r2, c2)


# even, even
def cal_4(r1, c1, r2, c2):
    if r1 - c1 == r2 - c2:
        return c2 - c1
    else:
        return cal_2(r1 + 1, c1, r2, c2)


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    r_a = list(map(int, stdin.readline().split()))
    c_a = list(map(int, stdin.readline().split()))
    r = triangular_paths(n, r_a, c_a)
    stdout.write(str(r) + '\n')
