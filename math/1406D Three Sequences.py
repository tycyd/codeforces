from sys import stdin, stdout


# a:  2 -1  7  3
# b: -3 -3  5  5
# c:  5  2  2 -2
#
# if a[i] < a[i-1]:
#   b[i] = b[i-1]
#   c[i] = c[i-1] + a[i] - a[i-1]
# if a[i] > a[i-1]:
#   c[i] = c[i-1]
#   b[i] = b[i-1] + a[i] - a[i-1]
#
# K = SUM( MAX(b[i]-b[i-1], 0) )    -- 1 < i < n
# b[n-1] = b[0] + K
# c[0] = a[0] - b[0]
#
# MAX(b[n-1], c[0])
# => MAX(b[0] + K, a[0] - b[0])
# => MAX(x + K, A - x)
# => x + K = A - x  -- optimal result
# => x = (A - K) / 2

def three_sequences(n, a_a, q_a):
    res_a = []
    dif_a = [0] * n
    K = 0
    for i in range(1, n):
        K += max(0, a_a[i] - a_a[i-1])
        dif_a[i] = a_a[i] - a_a[i-1]

    res_a.append(calc(K, a_a[0]))
    for q in q_a:
        l, r, x = q
        if l > 1:
            K -= max(0, dif_a[l-1])
            dif_a[l-1] += x
            K += max(0, dif_a[l-1])

        if r < n:
            K -= max(0, dif_a[r])
            dif_a[r] -= x
            K += max(0, dif_a[r])

        if l == 1:
            a_a[0] += x

        res_a.append(calc(K, a_a[0]))

    return res_a


def calc(K, a0):
    b0 = (a0 - K) // 2
    bn = b0 + K
    c0 = a_a[0] - b0

    return max(bn, c0)


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
q = int(stdin.readline())
q_a = []
for _ in range(q):
    l, r, x = map(int, stdin.readline().split())
    q_a.append([l, r, x])

res_a = three_sequences(n, a_a, q_a)
for res in res_a:
    stdout.write(str(res) + '\n')
