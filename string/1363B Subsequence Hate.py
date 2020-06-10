from sys import stdin, stdout


#010, 101
#01111110, 100000001
#0001111, 111000
#1011111
#01110011|0111011
def subsequence_hate(s):
    n = len(s)
    if n == 1:
        return 0

    la = get_la(s)
    ra = get_ra(s)

    #print(la)
    #print(ra)

    res = 2**31-1
    for i in range(1, n):

        # left 1, right 0
        # left 0, right 1
        # all 0
        # all 1
        res = min(res, la[i-1][0] + ra[i][1], la[i-1][1] + ra[i][0]
                  , la[i-1][0] + ra[i][0], la[i-1][1] + ra[i][1])

    return res


def get_la(s):
    la = [[0, 0] for i in range(len(s))]

    cnt0 = 0
    cnt1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        la[i][0] = cnt0
        la[i][1] = cnt1
    return la


def get_ra(s):
    ra = [[0, 0] for i in range(len(s))]

    cnt0 = 0
    cnt1 = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        ra[i][0] = cnt0
        ra[i][1] = cnt1
    return ra


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        s = stdin.readline().strip()
        stdout.write(str(subsequence_hate(s)) + '\n')