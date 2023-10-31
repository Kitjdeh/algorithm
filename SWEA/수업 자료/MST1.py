V,E = map(int,input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[ for _ in range(V+1)]]
for _ in range(E):
    u, v, w = map(int,input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    adjL[u].append((v,w))
    adjL[v].append((u,w))