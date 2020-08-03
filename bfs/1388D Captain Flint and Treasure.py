from sys import stdin, stdout


def captain_flint_and_treasure(n, a_a, b_a):
    ind = [0 for i in range(n + 1)]
    r_s = set(i + 1 for i in range(n))
    for i in range(n):
        if b_a[i] != -1:
            ind[b_a[i]] += 1
            r_s.discard(b_a[i])

    queue = list(r_s)
    ans1 = 0
    ans2 = []
    ans3 = []

    while queue:
        cnt = len(queue)
        for i in range(cnt):
            j = queue.pop()

            if b_a[j - 1] != -1:
                if a_a[j - 1] > 0:
                    a_a[b_a[j - 1] - 1] += a_a[j - 1]
                ind[b_a[j - 1]] -= 1
                if ind[b_a[j - 1]] == 0:
                    queue.append(b_a[j - 1])

            ans1 += a_a[j-1]

            if a_a[j - 1] > 0:
                ans2.append(j)
            else:
                ans3.append(j)

    ans3.reverse()
    return [ans1, ans2 + ans3]


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

ans = captain_flint_and_treasure(n, a_a, b_a)
stdout.write(str(ans[0]) + '\n')
stdout.write(" ".join(map(str, ans[1])) + '\n')
