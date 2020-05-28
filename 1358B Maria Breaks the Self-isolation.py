from sys import stdin, stdout


# 1,5,4,5,1,9
# 1 1 4 5 5 9
# 1 2 3 4 5 6
def maria_breaks_the_self_isolation(n, a):

    a.sort()

    res = 0
    for i in range(n):
        if a[i] <= (i+1):
            res = i+1

    return res + 1


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        stdout.write(str(maria_breaks_the_self_isolation(n, a)) + '\n')
