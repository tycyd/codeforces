from sys import stdin, stdout


# 0 1 0 1
# 0 0 1 1

# 0 1 0 0 1 1 0 1
# 0 0 1 0 1 0 1 1
# 0 0 0 1 0 1 1 1
def five_O_five(n, m, a_2d):
    if n > 3:
        return -1
    if n == 1:
        return 0

    MAX = 10**9
    if n == 2:

        preMask = [0, 0, 0, 0]
        for i in range(m):
            curMask = [MAX, MAX, MAX, MAX]
            for j in range(4):
                val = ord(a_2d[0][i]) - ord('0') + 2*(ord(a_2d[1][i]) - ord('0'))
                cnt = 0
                for k in range(2):
                    if ((j >> k) & 1) != ((val >> k) & 1):
                        cnt += 1

                for k in range(4):
                    bits = (j & 1) + ((j >> 1) & 1) + (k & 1) + ((k >> 1) & 1)
                    if bits % 2 == 1:
                        curMask[j] = min(curMask[j], preMask[k] + cnt)

            preMask = curMask

        return min(preMask)

    else:
        preMask = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(m):
            curMask = [MAX, MAX, MAX, MAX, MAX, MAX, MAX, MAX]
            for j in range(8):
                val = ord(a_2d[0][i]) - ord('0') + 2 * (ord(a_2d[1][i]) - ord('0')) + 4 * (ord(a_2d[2][i]) - ord('0'))
                cnt = 0
                for k in range(3):
                    if ((j >> k) & 1) != ((val >> k) & 1):
                        cnt += 1

                for k in range(8):
                    bits_up = (j & 1) + ((j >> 1) & 1) + (k & 1) + ((k >> 1) & 1)
                    bits_down = ((j >> 1) & 1) + ((j >> 2) & 1) + ((k >> 1) & 1) + ((k >> 2) & 1)
                    if bits_up % 2 == 1 and bits_down % 2 == 1:
                        curMask[j] = min(curMask[j], preMask[k] + cnt)

            #print(curMask)
            preMask = curMask

        return min(preMask)


n, m = map(int, stdin.readline().split())
a_2d = []
for _ in range(n):
    a_2d.append(stdin.readline().strip())
stdout.write(str(five_O_five(n, m, a_2d)) + '\n')
