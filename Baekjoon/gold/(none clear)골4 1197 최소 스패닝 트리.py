# def dijkstra(V,X,adj,d):
#     d[X]=2147483647
#     for i in range(1,V+1):
#         d[i] = adj[X][i]
#     U = [X]
#     while len(U) !=V-1:
#         w=1
#         for i in range(1,V+1):
#             if (i not in U) and d[i]<d[w]:
#                 w= i
#         U.append(w)
#         for j in range(1,V+1):
#             if adj[w][j]<2147483647:
#                 d[j]=min(d[j],d[w]+adj[w][j])
#
# V,E = map(int,input().split())
# adj = [[2147483647]*(V+1) for _ in range(V+1)]
# for _ in range(E):
#     A,B,C = map(int,input().split())
#     adj[A][B] = C
#     min_V=2147483647
# for i in range(1,E+1):
#     dout = [2147483647] * (V + 1)
#     dijkstra(V, i, adj, dout)
#     result = -dout[i]
#     for j in range(1, V + 1):
#         result += dout[j]
#     if min_V>result:
#         min_V = result
#         print(i,j)
# print(min_V)
# print(dout)
def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

V,E = map(int,input().split())
arr = [0]*E
for i in range(E):
    A,B,C = map(int,input().split())
    arr[i] = [A,B,C]
arr.sort(key=lambda x:x[2])
U = [arr[0][1],arr[0][0]]
result = arr[0][2]
visited = [0]*(V+1)
visited[arr[0][1]]=1
visited[arr[0][0]]=1
cnt = 2
T = arr[0::]
while cnt !=V:
    A = T.pop(0)
    p,q,r = A[0],A[1],A[2]
    if visited[p] ==0 and visited[q]==0:
        visited[p],visited[q] = 1,1
        result +=r
        cnt +=2
    elif visited[p]==0:
        visited[p] =1
        result +=r
        cnt +=1
    elif visited[q]==0:
        visited[q] =1
        result += r
        cnt +=1
#그룹화 끝났으니 그룹 통합
    for a,b in arr:
        if find_set(a) != find_set(b):
            union(a,b)
print(result)



# while len(U) != V:
#     for t in range(1,E):
#         p,q = arr[t][0],arr[t][1]
#         if (p not in U) and (q not in U):
#             U.append(p)
#             U.append(q)
#             result +=arr[t][2]
#             break
#         elif (p not in U) and (q in U):
#             U.append(p)
#             result +=arr[t][2]
#             break
#         elif (q not in U) and (p in U):
#             U.append(q)
#             result +=arr[t][2]
#             break