from sys import stdin, stdout

# R S P R R P
# P R S P P S

# P P P
# S S S

# P P S
# S S R

if __name__ == '__main__':

    def universal_solution(s):
        n = len(s)
        R = P = S = 0
        for c in s:
            if c == 'R':
                R += 1
            elif c == 'P':
                P += 1
            else:
                S += 1

        if R >= P and R >= S:
            return ['P'] * n
        elif P >= R and P >= S:
            return ['S'] * n
        else:
            return ['R'] * n

    t = int(stdin.readline())

    for i in range(t):
        s = stdin.readline().strip()
        res = universal_solution(s)
        stdout.write("".join(res) + '\n')


