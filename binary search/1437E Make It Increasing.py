from sys import stdin, stdout


# 10 3
# 1 (3) 5 (6) 12 9 8 10 (13) 15
# 2 4 9
#
# 5 0
# 4 3 1 2 3
# -1 -2 1 2 3
def make_it_increasing(n, k, a_a, b_a):
    res = 0

    a_a.insert(0, -10**10)
    a_a.append(10**20)
    b_a.insert(0, 0)
    b_a.append(len(a_a)-1)

    # 7 8 9 10
    for i in range(1, len(b_a)):
        l = b_a[i-1]
        r = b_a[i]
        lv = a_a[l]
        rv = a_a[r]
        if r - l > rv - lv:
            return -1

        lst = []
        inc = 0
        for j in range(l+1, r):
            inc += 1
            a_a[j] -= inc
            if a_a[j] < lv or a_a[j] > rv - (r - l):
                res += 1
                continue
            lst.append(a_a[j])
        res += len(lst) - lil(lst)

    return res


def lil(lst):
    tail = []
    for i in range(len(lst)):
        v = lst[i]
        l = 0
        h = len(tail)-1

        if h == -1 or v >= tail[h]:
            tail.append(v)
            continue

        # right bound
        while l < h:
            m = (l + h) // 2
            if v >= tail[m]:
                l = m + 1
            else:
                h = m

        tail[l] = v

    return len(tail)


n, k = map(int, stdin.readline().split())
a_a = list(map(int, stdin.readline().split()))
b_a = []
if k > 0:
    b_a = list(map(int, stdin.readline().split()))
r = make_it_increasing(n, k, a_a, b_a)
stdout.write(str(r))