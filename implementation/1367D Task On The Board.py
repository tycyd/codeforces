from sys import stdin, stdout

# 4
# abac
# 2 1 0
# aac
# 0 => c
# 1 =>
# z b z a a a a c
# |i-k| + |j-k| =
# i+j-2k
# i-k-j+k = i-j
# j-i
# 2k-i-j
# 5000 * 50 = 25 * 10^4 * 50 =
def task_on_the_board(s, m, b):

    cha = [0 for i in range(26)]
    for c in s:
        cha[ord(c)-ord('a')] += 1

    k = 25
    res = [' ' for i in range(m)]
    cnt = 0
    prea = []

    while cnt != m:
        cura = []
        for i in range(len(b)):
            if res[i] == ' ' and b[i] == cal(prea, i):
                cura.append(i)

        while cha[k] < len(cura):
            k -= 1

        for i in cura:
            prea.append(i)
            res[i] = chr(97 + k)
        cnt += len(cura)
        k -= 1

    return res


def cal(prea, i):
    r = 0
    for p in prea:
        r += abs(p - i)
    return r


if __name__ == '__main__':
    q = int(stdin.readline())
    for i in range(q):
        s = stdin.readline().strip()
        m = int(stdin.readline())
        b = list(map(int, stdin.readline().split()))

        stdout.write("".join(task_on_the_board(s, m, b)) + '\n')
