# 벽을 최소한으로 부순다.
# ==> [1,1]에서 [N,M]으로 이동하는데 만나는 최소한의 벽의 갯수를 찾기
# D[x][y]를 전부 INF로 설정
#


def bfs():


    return

M,N = map(int,input().split())
INF = 10**7

visited = [[0]*M for _ in range(N)]
arr = [0]*N
for i in range(N):
    arr[i] = list(input())
q = [[0,0]]
while q:
    x,y = q.pop(0)
    cnt = visited[x][y]
    for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        ni,nj = x+di,y+dj
        if ni<0 or ni>=N or nj <0 or nj>=M :
            continue
        if arr[ni][nj] == '1' and visited[ni][nj] < cnt + 1:
            visited[ni][nj] = cnt +1
        if arr[ni][nj] == '0':
            visited[ni][nj] = cnt
        q.append([ni,nj])
print(visited)