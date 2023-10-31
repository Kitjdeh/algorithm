#s에서 e 까지 이동하면서 무게제한이 최대가 되도록 설정
#다익스트라
#1. adj로 각 노드간의 연결 확인
#2. D[x][y]로 x에서 y로 이동할경우 최대 무게 제한 체크
#3. INF 로 D값 설정
#4. heap으로 가장 값이 큰 노드들 위주로 체크


#제일 큰 값으로 시작한다 가정
#현재 node
import heapq
from collections import deque
def dijkstra(x,y):
    global INF
    q = []
    heapq.heappush(q,(-INF,x))
    visited[x] = INF
    while q:
        r,w = heapq.heappop(q)
        r= -r
        if visited[w] > r:
            continue
        for node, distance in adj[w]:
            temp = min(distance,r)
            if visited[node] <temp:
                visited[node] = temp
                heapq.heappush(q,(-temp,node))
    return visited[y]

N,M = map(int,input().split())
s,e = map(int,input().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    p,q,r = map(int,input().split())
    adj[p].append([q,r])
    adj[q].append([p,r])
INF =10000000
print(dijkstra(s,e))


# # w의 인접 중 제일 큰값을 따라 가는게 제일 베스트
# # 1, 3 ,4면 1 골라 봐야 3,4보다 높은 값 절대 안나옴
# # q=[s] 생성
# # adj[s] 중에서 제일 max 값 인 i 추출
# # 해당 값으로 D[i] 결정 밑 q.append(i)
# N,M = map(int,input().split())
# s,e = map(int,input().split())
# adj = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# for i in range(M):
#     p,q,r = map(int,input().split())
#     adj[p].append([r,q])
#     adj[q].append([r,p])
# for i in range(1,N+1):
#     adj[i].sort()
# INF =10000000
# D = [0]*(N+1)
# D[s] = INF
# # print(adj[2])
# # print(sorted(adj[2],reverse=True))
# def MST(s,e):
#     q = [s]
#     # visited[s] = 0
#     while q and visited[e] == 0:
#         x = q.pop(0)
#         visited[x] = 1
#         # print(adj[x])
#         r,p = adj[x].pop()
#         if visited[p] == 0:
#             D[p] = max(D[p],min(D[x],r))
#             q.append(p)
#
#         # for r,p in adj[x]:
#         #     print(r,p)
#         #     if visited[p] == 0:
#         #         D[p] = max(D[p],min(D[x],r))
#         #         q.append(p)
#         #         break
#         print(D,p)
#         # print(adj)
#     return D[e]
# print(MST(s,e))
