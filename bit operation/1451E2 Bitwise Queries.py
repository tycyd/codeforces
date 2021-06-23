from sys import stdin, stdout
import math

# 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6
n = int(stdin.readline())
l = int(math.log(n, 2.0))
mask = (1 << l) - 1
ca = []
dic = {}
dic2 = {}
a = b = c = -1
ma = mb = -1
for i in range(2, n+1):
    stdout.write('XOR ' + str(1) + ' ' + str(i) + '\n')
    stdout.flush()
    ca.append(int(stdin.readline()))

    if ca[-1] in dic:
        a = i
        b = dic[ca[-1]]
    elif ca[-1] == 0:
        a = 1
        b = i
    elif ca[-1] == mask:
        ma = 1
        mb = i

    dic[ca[-1]] = i
    dic2[i] = ca[-1]

# 0,1,2,3....n-1
#
if a == -1:
    d = 2
    if mb == 2:
        d = 3

    stdout.write('AND ' + str(ma) + ' ' + str(d) + '\n')
    stdout.flush()
    e = int(stdin.readline())
    stdout.write('AND ' + str(mb) + ' ' + str(d) + '\n')
    stdout.flush()
    f = int(stdin.readline())

    g = e | f
    c = dic2[d] ^ g
else:
    stdout.write('AND ' + str(a) + ' ' + str(b) + '\n')
    stdout.flush()
    c = int(stdin.readline())
    if a != 1:
        c ^= dic2[a]

r_a = [c]
for i in range(2, n+1):
    r_a.append(c ^ dic2[i])

stdout.write('! ' + ' '.join(map(str, r_a)))
stdout.flush()
