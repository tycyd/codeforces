from sys import stdin, stdout

MOD = int(1e9 + 7)
mxn = int(2e6) + 1
dp = [0] * mxn

for i in range(2, mxn):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]
    if (i + 1) % 3 == 0:
        dp[i] += 4

    dp[i] %= MOD

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n - 1])


# a: no child
# b: 1 child
# l1: adp[0]=0, bdp[0]=0, r[0] = 0
# l1: adp[1]=1, bdp[1]=0, r[1] = 0
# l2: adp[2]=1, bdp[2]=1, r[2] = 0
# l3: adp[3]=3, bdp[3]=1, r[3] = 1
# l4: adp[4]=5, bdp[4]=3, r[4] = 1
# l5: adp[5]=11, bdp[5]=5, r[5] = 3
# bdp[i] = adp[i-1]
# adp[i] = adp[i-1] + bdp[i-1]*2
# r[i] = r[i-3] + bdp[i-1]

# if __name__ == '__main__':
#
#     MOD = 10**9 + 7
#     t = int(stdin.readline())
#
#     adp = [0, 1]
#     bdp = [0, 0]
#     rdp = [0, 0]
#     cl = 2
#
#     def tedious_Lee(n):
#         global adp, bdp, rdp, cl, MOD
#
#         if n < cl:
#             return rdp[n]
#
#         while cl <= n:
#             bdp.append(adp[cl - 1])
#             adp.append(adp[cl - 1] + bdp[cl - 1] * 2)
#             rdp.append(bdp[cl - 1])
#             if cl >= 3:
#                 rdp[cl] += rdp[cl - 3]
#
#             bdp[cl] %= MOD
#             adp[cl] %= MOD
#             rdp[cl] %= MOD
#
#             cl += 1
#
#         return rdp[-1]
#
#
#     for i in range(t):
#         n = int(stdin.readline())
#         res = (tedious_Lee(n) * 4) % MOD
#         stdout.write(str(res) + '\n')

