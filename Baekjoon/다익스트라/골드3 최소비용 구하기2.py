from sys import stdin
def dijkstra(arr,s):
    global N
    visited = [0]*(N+1)
    # visited[s] = 1
    d[s] = 0
    # for i in range(1,N+1):
    #     d[i] = arr[s][i]
    for _ in range(N):
        w = 0                                   #어차피 인덱스0은 없는 도시에 INF처리 되어있으니 max 확인용으로 사용
        for i in range(1,N+1):
            if visited[i] ==0 and d[i]<d[w]:
                w = i
        visited[w] =1
        for i in range(1,N+1):
            if visited[i] == 0 and arr[w][i]<INF:
                if d[i] > d[w] + arr[w][i]:
                    d[i] = d[w] + arr[w][i]
                    way[i] = way[w][0::]
                    way[i].append(i)
                # d[i] = min(d[i],d[w]+arr[w][i])

N = int(stdin.readline())
M = int(stdin.readline())
INF = 1000000
road = [[INF]*(N+1) for _ in range(N+1)]        #도로 설정
for _ in range(M):
    x,y,c = map(int,stdin.readline().split())
    if road[x][y] > c:
        road[x][y] =c
S,E = map(int,stdin.readline().split())
d = [INF]*(N+1)
way = [[S] for _ in range(N+1)]
dijkstra(road,S)
print(d[E])
print(len(way[E]))
for i in way[E]:
    print(i,end=" ")