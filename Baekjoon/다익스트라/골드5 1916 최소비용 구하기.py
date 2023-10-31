from sys import stdin
def dijkstra(S,E,arr,d):
    global N
    global M
    global INF
    for i in range(N):
        d[i] = arr[S][i]                        #S와 직행인 거리들 정리 -> 나머지는 INF
    visited = [0]*N
    # 시작점은 방문 처리
    visited[S] = 1
    # w = S
    #시작점 S를 제외 한 나머지 N-1개의 도시들 거리를 구해야 하니 N-1
    for _ in range(N-1):
        # 우선 시작도시 S에서 시작해서
        w= S
        # 방문하지 않은 도시들 중 제일 d값이 짧은 도시를 뽑아야함
        for i in range(N):
            if visited[i] ==0 and 0<=d[i]<d[w]:
                w = i
        #제일 짧은 곳을 방문하고 연관된 도시를 거리 재배치 해야함
        visited[w]=1
        for i in range(N):
            if visited[i] == 0 and 0<=arr[w][i]<INF:
                d[i] = min(d[i],d[w]+arr[w][i])
    return d[E]

N = int(stdin.readline())
M = int(stdin.readline())
INF = 10000000000
road = [[INF]*N for _ in range(N)]
for i in range(M):
    s,e,d= map(int,stdin.readline().split())
    s,e,d = s-1,e-1,d
    if road[s][e] > d:
        road[s][e] = d
S,E = map(int,stdin.readline().split())
S,E = S-1,E-1

distance = [0]*N
print(dijkstra(S,E,road,distance))