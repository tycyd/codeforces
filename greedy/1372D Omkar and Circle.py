from sys import stdin, stdout


# 7 10 2
# 4 2 3 1 5 6 7    -3, +4
# 4   3     12
#
if __name__ == '__main__':

    def omkar_and_circle(n, a):
        if n == 1:
            return a[0]

        oea = [0] * (n+1)
        oea[1] = a[0]   # odd
        oea[2] = a[1]   # even

        for i in range(3, n+1):
            oea[i] = a[i-1] + oea[i-2]

        res = 0
        for i in range(1, n+1):
            # pick i and i+1
            sr = 0
            if i%2 == 1:
                #odd
                sr = oea[i] + oea[n-1] - oea[i-1]
            else:
                #even
                sr = oea[i] + oea[n] - oea[i-1]
            res = max(res, sr)

        return res

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    print(omkar_and_circle(n, a))
