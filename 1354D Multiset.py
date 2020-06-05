from sys import stdin, stdout

# sum accumulation O(N)
def multiset(n, k, a):



    return res

if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        nk = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))

        stdout.write(str(constant_palindrome_sum(nk[0], nk[1], a)) + '\n')