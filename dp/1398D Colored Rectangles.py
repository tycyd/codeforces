from sys import stdin, stdout


# 1 2 3 4
# 5
# 5
def colored_rectangels(R, G, B, R_a, G_a, B_a):

    R += 1
    G += 1
    B += 1
    R_a.append(0)
    G_a.append(0)
    B_a.append(0)

    R_a.sort()
    G_a.sort()
    B_a.sort()

    dp = [[[0 for _ in range(B)] for _ in range(G)] for _ in range(R)]
    for i in range(0, R):
        for j in range(0, G):
            for k in range(0, B):
                r1 = r2 = r3 = 0

                if i > 0 and j > 0:
                    r1 = dp[i-1][j-1][k] + R_a[i]*G_a[j]
                if j > 0 and k > 0:
                    r2 = dp[i][j-1][k-1] + G_a[j]*B_a[k]
                if i > 0 and k > 0:
                    r3 = dp[i-1][j][k-1] + R_a[i]*B_a[k]
                dp[i][j][k] = max(r1, r2, r3)
                #print(dp)

    return dp[R-1][G-1][B-1]


R, G, B = map(int, stdin.readline().split())
R_a = list(map(int, stdin.readline().split()))
G_a = list(map(int, stdin.readline().split()))
B_a = list(map(int, stdin.readline().split()))

stdout.write(str(colored_rectangels(R, G, B, R_a, G_a, B_a)))