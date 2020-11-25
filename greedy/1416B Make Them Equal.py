from sys import stdin, stdout

#  2  16  4  18
#
#
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))

    sm = sum(a_a)
    if sm % n != 0:
        stdout.write('-1\n')
        continue
    avg = sm // n

    op_a = []
    for i in range(1, n):
        idx = i + 1
        m = a_a[i] % idx
        d = a_a[i] // idx
        if m != 0:
            d += 1
            op_a.append([1, idx, idx - m])

            #a_a[0] -= (idx - m)
            #a_a[i] += (idx - m)

        op_a.append([idx, 1, d])

        #a_a[0] += d*idx
        #a_a[i] -= d*idx

        #print(a_a)

    for i in range(1, n):
        op_a.append([1, i+1, avg])

        #a_a[0] -= avg
        #a_a[i] += avg

    #print(a_a)

    stdout.write(str(len(op_a)) + '\n')
    for op in op_a:
        stdout.write(' '.join(map(str, op)) + '\n')
