#그래프 탐색 (정점 번호 출력)
# A~G -> 0~6
# adjList = [[1, 2],      # 0
#            [0, 3, 4],   # 1
#            [0, 4],      # 2
#            [1, 5],      # 3
#            [1, 2, 5],   # 4
#            [3, 4, 6],   # 5
#            [5]]         # 6

def bfs(v, N):  #   v 시작정점, N 마지막 정점 번호
    visited = [0]* (N+1)    # visited 생성
    q = []                  # 큐 생성
    q.append(v)             # 시작점 인큐
    visited[v] = 1          # 시작점 처리 표시
    while q:                # 큐가 비어있지 않으면
        v = q.pop(0)            # 디큐
        print(v)                # visit(v)
        for w in adjList[v]:    # 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

V, E = map(int, input().split())
N = V + 1       # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(0, V)
#1219. 길찾기 (BFS)
def bfs(v, N, t):   # v 시작, N 마지막 정점번호, t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:      # visit(v)
            return 1    # 목표 발견, 경로의 길이인 경우 visited[99]
        for w in adjList[v]:    # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)            # 단방향

    print(f'#{tc} {bfs(0, 99, 99)}')  # 시작, 마지막정점, 목표 정점번호


#미로 탐색
def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):              # 출발점이 여러개인 경우에도 사용
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N)}')