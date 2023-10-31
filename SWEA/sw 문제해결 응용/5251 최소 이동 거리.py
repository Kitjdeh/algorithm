def dijkstra(N,X,adj,d):
    for i in range(N+1):
        d[i] = adj[X][i]
    U = [X]
    while N not in U:
        w = 0
        for i in range(1,N+1):
            if (i not in U) and d[i] < d[w]:
                w = i
        U.append(w)
        for j in range(1,N+1):
            if 0<adj[w][j]<10000000:
                d[j] = min(d[j],d[w]+adj[w][j])

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())
    adj = [[10000000]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
    dout = [0] * (N+1)
    dijkstra(N,0,adj,dout)
    print(f'#{tc} {dout[N]}')

