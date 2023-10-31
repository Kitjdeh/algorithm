#리프노드와 리프노드의 거리가 값이 제일 큰 간선을 뽑는 문제
#리프노드에서 DFS로 리프노드를 실행
N = int(input())
area = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B, L = map(int, input().split())
    area[A].append([B, L])
    area[B].append([A, L])

visited = [-1] * (N+1)
visited[1] = 0
q = [1]
while q:
    x = q.pop(0)
    for i in area[x]:
        y, d = i
        if visited[y] == -1:
            visited[y] = d + visited[x]
            q.append(y)

temp = max(visited)
q = [visited.index(temp)]
visited = [-1] * (N+1)
visited[q[0]] = 0

while q:
    x = q.pop(0)
    for i in area[x]:
        y, d = i
        if visited[y] == -1:
            visited[y] = d + visited[x]
            q.append(y)
print(max(visited))

#I. 트리의 지름은 Root 노드 기준으로 리프 노드 1개와 리프 노드 1개의 최단거리
#II. 각 리프 노드 기준으로 각 부모노드 까지의 합 depth을 구한다.
#2-1. par 리스트에 [(부모노드의 값, 거리)] 형식으로 설정한다.
#2-2. ch 리스트로 자식관계로 설정한다.
#2-3. depth 리스트 생성 / [(좌측최댓값,우측최댓값)]으로 만든다.
#2-4. 자식이 없은 리프노드를 확인할 leafnode를 만든다.
#III. 리프노드에서 Root 노드까지 가는 재귀함수 climb을 만든다.
# climb(노드값)
#3-2. Root 노드면 함수 종결
# 부모의 몇번때 아들인지 확인 후
#3-3. 부모가 있으면 본인의 좌,우측중 최댓값을 더해서 depth에 넣는다.
#3-4. 만약 이미 depth가 있다면 더 큰 값으로 설정한다.
#3-5. 현재 본인의 좌/우측 의 합이 maxV보다 큰지 확인하여 변경
#3-6. 부모 노드 값으로 climb(부모노드값)을 재귀로 넣어준다.
#III. 리프노드에서 Root 노드까지 가는 재귀함수 climb을 만든다.
def climb(node):                                            # climb(노드값)
    global maxV
    if par[node] == 0:                                      # 3-2. Root 노드면 함수 종결
        return
    else:
        p = par[node][0]
        h = par[node][1]
        L = len(ch[p])
        for t in range(L):
            if ch[p][t] == node:                            # 부모의 몇번때 아들인지 확인 후
                i = t
                break
        depth[p][i] = max(depth[p][i],max(depth[node])+h)
        if len(depth[p])>1:
            for j in range(len(depth[p])):
                for k in range(j+1,len(depth[p])):
                    if maxV < depth[p][j]+depth[p][k]:      #3-5. 현재 본인의 depth값들의 합이 maxV보다 큰지 확인하여 변경
                        maxV = depth[p][j]+depth[p][k]
        climb(p)                                            #3-6. 부모 노드 값으로 climb(부모노드값)을 재귀로 넣어준다.
maxV = 0
N = int(input())
par = [0]*(N+1)                                             #2-1. par 리스트에 [(부모노드의 값, 거리)] 형식으로 설정한다.
ch = [[0] for _ in range(N+1)]                              #2-2. ch 리스트로 자식관계로 설정한다.
depth = [[0] for _ in range(N+1)]                           #2-3. depth 리스트 생성 / [(좌측최댓값,우측최댓값)]으로 만든다.
leafnode = []                                               #2-4. 자식이 없은 리프노드를 확인할 leafnode를 만든다.
for _ in range(N-1):
    p, c, h = map(int,input().split())
    par[c] = [p,h]
    if ch[p][0] ==0:
        ch[p][0] = c
    else:
        ch[p].append(c)
        depth[p].append(0)

for i in range(1,N+1):
    if ch[i][0] ==0:
        leafnode.append(i)
for i in leafnode:
    climb(i)
print(maxV)

# 5
# 1 2 3
# 1 3 4
# 1 4 5
# 1 5 6
# #I. 트리의 지름은 Root 노드 기준으로 리프 노드 1개와 리프 노드 1개의 최단거리
# #II. 각 리프 노드 기준으로 각 부모노드 까지의 합 depth을 구한다.
# #2-1. par 리스트에 [(부모노드의 값, 거리)] 형식으로 설정한다.
# #2-2. ch 리스트로 자식관계로 설정한다.
# #2-3. depth 리스트 생성 / [(좌측최댓값,우측최댓값)]으로 만든다.
# #2-4. 자식이 없은 리프노드를 확인할 leafnode를 만든다.
#
# #III. 리프노드에서 Root 노드까지 가는 재귀함수 climb을 만든다.
# # climb(노드값)
# #3-2. Root 노드면 함수 종결
# # 부모의 좌측인지 우측인지 확인 후
# #3-3. 부모가 있으면 본인의 좌,우측중 최댓값을 더해서 depth에 넣는다.
# #3-4. 만약 이미 depth가 있다면 더 큰 값으로 설정한다.
# #3-5. 현재 본인의 좌/우측 의 합이 maxV보다 큰지 확인하여 변경
# #3-6. 부모 노드 값으로 climb(부모노드값)을 재귀로 넣어준다.
#
# #III. 리프노드에서 Root 노드까지 가는 재귀함수 climb을 만든다.
# def climb(node):                                            # climb(노드값)
#     global maxV
#     if par[node] == 0:                                      # 3-2. Root 노드면 함수 종결
#         return
#     else:
#         p = par[node][0]
#         h = par[node][1]
#         if ch[p][0] != node:                                # 부모의 좌측인지 우측인지 확인 후
#                                                             # 3-3. 본인의 좌,우측중 최댓값을 부모 depth에 넣는다.
#                                                             # 3-4. 만약 이미 depth가 있다면 더 큰 값으로 설정한다.
#             depth[p][1] = max(depth[p][1],max(depth[node])+h)
#         else:
#             depth[p][0] = max(depth[p][1],max(depth[node])+h)
#         if depth[p][0] !=0 and depth[p][1] != 0:
#             if maxV < depth[p][0]+depth[p][1]:              #3-5. 현재 본인의 좌/우측 의 합이 maxV보다 큰지 확인하여 변경
#                 maxV = depth[p][0]+depth[p][1]
#         climb(p)                                            #3-6. 부모 노드 값으로 climb(부모노드값)을 재귀로 넣어준다.
# maxV = 0
# N = int(input())
# par = [0]*(N+1)                                             #2-1. par 리스트에 [(부모노드의 값, 거리)] 형식으로 설정한다.
# ch = [[0,0] for _ in range(N+1)]                            #2-2. ch 리스트로 자식관계로 설정한다.
# depth = [[0,0] for _ in range(N+1)]                         #2-3. depth 리스트 생성 / [(좌측최댓값,우측최댓값)]으로 만든다.
# leafnode = []                                               #2-4. 자식이 없은 리프노드를 확인할 leafnode를 만든다.
# for _ in range(N-1):
#     p, c, h = map(int,input().split())
#     par[c] = [p,h]
#     if ch[p][0] ==0:
#         ch[p][0] = c
#     else:
#         ch[p][1] = c
#
# for i in range(1,N+1):
#     if ch[i][0] ==0:
#         leafnode.append(i)
# for i in leafnode:
#     climb(i)
# print(par)
# print(ch)
# print(depth)
# print(maxV)