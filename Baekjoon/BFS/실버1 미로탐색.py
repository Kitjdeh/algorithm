#bfs로 1,1에서 한칸씩 이동 -
#visited= 0 에서 +1 씩하면서 전진
# visited[N-1][M-1] 나오면 시마이
from collections import deque

direction=[[1,0],[-1,0],[0,1],[0,-1]]
N,M = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(input())
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1

q = deque()
q.append([0,0])
cnt = 0

while q:
    x,y = q.popleft()
    if x==N-1 and y==M-1:
        break
    else:
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '1' and visited[ni][nj] ==0:
                visited[ni][nj] = visited[x][y]+1
                q.append([ni,nj])
print(visited[N-1][M-1])