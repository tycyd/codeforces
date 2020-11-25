from sys import stdin, stdout


def number_of_subsequences(n, s):

    MOD = 1000000007
    # contains a count
    a_a = [0 for i in range(n+1)]
    # contains ab count
    ab_a = [0 for i in range(n+1)]
    # contains abc count
    abc_a = [0 for i in range(n+1)]

    m = 1
    for i in range(1, n+1):
        if s[i-1] == 'a':
            a_a[i] = a_a[i-1] + m
            a_a[i] %= MOD
            ab_a[i] = ab_a[i-1]
            abc_a[i] = abc_a[i - 1]
        elif s[i-1] == 'b':
            a_a[i] = a_a[i - 1]
            ab_a[i] = ab_a[i - 1] + a_a[i - 1]
            ab_a[i] %= MOD
            abc_a[i] = abc_a[i - 1]
        elif s[i-1] == 'c':
            a_a[i] = a_a[i - 1]
            ab_a[i] = ab_a[i - 1]
            abc_a[i] = abc_a[i - 1] + ab_a[i - 1]
            abc_a[i] %= MOD
        else:
            a_a[i] = 3*a_a[i - 1] + m
            a_a[i] %= MOD
            ab_a[i] = 3*ab_a[i - 1] + a_a[i - 1]
            ab_a[i] %= MOD
            abc_a[i] = 3*abc_a[i - 1] + ab_a[i - 1]
            abc_a[i] %= MOD

            m *= 3
            m %= MOD

    return abc_a[n]


n = int(stdin.readline())
s = stdin.readline().strip()

res = number_of_subsequences(n, s)
stdout.write(str(res) + '\n')
