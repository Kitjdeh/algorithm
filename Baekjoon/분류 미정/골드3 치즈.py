#1. 전체 arr 수령
#2. 치즈(1)의 좌표값들을 가지고 있는 cheese_list를 생성하여 저장한다.
#2-1. (0,0)에서  주변에 치즈가 있으면 0  을 -1로 하여 외부공간임을 구분
#3. cheese_list 전체를 순회하면 1시간 이걸린다 => for문 한번이 1시간
#4. cheese_list가 다 사라지면 끝이다. -> while cheese_list: 로 종료 시점 파악
#5. for문 안에서 cheese 한개의 좌표 x,y를 pop로 뽑아낸다.
#6. direction으로 확인
#6-1. 상온이 2개 이상이면 해당 x,y를  melt_list에 넣는다.
#6-2. 상온이 1개 이하이면 arr는 놔두고 다시 append한다.
#6-3. melt_list 의 arr[x][y] =0 으로 바꾼다.
#7. for 문 한개 끝날 경우 cnt +=1 한다.
#8. cnt 출력

from collections import deque

#2-1. (0,0)에서 dfs돌려서 주변에 치즈가 있으면 0  을 -1로 하여 외부공간임을 구분
def check(a,b):
    q = [[a,b]]
    arr[a][b] = -1
    while q:
        x,y = q.pop(0)
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
               arr[ni][nj] = -1
               q.append([ni,nj])

N,M = map(int,input().split())
direction = [[1,0],[0,1],[-1,0],[0,-1]]
visited = [[0]*M for i in range(N)]

                                        #1. 전체 arr 수령
arr = [[0]*M for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int,input().split()))
cheese_list=[]
                                        #2. 치즈(1)의 좌표값들을 가지고 있는 cheese_list를 생성하여 저장한다.
for i in range(N):
    for j in range(M):
        if arr[i][j] ==1:
            cheese_list.append([i,j])
cnt = 0
                                        #2-1. (0,0)에서 주변에 치즈가 있으면 0  을 -1로 하여 외부공간임을 구분
check(0,0)
                                        #4. cheese_list가 다 사라지면 끝이다.
                                        # -> while cheese_list: 로 종료 시점 파악
while cheese_list:
    L = len(cheese_list)
    melt_list=[]
                                        # 3. cheese_list 전체를 순회하면 1시간 이걸린다 => for문 한번이 1시간
    for i in range(L):
                                        # 5. for문 안에서 cheese 한개의 좌표 x,y를 pop로 뽑아낸다.
        x,y = cheese_list.popleft()
        temp = 0
                                        # 6. direction으로 확인
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == -1:
                temp +=1
        if temp >1:
                                        #6-1. 상온이 2개 이상이면 해당 x,y를  melt_list에 넣는다.
            melt_list.append([x,y])
        else:
                                        #6-2. 상온이 1개 이하이면 arr는 놔두고 다시 append한다.
            cheese_list.append([x,y])
                                        # 6-3. melt_list 의 arr[x][y] =-1 으로 바꾼다.
    for x,y in melt_list:
        check(x,y)                      # 외부공기 연결 여부 파악해야하니 check 함수돌림
                                        # 7. for 문 한개 끝날 경우 cnt +=1 한다.
    cnt +=1
print(cnt)