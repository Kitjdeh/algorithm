import sys
sys.stdin = open('미로.txt')
def f(i,j,N):
    stack = [(i,j)] #스택생성, 시작점 push
    visited = [[0]*N for i in range(N)]
    visited[i][j] = 1
    while stack:
        i,j = stack.pop()
        if maze[i][j] ==3:
            return 1
        for di, dj, in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i +di,j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj] == 0:
                stack.append((ni,nj))               # 방문한 칸 대신 갈수잇는 칸들을 스택에 push
                visited[ni][nj] = 1
    return 0
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j
T = int(input())
for tc in range(1,T+1):
    N=int(input())
    maze = [list(map(int,input())) for __ in range(N)]
    sti,stj = find_start(N)
    print(f'#{tc} {f(sti,stj,N)}')