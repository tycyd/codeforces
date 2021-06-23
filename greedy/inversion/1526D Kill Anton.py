from sys import stdin, stdout
from itertools import permutations


dic = {'A': 0, 'N': 1, 'O': 2, 'T': 3}
dic2 = {0: 'A', 1: 'N', 2: 'O', 3: 'T'}


def kill_anton(a):
    global dic
    cnta1 = [[0 for _ in range(4)] for _ in range(4)]
    cnta2 = [0 for _ in range(4)]

    for c in a:
        for i in range(4):
            cnta1[dic[c]][i] += cnta2[i]
        cnta2[dic[c]] += 1

    rmoves = 0
    rperm = [0, 1, 2, 3]
    for perm in permutations([0, 1, 2, 3]):
        moves = 0
        for i in range(4):
            for j in range(i+1, 4):
                moves += cnta1[perm[i]][perm[j]]
        if moves > rmoves:
            rmoves = moves
            rperm = perm

    r = ''
    for p in rperm:
        r += dic2[p]*cnta2[p]
    return r


t = int(stdin.readline())
for _ in range(t):
    a = stdin.readline().strip()
    r = kill_anton(a)
    stdout.write(r + '\n')
