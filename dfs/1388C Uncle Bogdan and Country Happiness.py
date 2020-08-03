import collections,sys,threading
sys.setrecursionlimit(10**4)
threading.stack_size(32*1024)

from sys import stdin, stdout
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


# dfs
def uncle_bogdan_and_country_happiness(n, m, p_a, h_a, xy_dic):

    ans = dfs(-1, 0, p_a, h_a, xy_dic)
    #ans = dfs2(-1, 0, p_a, h_a, xy_dic)

    return ans[0]

@bootstrap
def dfs2(pcity, city, p_a, h_a, xy_dic):

    people = p_a[city]
    sub_bad_mood = 0
    sub_people = 0

    if city in xy_dic:
        for ncity in xy_dic[city]:
            if pcity != ncity:
                subans = yield dfs(city, ncity, p_a, h_a, xy_dic)

                if not subans[0]:
                    yield [False, None, None]
                sub_people += subans[1]
                sub_bad_mood += subans[2]

    people += sub_people
    bad_mood = (people - h_a[city]) // 2

    if (people - h_a[city]) % 2 == 1 or h_a[city] > people or bad_mood > (sub_bad_mood + p_a[city]):
        yield [False, None, None]

    yield [True, people, bad_mood]


def dfs(pcity, city, p_a, h_a, xy_dic):

    people = p_a[city]
    sub_bad_mood = 0
    sub_people = 0

    if city in xy_dic:
        for ncity in xy_dic[city]:
            if pcity != ncity:
                subans = dfs(city, ncity, p_a, h_a, xy_dic)

                if not subans[0]:
                    return [False, None, None]
                sub_people += subans[1]
                sub_bad_mood += subans[2]

    people += sub_people
    bad_mood = (people - h_a[city]) // 2

    if (people - h_a[city]) % 2 == 1 or h_a[city] > people or bad_mood > (sub_bad_mood + p_a[city]):
        return [False, None, None]

    return [True, people, bad_mood]


def solve():
    t = int(stdin.readline())
    for i in range(t):
        n, m = map(int, stdin.readline().split())
        p_a = list(map(int, stdin.readline().split()))
        h_a = list(map(int, stdin.readline().split()))
        xy_dic = {}

        for _ in range(n-1):
            x, y = map(int, stdin.readline().split())
            x -= 1
            y -= 1
            if x not in xy_dic:
                xy_dic[x] = []
            if y not in xy_dic:
                xy_dic[y] = []
            xy_dic[x].append(y)
            xy_dic[y].append(x)

        ans = uncle_bogdan_and_country_happiness(n, m, p_a, h_a, xy_dic)
        if ans:
            stdout.write('YES\n')
        else:
            stdout.write('NO\n')

threading.Thread(target=solve).start()
