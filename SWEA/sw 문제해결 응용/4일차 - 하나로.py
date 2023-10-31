import sys
sys.stdin = open('4일차_하나로.txt')

def dijkstra(N,E):
    visited[0]=1
    for _ in range(N-1):
        w = 0
        for i in range(1,N):
            if visited[i]==0 and D[i] <D[w]:
                w = i
        visited[w] =1
        for i in range(0,N):
            if i != w and visited[i] ==0:
                D[i] = min(D[i],(x[w]-x[i])**2+(y[w]-y[i])**2)
    result = 0
    for i in range(1,N):
        result +=D[i]
    return round(result*E)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[] for i in range(N)]
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    INF = 1000000000000000000
    D = [INF]*N
    visited = [0] *N
    print(f'#{tc} {dijkstra(N,E)}')