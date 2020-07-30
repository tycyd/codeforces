from sys import stdin, stdout

# 2 3
# 14
# 2 4
# 2 1
# 1 0

# 14
# 2 4
# => 14,
# 2 1
# => 11
# 1 0
# => 0 1
if __name__ == '__main__':


    n, m = map(int, stdin.readline().split())
    c = stdin.readline().strip()
    for i in range(m):
        x, d = map(int, stdin.readline().split())
