from sys import stdin, stdout

# 6
# 010000
# 000001
#  1   0
#
# 101000
# 101  1
# 010110
#
# 1010100
# 0100011
# 101 100
#
# 10
# 1111100000
# 0000011111
# 1111100000
#
# if count(s0) == count(t0), count(s1) == count(t1)
#   res <= count(dif bit) // 2
if __name__ == '__main__':
    n = int(stdin.readline())
    s = stdin.readline().strip()
    t = stdin.readline().strip()


    def binary_subsequence_rotation(n, s, t):
        scnt0 = 0
        scnt1 = 0
        tcnt0 = 0
        tcnt1 = 0

        for i in range(n):
            if s[i] == '0':
                scnt0 += 1
            else:
                scnt1 += 1

            if t[i] == '0':
                tcnt0 += 1
            else:
                tcnt1 += 1

        if scnt0 != tcnt0 or scnt1 != tcnt1:
            return -1

        tl0 = 0
        tl1 = 0
        for i in range(n):
            if s[i] == t[i]:
                continue

            if s[i] == '1':
                if tl0 == 0:
                    tl1 += 1
                else:
                    tl0 -= 1
                    tl1 += 1
            else:
                if tl1 == 0:
                    tl0 += 1
                else:
                    tl1 -= 1
                    tl0 += 1

        return tl0 + tl1


    print(str(binary_subsequence_rotation(n, s, t)))
