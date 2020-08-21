from sys import stdin, stdout


#   1 1 1 =>    1 0 0, 0 1 1
# 1 1 0 0 =>           1 0 0
#
def boboniu_and_bit_operations(n, m, a_a, b_a):

    for k in range(513):
        cnt = 0
        for a in a_a:
            for b in b_a:
                if ((a & b) | k) == k:
                    cnt += 1
                    break
        if cnt == n:
            return k

    return -1


n, m = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

stdout.write(str(boboniu_and_bit_operations(n, m, a_a, b_a)) + '\n')
