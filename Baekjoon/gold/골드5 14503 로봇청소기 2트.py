direction = {
    0:[-1,0],
    1:[0,1],
    2:[1,0],
    3:[0,-1]
}
dir_change = [3,0,1,2]

N, M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0
rotate = 0
while True:
    ni,nj = r+direction[d][0],c+direction[d][1]
    if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 0: #2-1상황
        rotate = 0
        r,c = ni,nj
        result +=1
        visited[r][c] = 1
        d = dir_change[d]
        rotate +=1
    elif ni<0 or ni==M or nj<0 or nj ==N:
        rotate += 1
        d = dir_change[d]
    elif 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 1 and rotate < 4:  # 2-2
        d = dir_change[d]
        rotate += 1
