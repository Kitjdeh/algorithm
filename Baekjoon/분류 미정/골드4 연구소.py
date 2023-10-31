#1.세균들이 bfs로 최대한 번식을 마친 후에 남은 0의 갯수를 파악하는 함수를 만든다.
#2-1.세균들의 위치를 germ에 담는다.
#2-2.안전구역을 stack에 담는다.
#3.comb함수를 구현하여 nCr을 돌려서 벽3개를 만드는 모든 경우의 수를 구한다.
#4-1.각 경우의 수로 벽을 구현하였을 때
#4-2.bfs함수를 돌린 후 남은 안전구역의 갯수를 확인한다.
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

direction = [[1,0],[0,1],[-1,0],[0,-1]]
#1.세균들이 bfs로 최대한 번식을 마친 후에 남은 0의
#갯수를 파악하는 함수를 만든다.
def bfs(x,y):
    for di,dj in direction:
        ni,nj = x+di,y+dj
        if 0<=ni<N and 0<=nj<M and maze[ni][nj]==0:
            maze[ni][nj] = 2
            bfs(ni,nj)

def comb(arr,r):
    result = []
    if r ==1:
        for i in arr:
            result.append([i])
    elif r >1:
        for i in range(len(arr)-r+1):
            for j in comb(arr[i+1:],r-1):
                result.append([arr[i]] + j)
    return result

stack = []
germ = []
for i in range(N):
    for j in range(M):
        # 2-1.안전구역을 stack에 담는다.
        if arr[i][j] == 0:
            stack.append([i,j])
        # 2-2.세균들의 위치를 germ에 담는다.
        elif arr[i][j]== 2:
            germ.append([i,j])

#3.comb함수를 구현하여 nCr을 돌려서 벽3개를 만드는 모든 경우의 수를 구한다.
arr_comb = comb(stack,3)
L = len(arr_comb)
max_result = 0
for i in range(L):
    maze =[[]for _ in range(N)]
    for j in range(N):
        maze[j] = arr[j][:]

    for j in range(3):
# 4-1.각 경우의 수로 벽을 구현하였을 때
        maze[arr_comb[i][j][0]][arr_comb[i][j][1]] = 1
# 4-2.germ들을 bfs함수를 돌린 후 남은 안전구역의 갯수를 확인한다.
    for j in range(len(germ)):
        x,y = germ[j][0], germ[j][1]
        bfs(x,y)
    cnt = 0
    for j in range(N):
        for t in range(M):
            if maze[j][t]==0:
                cnt +=1
    if cnt > max_result:
        max_result = cnt
print(max_result)