from sys import stdin, stdout

# 4 3 2 1
# 1 4, 2 4, 3 4
# 4 3 1 2
# 4 2 1 3
# 3 2 1 4

# 1 6 8 1
# 2 4, 3 4
#
# 1 1 8 6
# 1 1 6 8
#
# 1 8 6 1
# 2 4, 3 4, 2 3
# 1 8 1 6
# 1 6 1 8
# 1 1 6 8
#
if __name__ == '__main__':
    def inversion_swapsort(n, a):

        I = []
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] > a[j]:
                    I.append([a[i], i + 1, j + 1])

        #print(I)

        I.sort()
        #print(I)

        I.sort(key=lambda x: x[2], reverse=True)
        #print(I)
        print(len(I))
        if len(I) > 0:
            for i in I:
                j = i[1:]
                print(*j)

        return

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    inversion_swapsort(n, a)
