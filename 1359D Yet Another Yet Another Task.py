from sys import stdin, stdout

#5
#5 -2 10 -4 1
#5 -2 -1 1
#3 -2 -1 2
#11
#3 0 1 -2 999 -5 -1 0 3 2 2
#9999 -1 -2 -3 3 2 2 2 2
#1 2 3

#3 1

#segment tree
def yet_another_yet_another_task(a):

    n = len(a)
    preSum = [0 for i in range(n)]
    postSum = [0 for i in range(n)]

    preSum[0] = a[0]
    postSum[n-1] = a[n-1]

    for i in range(1, n):
        preSum[i] = preSum[i-1] + a[i]

    for i in range(n-2, -1, -1):
        postSum[i] = postSum[i+1] + a[i]

    preSumSegmentTree = SegmentTree(0, n-1, preSum)
    postSumSegmentTree = SegmentTree(0, n-1, postSum)

    st = []
    leftSum = [0 for i in range(n)]
    for i in range(n):
        j = i
        while len(st) > 0 and st[-1][0] <= a[i]:
            j = st.pop()[1]
        st.append([a[i], j])

        leftSum[i] = postSumSegmentTree.query(j, i) - postSum[i]

    st = []
    rightSum = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        j = i
        while len(st) > 0 and st[-1][0] <= a[i]:
            j = st.pop()[1]
        st.append([a[i], j])

        rightSum[i] = preSumSegmentTree.query(i, j) - preSum[i]

    res = 0
    for i in range(n):
        res = max(res, leftSum[i] + rightSum[i])

    return res


class SegmentTree:

    def __init__(self, i, j, sum):

        self.l = i
        self.r = j
        m = (i + j) // 2

        if i == j:
            self.maxVal = sum[i]
            return
        if i > j:
            return -1000000000

        self.lst = SegmentTree(i, m, sum)
        self.rst = SegmentTree(m+1, j, sum)

        if self.lst is not None and self.rst is not None:
            self.maxVal = max(self.lst.maxVal, self.rst.maxVal)
        elif self.lst is None:
            self.maxVal = self.rst.maxVal
        elif self.rst is None:
            self.maxVal = self.lst.maxVal

    def query(self, i, j):

        if j < self.l or self.r < i:
            return -1000000000

        if i <= self.l and self.r <= j:
            return self.maxVal

        ql = -1000000000
        qr = -1000000000

        if self.lst is not None:
            ql = self.lst.query(i,j)
        if self.rst is not None:
            qr = self.rst.query(i,j)

        return max(ql, qr)


#Kadane algorithm
def yet_another_yet_another_task2(a):

    res = 0
    for i in range(1, 31):

        mxr = 0
        mnr = 0
        for j in a:
            if j > i:
                mxr = 0
                mnr = 0
            else:
                mxr += j
                mnr = min(mxr, mnr)
                res = max(res, mxr - mnr - i)

    return res


if __name__ == '__main__':

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    stdout.write(str(yet_another_yet_another_task(a)) + '\n')