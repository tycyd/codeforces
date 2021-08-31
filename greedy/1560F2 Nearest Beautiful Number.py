from sys import stdin, stdout

# if has next big, res = next big + min
# 724533 4
# 724542

# else move backwards until dic[i] = 0, res = (res[i] + 1) --
# 177890 2
# 181111

# 6
# 2021 3
# 177890 2
# 34512 3
# 724533 4
# 998244353 1
# 12345678 10

# k=3
# expected: '111676111', found: '111681111'
#  111671119 3


def find_next_big(d, dic):
    for i in range(d+1, 10):
        if dic[i] > 0:
            return i
    return -1


def find_min(dic):
    for i in range(0, 10):
        if dic[i] > 0:
            return i
    return -1


def find_cnt(dic):
    cnt = 0
    for i in range(0, 10):
        if dic[i] > 0:
            cnt += 1
    return cnt


def solve(n, k):
    dic = {}
    for i in range(10):
        dic[i] = 0

    sn = str(n)
    ck = 0

    for i in range(len(sn)):
        d = ord(sn[i]) - ord('0')

        if dic[d] == 0:
            if ck == k:
                nb = find_next_big(d, dic)
                if nb >= 0:
                    cm = find_min(dic)
                    res = sn[:i] + str(nb) + (str(cm) * (len(sn) - i - 1))
                    return res
                else:
                    j = i-1
                    tv = -1
                    while dic[ord(sn[j]) - ord('0')] != 1:
                        tv = find_next_big(ord(sn[j]) - ord('0'), dic)
                        if tv != -1:
                            break

                        dic[ord(sn[j]) - ord('0')] -= 1
                        j -= 1

                    pv = ord(sn[j]) - ord('0')
                    if tv == -1:
                        tv = pv + 1

                    dic[tv] += 1
                    dic[pv] -= 1

                    if find_cnt(dic) < k:
                        res = sn[:j] + str(tv) + ('0' * (len(sn) - j - 1))
                    else:
                        cm = find_min(dic)
                        res = sn[:j] + str(tv) + (str(cm) * (len(sn) - j - 1))

                    return res
            ck += 1

        dic[d] += 1
    return sn


t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    r = solve(n, k)
    stdout.write(r + '\n')
