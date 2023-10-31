# 물이 찰 예정인 칸으로 갈 수 없다 -> 이동 전에 물을 먼저 채운다.
# 현재 물이 찰 공간인 water에서 arr 값을 변경한다.
# 채운 공간을 temp_water에 넣었다가 끝나면 water 다시 한번에 넣는다.
# 나머지는 걍 bfs

from collections import deque
direction = [[0,1],[1,0],[0,-1],[-1,0]]
R,C = map(int,input().split())
arr = [[0]*C for _ in range(R)]
for i in range(R):
    arr[i] = list(input())
visited = [[0]*C for _ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            water.append([i,j])
        elif arr[i][j] =='D':
            X,Y = i,j
        elif arr[i][j] =='S':
            A,B = i,j
visited[A][B] = 0
q = [[A,B]]
while q:
    # 물부터 우선 채운다.
    water_temp = []
    while water:
        a,b = water.pop(0)
        for di,dj in direction:
            wi,wj = a+di,b+dj
            if 0<=wi<R and 0<=wj<C and (arr[wi][wj]=='S' or arr[wi][wj]=='.'):
                arr[wi][wj] ='*'
                water_temp.append([wi,wj])
    #지금 쓸 애들 집어 넣는다.
    temp = []
    while q:
        x,y = q.pop(0)
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0 <= ni< R and 0 <= nj < C and (arr[ni][nj]=='.' or arr[ni][nj]=='D' ) and visited[ni][nj]==0:
                visited[ni][nj] = visited[x][y]+1
                temp.append([ni,nj])
    if visited[X][Y] !=0:
        break
    else:
        water = water_temp[:]
        q = temp[:]
    # for i in range(R):
    #     print(visited[i],arr[i])
    # print('')
if visited[X][Y] !=0:
    print(visited[X][Y])
else:
    print('KAKTUS')