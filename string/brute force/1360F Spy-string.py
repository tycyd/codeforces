from sys import stdin, stdout

# case 1: 2 char diff
# abac
# zbab
# zbac or abab

# case 2: 1 char diff
# abac
# zbac
# ?bac

# brute force
# O(26*M^2*N)
def spy_string(a, n, m):

    ca = list(a[0])

    for i in range(m):

        org = ca[i]
        for j in range(26):
            ca[i] = chr(ord('a') + j)
            found = True

            for k in range(1, n):
                dif = 0
                for l in range(m):
                    if a[k][l] != ca[l]:
                        dif += 1

                if dif > 1:
                    found = False
                    break

            if found:
                return "".join(ca)

        ca[i] = org

    return "-1"


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        (n, m) = list(map(int, stdin.readline().split()))

        a = []
        for j in range(n):
            a.append(stdin.readline().strip())

        stdout.write(spy_string(a, n, m) + '\n')
