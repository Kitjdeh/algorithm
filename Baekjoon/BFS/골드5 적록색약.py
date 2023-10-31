#I. R-G-B 로 구분하는 함수 Color 함수, RG-B로 구분하는 함수 NonColor 함수
#2중 for문으로 Color[i][j] 진행
#1. 현재 색인 now_color들이 상하좌우에 있는 지 확인
#2. 있으면 visited처리 후 q에 append
#3. while q: 가 끝나면 cnt +=1
#4.Color(i,j)가 끝나면 arr[i][j]가 R이면 G로 바꿔 버림
#5.Color 순회 끝나면 nonColor 함수 진행 (R을 G로 바꿔나서 바로 가능)
def Color(x,y):
    global color_cnt
    if color_visited[x][y]:
        return
    else:
        now_color=arr[x][y]
        q = [[x,y]]
        while q:
            a,b = q.pop()
            for di,dj in direction:
                ni,nj = a+di,b+dj
                if 0<=ni<N and 0<=nj<N and color_visited[ni][nj]==0 and arr[ni][nj] == now_color:
                    color_visited[ni][nj] = 1
                    q.append([ni,nj])
        color_cnt +=1
def NonColor(x,y):
    global noncolor_cnt
    if noncolor_visited[x][y]:
        return
    else:
        now_color=arr[x][y]
        q = [[x,y]]
        while q:
            a,b = q.pop()
            for di,dj in direction:
                ni,nj = a+di,b+dj
                if 0<=ni<N and 0<=nj<N and noncolor_visited[ni][nj]==0 and arr[ni][nj] == now_color:
                    noncolor_visited[ni][nj] = 1
                    q.append([ni,nj])
        noncolor_cnt +=1




direction =[[1,0],[-1,0],[0,1],[0,-1]]
N = int(input())
arr = [list(input())for _ in range(N)]
color_visited = [[0]*N for _ in range(N)]
noncolor_visited=[[0]*N for _ in range(N)]
color_cnt = 0
noncolor_cnt = 0
for i in range(N):
    for j in range(N):
        Color(i,j)
        if arr[i][j] =='R':
            arr[i][j] = 'G'

for i in range(N):
    for j in range(N):
        NonColor(i,j)
print(color_cnt,noncolor_cnt)


