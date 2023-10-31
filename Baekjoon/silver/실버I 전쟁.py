def bfs(i,j,N):
    visited = [[0]*N for _ in range(M)]#vistied 생성
    q =[]
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i +di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] == 'W' and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] +1
    return 0
N,M = map(int,input())
arr = [list(input().split() for _ in range(M))
