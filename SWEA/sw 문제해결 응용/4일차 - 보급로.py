import sys
sys.stdin = open('5250 최소비용.txt')
def dijkstra(N):
    D = [[INF]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    D[0][0] = 0
    while D[N-1][N-1] ==INF:
        wi, wj = 0,0            #D[w]가 최소인 w 찾기
        minV = INF
        for i in range(N):
            for j in range(N):
                if visited[i][j] ==0 and minV >D[i][j]:
                    minV = D[i][j]
                    wi,wj = i,j
        visited[wi][wj] = 1
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni,nj = wi+di,wj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                D[ni][nj] = min(D[ni][nj], D[wi][wj]+arr[ni][nj])   #기존의 D값과 [wi][wj]에서 ni,nj로 가는 값중 더 작은값을 경로로 가진다.
    return D[N-1][N-1]

T= int(input())
INF = 100000000
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    print(f'#{tc} {dijkstra(N)}')
