from sys import stdin, stdout

# RL, RRL, RLL, RRLL
#
#
#
def shift(c_a):
    c = c_a[0]
    for i in range(n-1):
        c_a[i] = c_a[i+1]
    c_a[n-1] = c


def omkar_and_bed_wars(n, s):

    c_a = list(s)

    r1 = cal_dp(n, c_a)
    shift(c_a)
    r2 = cal_dp(n, c_a)
    shift(c_a)
    r3 = cal_dp(n, c_a)
    shift(c_a)
    r4 = cal_dp(n, c_a)

    return min(r1, r2, r3, r4)


def cal_dp(n, c_a):
    dp = [10**9] * n
    for i in range(1, n):
        # RL
        rl = get_cnt(i-1, c_a, 'RL')
        if i > 1:
            rl += dp[i-2]

        rrl = 10 ** 9
        rll = 10 ** 9
        if i > 1:
            rrl = get_cnt(i - 2, c_a, 'RRL')
            rll = get_cnt(i - 2, c_a, 'RLL')
            if i > 2:
                rrl += dp[i - 3]
                rll += dp[i - 3]

        rrll = 10 ** 9
        if i > 2:
            rrll = get_cnt(i - 3, c_a, 'RRLL')
            if i > 3:
                rrll += dp[i - 4]

        dp[i] = min(rl, rrl, rll, rrll)

    #print(''.join(c_a))
    #print(dp)
    return dp[n-1]


def get_cnt(idx, c_a, s):
    cnt = 0
    for i in range(len(s)):
        if c_a[idx+i] != s[i]:
            cnt += 1
    return cnt


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    stdout.write(str(omkar_and_bed_wars(n, s)) + '\n')
