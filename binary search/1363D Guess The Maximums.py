from sys import stdin, stdout

# 1
# 4 2
# 2 1 3
# 2 2 4
#
# [1,2,3,4]
# find max
if __name__ == '__main__':

    def querymx(n):
        s = ""
        for i in range(1, n+1):
            s += str(i) + " "

        cmd = "? " + str(n) + " " + s + '\n'
        stdout.write(cmd)
        stdout.flush()

        return int(stdin.readline())

    def query(S, l, h):
        ary = []
        for i in range(l, h+1):
            for j in range(0, len(S[i])):
                ary.append(S[i][j])

        cmd = "? " + str(len(ary)) + " " + " ".join(map(str, ary)) + '\n'
        stdout.write(cmd)
        stdout.flush()

        return int(stdin.readline())

    def query2(S, ec, n):
        st = set(S[ec])
        s = ""
        for i in range(1, n + 1):
            if i not in st:
                s += str(i) + " "

        cmd = "? " + str(n-len(st)) + " " + s + '\n'
        stdout.write(cmd)
        stdout.flush()

        return int(stdin.readline())

    def populate(res, l, h, v):
        for i in range(l, h+1):
            res[i] = v

    t = int(stdin.readline())
    for i in range(t):
        n, k = map(int, stdin.readline().split())
        #A = list(map(int, stdin.readline().split()))

        S = []
        res = [0] * k
        for j in range(k):
            S.append(list(map(int, stdin.readline().split())))
            S[len(S)-1].pop(0)

        mx = querymx(n)
        # binary search
        l = 0
        h = len(S)-1
        while l < h:
            m = (l+h)//2
            lmq = query(S, l, m)

            if lmq == mx:
                populate(res, l, h, mx)
                h = m
            else:
                populate(res, l, m, mx)
                l = m + 1

        res[h] = query2(S, h, n)

        #output result
        rcmd = "! " + " ".join(map(str, res)) + '\n'
        stdout.write(rcmd)
        stdout.flush()
        stdin.readline()
