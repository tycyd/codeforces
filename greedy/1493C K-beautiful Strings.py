from sys import stdin, stdout


def k_beautiful_strings(n, k, s):
    if n % k != 0:
        return '-1'

    cnt_a = [0] * 26
    for c in s:
        cnt_a[ord(c) - ord('a')] += 1
    need = calc_need(cnt_a, k)
    if need == 0:
        return s

    for i in range(n-1, -1, -1):
        # update need
        need += delta_need(cnt_a, ord(s[i]) - ord('a'), k, -1)
        cnt_a[ord(s[i]) - ord('a')] -= 1

        slots = n - i - 1
        for j in range(ord(s[i])-ord('a')+1, 26):
            cnt = delta_need(cnt_a, j, k, 1)
            need += cnt

            if need <= slots:
                cnt_a[j] += 1

                # found
                suffix = []
                for _ in range(need, slots):
                    suffix.append('a')
                for z in range(0, 26):
                    cn = (k - cnt_a[z] % k) % k
                    for _ in range(cn):
                        suffix.append(chr(z + ord('a')))
                return s[:i] + chr(j + ord('a')) + ''.join(suffix)

            need -= cnt

    return '-1'


def delta_need(cnt_a, i, k, d):
    delta = 0
    delta -= (k - cnt_a[i] % k) % k
    delta += (k - (cnt_a[i]+d) % k) % k
    return delta


def calc_need(cnt_a, k):
    need = 0
    for cnt in cnt_a:
        need += (k - cnt % k) % k
    return need


T = int(stdin.readline())
for _ in range(T):
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    r = k_beautiful_strings(n, k, s)
    stdout.write(r + '\n')
