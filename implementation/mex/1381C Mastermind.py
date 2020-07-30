from sys import stdin, stdout
import heapq

# 5 3 4
# 1 1 2 1 2
# 3 1 1 1 2
# 1 1 2 1 2
# 4 1 4
# 2 3 2 3
# 2 2 3 3

# 1 2 1 2
# 0 2 1 3
# 1 3 0 2

def Mastermind(n, x, y, b_a):
    ans = [-1] * n

    # find mex
    b_s = set(b_a)
    mex = 1
    while mex in b_s:
        mex += 1

    #print(mex)

    # get frequency
    fq_d = {}
    for i in range(len(b_a)):
        if b_a[i] not in fq_d:
            fq_d[b_a[i]] = []
        fq_d[b_a[i]].append(i)

    fq_h = []
    for key in fq_d:
        heapq.heappush(fq_h, (-len(fq_d[key]), key, fq_d[key]))

    #print(fq_h)

    for _ in range(x):
        l, v, f_a = heapq.heappop(fq_h)
        ans[f_a.pop()] = v
        l += 1
        if l < 0:
            heapq.heappush(fq_h, (l, v, f_a))

    #print(ans)

    if x == n:
        return ans

    z = n - y
    shift_a = []
    for fq in fq_h:
        for idx in fq[2]:
            shift_a.append([idx, fq[1]])

    #print(shift_a)

    offset = -fq_h[0][0]

    #print(offset)

    idx_a = []
    for i in range(len(shift_a)):
        shift = shift_a[i]
        nidx = (i + offset) % (n - x)
        #print(shift[1])
        #print(shift_a[nidx][0])
        nv = shift_a[nidx][1]
        if shift[1] == nv:
            if z == 0:
                return []
            z -= 1
            ans[shift_a[nidx][0]] = mex
        else:
            idx_a.append(shift_a[nidx][0])
            ans[shift_a[nidx][0]] = shift[1]

    while z > 0:
        if not idx_a:
            return []
        ans[idx_a.pop()] = mex
        z -= 1

    return ans


t = int(stdin.readline())
for _ in range(t):
    n, x, y = map(int, stdin.readline().split())
    b_a = list(map(int, stdin.readline().split()))

    ans = Mastermind(n, x, y, b_a)
    if ans:
        stdout.write('Yes\n')
        stdout.write(' '.join(map(str, ans)) + '\n')
    else:
        stdout.write('No\n')
