from sys import stdin, stdout

if __name__ == '__main__':

    # 1 2 3 4 5 6 7
    # 3 2 4 5 1 6 7
    #
    # 1 2 3 5
    # 1 4 3 6
    def omkar_and_baseball(n, a):
        ast = sorted(a)

        l = 0
        r = n-1

        while l < n and a[l]==ast[l]:
            l += 1
        while r >= 0 and a[r] == ast[r]:
            r -= 1

        if l >= r:
            return 0

        for i in range(l, r+1):
            if a[i] == ast[i]:
                return 2

        return 1

    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        ans = omkar_and_baseball(n, a)
        print(ans)
