from sys import stdin, stdout

#  4  5  2  3
#  2  3  2  7
# -2 -2  0  4
#
#  3   3   3
#  2   3   4
# -1   0   1

#  2  3  4  5
#  3  7  2  2
#  1  4 -2 -3
if __name__ == '__main__':

    def network_coverage(n, a, b):
        l = 0
        h = min(a[0], b[-1]) + 1

        while l < h:
            take = (l + h)//2
            avail = take

            for i in range(n):
                need = max(0, a[i] - avail)

                if i < n-1:
                    if b[i] < need:
                        l = take + 1
                        break
                else:
                    if b[i] - take < need:
                        h = take
                        break
                    else:
                        return "YES"

                avail = b[i] - need

        return "NO"

    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))

        stdout.write(network_coverage(n, a, b) + '\n')
