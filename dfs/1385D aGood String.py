from sys import stdin, stdout

# 2**17
# 8
# bbaaddcc
# aaaabbcd
# aaaa
#     aaaa
# bb
#   bb
#     bb
#       bb
# dc
if __name__ == '__main__':

    def a_good_string(n, s):
        ans = dfs(s, 0, n-1, 'a')
        return ans

    def dfs(s, b, e, c):
        if b == e:
            if s[b] == c:
                return 0
            else:
                return 1

        m = (b+e)//2
        cnt1 = 0
        cnt2 = 0

        for i in range(b, m+1):
            if s[i] != c:
                cnt1 += 1

        for i in range(m+1, e+1):
            if s[i] != c:
                cnt2 += 1

        #print('-----')
        #print(c)
        #print(cnt1)
        #print(cnt2)

        ans1 = cnt1 + dfs(s, m+1, e, chr(ord(c) + 1))
        ans2 = cnt2 + dfs(s, b, m, chr(ord(c) + 1))

        return min(ans1, ans2)


    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        s = stdin.readline().strip()
        ans = a_good_string(n, s)
        stdout.write(str(ans) + '\n')

