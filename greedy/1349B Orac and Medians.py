from sys import stdin, stdout


# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 3 3 3 3 3 3 7 8 9 10
# 3 2
# 1 2 3

# fact: if can find 3 3 =>  3 3 3 3 3 =>  yes
#       2 1 1 1 [3 3]
#       [2 1 3]          
#       [3 1 2]
if __name__ == '__main__':

    def orac_and_medians(n, k, a):

        if len(a) == 1 and a[0] == k:
            return "yes"

        f1 = False
        f2 = False

        for i in range(n):

            if a[i] == k:
                f1 = True

            if i - 1 >= 0 and a[i] >= k and a[i-1] >= k:
                f2 = True
                if f1: break

            if i - 2 >= 0 and a[i] >= k and a[i-2] >= k:
                f2 = True
                if f1: break

        if f1 and f2:
            return "yes"
        else:
            return "no"

    t = int(stdin.readline())
    for i in range(t):
        n, k = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))

        stdout.write(orac_and_medians(n, k, a) + '\n')
