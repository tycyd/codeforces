from sys import stdin, stdout


def maximize_the_remaining_string(s):
    check_a = [False] * 26
    c_a = [[] for _ in range(26)]
    hs = set()

    for i in range(len(s)):
        c_a[ord(s[i]) - ord('a')].append(i)
        check_a[ord(s[i]) - ord('a')] = True
        hs.add(s[i])

    r = ''
    p = -1
    for _ in range(len(hs)):
        for i in range(25, -1, -1):
            if not check_a[i]:
                continue

            # right bound binary search
            l = 0
            h = len(c_a[i])
            while l < h:
                m = (l + h) // 2
                if c_a[i][m] <= p:
                    l = m + 1
                else:
                    h = m

            # check if index can be left most position
            found = True
            for j in range(i-1, -1, -1):
                if not check_a[j]:
                    continue
                if c_a[i][h] > c_a[j][-1]:
                    found = False
                    break

            if found:
                check_a[i] = False
                r += chr(i + ord('a'))
                p = c_a[i][h]
                break
    return r


t = int(stdin.readline())
for _ in range(t):
    s = stdin.readline().strip()
    r = maximize_the_remaining_string(s)
    stdout.write(str(r) + '\n')
