# N: length of array
# S: required sum
# K: K or S-K , 2 10-2=8
# 1=>{4}, 2=>{1,3} {2,2} {3,1} 3=>{1,1,2} {1,2,1} {2,1,1}
# 6=>{1,1,4}   min:1   max:4  => 1 1 4
# 6=>{1 1 1 3} min:1   max:3
# 6=>{1 3 1 1} min:1   max:3
# 6=>{2 1 1 2} min:1   max:3
# 6=>{2 2 2}
# 8=>{1 1 6} 1~4
# 6=>{1 1 4} 1~3
# 1=>{1}
# 9=>{1 1 1 1 1 1 3}
# prove:
# S=>{1 1 1 1 1 X}  S/2
# if S/2 > N - 1, then "YES", let K=N
# if S/2 < N, then "NO" ?
# must exist 1, => 1, {1,1...1, S-N-1}
# must exist 1, => 1, {1,1...2, S-N-2}
# {1,2,2,2} S/2 = 3

def game_with_arry(N, S):

    ary = [1 for i in range(N)]
    ary[0] = S - N + 1

    if S//2 > N - 1:
        print("YES")
        print(*ary)
        print(N)
    else:
        print("NO")


if __name__ == '__main__':
    NS = input().split(' ')
    N = int(NS[0])
    S = int(NS[1])

    game_with_arry(N, S)
