import sys
sys.stdin = open("220923 디저트 카페.txt")
def f(start,d,result,num):
    global N
    global tc
    # if tc == 3 and start == [2, 2]:
    #     print(start, d, num)

    if d == 3 and start[0] == result[-1][0]+direction[d][0] and start[1] == result[-1][1]+direction[d][1]:        # if arr[start[0]][start[1]] not in result:
        # result.append(arr[start[0]][start[1]])
        # print(num,result,start)
        odd.append(len(num))

        return
    elif d == 2 and start[0] == result[-1][0]+direction[d+1][0] and start[1] == result[-1][1]+direction[d+1][1]:        # if arr[start[0]][start[1]] not in result:
        # result.append(arr[start[0]][start[1]])
        odd.append(len(num))
        return
    elif d<4:
        ni,nj = result[-1][0]+direction[d][0],result[-1][1]+direction[d][1]
        if d<4 and 0<=ni<N and 0<=nj<N and arr[ni][nj] not in num:
            result.append([ni,nj])
            num.append(arr[ni][nj])
            # print(tc, start,d,[ni,nj],result,num)
            f(start,d,result,num)
            f(start,d+1,result,num)

        elif 0<=ni<N and 0<=nj<N and arr[ni][nj] in result:
            return
        else:

            return
                # d = direction[i]
                # ni,nj = end[0]+d[0],end[1]+d[1]
                # if 0<ni<N and 0<nj<N and arr[ni][nj] not in result:
                #     result.append(arr[ni][nj])
                #     f(start,d,n+1,[ni,nj],result)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    direction = [[-1,1],[1,1],[1,-1],[-1,-1]]
    d = 0
    odd =[]
    for i in range(N):
        for j in range(N):
            f([i,j],0,[[i,j]],[arr[i][j]])
    max_lenght = 0
    # print(tc,odd)
    if len(odd)==0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(odd)}')


