from sys import stdin, stdout


# x: 01
# y: 10
def grime_zoo(s, x, y):
    if x > y:
        tmp = x
        x = y
        y = tmp

        c_a = []
        for c in s:
            if c == '0':
                c_a.append('1')
            elif c == '1':
                c_a.append('0')
            else:
                c_a.append(c)
        s = ''.join(c_a)

    # right to left ?0
    rcnt_a = [0]
    zeroCnt = 0
    needCnt = 0
    oneZeroSub = 0
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        if c == '0':
            zeroCnt += 1
        elif c == '1':
            oneZeroSub += zeroCnt
        elif c == '?':
            needCnt += 1
            rcnt_a.append(rcnt_a[-1] + zeroCnt)

    # left to right 1?
    lcnt_a = [0]
    oneCnt = 0
    for i in range(0, len(s)):
        c = s[i]
        if c == '1':
            oneCnt += 1
        elif c == '?':
            lcnt_a.append(lcnt_a[-1] + oneCnt)

    if needCnt == 0:
        return zeroCnt*oneCnt*x + oneZeroSub*(y-x)

    r = 10**20
    for zeroSup in range(0, needCnt+1):
        oneSup = needCnt - zeroSup

        lr = (zeroCnt + zeroSup)*(oneCnt + oneSup)*x + (oneZeroSub + lcnt_a[zeroSup] + rcnt_a[oneSup])*(y-x)
        r = min(r, lr)

    return r


s = stdin.readline().strip()
x, y = map(int, stdin.readline().split())
r = grime_zoo(s, x, y)
stdout.write(str(r))
