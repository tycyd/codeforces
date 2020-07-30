from sys import stdin, stdout

t = int(stdin.readline())

# a + (x-1)*b
# 9 6 (4) 3
for k in range(t):

    n, m = map(int, stdin.readline().split())

    abs_list = []
    for _ in range(m):
        abs_list.append(list(map(int, stdin.readline().split())))

    abs_list.sort(key=lambda x: -x[0])
    abs_list[0].append(abs_list[0][0])
    for i in range(1, m):
        abs_list[i].append(abs_list[i-1][2] + abs_list[i][0])




    res = 0
    for i in range(m):
        if abs_list[i][1] > abs_list[0][0]:
            res = max(res, abs_list[i][0] + (n - 1) * abs_list[i][1])
            continue

        l, h = 0, m-1
        while l < h:
            mid = (l + h + 1)//2
            if abs_list[mid][0] < abs_list[i][1]:
                h = mid - 1
            else:
                l = mid

        if l+1 >= n:
            res = max(res, abs_list[n-1][2])
        else:
            if i <= l:
                res = max(res, abs_list[l][2] + (n - l - 1) * abs_list[i][1])
            else:
                res = max(res, abs_list[l][2] + abs_list[i][0] + (n - l - 2) * abs_list[i][1])

    stdout.write(str(res) + '\n')
    if k != t-1:
        stdin.readline()
