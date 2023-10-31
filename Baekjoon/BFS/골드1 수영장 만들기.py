#모든 벽의 높이는 1~9이다.
#높이가 h일때 수영장을 만들 수 있는지 확인하는 swim(h)함수를 만든다.
# - swim(h)
# 1. [0,0]~[N-1,M-1] 까지 순회하며 h와 같거나 높으면 0 으로 아니면 arr[x][y]값 그대로 체크하는 pool을 그린다.
# 2. visited를 새로 그린다.
# 3. [1,1] 부터 근접한 곳들을 BFS로 다 확인한다.
#   3-1. 만약 [x,y]에서 x나 y중 하나라도 0이 나오면 즉시 종료
#   3-2. 0이 아니면 해당 높이를 계속 temp에 + 한다.
#   3-3. 0을 만나지 않고 종료하면 result에 넣는다.
def swim(h):
    global result
    global N
    global M
    pool = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    h_ch = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >=h:
                pool[i][j] = 1
                h_ch=1
            else:
                pool[i][j] = 0
    if h_ch ==0:
        return
    for i in range(1,N-1):
        for j in range(1,M-1):
            if pool[i][j] == 0 and visited[i][j] == 0:
                temp =0
                q = [[i,j]]
                ch =1
                visited[i][j] =1
                while q:
                    x,y = q.pop(0)
                    if x==0 or y == 0 or x==N-1 or y ==M-1:
                        ch = 0
                        break
                    else:
                        temp += 1
                        for di,dj in direction:
                            ni,nj = x+di,y+dj
                            if 0<=ni<N-1 and 0<=nj<M-1 and visited[ni][nj] ==0 and pool[ni][nj] ==0:
                                visited[ni][nj] =1
                                q.append([ni,nj])
                if ch ==1:
                    result +=temp
                    for i in range(N):
                        print(visited[i],temp)
                    print()
                    for i in range(N):
                        print(pool[i])
                    print(h,result,temp)
direction = [[1,0],[0,1],[-1,0],[0,-1]]
N,M = map(int,input().split())
arr = [0]*N
result = 0
for i in range(N):
    arr[i] = list(map(int,input()))
for i in range(1,10):
    swim(i)
print(result)
