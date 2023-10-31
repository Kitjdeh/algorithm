def bfs(N):
    global result
    visited[0][0] = 1
    #첫시작 0,0 부터
    q = []
    q.append([0,0])
    gram_d = 0
    #그람으로 벽뿌수고 간 시간
    while q:
        i,j = q.pop(0)
        #늘 하던 BFS
        if i == N and j ==M :
            break
        else:
            for di,dj in direction:
                ni,nj = i+di,j+dj
                if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and maze[ni][nj]==0:
                    visited[ni][nj]=1
                    d[ni][nj] = d[i][j]+1
                    #이전 칸 시간 +1
                    q.append([ni,nj])
                elif 0<=ni<N and 0<=nj<M and visited[ni][nj]==0and maze[ni][nj]==2:
                    #그람을 발견 할 경우
                    visited[ni][nj]=1
                    gram_d = d[i][j]+ (N-1-ni)+(M-1-nj)+1
                    #그동안 온거리 + 공주까지 직행거리
                    d[ni][nj]= d[i][j]+1
                    #그거랑 별개로 묵묵히 BFS
    if d[N-1][M-1] ==0 and gram_d ==0:
        #그람도 못가고 공주도 못구할경우
        result = 100000
        #INF
    else:
        if d[N-1][M-1] !=0:
            #BFS로도 가지고 그람으로도 가질 경우
            result = min(d[N-1][M-1],gram_d)
        else:
            #BFS로는 못가고 그람으로만 가질 경우
            result = gram_d
    return

N,M,T = map(int,input().split())
maze=[list(map(int,input().split())) for _ in range(N)]
visited =[[0]*M for _ in range(N)]
d = [[0]*M for _ in range(N)]
#각 칸까지 걸리는 거리 측정용
direction = [[-1,0],[1,0],[0,1],[0,-1]]
result = 0
bfs(N)
if result >T:
    print("Fail")
else:
    print(result)
