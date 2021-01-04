from sys import stdin


def water_level(k, l, r, t, x, y):
    if k < l:
        return 'No'

    seen = [False] * x
    while t > 0:
        d = (k - l) // x
        t -= d
        if t <= 0:
            return 'Yes'
        m = (k - l) % x
        if seen[m]:
            return 'Yes'
        seen[m] = True

        if l + m + y > r:
            return 'No'
        k = l + m + y - x
        t -= 1

    return 'Yes'


k, l, r, t, x, y = map(int, stdin.readline().split())
if y > x:
    print(water_level(k, l, r, t, x, y))
else:
    if k + y <= r and (k + (y - x) * t) >= l:
        print('Yes')
    elif k <= r and (k - x + (y - x) * (t - 1)) >= l:
        print('Yes')
    else:
        print('No')
