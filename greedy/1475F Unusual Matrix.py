from sys import stdin, stdout


# 110
# 001
# 110
#
# 000
# 000
# 000
def unusual_matrix(n, m_a, m_b):
    for i in range(n):
        if m_a[i][0] != m_b[i][0]:
            for j in range(n):
                m_a[i][j] ^= 1

    for j in range(n):
        if m_a[0][j] != m_b[0][j]:
            for i in range(n):
                m_a[i][j] ^= 1

    for i in range(n):
        for j in range(n):
            if m_a[i][j] != m_b[i][j]:
                return 'NO'
    return 'YES'


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    m_a = []
    m_b = []
    for _ in range(n):
        m_a.append(list(map(int, stdin.readline().strip())))
    stdin.readline()
    for _ in range(n):
        m_b.append(list(map(int, stdin.readline().strip())))

    r = unusual_matrix(n, m_a, m_b)
    stdout.write(r + '\n')
