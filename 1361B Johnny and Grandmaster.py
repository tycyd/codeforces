from sys import stdin, stdout

# 5 2
# 2 3 3 4 4
# 3 3 4 4
# 2 2 3 3 3 4 4
# =>
# 1 1 3 3 3 4 4
# =>      2 3 4 5
# =>
# 1  50 50 100
# k - (k-1) = k-1
# k - (k-2) = (k-1) + (k-1) - (k-2) = (k-1) + (k-2)
#
# 2 (2 2) (2 2) (3 3) (3 3)
# 2 (2 2) (2 2) (2 2 2 2) (2 2 2 2)
# 1    2     2         4         4
#
#         4
#     3       3
#   2   2   2   2
#  1 1 1 1 1 1 1 1
#
# 4^2 = 4^1 + 4^1 + 4^1 + 4^1
# 3^5-3^2,      5 - 2
# 3^2*(3^3) - 3^2 = (3^3-1)*(3^2)
# 3^3
if __name__ == '__main__':
    MOD = 10**9 + 7

    def bpow(p, k):
        if k == 0:
            return 1
        if k == 1:
            return p

        res = (bpow(p, k//2) * bpow(p, k//2)) % MOD
        #res = (bpow(p, k // 2) * bpow(p, k // 2))
        if k % 2 == 1:
            res *= p
        res %= MOD

        return res

    def johnny_and_grandmaster(n, p, k):
        if p == 1:
            return n%2

        k.sort(reverse=True)
        s = i = 0
        while i < n:
            if s == 0:
                s += bpow(p, k[i])
                s %= MOD

                if i + 1 < n and k[i] - k[i-1] >= 20:
                    break
            else:
                s -= bpow(p, k[i])

            i += 1

        d = 0
        for j in range(i+1, n):
            d += bpow(p, k[j])
            d %= MOD

        res = s - d
        if res < 0:
            res += MOD

        return res


    def johnny_and_grandmaster2(n, p, k):

        if p == 1:
            return n%2

        k.sort()

        st = []
        for i in range(len(k)-1, -1, -1):

            st.append(k[i])

            if len(st) == 2 and st[-1] == st[0]:
                st.pop()
                st.pop()

            while len(st)-p >= 0 and st[-1] == st[len(st)-p]:
                cur = 0
                for j in range(p):
                    cur = st.pop()
                st.append(cur+1)

            if len(st) == 2 and st[-1] == st[0]:
                st.pop()
                st.pop()

        if len(st) == 0:
            return 0

        #print(st)

        r1 = bpow(p, st[0])
        r2 = 0
        for i in range(1, len(st)):
            r2 += bpow(p, st[i])
            r2 %= MOD

        r = (r1 - r2)%MOD
        if r < 0:
            r += MOD

        return r

    t = int(stdin.readline())
    for i in range(t):
        n, p = map(int, stdin.readline().split())
        k = list(map(int, stdin.readline().split()))

        res = johnny_and_grandmaster(n, p, k)

        stdout.write(str(res) + '\n')
