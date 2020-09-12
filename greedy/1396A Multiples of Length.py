from sys import stdin, stdout


# 1: choose all a, a - a*n = a*(1-n)
# 2: choose n-1 a, a*(1-n) + a*(n-1)
# 3: choose last a, a*(1-n) - a*(1-n)
def multiples_of_length(n, a_a):
    if n == 1:
        return [[1,1], [1], [1,1], [1], [1,1], [-a_a[0]-2]]

    ans_a = [[] for _ in range(6)]
    # step 1
    ans_a[0].append(1)
    ans_a[0].append(n)

    # step 2
    ans_a[2].append(1)
    ans_a[2].append(n-1)

    # step 3
    ans_a[4].append(n)
    ans_a[4].append(n)

    for i in range(n):
        ans_a[1].append(-a_a[i]*n)
        if i < n-1:
            ans_a[3].append(a_a[i] * (n-1))
        elif i == n-1:
            ans_a[5].append(-a_a[i]*(1-n))

    return ans_a


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))

ans_a = multiples_of_length(n, a_a)
for ans in ans_a:
    stdout.write(' '.join(map(str, ans)) + '\n')
