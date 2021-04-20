from sys import stdin, stdout


def powerful_ksenia(n, a_a):
    xor = 0
    for a in a_a:
        xor ^= a
    if n % 2 == 0 and xor != 0:
        return ['NO']
    else:
        r_a = ['YES', str(((n-1) // 2) * 2)]
        for i in range((n-1) // 2):
            r_a.append(str(1) + ' ' + str(i*2+2) + ' ' + str(i*2+3))
        for i in range((n-1) // 2):
            r_a.append(str(1) + ' ' + str(i*2+2) + ' ' + str(i*2+3))
        return r_a


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
r_a = powerful_ksenia(n, a_a)
for r in r_a:
    stdout.write(r + '\n')
