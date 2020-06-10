from sys import stdin, stdout


# game theory, nim
# if x already leaf, Ayush wins
# else only optimal move is to remove leaf which will not let x be leaf. (total count - 1)
#   whoever let x be the leaf after removing will lose (nim (total count - 1)%2)
#
#       4
#           6
#       1       5
#   3
#2
#       2
#   1
#3
def game_on_leaves(dic, x):

    if x not in dic or len(dic[x]) == 1:
        return "Ayush"

    #res = 0
    #for node in dic[x]:
    #    res ^= ((count_nodes(dic, node, x) + 1)) % 2
    res = (count_nodes(dic, x, -1) - 1)%2

    if res > 0:
        return "Ayush"
    else:
        return "Ashish"


def count_nodes(dic, node, parent):
    res = 0

    for i in dic[node]:
        if i != parent:
            res += count_nodes(dic, i, node)

    return res + 1


if __name__ == '__main__':

    t = int(stdin.readline())

    for i in range(t):
        dic = {}
        (n, x) = list(map(int, stdin.readline().split()))
        for j in range(n-1):
            (u, v) = list(map(int, stdin.readline().split()))
            if u not in dic:
                dic[u] = []
            if v not in dic:
                dic[v] = []
            dic[u].append(v)
            dic[v].append(u)

        stdout.write(str(game_on_leaves(dic, x)) + '\n')
