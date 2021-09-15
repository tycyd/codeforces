from sys import stdin, stdout
import math

# 2^2 + 2^1 + 2^0
#  1 4 8 = 8 X
#  (1  2 2 2 2   3 3 3) 3 3 3 3 3
#  1       2          3       4
#  (12)    12       (34)      34
#  (1234)  (1234)   1234    1234
#  2^13 = 8192
#  8192 / 2 = 4096 * 13 = 53248
#  3 | 4    4 | 3


def get_pairs(i, j, res):
    if i == j:
        return

    m = (i+j)//2
    # 1 2 | 3 4
    get_pairs(i, m, res)
    get_pairs(m+1, j, res)

    for k in range((j-i) // 2 + 1):
        res.append([i+k, m+1+k])


n = int(stdin.readline())
res = []
f = int(math.floor(math.log(n, 2)))
v = int(math.pow(2, f))
get_pairs(1, v, res)
if v < n-1:
    get_pairs(n-v+1, n, res)

stdout.write(str(len(res)) + '\n')
for r in res:
    stdout.write(str(r[0]) + ' ' + str(r[1]) + '\n')
