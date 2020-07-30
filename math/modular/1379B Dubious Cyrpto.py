from sys import stdin, stdout

# m = n*a + b - c
# |m - na| min
# l <= a, b, c <= r
if __name__ == '__main__':

    def dubious_cyrpto(l, r, m):

        mr = 10**6
        a, b, c = 0, 0, 0
        for i in range(l, r+1):

            m1 = m%i
            m2 = (i-m%i)

            if m < i:
                mm = m2
            else:
                mm = min(m1, m2)

            if mm < mr:
                a = i
                mr = mm

        if (a-m%a) == mr:
            # negative
            b, c = l, l + mr
        else:
            # positive
            b, c = r, r - mr

        return [a, b, c]

    t = int(stdin.readline())
    for i in range(t):
        l, r, m = map(int, stdin.readline().split())
        res = dubious_cyrpto(l, r, m)
        stdout.write(" ".join(map(str, res)) + '\n')
