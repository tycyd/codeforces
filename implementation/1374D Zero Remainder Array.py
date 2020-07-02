from sys import stdin, stdout

# 4 3
# 1 2 1 3
# 6
# 2 1 2 0
#

# 1 1 2 3 3 3 3
# 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3
# 3: 4
# 1: 2
# 2: 1
if __name__ == '__main__':

    def zero_remainder_array(n, k, a):
        dic = {}
        maxcnt = 0
        maxa = 0

        for v in a:
            vk = (k-v%k)
            if vk == k:
                continue

            if vk not in dic:
                dic[vk] = 0
            dic[vk] += 1

            if dic[vk] > maxcnt:
                maxcnt = dic[vk]
                maxa = vk
            elif dic[vk] == maxcnt and vk > maxa:
                maxa = vk

        if maxcnt == 0:
            return 0

        return (maxcnt-1)*k + maxa + 1;

    t = int(stdin.readline())
    for i in range(t):
        n, k = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        stdout.write(str(zero_remainder_array(n, k, a)) + '\n')
