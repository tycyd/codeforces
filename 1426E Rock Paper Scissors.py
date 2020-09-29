from sys import stdin, stdout


def update(a_a, b_a, i, j):
    v = min(a_a[i], b_a[j])
    a_a[i] -= v
    b_a[j] -= v


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

rounds = sum(a_a)

# max flow
#      A0 ---------> B0
#
#  S   A1 ---------> B1  S
#
#      A2 ---------> B2
#
#

res2 = min(a_a[0], b_a[1]) + min(a_a[1], b_a[2]) + min(a_a[2], b_a[0])

# a[0] -> b[0]
update(a_a, b_a, 0, 0)

print(a_a)
print(b_a)

# a[0] -> b[2]
update(a_a, b_a, 0, 2)

print(a_a)
print(b_a)

# a[1] -> b[0]
update(a_a, b_a, 1, 0)

print(a_a)
print(b_a)

# a[1] -> b[1]
update(a_a, b_a, 1, 1)

print(a_a)
print(b_a)

# a[2] -> b[1]
update(a_a, b_a, 2, 1)

print(a_a)
print(b_a)

# a[2] -> b[2]
update(a_a, b_a, 2, 2)

print(a_a)
print(b_a)

res1 = sum(b_a)

stdout.write(str(res1))
stdout.write(' ')
stdout.write(str(res2))
