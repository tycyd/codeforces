from sys import stdin, stdout

# 0   0   0   0
# 2^3 2^4 2^5 2^6
# 0   0   0   0
# 2^5 2^6 2^7 2^8
#

def construct(n):
    p_a = [[0 for _ in range(n)] for _ in range(n)]
    v = 1 << 3

    for i in range(1, n, 2):
        for j in range(n):
            p_a[i][j] = v
            v = v << 1
        v = v >> (n-2)
    return p_a


def omkar_and_duck(n, p_a, k):

    c = 0
    b = 1 << 3
    for i in range(n//2):
        while k & b == 0:
            stdout.write(str(2*i + 1) + ' ' + str(c + 1) + '\n')

            b = b << 1
            c += 1

        stdout.write(str(2 * i + 1) + ' ' + str(c + 1) + '\n')
        stdout.write(str(2 * i + 2) + ' ' + str(c + 1) + '\n')

        while k & (b << 1) != 0:
            c += 1
            stdout.write(str(2 * i + 2) + ' ' + str(c + 1) + '\n')
            b = b << 1

        b = b << 2

    if n % 2 == 1:
        for i in range(c, n):
            stdout.write(str(n) + ' ' + str(i + 1) + '\n')

    return


n = int(stdin.readline())
p_a = construct(n)
for p in p_a:
    stdout.write(' '.join(map(str, p)) + '\n')
stdout.flush()

q = int(stdin.readline())
for _ in range(q):
    k = int(stdin.readline())
    omkar_and_duck(n, p_a, k)
    stdout.flush()
