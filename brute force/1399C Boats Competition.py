from sys import stdin, stdout


# 1 2 3 4 5
# (1,5), (2,4)
def boats_competition(n, w_a):

    ans = 0
    for i in range(2, 101):
        cnt = 0
        dic = {}
        for w in w_a:
            if (i - w) in dic and dic[i-w] > 0:
                cnt += 1
                dic[i - w] -= 1
            else:
                if w not in dic:
                    dic[w] = 1
                else:
                    dic[w] += 1

        ans = max(ans, cnt)

    return ans


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    w_a = list(map(int, stdin.readline().split()))

    ans = boats_competition(n, w_a)
    stdout.write(str(ans) + '\n')
