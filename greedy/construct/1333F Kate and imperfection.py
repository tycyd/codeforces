from sys import stdin, stdout


# pick prime numbers first, then factors 2, 3, 4
# {1,2,3,5}
# pick 4,8,16 => 2, pick 6,9,12 => 3, pick 10,15,20 => 5
n = int(stdin.readline())
s_a = [1 for _ in range(n+1)]
for i in range(2, n):
    for j in range(i*2, n+1, i):
        s_a[j] = i
s_a.sort()
s_a.pop(0)
s_a.pop(0)

stdout.write(' '.join(map(str, s_a)))
