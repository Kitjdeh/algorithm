# 누적으로 가장 최소 값 -> bfs

dir = [[0,1],[1,0],[-1,0],[0,-1]]
def bfs(n):
    q = [[0,0]]
    while q:
        x,y = q.pop(0)
        for di,dj in dir:
            ni,nj = x+di,y+dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == 0 or D[ni][nj] > D[x][y] + arr[ni][nj]:
                    visited[ni][nj] =1
                    D[ni][nj] = D[x][y] + arr[ni][nj]
                    q.append([ni,nj])
    return D[n-1][n-1]
N = 1
cnt = 1
while N!=0:
    N = int(input())
    if N == 0:
        break
    arr =[0]*N
    visited = [[0]*N for _ in range(N)]
    D = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int,input().split()))
    D[0][0] = arr[0][0]
    visited[0][0]= 1
    print(f"Problem {cnt}: {bfs(N)}")
    cnt +=1

