from sys import stdin, stdout


# if erased left elements >= (k-1)/2
#   and erased right elements >= (k-1)/2
#   and (n-m)%(k-1) == 0
# then YES
# Prove:
# set d = (k-1)/2
# left elements: d + x
# right elements: d + y
# ------------------------------------------
# if x + y >= k, set x + y = x + y - n*(k-1)
# then x + y < k
# ------------------------------------------
# because (2d + x + y) % (k-1) == 0,
# so x + y = k - 1
# ------------------------------------------
# d x b d y
# => d d-z b d d+z
# => d (d-z) b (z) d [d]
#
def k_and_medians(n, k, m, b_a):
    if (n-m) % (k-1) != 0:
        return False

    b_s = set(b_a)
    l_a = [0] * (n+1)
    for i in range(1, n+1):
        l_a[i] = l_a[i - 1]
        if i not in b_s:
            l_a[i] = l_a[i-1] + 1

    r = 0
    for i in range(n, 0, -1):
        if i not in b_s:
            r += 1
        elif r >= (k-1) // 2 and l_a[i] >= (k-1) // 2:
            return True

    return False


t = int(stdin.readline())
for _ in range(t):
    n, k, m = map(int, stdin.readline().split())
    b_a = list(map(int, stdin.readline().split()))
    r = k_and_medians(n, k, m, b_a)
    if r:
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')
