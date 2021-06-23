from sys import stdin, stdout

# 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6
n = int(stdin.readline())
mask = (1 << n) - 1
ca = []
dic = {}
a, b = -1
ma, mb = -1
for i in range(2, n+1):
    stdout.write('XOR ' + str(1) + ' ' + str(i+1))
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
        ma = i

    dic[ca[-1]] = i

# 0,1,2,3....n-1
#
if a == -1:








