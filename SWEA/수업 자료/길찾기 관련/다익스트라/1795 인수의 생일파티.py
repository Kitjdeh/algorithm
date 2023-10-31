import sys
sys.stdin = open('1795 인수의 생일파티.txt')
def dijkstra_go(arr,x,d):
    visited = [0]*(N+1)
    visited[x] = 1
    for i in range(1,N+1):
        d[i] = arr[x][i]
    for _ in range(N-1):
        w = x
        for i in range(1,N+1):
            if visited[i] ==0 and 0<d[i]<d[w]:
                w = i
        visited[w] = 1
        for i in range(1,N+1):
            if visited[i] ==0 and arr[w][i] <INF:
                d[i] = min(d[i],d[w]+arr[w][i])
def dijkstra_back(arr,x,d):
    visited = [0]*(N+1)
    visited[x] = 1
    for i in range(1,N+1):
      d[i] = arr[i][x]
    for _ in range(N-1):
        w = x
        for i in range(1,N+1):
            if visited[i] ==0 and 0<d[i]<d[w]:
                w= i
        visited[w] = 1
        for i in range(1,N+1):
            if visited[i] ==0 and arr[i][w] <INF:
                d[i] = min(d[i],d[w]+arr[i][w])

T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split())
    INF = 1000000000
    road = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x,y,c = map(int,input().split())
        road[x][y] = c
    distance_go = [0]*(N+1)
    distance_back = [0]*(N+1)
    dijkstra_go(road,X,distance_go)
    dijkstra_back(road,X,distance_back)
    max_V = 0
    for i in range(1,N+1):
        if i != X and distance_back[i]+distance_go[i]>max_V:
            max_V= distance_back[i]+distance_go[i]
    print(f'#{tc} {max_V}')



