from sys import stdin, stdout


# lcm(a,b) = a*b/gcd(a,b)
# c*lcm(a,b) - d*gcd(a,b) = x
#   =>  c*a*b/gcd(a,b) - d*gcd(a,b) = x
#       c*a*b/g^2 - d = x/g
#       =>  a=A*g, b=B*g, A and B co-prime
#           c*A*B = x + d*g
#           A*B = (x/g + d)/c
#           => since gcd(A,B) = 1, then res = 2^(count of prime factors)
def the_number_of_pairs(c, d, x):
    r = 0
    g = 1
    while g*g <= x:
        if x % g != 0:
            g += 1
            continue
        k = x // g + d
        if k % c == 0:
            r += 1 << val[k//c]

        if g*g == x:
            g += 1
            continue

        k2 = g + d
        if k2 % c == 0:
            r += 1 << val[k2//c]
        g += 1

    return r


t = int(stdin.readline())
# prime factors array
MAX = 2 * (10 ** 7)
# MAX = 10
mind = [-1 for _ in range(MAX)]
for i in range(2, MAX):
    if mind[i] != -1:
        continue
    for j in range(i, MAX, i):
        if mind[j] != -1:
            continue
        mind[j] = i

val = [0] * MAX
for i in range(2, MAX):
    j = i // mind[i]
    val[i] = val[j]
    if mind[i] != mind[j]:
        val[i] += 1

# print(mind)
# print(val)

for _ in range(t):
    c, d, x = map(int, stdin.readline().split())
    r = the_number_of_pairs(c, d, x)
    stdout.write(str(r) + '\n')
