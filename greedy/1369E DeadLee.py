from sys import stdin, stdout

# 3 3
# 1 2 1
# 1 1 1
# 1 2
# 2 3
# 1 3
#
#  2  2  2
# -1  0 -1
#
# 1,3,2
#
# 4 4
# 1 2 0 1
# 1 3
# 1 2
# 2 3
# 2 4
# 2 3 2 1
# ALIVE
# 1 3 2 4
#
# define s = number of friends who like food i. if s > w then no answer exist
# proof contradiction: last person, s=1, if s >= w, there is an answer, then w should >=1, which is not true
# w: 1 2 1
# s: 2 2 2
#
if __name__ == '__main__':

    def dead_lee(n, m, w, xy, s):
        queue = []
        for i in range(n):
            if w[i] >= len(s[i]):
                queue.append(i)

        #print(w)
        #print(xy)
        #print(s)
        #print(queue)

        pl = []
        while len(queue) > 0:
            cur = queue.pop()
            w[cur] = 0
            for i in s[cur]:
                pl.append(i+1)
                if xy[i][0] != cur:
                    s[xy[i][0]].remove(i)
                    if w[xy[i][0]] == len(s[xy[i][0]]) and w[xy[i][0]] > 0:
                        queue.append(xy[i][0])
                else:
                    #print("-------------")
                    #print(cur)
                    #print(s[xy[i][1]])
                    #print(i)
                    s[xy[i][1]].remove(i)
                    if w[xy[i][1]] == len(s[xy[i][1]]) and w[xy[i][1]] > 0:
                        queue.append(xy[i][1])

        if len(pl) == m:
            pl.reverse()
            return ["ALIVE", pl]
        else:
            return ["DEAD"]


    n, m = map(int, stdin.readline().split())
    w = list(map(int, stdin.readline().split()))
    xy = [None for i in range(m)]
    s = [set() for i in range(n)]
    for i in range(m):
        xy[i] = list(map(int, stdin.readline().split()))
        xy[i][0] -= 1
        xy[i][1] -= 1

        s[xy[i][0]].add(i)
        s[xy[i][1]].add(i)

    res = dead_lee(n, m, w, xy, s)
    stdout.write(res[0] + '\n')
    if len(res) > 1:
        stdout.write(" ".join(map(str, res[1])) + '\n')
