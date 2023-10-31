#고슴도치가 이동 할 수 없는 경우
#   - 물이 이미 차있는 곳, 물이 차오를 예정인 곳
#비버가 한칸 이동하는 경우 <-> 물이 한칸씩 차오르는 경우
#즉 비버가 움직이려는 칸의 상하좌우에 *가 있으면 안된다.
#1. bfs방식으로 비버가 움직이게 해야함
#   - 움직이려는 칸 주변에 물이 없어야함
#2. 물은 bfs방식으로 그냥 차오름

dir = [[0,1],[1,0],[-1,0],[0,-1]]
R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
q =[]
water =[]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            q = [[i,j]]
        if arr[i][j] == '*':
            water.append([i,j])
        if arr[i][j] == 'D':
            Ex,Ey = i,j
    if q and water:
        break
# print(S)
def bfs(cnt):
    tmp =[]
    for i,j in water:
        for di,dj in dir:
            ni,nj = i+di,j+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] != '*':
                arr[i][j] = '*'
                tmp.append([i,j])
    water = tmp[:]
    temp = []
    for x,y in q:
        for di,dj in dir:
            ni,nj = x+di,y+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] != '*':
                visited[ni][nj] = cnt
