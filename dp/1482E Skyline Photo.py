from sys import stdin, stdout


def skyline_photo(n, h_a, b_a):
    # idx, v include self, result
    st = []
    for i in range(n):
        h = h_a[i]
        b = b_a[i]

        v1 = b
        if len(st) > 0:
            v1 += st[-1][2]

        while len(st) > 0 and h_a[st[-1][0]] > h:
            cur = st.pop()
            v1 = max(v1, cur[1] - b_a[cur[0]] + b)

        if len(st) > 0:
            v1 = max(v1, st[-1][2] + b)
            v2 = max(v1, st[-1][2])
        else:
            v2 = v1

        st.append([i, v1, v2])

    return st[-1][2]


n = int(stdin.readline())
h_a = list(map(int, stdin.readline().split()))
b_a = list(map(int, stdin.readline().split()))

r = skyline_photo(n, h_a, b_a)
stdout.write(str(r))
