from sys import stdin, stdout


def new_game_plus(n, k, c_a):

    c_a.sort(reverse=True)
    r = 0
    i = 0
    b = 0
    for c in c_a:
        if i == n - 1:
            return r

        if b + c >= 0:
            r += b + c
            b = b + c
        else:
            break
        i += 1

    ncnt = n - i
    if ncnt <= k + 1:
        return r

    initial = b + c_a[i]
    neg_a = [initial] + c_a[i+1:(len(c_a) - (k + 1))]
    ncnt = len(neg_a)
    m = ncnt % (k + 1)
    d = ncnt // (k + 1)
    sa = [0] * (k+1)
    cur = d + 1

    for i in range(ncnt - m):
        if i % d == 0:
            cur -= 1

        r += cur * neg_a[i]
        sa[i % (k+1)] += neg_a[i]

    sa.sort(reverse=True)
    for j in range(m):
        r += neg_a[ncnt - j - 1]
        r += sa[j]

    return r


n, k = map(int, stdin.readline().split())
c_a = list(map(int, stdin.readline().split()))
r = new_game_plus(n, k, c_a)
stdout.write(str(r) + '\n')
