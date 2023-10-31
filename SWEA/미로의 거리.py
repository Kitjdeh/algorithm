import sys
sys.stdin = open('미로의 거리.txt')
def dfs(i,j,s):
    global dep
    global cnt
    if maze[i][j] == 3:
        cnt +=1
        if s*1<dep:
            dep = s-1
        return

    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni, nj = i +di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] ==0 and maze[ni][nj] !=1:
                dfs(ni,nj,s+1)
        visited[i][j] = 0

        return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti = -1
    stj = -1
    cnt = 0
    dep = N*N
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti,stj = i,j   ##시작점 2 인 점의 좌표 sti, stj를 주어 준다

        if sti != -1:
            break
    visited = [[0]*N for _ in range(N)]
    dfs(sti,stj,0)
    if cnt>0:
        print(f'#{tc} {dep}')
    else:
        print(f'#{tc} 0')