from sys import stdin, stdout

#        +A
#    -B      -C
#  +D  +E  +F  +G
#
#    +A       +A
#    -B       -B -D
#    +C       +C
#   1 2 3 4 5 6
#   99 99
#   99
def three_bags(n1, n2, n3, a1_a, a2_a, a3_a):
    s1 = sum(a1_a)
    s2 = sum(a2_a)
    s3 = sum(a3_a)
    s = s1 + s2 + s3
    m1 = 1000000000
    m2 = 1000000000
    m3 = 1000000000
    for a1 in a1_a:
        m1 = min(m1, a1)

    for a2 in a2_a:
        m2 = min(m2, a2)

    for a3 in a3_a:
        m3 = min(m3, a3)

    m = min(m1 + m2, m1 + m3, m2 + m3, s1, s2, s3)
    return s - 2*m


n1, n2, n3 = map(int, stdin.readline().split())
a1_a = list(map(int, stdin.readline().split()))
a2_a = list(map(int, stdin.readline().split()))
a3_a = list(map(int, stdin.readline().split()))

res = three_bags(n1, n2, n3, a1_a, a2_a, a3_a)
stdout.write(str(res))