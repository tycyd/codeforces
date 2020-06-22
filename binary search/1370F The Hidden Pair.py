from sys import stdin, stdout

#       1
#   2       3
# 4 5 6   7   8

# 1. query all nodes to get min distance between hidden nodes.
# 2. root No.1 node, binary search for one hidden node.
# 3. get another hidden node at querying all nodes satisfy min distance.
if __name__ == '__main__':

    def get_all_nodes(n):
        res = []
        for i in range(n):
            res.append(i+1)
        return res

    def get_nodes(dic, r, d):
        visited = set()

        visited.add(r)
        queue = [r]

        while len(queue) > 0 and d > 0:
            n = len(queue)

            for i in range(n):
                cur = queue.pop(0)
                for nxt in dic[cur]:
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    queue.append(nxt)
            d -= 1

        return queue


    t = int(stdin.readline())

    for i in range(t):
        n = int(stdin.readline())
        dic = {}
        for j in range(n-1):
            u, v = map(int, stdin.readline().split())
            if u not in dic:
                dic[u] = []
            if v not in dic:
                dic[v] = []
            dic[u].append(v)
            dic[v].append(u)

        # 1
        cmd = get_all_nodes(n)
        stdout.write("? " + str(len(cmd)) + " " + " ".join(map(str, cmd)) + '\n')
        stdout.flush()

        r, d = map(int, stdin.readline().split())

        # 2
        node1 = -1
        l = d//2
        h = d

        while l < h:
            m = (l + h + 1) // 2
            cmd = get_nodes(dic, r, m)

            if len(cmd) == 0:
                h = m - 1
                continue

            stdout.write("? " + str(len(cmd)) + " " + " ".join(map(str, cmd)) + '\n')
            stdout.flush()

            s_n, s_d = map(int, stdin.readline().split())

            if d == s_d:
                node1 = s_n
                l = m
            else:
                h = m - 1

        if node1 == -1:
            cmd = get_nodes(dic, r, l)
            stdout.write("? " + str(len(cmd)) + " " + " ".join(map(str, cmd)) + '\n')
            stdout.flush()

            node1, s_d = map(int, stdin.readline().split())

        # 3
        node2 = 0
        cmd = get_nodes(dic, node1, d)
        stdout.write("? " + str(len(cmd)) + " " + " ".join(map(str, cmd)) + '\n')
        stdout.flush()

        node2, s_d = map(int, stdin.readline().split())

        stdout.write("! " + str(node1) + " " + str(node2) + '\n')
        stdout.flush()

        res = stdin.readline()
