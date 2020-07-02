from sys import stdin, stdout

# 3 1 100 100
# 1 3 8
# Sum( max(h) - hi ) * A = CountA
# Sum( hi - min(h)) * D  = CountD
# 1 9
# 4R, 8A, 8D
# 3R + 2A
# 2R + 4A
#  R + 6A
#      8A
#
# 5 1 2 4
# 5 5 3 6 5 => 24
# 4R + 4D
# 5R + 1A
if __name__ == '__main__':
    N, A, R, M = map(int, stdin.readline().split())
    ha = list(map(int, stdin.readline().split()))

    def calc(v, ha, A, R, M):
        a = 0
        r = 0

        for h in ha:
            a += max(v-h, 0)
            r += max(h-v, 0)
        m = min(a, r)

        return min(a*A + r*R, m*M + (a-m)*A + (r-m)*R)


    def restorer_distance(N, A, R, M, ha):

        l = min(ha)
        r = max(ha)
        lans = 0
        rans = 0

        while l < r:
            lm = l + (r - l)//3
            rm = r - (r - l)//3
            lans = calc(lm, ha, A, R, M)
            rans = calc(rm, ha, A, R, M)

            # 求凹函数的极小值
            if lans <= rans:
                r = rm - 1
            else:
                l = lm + 1

            # 求凸函数的极大值
            # if lans >= rans:
            #    l = lm + 1;
            # else:
            #    r = rm - 1;

        return min(lans, rans)

    stdout.write(str(restorer_distance(N, A, R, M, ha)) + '\n')
