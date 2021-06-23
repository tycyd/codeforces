from sys import stdin, stdout
import heapq


MAX = 2000001
dic = {}
#dic2 = {}
s = set()
hq = []
n, m, k = map(int, stdin.readline().split())
for _ in range(m):
    x, y, w = map(int, stdin.readline().split())
    if x not in dic:
        dic[x] = []
    if y not in dic:
        dic[y] = []
    dic[x].append([y, w])
    dic[y].append([x, w])
    heapq.heappush(hq, [w, x, y])
    #dic2[x + y*MAX] = w
    # dic2[y + x*MAX] = w
    #dic2[x + x * MAX] = 0
    #dic2[y + y * MAX] = 0
    s.add(x + x*MAX)
    s.add(y + y * MAX)


cw = cx = cy = 0
for _ in range(k):
    #while (hq[0][1] + hq[0][2] * MAX) in dic2 or (hq[0][2] + hq[0][1] * MAX) in dic2:
    while (hq[0][1] + hq[0][2] * MAX) in s:
        heapq.heappop(hq)
    [cw, cx, cy] = heapq.heappop(hq)

    s.add(cx + cy * MAX)
    s.add(cy + cx * MAX)
    #dic2[cx + cy * MAX] = cw
    #s.add(cx + cy * MAX)
    #s.add(cy + cx * MAX)

    for nxt in dic[cx]:
        nw = cw + nxt[1]
        k = cy + nxt[0] * MAX
        #if (k not in dic2 or dic2[k] > nw) or ((nxt[0] + cy * MAX) not in dic2 or dic2[nxt[0] + cy * MAX] > nw):
        #    heapq.heappush(hq, [nw, cy, nxt[0]])
        #    dic2[cy + nxt[0] * MAX] = nw
            #dic2[nxt[0] + cy * MAX] = nw
        if k not in s:
            heapq.heappush(hq, [nw, cy, nxt[0]])

    for nxt in dic[cy]:
        nw = cw + nxt[1]
        k = cx + nxt[0] * MAX
        #if (k not in dic2 or dic2[k] > nw) or ((nxt[0] + cx * MAX) not in dic2 or dic2[nxt[0] + cx * MAX] > nw):
        #    heapq.heappush(hq, [nw, cx, nxt[0]])
        #    dic2[cx + nxt[0] * MAX] = nw
            #dic2[nxt[0] + cx * MAX] = nw
        if k not in s:
            heapq.heappush(hq, [nw, cx, nxt[0]])

stdout.write(str(cw))
