from sys import stdin, stdout


class Node:
    def __init__(self, a, c):
        self.jump = [None] * 20
        self.a = a
        self.c = c

    def ac(self):
        return self.a * self.c

    def link(self, p_node):
        for i in range(0, 20):
            self.jump[i] = p_node
            if p_node is None:
                break
            p_node = p_node.jump[i]

    def find(self):
        for i in range(19, -1, -1):
            if self.jump[i] is not None and self.jump[i].a > 0:
                return self.jump[i].find()
        return self


def addNode(dic, r, p, a, c):
    dic[r] = Node(a, c)
    dic[r].link(dic[p])


def solve(dic, v, w):
    r1 = 0
    r2 = 0
    preNode = None
    node = dic[v].find()
    while node is not preNode and w > 0 and 0 < node.a <= w:
        w -= node.a
        r1 += node.a
        r2 += node.ac()
        node.a = 0
        preNode = node
        node = dic[v].find()

    if node.a > 0 and node is not preNode:
        r1 += w
        r2 += w * node.c
        node.a -= w

    return [r1, r2]


dic = {}
q, a, c = map(int, stdin.readline().split())

dic[0] = Node(a, c)
for i in range(1, q + 1):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 1:
        # addNode(dic, i, cmd[1], cmd[2], cmd[3])
        dic[i] = Node(cmd[2], cmd[3])
        dic[i].link(dic[cmd[1]])
    else:
        res = solve(dic, cmd[1], cmd[2])
        stdout.write(str(res[0]) + ' ' + str(res[1]) + '\n')
        stdout.flush()
