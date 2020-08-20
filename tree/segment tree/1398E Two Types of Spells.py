from sys import stdin, stdout

# 1 5
# 0 10
# 1 -5
# 0 5
# 1 11
# 0 -10
#
# (5) => 5
# (5) 10 => 5 + 2*10
# 10 => 10
# 10 5 => 15
# 10 5 (11) => 11 + 2*10 + 5 = 36
# 5 (11) => 11 + 2*5 = 21

#         1-11 (sum, cnt)
#    1-5        6-11
# 1-2  2-5   6-8    9-11
#

class seg_node:
    def __init__(self, l, r, c, v):
        self.l = l
        self.r = r
        self.c = c
        self.v = v
        self.ln = None
        self.rn = None

    def seg_update(self, i, c, v):
        if self.l == self.r:
            self.c += c
            self.v += v

            return

        m = (self.l + self.r) // 2
        if i <= m:
            if not self.ln:
                self.ln = seg_node(self.l, m, 0, 0)
            self.ln.seg_update(i, c, v)

        else:
            if not self.rn:
                self.rn = seg_node(m+1, self.r, 0, 0)
            self.rn.seg_update(i, c, v)

        self.c += c
        self.v += v

    def seg_query_r(self, cnt):

        if self.l == self.r:
            if cnt >= self.c:
                return [self.c, self.v]
            else:
                return [cnt, self.v * cnt // self.c]

        if self.c <= cnt:
            return [self.c, self.v]

        r_a = [0, 0]
        if self.rn:
            r_a = self.rn.seg_query_r(cnt)

        if r_a[0] >= cnt:
            return r_a

        l_a = [0, 0]
        if self.ln:
            l_a = self.ln.seg_query_r(cnt - r_a[0])

        res = [r_a[0] + l_a[0], r_a[1] + l_a[1]]
        return res


class seg_minnode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.c = 0
        self.v = 10**10
        self.ln = None
        self.rn = None

    def seg_update(self, i, c, v):
        if self.l == self.r:
            self.c += c
            self.v = v if self.c > 0 else 10**10
            return self.v

        m = (self.l + self.r) // 2
        lv = 10**10 if not self.ln else self.ln.v
        rv = 10**10 if not self.rn else self.rn.v
        if i <= m:
            if not self.ln:
                self.ln = seg_minnode(self.l, m)
            lv = self.ln.seg_update(i, c, v)
        else:
            if not self.rn:
                self.rn = seg_minnode(m + 1, self.r)
            rv = self.rn.seg_update(i, c, v)

        self.v = min(lv, rv)
        return self.v

    def seg_query(self):
        return self.v


def two_types_of_spells(n, s, tpd_a):
    # 5, 10, 15 => 0, 1, 2
    dic = {}
    ls = list(s)
    ls.sort()
    for i in range(len(ls)):
        dic[ls[i]] = i

    seg_root = seg_node(0, len(ls)-1, 0, 0)
    seg_minroot = seg_minnode(0, len(ls)-1)

    rsum = 0
    lcnt = 0
    ans = []
    for tpd in tpd_a:

        i = dic[abs(tpd[1])]
        c = 1 if tpd[1] > 0 else -1
        v = tpd[1]

        rsum += tpd[1]

        if tpd[0] == 1:
            if tpd[1] > 0:
                lcnt += 1
            else:
                lcnt -= 1
            i = dic[abs(tpd[1])]
            c = 1 if tpd[1] > 0 else -1
            seg_minroot.seg_update(i, c, abs(v))

        seg_root.seg_update(i, c, v)

        if lcnt < 1:
            ans.append(rsum)
            continue

        # remove minimum lighting
        minV = seg_minroot.seg_query()

        seg_root.seg_update(dic[minV], -1, -minV)

        cnt, v = seg_root.seg_query_r(lcnt)

        # add minimum lighting
        seg_root.seg_update(dic[minV], 1, minV)

        ans.append(rsum + v)

    return ans

n = int(stdin.readline())
tpd_a = []
s = set()
for _ in range(n):
    tp, d = map(int, stdin.readline().split())
    tpd_a.append([tp, d])
    s.add(abs(d))
ans = two_types_of_spells(n, s, tpd_a)
for a in ans:
    stdout.write(str(a) + '\n')
