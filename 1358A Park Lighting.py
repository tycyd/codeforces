from sys import stdin, stdout


def park_lighting(n, m):
    return n*m//2 + n*m%2


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        nm = list(map(int, stdin.readline().split()))

        stdout.write(str(park_lighting(nm[0], nm[1])) + '\n')
