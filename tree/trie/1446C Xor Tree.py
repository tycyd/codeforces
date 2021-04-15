from sys import stdin, stdout


class TrieNode:
    def __init__(self):
        self.next_nodes = [None for i in range(2)]
        self.count = 0

def xor_tree(n, a_a):
    root = TrieNode()

    for a in a_a:
        cur = root
        for k in range(29, -1, -1):
            cur.count += 1

            v = (a >> k) & 1
            if cur.next_nodes[v] is None:
                cur.next_nodes[v] = TrieNode()
            cur = cur.next_nodes[v]
        cur.count += 1

    res_a = dfs(root)
    return res_a[1]


# out1: count of elements in the tree
# out2: count of elements need to be removed to form the tree
def dfs(root):
    if root is None:
        return [0, 0]

    if root.count <= 3:
        return [root.count, 0]

    res_a = [0, 0]
    l_a = dfs(root.next_nodes[0])
    r_a = dfs(root.next_nodes[1])

    removeCnt = 0
    if l_a[0] >= 2 and r_a[0] >= 2:
        removeCnt = min(l_a[0], r_a[0]) - 1

    res_a[0] = l_a[0] + r_a[0] - removeCnt
    res_a[1] = l_a[1] + r_a[1] + removeCnt

    return res_a


def xor_tree2(n, a_a):
    root = [[None, None], 0]

    for a in a_a:
        cur = root
        for k in range(29, -1, -1):
            cur[1] += 1

            v = (a >> k) & 1
            if cur[0][v] is None:
                cur[0][v] = [[None, None], 0]
            cur = cur[0][v]
        cur[1] += 1

    #res_a = dfs2(root)

    # node, rtn, left, right
    res = 0
    st = [[root, None, None, None]]
    while len(st) > 0:
        cur = st[-1]
        if cur[1] is None:
            if cur[0] is None:
                cur[1] = [0, 0]
            elif cur[0][1] <= 3:
                cur[1] = [cur[0][1], 0]
            else:
                if cur[2] is None:
                    st.append([cur[0][0][0], None, None, None])
                elif cur[3] is None:
                    st.append([cur[0][0][1], None, None, None])
        else:
            cur = st.pop()
            if len(st) == 0:
                res = cur[1][1]
                break

            pre = st[-1]
            rtn = cur[1]

            if pre[2] is None:
                pre[2] = rtn
            elif pre[3] is None:
                pre[3] = rtn

                res_a = [0, 0]
                l_a = pre[2]
                r_a = pre[3]
                removeCnt = 0
                if l_a[0] >= 2 and r_a[0] >= 2:
                    removeCnt = min(l_a[0], r_a[0]) - 1

                res_a[0] = l_a[0] + r_a[0] - removeCnt
                res_a[1] = l_a[1] + r_a[1] + removeCnt

                pre[1] = res_a

    return res


def dfs2(root):
    if root is None:
        return [0, 0]

    if root[1] <= 3:
        return [root[1], 0]

    res_a = [0, 0]
    l_a = dfs2(root[0][0])
    r_a = dfs2(root[0][1])

    removeCnt = 0
    if l_a[0] >= 2 and r_a[0] >= 2:
        removeCnt = min(l_a[0], r_a[0]) - 1

    res_a[0] = l_a[0] + r_a[0] - removeCnt
    res_a[1] = l_a[1] + r_a[1] + removeCnt

    return res_a


n = int(stdin.readline())
a_a = list(map(int, stdin.readline().split()))
r = xor_tree2(n, a_a)
stdout.write(str(r))
