from sys import stdin, stdout


# A X X A X X A
def pinkie_pie_eas_patty_cakes(n, a_a):
    dic = {}
    mx = 0

    for a in a_a:
        if a not in dic:
            dic[a] = 0
        dic[a] += 1
        mx = max(dic[a], mx)

    cnt = 0
    for k in dic:
        if dic[k] == mx:
            cnt += 1

    res = cnt - 1
    res += (n - cnt*mx) // (mx - 1)

    return res


T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    ans = pinkie_pie_eas_patty_cakes(n, a_a)
    stdout.write(str(ans) + '\n')
