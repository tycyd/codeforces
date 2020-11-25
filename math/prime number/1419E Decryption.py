from sys import stdin, stdout

# 6
# 2 3 6

# 30
# 2,3,5
# 2 30 6 3 15 5 10
# 2 - (30) - 6 - 3 - 15 - 5 - 10
# P1 - (x*P1) - P1P2 - P2 - (x*P2) - P2P3 - P3 - (x*P3) - P1P3


def decryption(n):
    r1 = []
    r2 = 0

    factor_a = getfactor(n)
    prime_a = getprime(n)

    hs = set()
    prime_dic = {}

    #print(factor_a)
    #print(prime_a)

    for i in range(len(prime_a)):
        ni = (i+1)%len(prime_a)
        prime_dic[prime_a[i]] = []

        if (prime_a[i] * prime_a[ni]) not in hs:
            prime_dic[prime_a[i]].append(prime_a[i] * prime_a[ni])

        hs.add(prime_a[i])
        hs.add(prime_a[ni])
        hs.add(prime_a[i] * prime_a[ni])

    #print(prime_dic)
    # 2 4 7 14
    # special case for two prime numbers and factors > 3
    if len(factor_a) > 3 and len(prime_a) == 2:
        for fac in factor_a:
            if fac not in hs:
                p = getoneprime(fac)
                if p == prime_a[0]:
                    prime_dic[prime_a[0]] = []
                    prime_dic[prime_a[1]].append(prime_a[0] * prime_a[1])
                break

    for fac in factor_a:
        if fac in hs:
            continue

        p = getoneprime(fac)
        prime_dic[p].append(fac)
        hs.add(fac)

    for p in prime_dic:
        r1.append(p)
        prime_dic[p].reverse()
        for f in prime_dic[p]:
            r1.append(f)

    if len(factor_a) == 3 and len(prime_a) == 2:
        r2 = 1

    return [r1, r2]


def getfactor(n):

    factor_a = [n]
    i = 2
    while i*i < n:
        if n % i == 0:
            factor_a.append(i)
            factor_a.append(n//i)
        i += 1

    if i*i == n:
        factor_a.append(i)

    return factor_a


def getprime(n):

    prime_a = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            prime_a.append(i)
            while n % i == 0:
                n //= i
        i += 1

    if n > 1:
        prime_a.append(n)

    return prime_a


def getoneprime(n):

    i = 2
    while i*i <= n:
        if n % i == 0:
            return i
        i += 1

    return -1


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    res_a = decryption(n)
    stdout.write(' '.join(map(str, res_a[0])) + '\n')
    stdout.write(str(res_a[1]) + '\n')
