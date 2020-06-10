from sys import stdin, stdout


# #B.
# #..
# GG.
def solve_the_maze(maze, n, m):

    dir = [[1,0], [-1,0], [0, 1], [0, -1]]

    # no B, G close to each other
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'B':
                for d in dir:
                    di = i + d[0]
                    dj = j + d[1]
                    if 0 <= di < n and 0 <= dj < m:
                        if maze[di][dj] == 'G':
                            return "NO"
                        elif maze[di][dj] == '.':
                            maze[di][dj] = '#'

    # union find G
    ufa = [0 for i in range(m*n)]
    for i in range(len(ufa)):
        ufa[i] = i

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if maze[i][j] == '#':
                continue

            # right
            if j+1 < m and maze[i][j+1] != '#':
                union(ufa, m*i + j, m*i + j + 1)

            # left
            if i+1 < n and maze[i+1][j] != '#':
                union(ufa, m*i + j, m * (i+1) + j)

    #print(ufa)

    # check if all G belongs to same group
    root = ufind(ufa, n*m-1)
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                grp = ufind(ufa, i*m+j)
                if grp != root:
                    return "NO"

    return "YES"


# assign a root to b
def union(ufa, a, b):
    ar = ufind(ufa, a)
    br = ufind(ufa, b)

    ufa[br] = ar


def ufind(ufa, a):
    if ufa[a] == a:
        return a

    ufa[a] = ufind(ufa, ufa[a])
    return ufa[a]


if __name__ == '__main__':
    t = int(stdin.readline())

    for i in range(t):
        (n, m) = list(map(int, stdin.readline().split()))
        maze = []
        for i in range(n):
            maze.append(list(stdin.readline().strip()))

        if i == 62:
            print(maze)

        stdout.write(solve_the_maze(maze, n, m) + '\n')
