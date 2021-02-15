from sys import stdin, stdout

# 2 2
#  3  11
# 12   8
def multiples_and_power_differences(n, m, b_a):
    for i in range(1, n):
        for j in range


n, m = map(int, stdin.readline().split())
b_a = []
for _ in range(n):
    b_a.append(stdin.readline().split())
r_a = multiples_and_power_differences(n, m, b_a)
for r in range(r_a):
    stdout.print(' '.join(map(str, r)))
