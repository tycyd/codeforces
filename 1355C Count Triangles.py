# b=3,c=6,d=6
# z区间 6
# y区间 3,4,5,6
# z-y差值如下
# 0,1,2,3
# 1,1,1,1相同数的数量统计
#
# b=3,c=6,d=7
# z区间 6,7
# y区间 3,4,5,6
# z-y差值如下
# 0,1,2,3
#   1,2,3,4
# 1,2,2,2,1相同数的数量统计
#
# b=3,c=6,d=8
# z区间 6,7,8
# y区间 3,4,5,6
# z-y差值如下
# 0,1,2,3
#   1,2,3,4
#     2,3,4,5
# 1,2,3,3,2,1相同数的数量统计

# 如a=1,b=3,c=6,d=11
# 构成三角形数量如下
# 枚举x区间1,2,3
# x=1,z-y小于1的数量有1
# x=2,z-y小于2的数量有3
# x=3,z-y小于3的数量有6
#
# 总的数量是1+3+6=10
def count_triangles(a, b, c, d):

    bc = c-b+1
    dc = d-c+1

    mx = min(bc, dc)
    l = -1
    r = d-b+1
    ttl = 0

    cnt = [0 for i in range(d+1)]

    while l<r:
        l+=1
        r-=1
        ttl+=1
        cnt[l] = min(ttl, mx)
        cnt[r] = cnt[l]

    sum = [0 for i in range(d + 1)]
    sum[0] = cnt[0]
    for i in range(1, d+1):
        sum[i] = sum[i - 1] + cnt[i]

    res = 0
    for i in range(a, b+1):
        res += sum[i-1]

    return res


#TLE
#O(N^2)
def count_triangles2(a, b, c, d):
    res = 0

    for i in range(c, d + 1):

        if a+b > i:
            res += (b-a+1)*(c-b+1)
            continue
        if b+c < i:
            break

        l = a
        h = c
        comb = 0

        while l <= b <= h:
            if l + h > i:
                comb += b - l + 1
                h -= 1
            else:
                l += 1

        res += comb

    return res


if __name__ == '__main__':
    abcd = input().split(' ')
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])

    res = count_triangles(a, b, c, d)
    print(res)
