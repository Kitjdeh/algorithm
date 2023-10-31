def price(i,cost,visited):
    global result
    if i == N-1:
        if cost<result:
            result = cost
        return
    else:
        if cost >=result:                                       #이미 최솟값 넘기면 중단
            return
        else:
            for j in range(N):
                if visited[j] ==0:                              #만약 j공장을 방문 안했으면
                    visited[j] =1
                    price(i+1,cost+arr[i+1][j],visited)         #i+1번째로 j 공장
                    visited[j] = 0
                else:
                    pass
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = arr[0][0]*N*N
    visited = [0]*N
    for i in range(N):
        visited[i] =1
        price(0,arr[0][i],visited)
        visited[i] = 0
    print(f'#{tc} {result}')
