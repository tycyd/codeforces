from sys import stdin, stdout


def fancy_fence(N, h_a, w_a):
    MOD = 10**9 + 7
    res = 0
    st = []
    for i in range(N):
        h = h_a[i]
        w = w_a[i]

        res += calc(h) * calc(w)
        res %= MOD

        lw = 0
        prw = 0
        while st and st[-1][0] > h:
            ph, pw, plw = st.pop()
            lw += pw

            sr = 0
            sr += plw * pw
            sr %= MOD
            sr += pw * prw
            sr %= MOD
            sr += plw * prw
            sr %= MOD
            sr *= ph
            res += sr
            res %= MOD

            prw += pw

        st.append([h, w, lw])

    prw = 0
    while st:
        ph, pw, plw = st.pop()
        sr = 0
        sr += plw * pw
        sr %= MOD
        sr += pw * prw
        sr %= MOD
        sr += plw * prw
        sr %= MOD
        sr *= ph
        res += sr
        res %= MOD

        prw += pw

    return res


def calc(v):
    return (v+1)*v//2


N = int(stdin.readline())
h_a = list(map(int, stdin.readline().split()))
w_a = list(map(int, stdin.readline().split()))

ans = fancy_fence(N, h_a, w_a)
stdout.write(str(ans) + '\n')
