
def melt(A):
    global N
    global M
    global ice_cnt
    global ch_point
    result = [[0]*M for _ in range(N)]
    #얼음이 0이 아닌곳 한개만 파악해서 연결 확인할거니 제일 큰 얼음값을 찾는 좌표
    max_ice = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            if A[i][j] !=0:
                for di,dj in direction:
                    ni,nj = di+i,dj+j
                    if 0<=ni<N and 0<=nj<M and A[ni][nj] ==0:
                        cnt +=1
                result[i][j] = A[i][j] -cnt
                if result[i][j] <=0:
                    result[i][j] = 0
                    ice_cnt += -1
                if result[i][j] >max_ice:
                    max_ice = result[i][j]
                    ch_point = [i,j]

    return result

#제일 큰 값 (=0이 아닌값) 에서 동서남북으로 BFS 진행해 가는 숫자 체크해서
#전체 남은 얼음과 동일한지 여부 확인
def slice(A,ch):
    global ice_cnt
    visited= [[0]*M for _ in range(N)]
    visited[ch[0]][ch[1]] =1
    cnt = 1
    stack = [[ch[0],ch[1]]]
    while stack:
        check_point = stack.pop(0)
        x,y = check_point[0],check_point[1]
        for di,dj in direction:
            ni,nj = x+di,y+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and A[ni][nj] !=0:
                visited[ni][nj] =1
                cnt +=1
                stack.append([ni,nj])
    if ice_cnt !=0 and cnt ==ice_cnt:
        return True
    else:
        return False
direction = [[1,0],[-1,0],[0,1],[0,-1]]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ice_cnt = 0
max_ice = 0
ch_point=[0,0]
for i in range(N):
    for j in range(M):
        if arr[i][j] !=0:
            ice_cnt +=1
        if arr[i][j]>max_ice:
            max_ice = arr[i][j]
            ch_point = [i,j]
result = 0

while slice(arr,ch_point):
    arr = melt(arr)

    result +=1

if ice_cnt ==0:
    print(0)
else:
    print(result)
