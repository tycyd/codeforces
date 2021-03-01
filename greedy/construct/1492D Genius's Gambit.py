from sys import stdin, stdout


# a => 0
# b => 1
def genius_gambit(a, b, k):
    if k != 0 and k > (a + b - 2):
        return []
    if (a == 0 or b == 1) and k != 0:
        return []

    s1 = ['1']
    s2 = ['1']
    b -= 1
    mid = []
    for _ in range(k-1):
        if b-1 > 0:
            mid.append('1')
            b -= 1
        elif a-1 > 0:
            mid.append('0')
            a -= 1

    if k > 0:
        s1 += ['1'] + mid + ['0']
        s2 += ['0'] + mid + ['1']
        a -= 1
        b -= 1

    for _ in range(a):
        s1.append('0')
        s2.append('0')

    for _ in range(b):
        s1.append('1')
        s2.append('1')

    return [''.join(s1), ''.join(s2)]


a, b, k = map(int, stdin.readline().split())
r = genius_gambit(a, b, k)
if r:
    stdout.write('YES\n')
    stdout.write(r[0] + '\n')
    stdout.write(r[1] + '\n')
else:
    stdout.write('NO\n')
