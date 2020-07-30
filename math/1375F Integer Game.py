from sys import stdin, stdout

# 5 2 6
# 5 2 6      +5
# (10) 2 6
# 5 (7) 6
# 5 2 (11)
#
# 5 2 (8) +2
#
# 5 (4) 6  +2
# 5 4 (7) +1
# (10) 4 7 +5  or 5 (9) 7
#
# (7) 2 6 +2
# 7 (8) 6 +6 or 7 2 (12)
#
# 2, 5, 6
# 2, 5, (8) +2
# proof
# A, B, C,
# 2  5  100
# C > B > A and 2B-A-C < 0
#

# C > B > A and 2B-A-C >= 0
# cmd1 : (2B-A-C) count
# 1. A, B, 2B-A,
#
# (4), 5, 6
# 2. A+2B-A-C, B, C
#    2B-C, B, C    => B-(2B- C) = C-B
# cmd2: C-B
# 4, 5, (7)
#    2B-C, B, 2C-B
# cmd3: (2C-B - (2B-C)) + (2C-B - B)
#       (3C - 3B) + (2C-2B)
#       = 5C-5B
#  op1: (9), 5, 7
#       2B-C+5C-5B, B, 2C-B
#       4C-3B, B, 2C-B    => res
#
# 2 (7) 6
# 3. A, B+2B-A-C, C
#    A, 3B-A-C, C
#
# if 3B-A-C > C:
# cmd2: 3B-A-C - A + 3B-A-C - C
#       3B-2A-C + 3B-A-2C
#       6B-3A-3C
#
#  (8) 7 6  +6
#  opt1: A+6B-3A-3C, 3B-A-C, C
#        6B-2A-3C, 3B-A-C, C => dif = 3B-A-2C res
#
#  2 7 (12)  +6
#  opt1: A, 3B-A-C, C + 6B-3A-3C
#        A, 3B-A-C, 6B-3A-2C => dif = 3B-2A-C res
#
# if 3B-A-C < C:
#  2, (6), 7
#  A < B < C
#
#
# 2, 5, 7
# +1
# c1: 2, 5, (8)
# c2: 2, (6), 7
#

if __name__ == '__main__':
    # a < b < c
    def integer_game(lst):
        sl = sorted(lst)
        a = sl[0]
        b = sl[1]
        c = sl[2]

        stdout.write("First\n")

        while True:

            d = 2*c-a-b

            stdout.write(str(d) + '\n')
            stdout.flush()

            p = int(stdin.readline())
            lst[p-1] += d

            sl = sorted(lst)
            a = sl[0]
            b = sl[1]
            c = sl[2]

            if c - b == b - a:
                break

        stdout.write(str(c-b) + '\n')
        stdout.flush()

        stdin.readline()

    lst = list(map(int, stdin.readline().split()))
    integer_game(lst)
