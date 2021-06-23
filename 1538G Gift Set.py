from sys import stdin, stdout


t = int(stdin.readline())
for _ in range(t):
    x, y, a, b = map(int, stdin.readline().split())

    if a == b:
        stdout.write(str(min(x, y)//a) + '\n')
    else:
        if a < b:
            tmp = b
            b = a
            a = tmp

        l = 0
        h = 10 ** 10
        while l < h:
            m = (l + h + 1) // 2
            r1 = (x - m*b)//(a-b)
            r2 = (y - m*a)//(b-a)

            #print(m)
            #print(r1)
            #print(r2)
            #print('---------------------')

            if r1 < 0 or r2 > m or r1 < r2:
                # not exist
                h = m - 1
            else:
                l = m

        stdout.write(str(l) + '\n')
