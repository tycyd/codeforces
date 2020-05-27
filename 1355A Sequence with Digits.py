from sys import stdin, stdout

# 𝑎𝑛+1=𝑎𝑛+𝑚𝑖𝑛𝐷𝑖𝑔𝑖𝑡(𝑎𝑛)⋅𝑚𝑎𝑥𝐷𝑖𝑔𝑖𝑡(𝑎𝑛).
# Prove:
# range: 1*1 ~ 9*9
# if a is infinite, a can be more than 1000. 1000*(a/1000 + 1)
# also, 1000 - 1099, has at least 99, which is smaller than 9*9, contradiction


def sequence_with_digits(a1, k):

    a = a1

    while k > 1:
        mm = get_max_min_digits(a)
        if mm == 0:
            break
        a += mm
        k -= 1

    return a


def get_max_min_digits(a):

    mx = 0
    mn = 9

    while a > 0:
        mx = max(a%10, mx)
        mn = min(a%10, mn)
        a //= 10

    return mx*mn


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        ak = list(map(int, stdin.readline().split()))

        a1 = ak[0]
        k = ak[1]

        stdout.write(str(sequence_with_digits(a1, k)) + '\n')
