from sys import stdin, stdout

# ( A )(9 10 11)(      8)( B )
# ( B )(      8)(9 10 11)( A )
def unshuffling_a_deck(n, c_a):

    res_a = []
    while True:
        dic = {}
        a = b = c = -1
        for i in range(n):
            if c_a[i] in dic:
                a = dic[c_a[i]]
                c = i
                break

            dic[c_a[i]-1] = i

        if a == -1:
            break

        b = a + 1
        while b < c and c_a[b] - 1 == c_a[b-1]:
            b += 1

        q = []
        res = []
        if a-1 >= 0:
            q.append(c_a[0:a])
            res.append(len(q[-1]))
        if b-1 >= a:
            q.append(c_a[a:b])
            res.append(len(q[-1]))
        if c >= b:
            q.append(c_a[b:c+1])
            res.append(len(q[-1]))
        if n-1 >= c+1:
            q.append(c_a[c+1:n])
            res.append(len(q[-1]))

        #stdout.write(str(len(res)))
        #for v in res:
        #    stdout.write(' ' + str(v))
        #stdout.write('\n')
        s = str(len(res))
        for v in res:
            s += ' ' + str(v)
        res_a.append(s)

        # block reverse
        q.reverse()
        idx = 0
        for bl in q:
            for v in bl:
                c_a[idx] = v
                idx += 1

        #print(q)
        #print(c_a)

    return res_a

n = int(stdin.readline())
c_a = list(map(int, stdin.readline().split()))

res_a = unshuffling_a_deck(n, c_a)
stdout.write(str(len(res_a)) + '\n')
stdout.write('\n'.join(res_a))
