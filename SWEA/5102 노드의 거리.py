import sys
sys.stdin = open('5102 노드의 거리.txt')
def bfs(S,G,V):

    q=[]
    q.append(S)
    visited[S]=1
    while q:
        v = q.pop()
        if v == G:
            return visited[v]-1

        for w in adjList[v]:
            if visited[w] ==0:
                q.append(w)
                visited[w] = visited[v] +1  #이동할 때 마다 1씩 증가
    return 0
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adjList = [[] for _ in range(V+1)]
    visited = [0] *(V+1)
    for i in range(E):
        a,b = map(int,input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    S,G = map(int,input().split())
    print(f'#{tc} {bfs(S,G,V)}')

