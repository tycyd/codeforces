from sys import stdin, stdout

# 3 5 4 0 2 1
#           6
# 1
#     3
#       4
# 0 1     5
#
#
#
# 0 1 2 3 4 5
#           6
#         5
#       4
#     3
#   2
# 1

# 0 5 2 3 4   1
# (0 5 2 3 4) 6

if __name__ == '__main__':

    def replace_by_MEX(n, a):
        dic = {}
        s = set()
        res = []
        for i in range(n):
            if a[i] not in dic:
                dic[a[i]] = 1
            else:
                dic[a[i]] += 1
            if a[i] != i:
                s.add(i)

        while len(s) > 0:
            m = MEX(dic)
            idx = -1
            if n == MEX(dic):
                idx = next(iter(s))
            else:
                idx = m
                s.remove(idx)

            res.append(idx + 1)
            dic[a[idx]] -= 1
            a[idx] = m
            dic[m] = 1

        #print(a)

        return res

    def MEX(dic):
        mex = 0
        while mex in dic and dic[mex] > 0:
            mex += 1
        return mex

    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        res = replace_by_MEX(n, a)
        stdout.write(str(len(res)) + '\n')
        stdout.write(" ".join(map(str, res)) + '\n')
