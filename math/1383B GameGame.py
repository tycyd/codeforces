from sys import stdin, stdout

#
# 1 1
# 1
def gamegame(n, a):
    bc = [[0]*30, [0]*30]

    for v in a:
        for i in range(30):
            bc[(v >> i) & 1][i] += 1

    for i in range(29, -1, -1):
        if bc[1][i] % 2 == 1:
            if bc[1][i] % 4 == 3 and bc[0][i] % 2 == 0:
                return "LOSE"
            else:
                return "WIN"

    return "DRAW"


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    stdout.write(gamegame(n, a) + '\n')

