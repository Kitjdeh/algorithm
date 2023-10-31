def bfs(v):
    visited = [0]*1001
    q= []
    q.append(v)
    visited[v] = 1
    bway=[]
    bway.append(v)
    while q:
        v = q.pop(0)
        adjList[v].sort()
        for w in adjList[v]: #v에 인접하고 방문안한 w인 q
            if visited[w] ==0:
                q.append(w)
                bway.append(w)
                visited[w] = visited[v]+1
    return bway
N,M,V = map(int,input().split())

q = []
adjList = [[]for _ in range(1001)]
for i in range(M):
    a,b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)
path_d = []
visited_d=[0]*1001
def dfs(V):
    if visited_d[V] == 1:
        return
    else:
        visited_d[V] = 1
        path_d.append(V)
        adjList[V].sort()
    for i in adjList[V]:
        dfs[i]
    return path_d



print(*bfs(V))
print(*dfs(V))
