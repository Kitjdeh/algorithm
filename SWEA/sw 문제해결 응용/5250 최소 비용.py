def dijkstra(N,X,d):
    min_V=100000000
#[1,0]과[0,1]중 한개는 무조건 지나가야 하니 작은 값 한개를 선정하여 계산
    # if arr[0][1] > arr[1][0]:
    #     d[1][0] = arr[1][0]-arr[0][0]+1
    # elif arr[1][0] > arr[0][1]:
    #     d[0][1] = arr[0][1]-arr[0][0]+1
    # else:
    #     d[0][1],d[1][0] = arr[0][1]-arr[0][0]+1,arr[0][1]-arr[0][0]+1
    U = [[0]*N for _ in range(N)]
    d[0][0] =0
    U[0][0] =1
    while U[N-1][N-1] ==0:
        for i in range(N):
            for j in range(N):
                if minV>D[i][j]:
                    minV = D[i][j]
                    wi,wj = i,j
        Ch=[]
        U[wi][wj] = 1
        for di,dj in [[-1,0],[0,-1],[1,0],[0,1]]:
            ni,nj = wi+di,wj+dj
            if 0<=ni<N and 0<=nj<N and (U[ni][nj] ==0):
                Ch.append([ni,nj])
        #최솟값을 찾아야 하니 append한 Ch에서 arr 값과 x,y 합(=이동거리)계산
        w = Ch[0]
        for x,y in Ch:
            if arr[x][y]+x+y <= arr[w[0]][w[1]]+w[0]+w[1]:
                w = [x,y]
        U[w[0]][w[1]] =1
        for di,dj in [[-1,0],[0,-1],[1,0],[0,1]]:
            ni,nj = w[0]+di,w[1]+dj
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] > arr[w[0]][w[1]]:
                    d[ni][nj] =min(d[ni][nj],d[w[0]][w[1]]+arr[ni][nj]-arr[w[0]][w[1]]+1)
                else:
                    d[ni][nj] =min(d[ni][nj],d[w[0]][w[1]]+1)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= [list(map(int,input().split())) for _ in range(N)]
    dout = [[10000]*N for _ in range(N)]
    dijkstra(N, [0,0], dout)
    print(f'#{tc} {dout[N-1][N-1]}')
    for i in range(N):
        print(dout[i])