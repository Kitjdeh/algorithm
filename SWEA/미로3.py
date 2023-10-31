import sys
sys.stdin = open('미로.txt')
def f(i,j,N):
    stack = []
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1                   #시작 정점 v
    while True:
        if maze[i][j]==3:
            return 1                    #방문 청리
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:       #v에 인전합 w 찾기 di:-1 dj :0
            ni ,nj = i+di, j +dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj] == 0:
                stack.append((i,j))
                i,j = ni, nj
                visited[i][j] = 1
                break
        else:                           #w가 없으면
            if stack:
                i,j = stack.pop()       #stack에 지나온 칸이 남은 경우
            else:
                break                   #스택이 비어있는 경우
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for __ in range(N)]
