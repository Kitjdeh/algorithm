import sys
sys.stdin = open('BFS,DFS 미로찾기.txt')
def dfs(i,j,s,N):
    global cnt
    global minV
    if maze[i][j] ==3:
        cnt +=1
        if minV >s +1:
            minV = s +1
        return
    else:
        visited[i][j] =1
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni, nj = i+di,j+dj
            if maze[ni][nj] !=1 and visited[ni][nj]==0:     #벽으로 둘러 쌓여 있기때문에 범위 제한 안둬도 ㄱㅊ
                dfs(ni,nj,s+1,N)
        visited[i][j] =0                                    #다른 경로를 찾을 수 있도록 지워야함
        return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti  =-1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                sti,stj = i, j
                break
        if sti != -1:
            break
    cnt = 0             #경로의 수
    minV =0
    minV=N*N
    visited = [[0]*N for _ in range(N)]
    dfs(sti,stj,0,N)
    print(minV)

a=3
b=2
if a>b:
    print('a>b')
else:
