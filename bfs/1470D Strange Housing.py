from sys import stdin, stdout


def strange_housing(n, m, uv_d):
    c_a = [-1] * (n + 1)
    st = [1]

    while len(st) > 0:
        c = st.pop()
        if c_a[c] != -1:
            continue

        c_a[c] = 1
        s = set()
        if c in uv_d:
            for nc in uv_d[c]:
                if c_a[nc] == -1:
                    c_a[nc] = 0
                    s.add(nc)

        for nc in s:
            if nc in uv_d:
                for nnc in uv_d[nc]:
                    if c_a[nnc] == -1:
                        st.append(nnc)

    r = []
    for i in range(1, n+1):
        if c_a[i] == -1:
            return ['NO']
        elif c_a[i] == 1:
            r.append(i)
    return ['YES', len(r), r]


t = int(stdin.readline())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    uv_d = {}
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        if u not in uv_d:
            uv_d[u] = []
        if v not in uv_d:
            uv_d[v] = []
        uv_d[u].append(v)
        uv_d[v].append(u)
    r = strange_housing(n, m, uv_d)
    stdout.write(r[0] + '\n')
    if len(r) > 1:
        stdout.write(str(r[1]) + '\n')
        stdout.write(' '.join(map(str, r[2])) + '\n')
