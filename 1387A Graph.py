from sys import stdin, stdout

#
# 1 ---- 2
#   \    |
#     \  |
#        3---4
#
# 0.5 0.5 1.5 -0.5
# b: 0.5 0.5 0.5 0.5
# r: 1   1   1
N, M = map(int, stdin.readline())
for _ in range(M):
    a, b, c = map(int, stdin.readline())
