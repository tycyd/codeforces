from sys import stdin, stdout


# case 1, if any a > s // 2, T win
# case 2, if s % 2 == 0, HL win
#   proof: After T choose one stone, total will be (s - 1) // 2.
#           Since s // 2 > (s - 1) // 2, HL has two choices:
#               if any pile has more than (s - 1) // 2, goto case 1, HL win
#               else remove one stone, then (s - 2) // 2. Since  (s - 1) // 2 = (s - 2) // 2, T cannot win
# case 3: if s % 2 == 1, T win
#   proof: after T remove one stone, goto case 2.
def stoned_game(n, a_a):
    s = sum(a_a)

    for a in a_a:
        if a > s//2:
            return 'T'

    if s % 2 == 0:
        return 'HL'
    else:
        return 'T'


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a_a = list(map(int, stdin.readline().split()))
    stdout.write(stoned_game(n, a_a) + '\n')

