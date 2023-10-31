#1.bfs(x,y)로 [x,y]에서 시작한 같은 영역을 visited처리
#2.[x,y]의 영역을 체크하면서 양의 수와 늑대의 수 체크
#3.양과 늑대 중 이긴 쪽의 숫자를 전체 값에 +

def bfs(x,y):
    global sheep
    global wolf
    if visited[x][y] == 1:
        return
    q = [[x,y]]
    s=0
    w=0
    while q:
        r,c = q.pop(0)
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = r+di,c+dj
            if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0 and arr[ni][nj] !='#':
                visited[ni][nj] =1
                if arr[ni][nj] == 'o':
                    s +=1
                elif arr[ni][nj] == 'v':
                    w +=1
                q.append([ni,nj])
    if s > w:
        sheep +=s
    else:
        wolf +=w

R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        bfs(i,j)
print(sheep,wolf)