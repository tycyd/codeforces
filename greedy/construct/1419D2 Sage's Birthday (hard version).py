from sys import stdin, stdout

# 1 3 2 2 4 5 4
# 3 1 4 2 4 2 5
def segas_birthday_hard(n, a_a):
    a_a.sort()
    r1 = 0
    r2 = []

    a1 = a_a[0:n//2]
    a2 = a_a[n//2:n]

    i = 0
    j = 0
    while i < len(a1) or j < len(a2):
        r2.append(a2[j])
        if i < len(a1):
            r2.append(a1[j])

        i += 1
        j += 1

    for i in range(1, n-1):
        if r2[i-1] > r2[i] < r2[i+1]:
            r1 += 1

    return [r1, r2]


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))

res_a = segas_birthday_hard(n, a_a)
stdout.write(str(res_a[0]) + '\n')
stdout.write(' '.join(map(str, res_a[1])) + '\n')
