from sys import stdin, stdout

# 5 2
# 5 2 3
# 3 1 4 5 2
# 3     5

# 1 2 3 4 5 6 7
if __name__ == '__main__':

    def get_ans(mx, x, k, y, a, l, r):
        cnt = r - l - 1
        amx = 0
        if l >= 0:
            amx = max(amx, a[l])
        if r < len(a):
            amx = max(amx, a[r])

        ans = (cnt//k)*x + (cnt%k)*y
        if amx > mx:
            ans = min(cnt*y, ans)
        else:
            if cnt < k:
                return [False, None]

            ans = min(x + (cnt-k)*y, ans)
        return [True, ans]

    def berserk_and_fireball(n, m, x, k, y, a, b):

        ans = 0
        j = 0
        mx = 0
        l = -1
        for r in range(n):

            if j < m and a[r] == b[j]:
                lr = get_ans(mx, x, k, y, a, l, r)
                if not lr[0]:
                    return -1

                #print(lr[1])
                ans += lr[1]
                j += 1
                l = r
                mx = 0
            else:
                mx = max(mx, a[r])

        if j < m:
            return -1

        #print(l)
        #print(r)

        lr = get_ans(mx, x, k, y, a, l, n)
        if not lr[0]:
            return -1
        ans += lr[1]

        return ans

    n, m = map(int, stdin.readline().split())
    x, k, y = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))

    stdout.write(str(berserk_and_fireball(n, m, x, k, y, a, b)))
