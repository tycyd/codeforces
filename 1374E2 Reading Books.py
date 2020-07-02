from sys import stdin, stdout

# a b ab
#
# [ab]
if __name__ == '__main__':

    def calc(abcnt, m, k, ta, tb, tab, tc):
        MAX = 2**31-1

        if len(ta) < k - abcnt or len(tb) < k - abcnt or abcnt + 2*(k-abcnt) > m:
            #return [MAX, None]
            return MAX

        rval = 0
        #res = [0] * m
        #idx = 0
        for i in range(abcnt):
            rval += tab[i][0]
            #res[idx] = tab[i][1]
            #idx += 1

        for i in range(k - abcnt):
            rval += ta[i][0]
            rval += tb[i][0]
            #res[idx] = ta[i][1]
            #idx += 1
            #res[idx] = tb[i][1]
            #idx += 1

        abi = abcnt
        ai = k - abcnt
        bi = k - abcnt
        ci = 0

        for i in range(m - abcnt - 2*(k-abcnt)):
            tmp = []
            if abi < len(tab):
                #tmp.append([tab[abi][0], 1, tab[abi][1]])
                tmp.append([tab[abi][0], 1])
            if ai < len(ta):
                #tmp.append([ta[ai][0], 2, ta[ai][1]])
                tmp.append([ta[ai][0], 2])
            if bi < len(tb):
                #tmp.append([tb[bi][0], 3, tb[bi][1]])
                tmp.append([tb[bi][0], 3])
            if ci < len(tc):
                #tmp.append([tc[ci][0], 4, tc[ci][1]])
                tmp.append([tc[ci][0], 4])

            tmp.sort(key=lambda x:x[0])
            rval += tmp[0][0]
            #res.append(tmp[0][2])
            #res[idx] = tmp[0][2]
            #idx += 1
            if tmp[0][1] == 1:
                abi += 1
            elif tmp[0][1] == 2:
                ai += 1
            elif tmp[0][1] == 3:
                bi += 1
            elif tmp[0][1] == 4:
                ci += 1

        #return [rval, res]
        return rval

    def calc2(abcnt, m, k, ta, tb, tab, tc):
        res = [0] * m

        idx = 0
        for i in range(abcnt):
            res[idx] = tab[i][1]
            idx += 1

        for i in range(k - abcnt):
            res[idx] = ta[i][1]
            idx += 1
            res[idx] = tb[i][1]
            idx += 1

        abi = abcnt
        ai = k - abcnt
        bi = k - abcnt
        ci = 0

        for i in range(m - abcnt - 2*(k-abcnt)):
            tmp = []
            if abi < len(tab):
                tmp.append([tab[abi][0], 1, tab[abi][1]])
            if ai < len(ta):
                tmp.append([ta[ai][0], 2, ta[ai][1]])
            if bi < len(tb):
                tmp.append([tb[bi][0], 3, tb[bi][1]])
            if ci < len(tc):
                tmp.append([tc[ci][0], 4, tc[ci][1]])

            tmp.sort(key=lambda x:x[0])
            res[idx] = tmp[0][2]
            idx += 1
            if tmp[0][1] == 1:
                abi += 1
            elif tmp[0][1] == 2:
                ai += 1
            elif tmp[0][1] == 3:
                bi += 1
            elif tmp[0][1] == 4:
                ci += 1

        return res


    def reading_books(n, m, k, ta, tb, tab, tc):

        if len(tab) + len(ta) < k or len(tab) + len(tb) < k:
            return [-1]

        ta.sort(key=lambda x:x[0])
        tb.sort(key=lambda x:x[0])
        tab.sort(key=lambda x:x[0])
        tc.sort(key=lambda x:x[0])

        l = 0
        r = min(len(tab), k)
        lans = 0
        rans = 0
        lmans = 0
        rmans = 0
        #lres = []
        #rres = []

        while l <= r:
            lm = l + (r - l) // 3
            rm = r - (r - l) // 3

            #lans, lres = calc(lm, m, k, ta, tb, tab, tc)
            #rans, rres = calc(rm, m, k, ta, tb, tab, tc)
            lans = calc(lm, m, k, ta, tb, tab, tc)
            rans = calc(rm, m, k, ta, tb, tab, tc)

            lmans = lm
            rmans = rm

            if lans < rans:
                r = rm - 1
            else:
                l = lm + 1

        if min(lans, rans) == 2**31-1:
            return [-1]

        if lans <= rans:
            return [lans, calc2(lmans, m, k, ta, tb, tab, tc)]
        else:
            return [rans, calc2(rmans, m, k, ta, tb, tab, tc)]

    n, m, k = map(int, stdin.readline().split())
    ta = []
    tb = []
    tab = []
    tc = []
    for i in range(n):
        t, a, b = map(int, stdin.readline().split())
        if a == 1 and b == 1:
            tab.append([t, i+1])
        elif a == 1:
            ta.append([t, i+1])
        elif b == 1:
            tb.append([t, i+1])
        else:
            tc.append([t, i+1])

    #print(ta)
    #print(tb)
    #print(tab)
    #print(tc)

    res = reading_books(n, m, k, ta, tb, tab, tc)
    stdout.write(str(res[0]) + '\n');
    if len(res) > 1:
        stdout.write(" ".join(map(str, res[1])))
