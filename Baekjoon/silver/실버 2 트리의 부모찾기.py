import sys
sys.setrecursionlimit(100000000)

def f(root):
    visited[root] =1
    for i in arr[root]:
        if visited[i] ==0:
            par[i] = root  # 각 해당 arr값들은 root 가 부모님을 적음
            f(i)

N = int(input())
arr = [[] for _ in range(N+1)] # 1~N의 인덱스를 사용해야 하니 N+1
par = [0] *(N+1) # 각 노드의 부모
for i in range(N-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
way = []
f(1)
for i in range(2,N+1):
    print(par[i])