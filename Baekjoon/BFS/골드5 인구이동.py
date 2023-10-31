#I. A[i][j]에서 연합이 되는 모든 나라를 찾아 통합하는 함수 union(i,j)를 만든다.
#1. [i,j]에서 동서남북으로 뻗어가며 연합이 가능한 나라들을 찾아 연합으로 통합한다.
#2. 이번이 K번째 연합이라면 나라의 수를 C[k]에 인구수를 P[k]에 넣는다.
#3. result = P[k]//C[k] 로 k 번째 연합의 인구를 통일한다.


#II. 인구이동 시간 확인
#1. 이중 포문으로 [0,0] 에서 [N-1,N-1]까지 확인한다.
#2. [0,0]에서 연합이 된 나라들의 visited값을 1로 만든다.
#3. 1이 아닌 나라에서 다른 연합이 발생하면 k번째 연합을 만든다.
#4. 전체를 순회하여 max(k)가 1이거나 0이면 종료한다.

def union(x,y):
    global ch
    if visited[x][y] != 0:
        return
    else:
        q = [[x,y]]
        temp = [[x,y]]
        cnt = 1
        popular = A[x][y]
        visited[x][y] = 1
        while q:
            a, b = q.pop(0)
            for di,dj in direction:
                ni,nj = a+di,b+dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and L<=abs(A[a][b]-A[ni][nj])and abs(A[a][b]-A[ni][nj])<=R:
                    q.append([ni,nj])
                    temp.append([ni,nj])
                    visited[ni][nj] = 1
                    cnt +=1
                    popular +=A[ni][nj]
        # print(temp)
        if cnt ==1:
            ch +=1
            return
        else:
            result = popular // cnt
            for p,q in temp:
                A[p][q] = result
                # print(p,q)




N,L,R = map(int,input().split())
A = [0]*N
C = [0]*N
P = [0]*N
direction = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(N):
    A[i] = list(map(int,input().split()))
day = 0
while True:
    ch = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            union(i,j)
    if ch == N*N:
        break
    else:
        day +=1
print(day)