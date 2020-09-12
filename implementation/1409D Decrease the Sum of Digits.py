from sys import stdin, stdout


# 217871987498122 10
def decrease_the_sum_of_digits(n, s):
    n_s = str(n)
    v = 0
    ans = 0
    for i in range(len(n_s)):
        v += ord(n_s[i]) - ord('0')
        if v >= s and ans == 0:
            ans = 10**(len(n_s)-i) - int(n_s[i:])

    if v == s:
        return 0
    else:
        return ans


t = int(stdin.readline())
for _ in range(t):
    n, s = map(int, stdin.readline().split())
    ans = decrease_the_sum_of_digits(n, s)
    stdout.write(str(ans) + '\n')
