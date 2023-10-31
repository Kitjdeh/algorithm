# 트램펄린을 전체 배치 할 수 있는 경우의 수
# = (N-L) * (M-L)
# 1. 전체 완탐?
# 2. [x,y] 위치의 별똥별을 받을 수 있는 트램펄린 갯수는 x-L<=X<=x+L && y-L<=X<=y+L
# 3. 해당 좌표계들에 +1 하면서 max 값 확인
N, M, L, K = map(int,input().split())
arr = [0]*K
maxcount = 0
for i in range(K):
    arr[i] = list(map(int,input().split()))
visited = [[0]*(M+1) for i in range(N+1)]
for i in range(K):
    y,x = arr[i]
    mx,Mx = x-L-1,x+L-1
    my,My = y-L-1,y+L-1
    for j in range(x-L-1,x+1):
        for t in range(y-L-1,y+1):
            if 0<j<=N and 0<t<=M:
                visited[j][t] +=1
                if visited[j][t] > maxcount:
                    maxcount = visited[j][t]
print(K-maxcount)




