from sys import stdin, stdout

#   1 2 3 4 5 6
#   5 6 3 4 1 2
#   X X 4 3 X X

# Key Idea:
#
# If we consider the unordered pair of elements {𝑎𝑖,𝑎𝑛−𝑖+1}
# then after any operation, the multiset of these pairs (irrespective of the ordering of elements within the pair) stays the same!
def swaps_again(n, a, b):

    if n % 2 == 1 and a[n//2] != b[n//2]:
        return "No"

    dica = {}

    for i in range(0, n//2):
        al = a[i]
        ar = a[n-1-i]

        if al not in dica:
            dica[al] = {}
        if ar not in dica:
            dica[ar] = {}
        if ar not in dica[al]:
            dica[al][ar] = 0
        if al not in dica[ar]:
            dica[ar][al] = 0
        dica[al][ar] += 1
        dica[ar][al] += 1

    #print(dica)

    for i in range(0, n//2):
        bl = b[i]
        br = b[n-1-i]
        if bl not in dica or br not in dica[bl] or dica[bl][br] == 0:
            return "No"
        dica[bl][br] -= 1
        dica[br][bl] -= 1

    return "Yes"


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))

        stdout.write(swaps_again(n, a, b) + '\n')