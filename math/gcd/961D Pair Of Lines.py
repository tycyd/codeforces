from sys import stdin, stdout


def pair_of_lines(n, xy_a):
    if len(xy_a) <= 3:
        return 'YES'

    p1, p2, p3 = xy_a[0], xy_a[1], xy_a[2]
    if judge(p1, kstr(p1, p2),xy_a):
        return 'YES'
    if judge(p1, kstr(p1, p3),xy_a):
        return 'YES'
    if judge(p2, kstr(p2, p3), xy_a):
        return 'YES'
    return 'NO'


def kstr(xy1, xy2):
    cx, cy = xy1[0], xy1[1]
    x, y = xy2[0], xy2[1]
    dx = x - cx
    dy = y - cy
    k = ''
    if dx == 0:
        k = str(x) + '/y'
    elif dy == 0:
        k = 'x/' + str(y)
    else:
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        k = str(dx) + '/' + str(dy)
    return k


def judge(p, k, xy_a):

    rl = []
    for xy in xy_a:
        if p[0] == xy[0] and p[1] == xy[1]:
            continue
        if kstr(p, xy) != k:
            rl.append(xy)

    if len(rl) > 2:
        ck = kstr(rl[0], rl[1])
        for i in range(2, len(rl)):
            if ck != kstr(rl[0], rl[i]):
                return False

    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


try:
    n = int(stdin.readline())
    xy_a = []
    for _ in range(n):
        xy_a.append(list(map(int, stdin.readline().split())))
    res = pair_of_lines(n, xy_a)
    stdout.write(res)
except Exception as e:
  print(e)
