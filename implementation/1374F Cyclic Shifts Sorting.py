from sys import stdin, stdout

# 56
# 1 2 3 3 4 6 iv = 0
# 1 2 3.5 3 6 4 iv = 2
# 1 2 3 6 3.5 4
# 1 2 3 3.5 4

# 3 3 4 4
# 3: 1 2 [6 3 3] 4
# 3: 1 2 [3 6 3] 4
# 4: 1 2 3 [4 6 3]
# 4: 1 2 3 [3 4 6]
# 1 2 3 4 5 6
# 1 2 3 3 4 6 iv = 0
#    [3, 3, 4] => [4, 3, 3] = +2, 0, 0
#    [3, 3, 4] => [3, 4, 3] =  0,+1, 0
if __name__ == '__main__':
    def cyclic_shifts_sorting(n, a):
        dic = {}
        dupi = -1
        dupj = -1
        for i in range(n):
            a[i] *= 1000
            if a[i] in dic:
                k = a[i]
                a[i] += dic[k][0]
                dic[k][0] += 1

                if dupi == -1:
                    dupi = dic[k][1]
                    dupj = i
            else:
                dic[a[i]] = [1, i]

        iv = 0
        for i in range(n):
            for j in range(i+1, n):
                if a[i] > a[j]:
                    iv += 1

        if iv % 2 == 1:
            if dupi == -1:
                return [-1]
            else:
                tmp = a[dupi]
                a[dupi] = a[dupj]
                a[dupj] = tmp

        sa = sorted(a)

        #print(a)
        #print(sa)

        res = []
        for i in range(n):
            if sa[i] == a[i]:
                continue

            idx = -1
            for j in range(n):
                if a[j] == sa[i]:
                    idx = j
                    break

            # 3 4 5 6 [7 8 1] 10
            # [3 1 4] 5 6
            # [1 4 3] 5 6
            while idx >= i + 2:
                tmp = a[idx]
                a[idx] = a[idx-1]
                a[idx-1] = a[idx-2]
                a[idx-2] = tmp
                res.append(idx-2+1)
                idx -= 2

            if idx > i:
                tmp = a[idx]
                a[idx] = a[idx+1]
                a[idx+1] = a[idx-1]
                a[idx-1] = tmp

                res.append(idx-1+1)
                res.append(idx-1+1)
                idx -= 1

        return [len(res), res]

    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        res = cyclic_shifts_sorting(n, a)
        stdout.write(str(res[0]) + '\n')
        if res[0] > -1:
            stdout.write(" ".join(map(str, res[1])) + '\n')

