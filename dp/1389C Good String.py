import sys
import threading
from sys import stdin, stdout

sys.setrecursionlimit(10**4)
threading.stack_size(32*1024)

# 1010
# 12121212
def good_string(s):
    dp = [[0 for _ in range(10)] for _ in range(10)]
    cnt = [0] * 10

    ans1 = 0
    ans2 = 0

    for c in s:
        cv = ord(c) - ord('0')

        cnt[cv] += 1
        ans1 = max(ans1, cnt[cv])

        for i in range(10):
            if cv == i:
                continue

            if dp[cv][i] % 2 == 0:
                dp[cv][i] += 1
            if dp[i][cv] % 2 == 1:
                dp[i][cv] += 1
                ans2 = max(dp[i][cv], ans2)

    return len(s) - max(ans1, ans2)


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        s = stdin.readline().strip()
        ans = good_string(s)
        stdout.write(str(ans) + '\n')


threading.Thread(target=solve).start()
